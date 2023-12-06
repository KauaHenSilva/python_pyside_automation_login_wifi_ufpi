
from PySide6.QtCore import Qt
from ui.AtualizarWindow import Ui_Form

from PySide6.QtGui import QIcon, QShortcut, QKeySequence
from PySide6.QtCore import QObject, Signal, QRunnable, Slot, QThreadPool
from PySide6.QtWidgets import QWidget, QApplication

from app.setupLogin import setup
from Windows.WindowDialog import MySetupDialog

from pathlib import Path

class mySignal(QObject):
    started = Signal()
    end = Signal()
    error = Signal(Exception)


class Thread(QRunnable):
    def __init__(self, funcao, **kwargs) -> None:
        super(Thread, self).__init__()
        self.funcao = funcao
        self.kwargs = kwargs
        self.signal = mySignal()

    @Slot()
    def run(self):
        try:
            self.signal.started.emit()
            self.funcao(**self.kwargs)
            self.signal.end.emit()
        except Exception as error:
            self.signal.error.emit(error)

class MyUpdateWindow(Ui_Form, QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self._mySetup()
        
        self.threadPoll = QThreadPool()
    
        self.enterInput = QShortcut(self)
        self.enterInput.setKey(Qt.Key.Key_Enter)
        self.enterInput.setKey(Qt.Key.Key_Return)
        self.enterInput.activated.connect(self.config)
        
        self.pushButton.clicked.connect(self.config)
            
        
    def _mySetup(self):
        self.setWindowIcon(
            QIcon(str(Path(__file__).parent / 'files' / 'icons' / 'ufpi1.ico')))
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
        
    def config(self):
        self.configThread = Thread(setup)
        self.configThread.signal.started.connect(self.disable)
        self.configThread.signal.end.connect(self.dialogSussess)
        self.configThread.signal.error.connect(self.dialogError)
        self.threadPoll.start(self.configThread)
        
    def disable(self):
        self.pushButton.setEnabled(False)    
    
    def enable(self):
        self.pushButton.setEnabled(True)    
    
    def dialogSussess(self):
        self.mensagem = MySetupDialog('O aplicativo foi Atualizado!')
        self.mensagem.show()
        self.close()

    def dialogError(self, error: Exception):
        self.mensagem = MySetupDialog(f'Erro: {error.__class__} \n\nPossivel Motivo do error:\n{str(error)}')
        self.mensagem.show()
        self.enable()

        
        
if __name__ == '__main__':
    app = QApplication()
    myWindowSetup = MyUpdateWindow()
        
    myWindowSetup.show()
    app.exec()
    