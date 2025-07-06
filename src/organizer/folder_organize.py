import os
import shutil
from pathlib import Path

class FolderOrganizer:
    def __init__(self, target_folder=None):
        self.target = target_folder if target_folder else str(Path(__file__).resolve().parent)
        self.file_types = {
            'Documents': {
                'Work': ['.doc', '.docx', '.xls', '.xlsx', '.ppt'],
                'Personal': ['.pptx', '.odt', '.ods', '.odp', '.pdf', '.txt', '.rtf', '.md', '.csv', '.xls', '.xlsx']
                },  
            'Media':  {
                'Images' : ['.jpg', '.jpeg', '.heic', '.raw', '.dng', '.psd', '.ai', '.svg', '.eps', '.webp', '.png'], 
                'Video' : ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.m4b']
                },
            'Archives': {
                'Zip' : ['.zip', '.rar', '.7z', '.tar.gz'],
                'Iso' : ['.iso', '.dmg', '.img']
                },
            'Executables':  {
                'Installer' : ['.exe', '.msi', '.ps1', '.apk', '.ipa'],
                'Scripts' : ['.py', '.bat', '.sh']
                },
            'Etc': {
                'temp' : ['.tmp', '.temp', '.~'],
                'logfile' : ['.log', '.old', '.bak'],
                'others' : ['.ini', '.cfg', '.conf',  '.db', '.dat', '']
                }
        }

    def create_folders(self):
        for category, sub_category in self.file_types.items():
            path = os.path.join(self.target, category)
            if not os.path.exists(path):
                try:
                    os.makedirs(path)
                except OSError as e:
                    print(f"Failed to create {category}: {e}")

            for sub_catergories in sub_category:
                sub_path = os.path.join(path, sub_catergories)
                if not os.path.exists(sub_path):
                    try:
                        os.makedirs(sub_path)
                    except OSError as e:
                        print(f"Failed to create {sub_catergories}: {e}")
        
        # Create Undefined folder if it doesn't exist
        undefined_path = os.path.join(self.target, 'Undefined')
        if not os.path.exists(undefined_path):
            os.makedirs(undefined_path)
                        
    def get_file_extension(self, file):
        extension = os.path.splitext(file)[1]
        return extension.lower()

    def move_files(self):
        self.create_folders()
        for filename in os.listdir(self.target):
            file_path = os.path.join(self.target, filename)
            if not os.path.isfile(file_path) or filename.startswith('.'):
                continue

            ext = self.get_file_extension(filename)  
            moved = False

            for category, sub_categories in self.file_types.items():
                for sub_category, extensions in sub_categories.items():
                    if ext in extensions:
                        dest_folder = os.path.join(self.target, category, sub_category)
                        try:
                            shutil.move(file_path, os.path.join(dest_folder, filename))
                            moved = True
                            break 
                            
                        except shutil.Error as e:
                            print(f"Failed to move {filename}: {e}")
                            moved = True
                            break
                if moved:
                    break

        # Move to Undefined if no category matched
            if not moved:
                dest_folder = os.path.join(self.target, 'Undefined')
                try:
                     shutil.move(file_path, os.path.join(dest_folder, filename))

                except shutil.Error as e:
                    print(f"Failed to move {filename} to Undefined: {e}")                    
  
                        
    def organize_folder(self, folder_path=None):
        if folder_path:
            self.target = folder_path
        self.move_files()


