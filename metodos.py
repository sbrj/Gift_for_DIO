from selenium import webdriver
from imports import By, WebDriverWait, expect,  Keys, sleep

def getDriver() -> object:
    driver = webdriver.Firefox()
    driver.get("https://web.dio.me/tracks")
    return driver

def getXpath(driver: object, xpath: str) -> None:
    sleep(2)
    result = driver.find_element(by=By.XPATH, value=xpath)
    result.click()
    sleep(2)
    return None

def getText(driver: object, text: str) -> None:
    sleep(2)
    result = driver.find_element(by=By.PARTIAL_LINK_TEXT, value=text)
    result.click()
    sleep(2)
    return None

def getEndPage(driver: object) -> None:       
        html = driver.find_element_by_tag_name('html')
        for i in range(12):
            html.send_keys(Keys.PAGE_DOWN)
            sleep(0.5)
        html.send_keys(Keys.END)
        sleep(3)
        return None

def listaBoots(driver: object) -> list:  
        sleep(5)      
        #lista = WebDriverWait(driver, 120, 30).until(
        #        expect.visibility_of_any_elements_located(
        #        (By.XPATH, "//h3")))
        lista = driver.find_elements(By.XPATH, value="//h3")
        sleep(5)
        return lista

def manipulaArquivo(c_refinados: list) -> None:
    with open('cursos.txt', 'w', encoding='utf8') as arquivo:
        for index, linha in enumerate(c_refinados):
                arquivo.write(str(index))
                arquivo.write(' - ')
                arquivo.write(linha)
                arquivo.write('\n')
    return None