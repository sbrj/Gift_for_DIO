from imports import *
from metodos import getDriver, getText, getXpath, getEndPage, listaBoots, manipulaArquivo
from secrets import DadosSecretos

try:    
    driver = getDriver()

    #preenche dados
    email = DadosSecretos(driver, xpath_login, login)
    senha = DadosSecretos(driver, xpath_senha, password, 'y')

    #abre paginas
    sleep(2)
    getXpath(driver, esquecer)
    getXpath(driver, camps)
    getXpath(driver, cognizant)
    '''
        getXpath(driver, conteudo)

        #vai até final pagina
        getEndPage(driver)

        #lista todos os cursos do bootcamp
        lista = listaBoots(driver)
        cursos = [curso.text for curso in lista]
        cursos_refinados = cursos[1:-1]

        #grava, com índice, em um arquivo *.txt
        manipulaArquivo(cursos_refinados, 'cursos.txt')
    '''
except Exception as error:
    print('Erro Bootcamps: ', error)
finally:
    print('Done Bootcamps')