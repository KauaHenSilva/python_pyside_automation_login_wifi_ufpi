from ui.DialogWindow import Ui_ErrorQdialog
from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtGui import QIcon, QKeySequence, QShortcut, Qt

from pathlib import Path

class MySetupDialog(QDialog, Ui_ErrorQdialog):
    def __init__(self, text: str) -> None:
        super().__init__()
        self.setupUi(self)
        self._mySetup()
    
        self.enterInput = QShortcut(self)
        self.enterInput.setKey(Qt.Key.Key_Enter)
        self.enterInput.setKey(Qt.Key.Key_Return)
        self.enterInput.activated.connect(self.close)
        
        self.label.setText(text)
        
        self.setModal(True)
        
    def _mySetup(self):
        self.setWindowIcon(
            QIcon(str(Path(__file__).parent / 'files' / 'icons' / 'ufpi1.ico')))
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())


        
        
if __name__ == '__main__':
    app = QApplication()
    window = MySetupDialog("Olá")
    
    window.show()
    app.exec()
    