from selenium.webdriver import Edge, EdgeService, EdgeOptions
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pathlib import Path
from time import sleep

# from app.setupLogin import setup

class MyEdge(Edge):
    def __init__(self, keep_alive=True) -> None:
        try:
            options = self._myEdgeOptions()
            service = self._myEdgeService()
            super().__init__(options, service, keep_alive)
        except:
            raise SystemError("- Algum drive está desatualizado!")
            
    def _myEdgeOptions(self) -> EdgeOptions:
        options = EdgeOptions()
        # options.add_argument('headless')
        return options

    def _myEdgeService(self) -> EdgeService:
        with open(Path(__file__).parent / 'localDrive.txt', 'r') as arq:
            CAMINHO = arq.read()
            
        service = EdgeService(CAMINHO)
        return service


class AutomationWeb(MyEdge):
    def __init__(self, user, password) -> None:
        self._user = user
        self._password = password
        super().__init__()

    def getScreenLogin(self):
        try:
            self.get(
                f"https://login.picos.ufpi.br:6082/php/uid.php?vsys=1&rule=3&url=http://google.com.br%2f")
        except:
            raise ConnectionError(f"- Você não está conectado ao Wi-Fi da Ufpi.\n- O Wi-Fi da UFPI não está funcionando.")

    def login(self):
        try:
            userLoginInput: WebElement
            userLoginInput = WebDriverWait(self, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH,
                    '/html/body/div[1]/form/div/div[1]/table/tbody/tr[1]/td[2]/input')
                )
            )

            passwordLoginInput: WebElement
            passwordLoginInput = WebDriverWait(self, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH,
                    '/html/body/div[1]/form/div/div[1]/table/tbody/tr[2]/td[2]/input')
                )
            )

            buttonLoginInput: WebElement
            buttonLoginInput = WebDriverWait(self, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH,
                    '/html/body/div[1]/form/div/div[1]/table/tbody/tr[3]/td[2]/input')
                )
            )

            userLoginInput.send_keys(self._user)
            passwordLoginInput.send_keys(self._password)
            buttonLoginInput.click()
        except:
            raise ConnectionError(f"- O Wi-Fi da UFPI não está funcionando. \n- Você foi desconectado da rede da UFPI.")
        
            
        try:
            userLoginInput: WebElement
            userLoginInput = WebDriverWait(self, 1).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH,
                    '/html/head/meta[1]')
                )
            )
        except:
            raise ConnectionRefusedError("-Usuario ou senha Invalido \n - O Wi-Fi da UFPI não está funcionando.")
        

def execAutomationWeb(login: str, password: str):
    web = AutomationWeb(login, password)
    web.getScreenLogin()
    web.login()
        