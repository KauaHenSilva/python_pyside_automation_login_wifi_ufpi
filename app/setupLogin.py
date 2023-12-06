from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pathlib import Path

from requests import exceptions

def setup():
    try:
        local = EdgeChromiumDriverManager().install()
        with open(Path(__file__).parent / 'localDrive.txt', 'w') as arq:
            arq.write(local)
    except exceptions.ConnectionError:
        raise exceptions.ConnectionError("Você não está conectado a Internet!\n\t(Esse processo só acontece uma vez, gasta poucos dados!)")

if __name__ == '__main__':
    setup()