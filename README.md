# Rails Migration Boy

A Sublime Text 3 plugin to manage Rails migrations with quick commands and CodeLens-like options.

## Features

- **Command Palette Integration**: Access "Migrate All", "Migrate Up", "Migrate Down", and "Migrate Redo" via the Command Palette.
- **Phantom Options**: Displays "Up", "Down", and "Redo" buttons below migration files for quick execution.
- **Progress Indicator**: Shows an npm-style spinner in the status bar during command execution.
- **Output Panel**: Displays command output and errors in a Sublime Text panel.

## Installation

### Manual Installation

1. Download the `RailsMigrationBoy` folder or `RailsMigrationBoy.sublime-package` from the [releases page](https://github.com/yourusername/rails-migration-boy/releases).
2. Place the folder in `~/.config/sublime-text-3/Packages/` or the `.sublime-package` file in `~/.config/sublime-text-3/Installed Packages/`.
3. Restart Sublime Text 3.

### Package Control (Coming Soon)

- Once available, install via Package Control by searching for "RailsMigrationBoy".

## Usage

1. Open a Rails project in Sublime Text 3.
2. Open a migration file (e.g., `db/migrate/20250306123456_create_users.rb`).
3. Use the Command Palette (`Ctrl+Shift+P`) and select "Rails Migration Boy" to choose an action.
4. Or click the "Up", "Down", or "Redo" buttons below the migration file.

## Requirements

- Sublime Text 3 (Linux)
- Ruby and Rails installed with `rails` in your PATH (or use `bundle exec rails` by modifying the commands in `rails_migration_boy.py`).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Author

- Haroon Rasheed ([@haroon26](https://github.com/haroon26))

## Acknowledgments

- Inspired by the VS Code `rails-migration-boy` extension.
