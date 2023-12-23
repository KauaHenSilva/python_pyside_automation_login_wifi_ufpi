from PySide6.QtCore import QEvent, QRunnable, Slot, QThreadPool, Signal, QObject, Qt, QEventLoop
from PySide6.QtGui import QIcon, QKeyEvent
from PySide6.QtWidgets import QMainWindow

from ui.LoginWindow import Ui_WindowLogin

from dbUserPassword import dbLogic
from pathlib import Path

from app.LoginUfpi import execAutomationWeb

from Windows.WindowDialog import MySetupDialog
from Windows.UpdateLogin import MyUpdateWindow

from typing import cast

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

class MyWindowLogin(Ui_WindowLogin, QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self._mySetup()

        self.threadPool = QThreadPool()
        
        self.loginButton.clicked.connect(self.setLogin)
        
        self.userLineEdit.installEventFilter(self)
        self.passwordLineEdit.installEventFilter(self)
        
    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        
        if event.type() == QEvent.Type.KeyPress:
            event = cast(QKeyEvent, event)
            if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
                self.enterLineEdit(watched)
                
        return super().eventFilter(watched, event)
    
    def enterLineEdit(self, watcher: QObject):
        if watcher == self.userLineEdit:
            self.passwordLineEdit.setFocus()
        else:
            self.loginButton.click()
            
    
        
    def setLogin(self):
        login = self.userLineEdit.text()
        password = self.passwordLineEdit.text()

        if self.lembrarMe.isChecked():
            self.threadPool.start(Thread(dbLogic.loginSave, login=login, password=password))

        self.loginThread = Thread(execAutomationWeb, login=login, password=password)
        self.loginThread.signal.started.connect(self.startedMensage)
        self.loginThread.signal.end.connect(self.sucessMensage)
        self.loginThread.signal.error.connect(self.errorMsg)
        self.threadPool.start(self.loginThread)

    def disableButton(self):
        self.loginButton.setEnabled(False)

    def activetButton(self):
        self.loginButton.setEnabled(True)
        
    def startedMensage(self):
        self.disableButton()

    def errorMsg(self, exception: Exception):
        if isinstance(exception, SystemError):
            print("Entrou no bloco SystemError")
            self.Update = MyUpdateWindow()
            self.Update.show()
            self.close()
        else:
            self.mensagem = MySetupDialog(f'Erro: {exception.__class__} \n\nPossivel Motivo do error:\n {str(exception)}')
            self.mensagem.exec()
            self.activetButton()
        
    def sucessMensage(self):
        self.mensagem = MySetupDialog(f'Sucesso: A solicitação de Login Foi enviada!!')
        self.mensagem.exec()
        self.close()
        

    def _mySetup(self):
        self.setWindowIcon(
            QIcon(str(Path(__file__).parent / 'files' / 'icons' / 'ufpi1.ico')))
        loginSenha = dbLogic.loginRecover()
        self.userLineEdit.setText(loginSenha[0])
        self.passwordLineEdit.setText(loginSenha[1])
        self.setFixedSize(self.width(), self.height())