import os
import shutil

CURRENT_FOLDER = Path(__file__).resolve().parent
target = str(CURRENT_FOLDER)

file_types = {
    'Documents': ['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.odt', '.ods', '.odp', '.pdf', '.txt', '.rtf', '.md', '.csv', '.xls', '.xlsx']
    'Images': ['.jpg', '.jpeg', '.png', '.heic', '.raw', '.dng', '.psd', '.ai', '.svg', '.eps', '.webp', '.png']   
    'Media':  ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.mp3', '.m4b']
    'Archives': ['.zip', '.rar', '.7z', '.zip', '.tar.gz', '.iso', '.dmg', '.img']
    'Executables':  ['.exe', '.msi', '.py', '.sh', '.bat', '.ps1', '.apk', '.ipa']
    'Etc': ['.tmp', '.temp', '.~', '.bak', '.old', '.ini', '.cfg', '.conf', '.log', '.db', '.dat', '']
}


'''
def create_folders():
    existing_folders = [f for f in os.listdir(target) if os.path.isdir(os.path.join(target, f))]
    
    for folder_name in file_types:
        if folder_name not in existing_folders:
            try:
                os.makedirs(os.path.join(target, folder_name))
            except OSError as e:
                print(f"Failed to create {folder_name}: {e}")
'''

def create_folders():
    exist_folder = []
    for folder in os.listdir(target):
        if os.path.isdir(os.path.join(target, folder)):
            exist_folder.append(folder)
    
    create = []
    for folder_name in file_types:
        path = os.path.join(target, folder_name)
        if folder_name not in exist_folder:
            try:
                os.makedirs(path)
                #create.append(folder_name)
            except OSError as e:
                print(f"Failed to create {folder_name}: {e}")
    #return create

def get_file_extension(file):
    #root = os.path.splitext(file)[0]
    extension = os.path.splitext(file)[1]
    return extension.lower()

def move_files():
    create_folders()
    for filename in os.listdir(target):
        file_path = os.path.join(target, filename)
        if not os.path.isfile(file_path) or filename.startswith('.'):
            continue

        ext = get_file_extension(filename)  

        for category, extensions in file_types.items():
                if ext in extensions:
                    dest_folder = os.path.join(target, category, filename)
                    try:
                        shutil.move(file_path, dest_folder)
                        break  # Move to next file after successful move
                    except shutil.Error as e:
                        print(f"Failed to move {filename}: {e}")
                        break

def main():
    print(f"Organizing files in: {target}")
    create_folders()
    move_files()
    print("Files organized successfully!")

if __name__ == "__main__":
    main()
