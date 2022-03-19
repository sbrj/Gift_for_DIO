from selenium import webdriver
from imports import By, Keys, sleep
import csv
from imports import WebDriverWait, expect

def getDriver() -> object:
    driver = webdriver.Firefox()
    driver.get("https://web.dio.me/tracks")
    return driver

def getDriverUSR(dv: object, user: str) -> None:
    dv.get(f"https://web.dio.me/users/{user}")
    return None

def getXpath(driver: object, xpath: str) -> None:
    sleep(3)
    result = driver.find_element(by=By.XPATH, value=xpath)
    '''result = WebDriverWait(driver, 10, 4).until(
        expect.visibility_of_element_located(
        (By.XPATH, xpath)))'''
    result.click()
    sleep(2)
    return None

def getText(driver: object, text: str) -> None:
    sleep(2.5)
    result = driver.find_elements(by=By.XPATH, value=text)
    '''result = WebDriverWait(driver, 10, 4).until(
                        expect.visibility_of_all_elements_located(
                        (By.XPATH, text)))'''
    sleep(0.5)
    return result

def getEndPage(driver: object) -> None:       
        html = driver.find_element_by_tag_name('html')
        for i in range(12):
            html.send_keys(Keys.PAGE_DOWN)
            sleep(0.5)
        html.send_keys(Keys.END)
        sleep(1)
        return None

def getDown(driver: object) -> None:       
        html = driver.find_element_by_tag_name('html')
        for i in range(2):
            html.send_keys(Keys.PAGE_DOWN)
            sleep(0.5)
        sleep(1)
        return None

def getTopPage(driver: object) -> None:  
        html = driver.find_element_by_tag_name('html')     
        html.send_keys(Keys.HOME)
        sleep(2)
        return None

def listaBoots(driver: object) -> list:  
        sleep(5)      
        #lista = WebDriverWait(driver, 120, 30).until(
        #        expect.visibility_of_any_elements_located(
        #        (By.XPATH, "//h3")))
        lista = driver.find_elements(By.XPATH, value="//h3")
        sleep(5)
        return lista

def manipulaArquivo(c_refinados: list, arq: str) -> None:
    with open(arq, 'w', encoding='utf8') as arquivo:
        for index, linha in enumerate(c_refinados):
                arquivo.write(str(index))
                arquivo.write(' - ')
                arquivo.write(linha)
                arquivo.write('\n')
    arquivo.close()
    return None

def getCidadeEstado(cid_est: str) -> str:
    if cid_est != '':
        dados = cid_est.split(' - ')
        cid = dados[0]
        est = dados[1]
    else:
        cid = ''
        est = ''
    
    return cid, est

def manipulaDevs(lista_devs: list, link_devs: list, arq: str) -> None:
    lista_ind = []
    with open(arq, 'a', encoding='utf8', newline='') as arquivo:
        writer = csv.writer(arquivo)
        for index, linha in enumerate(lista_devs):
            if (index % 2 == 0):
                lista_ind.append(linha)
            else:
                cidade, estado = getCidadeEstado(linha)
                lista_ind.append(cidade)
                lista_ind.append(estado)
                lista_ind.append(link_devs[int(index/2)])
                writer.writerow(lista_ind)  
                lista_ind.clear()
    arquivo.close()
    return None

def manipulaXP(d_pontos: dict, arq: str) -> None:
    with open(arq, 'a', encoding='utf8', newline='') as arquivo:
        writer = csv.writer(arquivo)
        vai_arquivo = [[chave, valor] for chave, valor in d_pontos.items()]
        writer.writerow(vai_arquivo[0])  
    arquivo.close()
    return None