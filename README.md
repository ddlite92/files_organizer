## 🚀 Future Development Roadmap

### **Core Improvements**

- [x] Migrate to PyQt6/DearPyGui for modern UI
- [ ] Add theme support (dark/light mode)
- [x] Use sub-category method eg: Documents > 'PDF' : .pdf, 'DOC' : .doc,
- [ ] Implement undo functionality
- [ ] More precise categorization and system file checking
- [ ] Package for other OS.

# File Organizer

A Python application that organizes files into categorized folders with a modern Qt interface.

https://github.com/user-attachments/assets/ff713a75-011f-433a-b634-d5ef35d8285a

## Features

- Creates category and sub-category folders automatically
- Moves files based on their extensions
- Handles undefined file types in undefine folder
- Modern GUI interface using PyQt5
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
- PyQt5 (`pip install PyQt5`)
- (Optional) pyqt5-tools for Qt Designer

## Installation

1. Clone or download the repository
2. cd to folder executables/linux_exe
3. Run the package name ```bash sudo dpkg -i ./Files_Organizer-0.1.deb```


## Usage

1. Click "Browse" and select your folder (e.g., /home/user/Documents/MyFiles)
2. Click "Organize Files"

### Using the PyQt GUI:

1. Navigate to the script directory:

   ```bash
   cd /path/to/script/files_organizer/src/organizer

   ```

2. Run the application:

   python3 qt_gui.py

   or if you need to specify the full path:

   python3 /full/path/to/qt_gui.py

### Thanks to: 

1. Icons are from flaticon
   - pocike https://www.flaticon.com/authors/pocike
   - Hopstarter https://www.flaticon.com/authors/hopstarter
   - kmg design https://www.flaticon.com/authors/kmg-design


# Known issues and development

1. The are 2 types of application that can be run, which is running with python3 or package installation .deb
2. As for now, direct run are tested, hence why there are folder src/organize kept for that purpose
3. deb package are not tested and futher OS package development in progress

