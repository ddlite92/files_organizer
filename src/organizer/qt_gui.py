# qt_gui.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import QDir
from organizer_ui import Ui_MainWindow
from folder_organize import FolderOrganizer

class FileOrganizerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set up UI from Designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Connect signals
        self.ui.browseButton.clicked.connect(self.browse_folder)
        self.ui.organizeButton.clicked.connect(self.organize_files)
        
        # Initialize organizer
        self.organizer = None
        
    def browse_folder(self):
        folder_path = QFileDialog.getExistingDirectory(
            self,
            "Select Folder to Organize",
            QDir.homePath(),
            QFileDialog.ShowDirsOnly
        )
        
        if folder_path:
            self.ui.browse_label.setText(folder_path)  # Changed from pathLineEdit to browse_label
            self.organizer = FolderOrganizer(folder_path)
    
    def organize_files(self):
        if not hasattr(self, 'organizer') or not self.organizer:
            QMessageBox.warning(self, "Warning", "Please select a folder first")
            return
            
        try:
            self.organizer.organize_folder()
            QMessageBox.information(self, "Success", "Files organized successfully!")
            self.ui.windows_dialog.setText("Organization complete!")  # Update status text
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Organization failed:\n{str(e)}")
            self.ui.windows_dialog.setText(f"Error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileOrganizerApp()
    window.show()
    sys.exit(app.exec_())