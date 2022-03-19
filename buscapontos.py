'''from imports import *
from metodos import getDriver, getDriverUSR, getText, getXpath, getEndPage, listaBoots, manipulaArquivo, manipulaXP
from secrets import DadosSecretos

driver = getDriver()

#preenche dados
email = DadosSecretos(driver, xpath_login, login)
senha = DadosSecretos(driver, xpath_senha, password, 'y')

sleep(2)
getXpath(driver, esquecer)



import csv
#from metodos import getDriver, getXpath

#dv = getDriver()
'''
from metodos import manipulaXP, getDriverUSR, getText
from bootcamps import driver, sleep
import csv
sleep(4)
dict_pontos = {}
try:
    with open('C:\Gift_for_DIO\devs.csv', 'r', encoding='UTF8') as arq:
        arquivo = csv.reader(arq)
        for i, usuario in enumerate(arquivo):
            '''        
            if i == 2:
                driver.close()
                break
            else:
            ''' 
            getDriverUSR(driver, usuario[-1])
            sleep(4)
            pontos = getText(driver, '/html/body/div[1]/div/div/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div[4]/div/span')
            #print('pontos - ', pontos)
            #print('pontos.text - ', pontos[0].text)
            xp = [pt.text.split(' / ')[0].split(' ')[1] for pt in pontos]
            dict_pontos[usuario[-1]] = xp[0]
            manipulaXP(dict_pontos, 'pontos.csv')
            sleep(0.5)
            dict_pontos.clear()

except Exception as error:
    print('Erro Buscapontos: ', error)
finally:
    sleep(2)
    print('Done Busca Pontos')        

