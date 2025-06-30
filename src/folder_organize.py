import os
import shutil

target = os.getcwd()

file_types = {
    'Documents': {
        'Work': ['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.odt', '.ods', '.odp'],
        'Personal': ['.pdf', '.txt', '.rtf', '.md'],
        'Financial': ['.csv', '.xls', '.xlsx']
    },
    'Images': {
        'Photos': ['.jpg', '.jpeg', '.png', '.heic', '.raw', '.dng'],
        'Graphics': ['.psd', '.ai', '.svg', '.eps', '.webp'],
        'Screenshots': ['.png']  # With filename pattern matching
    },
    'Media': {
        'Music': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a'],
        'Videos': ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv'],
        'Podcasts': ['.mp3', '.m4b']
    },
    'Archives': {
        'Software': ['.zip', '.rar', '.7z'],
        'Backups': ['.zip', '.tar.gz'],
        'Disk_Images': ['.iso', '.dmg', '.img']
    },
    'Executables': {
        'Windows': ['.exe', '.msi'],
        'Scripts': ['.py', '.sh', '.bat', '.ps1'],
        'Mobile': ['.apk', '.ipa']
    },
    'Etc': {
        'No_Extension': [''],
        'Temp_Files': ['.tmp', '.temp', '.~', '.bak', '.old'],
        'System_Files': ['.ini', '.cfg', '.conf', '.log', '.db', '.dat'],
        'Unrecognized': []  # Catch-all for other extensions
    }
}

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
        if not os.path.isfile(file_path):
            continue

        ext = get_file_extension(filename)  

        for category, extensions in file_types.items():
                if ext in extensions:
                    dest_folder = os.path.join(target, category, filename)
                    try:
                        shutil.move(file_path, dest_folder)
                    except shutil.Error as e:
                        print(f"Failed to move {filename}: {e}")

def main():
    create_folders()
    move_files()
    print("Files organized successfully!")

if __name__ == "__main__":
    main()