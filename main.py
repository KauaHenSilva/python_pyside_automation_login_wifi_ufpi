from Windows.LoginWindow import MyWindowLogin
from Windows.SetupWindow import MySetupWindow

from PySide6.QtWidgets import QApplication

from qdarktheme import setup_theme

import os
from pathlib import Path

CAMINHO_DRIVE = Path(__file__).parent / 'app' / 'localDrive.txt'

if __name__ == '__main__':
    app = QApplication()
    setup_theme()

    if os.path.exists(CAMINHO_DRIVE):
        windowLogin = MyWindowLogin()
        windowLogin.show()
    else:
        windowSetup = MySetupWindow()
        windowSetup.show()

    app.exec()
