# Rails Migration Boy

A Sublime Text plugin to manage Rails migrations with quick commands and CodeLens-like options.

## Installation

⚠️ **Important**: The Package Control crawler is currently not updating packages, so new releases of Rails Migration Boy may not appear in the standard Package Control list. For the latest version, use the "Add Repository" method below.

### Add Repository Method (Recommended for Latest Release)
1. Open Sublime Text.
2. Open the Command Palette (`Ctrl+Shift+P` on Windows/Linux, `Cmd+Shift+P` on macOS).
3. Type "Package Control: Add Repository" and press Enter.
4. Enter the repository URL: `https://github.com/haroon26/rails-migration-boy-subl`
5. Press Enter to add the repository.
6. Open the Command Palette again, type "Package Control: Install Package", and press Enter.
7. Search for "rails-migration-boy-subl" (it will now show the latest version) and install it.

### Package Control (Older Versions Only)
1. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`).
2. Type "Package Control: Install Package" and press Enter.
3. Search for "Rails Migration Boy" and install it.  
*Note*: This method may not provide the latest release due to the crawler issue.

## Features
- **Command Palette**: "Migrate All", "Migrate Up", "Migrate Down", "Migrate Redo", "Open Latest Migration".
- **Phantom Options**: "Up", "Down", "Redo" buttons below migration files.
- **Progress Indicator**: npm-style spinner in the status bar.
- **Output Panel**: Shows command output and errors.
- **Latest Migration**: Quick access to the most recent migration file.

## Usage
1. Open a Rails project in Sublime Text.
2. Use the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) to run commands like "Rails Migration Boy: Migrate All".
3. In migration files (e.g., `db/migrate/20250306123456_create_users.rb`), click "Up", "Down", or "Redo" buttons.

## Requirements
- Sublime Text 3 or 4 (tested on build 4192, Ubuntu; works with all ST3/ST4 builds)
- OS: Windows, macOS, Linux
- Ruby and Rails with `rails` in your PATH

## License
MIT License - see [LICENSE](LICENSE).

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Author
- Haroon Rasheed ([@haroon26](https://github.com/haroon26))

## Acknowledgments
- Inspired by the VS Code `rails-migration-boy` extension.
