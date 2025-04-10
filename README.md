# Rails Migration Boy

A Sublime Text plugin to manage Rails migrations with quick commands and CodeLens-like options.

## Features
- **Command Palette**: "Migrate All", "Migrate Up", "Migrate Down", "Migrate Redo", "Open Latest Migration".
- **Phantom Options**: "Up", "Down", "Redo" buttons below migration files.
- **Progress Indicator**: npm-style spinner in the status bar.
- **Output Panel**: Shows command output and errors.
- **Latest Migration**: Quick access to the most recent migration file.

## Installation
1. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`).
2. Type "Package Control: Install Package" and press Enter.
3. Search for "Rails Migration Boy" and install it.  

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
