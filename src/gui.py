import PySimpleGUI as sg
from . import folder_organize

def run_gui():
    organizer = folder_organize()
    layout = [
        [sg.Text('Folder Organizer', font=('Helvetica', 16))],
        [sg.Input(key='-FOLDER-'), sg.FolderBrowse()],
        [sg.Button('Organize'), sg.Button('Exit')],
        [sg.Output(size=(60, 10))]
    ]
    
    window = sg.Window('Folder Organizer', layout)
    
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Organize':
            organizer.organize_folder(values['-FOLDER-'])
    
    window.close()

if __name__ == '__main__':
    run_gui()