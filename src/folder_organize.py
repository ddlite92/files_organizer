import os
import shutil
from pathlib import Path

class FolderOrganizer:
    def __init__(self, target_folder=None):
        self.target = target_folder if target_folder else str(Path(__file__).resolve().parent)
        self.file_types = {
            'Documents': ['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.odt', '.ods', '.odp', '.pdf', '.txt', '.rtf', '.md', '.csv', '.xls', '.xlsx'],
            'Images': ['.jpg', '.jpeg', '.png', '.heic', '.raw', '.dng', '.psd', '.ai', '.svg', '.eps', '.webp', '.png'],   
            'Media':  ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.mp3', '.m4b'],
            'Archives': ['.zip', '.rar', '.7z', '.zip', '.tar.gz', '.iso', '.dmg', '.img'],
            'Executables':  ['.exe', '.msi', '.py', '.sh', '.bat', '.ps1', '.apk', '.ipa'],
            'Etc': ['.tmp', '.temp', '.~', '.bak', '.old', '.ini', '.cfg', '.conf', '.log', '.db', '.dat', ''],
            'Undefined': []
        }

    def create_folders(self):
        exist_folder = []
        for folder in os.listdir(self.target):
            if os.path.isdir(os.path.join(self.target, folder)):
                exist_folder.append(folder)
        
        create = []
        for folder_name in self.file_types:
            path = os.path.join(self.target, folder_name)
            if folder_name not in exist_folder:
                try:
                    os.makedirs(path)
                    #create.append(folder_name)
                except OSError as e:
                    print(f"Failed to create {folder_name}: {e}")

    def get_file_extension(self, file):
        #root = os.path.splitext(file)[0]
        extension = os.path.splitext(file)[1]
        return extension.lower()

    def move_files(self):
        self.create_folders()
        moved_files = set()
        for filename in os.listdir(self.target):
            file_path = os.path.join(self.target, filename)
            if not os.path.isfile(file_path) or filename.startswith('.'):
                continue

            ext = self.get_file_extension(filename)  
            moved = False

            for category, extensions in self.file_types.items():
                    if ext in extensions:
                        dest_folder = os.path.join(self.target, category, filename)
                        try:
                            shutil.move(file_path, dest_folder)
                            moved_files.add(filename.lower())
                            moved = True
                            break  # Move to next file after successful move
                            

                        except shutil.Error as e:
                            print(f"Failed to move {filename}: {e}")
                            moved = True
                            break

        # Move to Undefined if no category matched
            if not moved:
                dest_folder = os.path.join(self.target, 'Undefined', filename)
                try:
                    shutil.move(file_path, dest_folder)
                    moved_files.add(filename.lower())
                except shutil.Error as e:
                    print(f"Failed to move {filename} to Undefined: {e}")                    
  
                        
    def organize_folder(self, folder_path=None):
        if folder_path:
            self.target = folder_path
        self.move_files()


