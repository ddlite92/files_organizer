## 🚀 Future Development Roadmap

### **Core Improvements**

- [ ] Migrate to PyQt6/DearPyGui for modern UI
- [ ] Add theme support (dark/light mode)
- [/] Use sub-category method eg: Documents > 'PDF' :.pdf, 'DOC' : .doc,
- [ ] Implement undo functionality
- [ ] More precise categorization and system file checking
- [ ] Package for other OS.

# File Organizer

A Python application that organizes files into categorized folders with a graphical interface using tkinter.

https://github.com/user-attachments/assets/ff713a75-011f-433a-b634-d5ef35d8285a

## Features

- Creates category folders automatically
- Moves files based on their extensions
- Handles undefined file types in a dedicated folder
- Simple GUI interface using Tkinter
- Works with any selected directory

## Supported File Categories

| Category    | Example Extensions            |
| ----------- | ----------------------------- |
| Documents   | .doc, .docx, .pdf, .txt, .csv |
| Images      | .jpg, .png, .psd, .svg        |
| Media       | .mp3, .mp4, .avi, .mkv        |
| Archives    | .zip, .rar, .7z, .tar.gz      |
| Executables | .exe, .msi, .py, .sh          |
| Etc         | .tmp, .log, .cfg, .ini        |
| Undefined   | (All other file types)        |

## Requirements

- Python 3.6+
- Tkinter (usually included with Python)

## Installation

1. Clone or download the repository
2. Install requirements (if any):

## Usage

1. Click "Browse" and select your folder (e.g., /home/user/Documents/MyFiles)
2. Click "Organize Files"

### Using the GUI:

1. Navigate to the script directory:

   ```bash
   cd /path/to/script/files_organizer/src

   ```

2. Run the application:

   python3 gui_tkinter.py

   or if you need to specify the full path:

   python3 /full/path/to/gui_tkinter.py
