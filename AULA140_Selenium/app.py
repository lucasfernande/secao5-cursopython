from selenium import webdriver
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=Perfil')  # definindo a pasta de perfil de usuário
        self.chrome = webdriver.Chrome(self.driver_path, options=self.options)

    def acessa(self, site):  # função para acessar sites
        self.chrome.get(site)

    def sair(self):  # função para fechar o navegador
        self.chrome.quit()

    def clicar_entrar(self):  # função para clicar no botão entrar
        try:
            btn_sign_in = self.chrome.find_element_by_link_text('Sign in')
            btn_sign_in.click()
        except Exception as e:
            print(f'Erro: {e}')

    def fazer_login(self):
        try:
            input_login = self.chrome.find_element_by_id('login_field')  # selecionando o campo email
            input_password = self.chrome.find_element_by_id('password')  # selecionando o campo senha

            input_login.send_keys('lucasfernandemwm@gmail.com')
            input_password.send_keys('ap3kilimei')

            btn_sign_in = self.chrome.find_element_by_name('commit')
            btn_sign_in.click()
        except Exception as e:
            print(f'Erro no login: {e}')


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')
    chrome.clicar_entrar()
    chrome.fazer_login()

    sleep(5)
    chrome.sair()
