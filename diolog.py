from unicodedata import numeric
from login import email, senha
def __setEmail() -> str:
    v_email = email
    return v_email

def __setSenha() -> str:
    v_senha = senha
    return v_senha

login = __setEmail()
password = __setSenha()
xpath_login = "//input[@placeholder='Digite seu e-mail']"
xpath_senha = "//input[@placeholder='Digite sua senha']"
esquecer = '/html/body/div[4]/div/div[1]/div/div/div/div/div/div[2]/div/div[3]/button'
camps = '/html/body/div[1]/div/header/nav/ul/li[2]/a/span'
cognizant = "//*[contains(text(), 'Cognizant Cloud Data Engineer #2')]"
conteudo = '/html/body/div[1]/div/div[2]/div[3]/div[1]/div/button'
todos_devs = "//*[contains(text(), 'VER TODOS')]"
devs_lista = '//a[contains(@href,"/track/users/")]'
pega_xp = ''



