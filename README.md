# Rails Migration Boy

A Sublime Text plugin to manage Rails migrations with quick commands and CodeLens-like options.

## Features

- **Command Palette Integration**: Access "Migrate All", "Migrate Up", "Migrate Down", "Migrate Redo", and "Open Latest Migration" via the Command Palette.
- **Phantom Options**: Displays "Up", "Down", and "Redo" buttons below migration files for quick execution.
- **Progress Indicator**: Shows an npm-style spinner in the status bar during command execution.
- **Output Panel**: Displays command output and errors in a Sublime Text panel.
- **Latest Migration Access**: Quickly open the most recent migration file from anywhere in the project.

## Installation

### Package Control

1. Open Sublime Text.
2. Open the Command Palette (`Ctrl+Shift+P` on Windows/Linux, `Cmd+Shift+P` on macOS).
3. Type "Package Control: Install Package" and press Enter.
4. Search for "Rails Migration Boy" and select it to install.

## Usage

1. Open a Rails project in Sublime Text.
2. Use the Command Palette (`Ctrl+Shift+P` on Windows/Linux, `Cmd+Shift+P` on macOS) and select from:
   - "Rails Migration Boy: Migrate All" - Run all pending migrations
   - "Rails Migration Boy: Migrate Up" - Run the current migration up
   - "Rails Migration Boy: Migrate Down" - Run the current migration down
   - "Rails Migration Boy: Migrate Redo" - Redo the current migration
   - "Rails Migration Boy: Open Latest Migration" - Open the most recent migration file
3. When viewing a migration file (e.g., `db/migrate/20250306123456_create_users.rb`), click the "Up", "Down", or "Redo" buttons below the file for quick actions.

## Requirements

- Sublime Text 3 or 4 (tested with build 4192 on Ubuntu, compatible with all builds of ST3 and ST4)
- Supported Operating Systems: Windows, macOS, Linux
- Ruby and Rails installed with `rails` in your PATH

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Author

- Haroon Rasheed ([@haroon26](https://github.com/haroon26))

## Acknowledgments

- Inspired by the VS Code `rails-migration-boy` extension.
