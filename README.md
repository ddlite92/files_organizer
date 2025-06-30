# File Organizer

A simple Python script that organizes files in the current directory into categorized folders by its extension.

## Features

- Creates category folders automatically
- Moves files to their appropriate folders based on file extensions
- Works with the current directory where the script is run
- Simple and lightweight with no dependencies beyond Python standard library

## Supported File Types

| Category | Extensions                          |
|----------|-------------------------------------|
| Scripts  | `.py`                               |
| Doc      | `.pdf`, `.zip`                      |
| Images   | `.jpg`, `.png`, `.gif`              |

current_directory/
├── Scripts/
├── Doc/
└── Images/

Requirements
Python 3.x

Notes
The script only organizes files in the directory where it's run
Hidden files (starting with '.') are ignored
Existing files in target folders with the same names will cause errors

## Usage

1. Place the script in the directory you want to organize
2. Run the script:


```bash
python files_organizer.py


