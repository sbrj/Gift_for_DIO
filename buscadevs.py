from time import sleep
from metodos import getDown, getTopPage, getXpath, getText, manipulaArquivo, manipulaDevs, webdriver, Keys
from bootcamps import driver, By
from diolog import todos_devs, devs_lista

#Entra nas paginas
getTopPage(driver)
getXpath(driver, todos_devs)
ran = range(1,492)
try:
    for i in ran:
        if i == 1:
            sleep(2)
            getDown(driver)
        
        sleep(2)
        
        lista_devs = getText(driver, devs_lista)

        #Um pouco de list comprehension para facilitar a lista com as infos dos devs e os respectivos nomes de usuários
        devs = [dev.text for dev in lista_devs]
        links = [lnk.get_attribute("href").split('/')[-1] for i, lnk in enumerate(lista_devs) if i%2==1]
            
        sleep(0.5)
        
        #Grava as infos da pagina
        manipulaDevs(devs, links, 'devs.csv')
        
        if i == ran[-1]:
            pass
        else:
            #Pega próxima pagina
            b_text = i+1    
            numero = getXpath(driver, f'//button[text()="{b_text}"]')

except Exception as error:
    print('Erro Buscadevs: ', error)
finally:
    sleep(2)
    print('Done Busca Devs')
    