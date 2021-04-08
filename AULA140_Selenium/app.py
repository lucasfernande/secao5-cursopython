from selenium import webdriver
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=Perfil')  # definindo a pasta de perfil de usuário
        self.chrome = webdriver.Chrome(self.driver_path, options=self.options)

    def acessa(self, site): # função para acessar sites
        self.chrome.get(site)

    def sair(self): # função para fechar o navegador
        self.chrome.quit()


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://g1.globo.com')

    sleep(2)
    chrome.sair()
