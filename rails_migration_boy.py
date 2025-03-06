import sublime
import sublime_plugin
import os
import re
import subprocess
import threading

# Global dictionary to store phantoms per view
phantom_sets = {}
# Global dict to track loader states per view
loader_states = {}

class RailsMigrationBoyCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.view = self.window.active_view()
    if not self.view:
      sublime.message_dialog("No file open.")
      return

    # Determine if the current file is a migration file
    self.is_migration_file = self._is_migration_file(self.view.file_name())
    self.version = self._get_version(self.view.file_name()) if self.is_migration_file else None

    # Build the options list for the quick panel
    self.options = ["Migrate All"]
    if self.is_migration_file:
      self.options.extend(["Migrate Up", "Migrate Down", "Migrate Redo"])

    # Show quick panel with options (Sublime Text 3 compatible)
    self.window.show_quick_panel(
      self.options,
      self.on_select,
      sublime.MONOSPACE_FONT
    )

  def on_select(self, index):
    if index == -1:  # User canceled
      return

    commands = {
      "Migrate All": "rails db:migrate",
      "Migrate Up": f"rails db:migrate:up VERSION={self.version}",
      "Migrate Down": f"rails db:migrate:down VERSION={self.version}",
      "Migrate Redo": f"rails db:migrate:redo VERSION={self.version}"
    }
    selected_option = self.options[index]
    self._run_command(commands[selected_option])

  def _is_migration_file(self, file_path):
    if not file_path:
      return False
    return bool(re.match(r".*db/migrate/\d{14}_.*\.rb$", file_path))

  def _get_version(self, file_path):
    if not file_path:
      return None
    match = re.search(r"(\d{14})_", file_path)
    return match.group(1) if match else None

  def _run_command(self, command):
    project_root = self._find_project_root()
    if not project_root:
      self._show_output("Could not find Rails project root.")
      return

    # Start loader animation
    self._start_loader(command)
    # Run the command in a separate thread
    thread = threading.Thread(
      target=self._execute_command,
      args=(command, project_root)
    )
    thread.start()

  def _start_loader(self, command):
    view_id = self.view.id()
    loader_states[view_id] = {"command": command, "running": True, "frame": 0}
    sublime.set_timeout(lambda: self._update_loader(view_id), 100)

  def _update_loader(self, view_id):
    if view_id not in loader_states or not loader_states[view_id]["running"]:
      return
    frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    frame = loader_states[view_id]["frame"] = (loader_states[view_id]["frame"] + 1) % len(frames)
    status = f"Rails Migration: {loader_states[view_id]['command']} {frames[frame]}"
    self.view.set_status("rails_migration_boy", status)
    sublime.set_timeout(lambda: self._update_loader(view_id), 100)

  def _stop_loader(self, view_id, status):
    if view_id in loader_states:
      loader_states[view_id]["running"] = False
      self.view.set_status("rails_migration_boy", f"Rails Migration: {loader_states[view_id]['command']} - {status}")

  def _execute_command(self, command, project_root):
    view_id = self.view.id()
    try:
      process = subprocess.Popen(
        command,
        shell=True,
        cwd=project_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
      )
      stdout, stderr = process.communicate()
      exit_code = process.returncode

      output = f"Command: {command}\n\n"
      output += f"Output:\n{stdout}\n"
      if stderr:
        output += f"Errors:\n{stderr}\n"
      output += f"Exit Code: {exit_code}"

      self._show_output(output)
      status = "Completed" if exit_code == 0 else "Failed"
      self._stop_loader(view_id, status)
    except Exception as e:
      self._show_output(f"Error running command: {str(e)}")
      self._stop_loader(view_id, "Failed")

  def _find_project_root(self):
    folders = self.window.folders()
    if not folders:
      return None
    project_root = folders[0]
    if os.path.isdir(os.path.join(project_root, "db", "migrate")):
      return project_root
    return None

  def _show_output(self, text):
    sublime.set_timeout(lambda: self._update_output_panel(text), 0)

  def _update_output_panel(self, text):
    output_panel = self.window.create_output_panel("rails_migration_boy")
    output_panel.set_read_only(False)
    output_panel.run_command("append", {"characters": text + "\n"})
    output_panel.set_read_only(True)
    self.window.run_command("show_panel", {"panel": "output.rails_migration_boy"})

