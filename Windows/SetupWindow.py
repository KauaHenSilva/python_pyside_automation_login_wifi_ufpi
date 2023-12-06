
from PySide6.QtCore import Qt
from ui.ConfigInicial import Ui_ConfigInicial

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

class MySetupWindow(Ui_ConfigInicial, QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self._mySetup()
        
        self.threadPoll = QThreadPool()
    
        self.enterInput = QShortcut(self)
        self.enterInput.setKey(Qt.Key.Key_Enter)
        self.enterInput.setKey(Qt.Key.Key_Return)
        self.enterInput.activated.connect(self.config)
        
        self.ButtonConfig.clicked.connect(self.config)
        
        
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
        self.ButtonConfig.setEnabled(False)    
    
    def enable(self):
        self.ButtonConfig.setEnabled(True)    
    
    def dialogSussess(self):
        self.mensagem = MySetupDialog('Sucesso: O aplicativo está configurado!')
        self.mensagem.exec()
        self.close()

    def dialogError(self, text: Exception):
        self.mensagem = MySetupDialog(f'Erro: {text.__class__} \n\nPossivel Motivo do error:\n{str(text)}')
        self.mensagem.exec()
        self.enable()

        
        
if __name__ == '__main__':
    app = QApplication()
    myWindowSetup = MySetupWindow()
        
    myWindowSetup.show()
    app.exec()
    