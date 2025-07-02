## 🚀 Future Development Roadmap

### **Core Improvements**

- [ ] Migrate to PyQt6/DearPyGui for modern UI
- [ ] Add theme support (dark/light mode)
- [/] Use sub-category method eg: Documents > 'PDF' : .pdf, 'DOC' : .doc,
- [ ] Implement undo functionality
- [ ] More precise categorization and system file checking
- [ ] Package for other OS.

# File Organizer

A Python application that organizes files into categorized folders with a graphical interface using tkinter.

https://github.com/user-attachments/assets/ff713a75-011f-433a-b634-d5ef35d8285a

## Features

- Creates category and sub-category folders automatically
- Moves files based on their extensions
- Handles undefined file types in undefine folder
- Simple GUI interface using Tkinter
- Works with any selected directory

# Supported File Categories (Detailed)

| Main Category   | Sub-Category | Example Extensions                                                            |
| --------------- | ------------ | ----------------------------------------------------------------------------- |
| **Documents**   | Work         | .doc, .docx, .xls, .xlsx, .ppt                                                |
|                 | Personal     | .pptx, .odt, .ods, .odp, .pdf, .txt, .rtf, .md, .csv                          |
| **Media**       | Images       | .jpg, .jpeg, .heic, .raw, .dng, .psd, .ai, .svg, .eps, .webp, .png            |
|                 | Video/Audio  | .mp3, .wav, .flac, .aac, .ogg, .m4a, .mp4, .avi, .mov, .mkv, .wmv, .flv, .m4b |
| **Archives**    | Zip          | .zip, .rar, .7z, .tar.gz                                                      |
|                 | Disk Images  | .iso, .dmg, .img                                                              |
| **Executables** | Installer    | .exe, .msi, .ps1, .apk, .ipa                                                  |
|                 | Scripts      | .py, .bat, .sh                                                                |
| **Etc**         | Temporary    | .tmp, .temp, .~                                                               |
|                 | Logs         | .log, .old, .bak                                                              |
|                 | Config/Data  | .ini, .cfg, .conf, .db, .dat                                                  |
| **Undefined**   | -            | (All other file types)                                                        |

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