class RailsMigrationBoyListener(sublime_plugin.EventListener):
  def on_load_async(self, view):
    self._update_phantoms(view)

  def on_activated_async(self, view):
    self._update_phantoms(view)

  def on_close(self, view):
    if view.id() in phantom_sets:
      del phantom_sets[view.id()]
    if view.id() in loader_states:
      del loader_states[view.id()]

  def _update_phantoms(self, view):
    file_path = view.file_name()
    if not file_path or not self._is_migration_file(file_path):
      if view.id() in phantom_sets:
        phantom_sets[view.id()].update([])
      return

    version = re.search(r"(\d{14})_", file_path).group(1)
    phantom_html = (
      '<style>'
      '  a {'
      '  padding: 5px 10px;'
      '  margin-right: 15px;'
      '  background-color: #252526;'
      '  color: #66d9ef;'
      '  text-decoration: none;'
      '  border-radius: 3px;'
      '  }'
      '  a:hover {'
      '  background-color: #3e3e40;'
      '  }'
      '  body {'
      '  padding: 5px;'
      '  }'
      '</style>'
      f'<a href="up:{version}">Up</a>'
      f'<a href="down:{version}">Down</a>'
      f'<a href="redo:{version}">Redo</a>'
    )

    if view.id() not in phantom_sets:
      phantom_sets[view.id()] = sublime.PhantomSet(view, "rails_migration_boy")
    
    phantoms = [sublime.Phantom(
      sublime.Region(0),
      phantom_html,
      sublime.LAYOUT_BELOW,  # Changed to LAYOUT_BELOW for Sublime Text 3
      self._on_phantom_click
    )]
    phantom_sets[view.id()].update(phantoms)

  def _is_migration_file(self, file_path):
    if not file_path:
      return False
    return bool(re.match(r".*db/migrate/\d{14}_.*\.rb$", file_path))

  def _on_phantom_click(self, href):
    action, version = href.split(":", 1)
    commands = {
      "up": f"rails db:migrate:up VERSION={version}",
      "down": f"rails db:migrate:down VERSION={version}",
      "redo": f"rails db:migrate:redo VERSION={version}"
    }
    view = sublime.active_window().active_view()
    if view:
      window = view.window()
      window.run_command("rails_migration_boy_execute", {"command": commands[action]})

class RailsMigrationBoyExecuteCommand(sublime_plugin.WindowCommand):
  def run(self, command):
    self.view = self.window.active_view()
    if not self.view:
      sublime.message_dialog("No active view available.")
      return
    self._run_command(command)

  def _run_command(self, command):
    project_root = self._find_project_root()
    if not project_root:
      self._show_output("Could not find Rails project root.")
      return

    self._start_loader(command)
    thread = threading.Thread(
      target=self._execute_command,
      args=(command, project_root)
    )
    thread.start()

  def _start_loader(self, command):
    view_id = self.view.id()
    loader_states[view_id] = {"command": command, "running": True, "frame": 0}
    sublime.set_timeout(lambda: self._update_loader(view_id), 100)

  def _update_loader(self, view_id):
    if view_id not in loader_states or not loader_states[view_id]["running"]:
      return
    frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    frame = loader_states[view_id]["frame"] = (loader_states[view_id]["frame"] + 1) % len(frames)
    status = f"Rails Migration: {loader_states[view_id]['command']} {frames[frame]}"
    self.view.set_status("rails_migration_boy", status)
    sublime.set_timeout(lambda: self._update_loader(view_id), 100)

  def _stop_loader(self, view_id, status):
    if view_id in loader_states:
      loader_states[view_id]["running"] = False
      self.view.set_status("rails_migration_boy", f"Rails Migration: {loader_states[view_id]['command']} - {status}")

  def _execute_command(self, command, project_root):
    view_id = self.view.id()
    try:
      process = subprocess.Popen(
        command,
        shell=True,
        cwd=project_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
      )
      stdout, stderr = process.communicate()
      exit_code = process.returncode

      output = f"Command: {command}\n\n"
      output += f"Output:\n{stdout}\n"
      if stderr:
        output += f"Errors:\n{stderr}\n"
      output += f"Exit Code: {exit_code}"

      self._show_output(output)
      status = "Completed" if exit_code == 0 else "Failed"
      self._stop_loader(view_id, status)
    except Exception as e:
      self._show_output(f"Error running command: {str(e)}")
      self._stop_loader(view_id, "Failed")

  def _find_project_root(self):
    folders = self.window.folders()
    if not folders:
      return None
    project_root = folders[0]
    if os.path.isdir(os.path.join(project_root, "db", "migrate")):
      return project_root
    return None

  def _show_output(self, text):
    sublime.set_timeout(lambda: self._update_output_panel(text), 0)

  def _update_output_panel(self, text):
    output_panel = self.window.create_output_panel("rails_migration_boy")
    output_panel.set_read_only(False)
    output_panel.run_command("append", {"characters": text + "\n"})
    output_panel.set_read_only(True)
    self.window.run_command("show_panel", {"panel": "output.rails_migration_boy"})

# Force phantom update on plugin load for existing views
def plugin_loaded():
  for window in sublime.windows():
    for view in window.views():
      if view.file_name() and re.match(r".*db/migrate/\d{14}_.*\.rb$", view.file_name()):
        RailsMigrationBoyListener()._update_phantoms(view)