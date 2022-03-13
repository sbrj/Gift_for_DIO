from time import sleep
from metodos import getTopPage, getXpath, getText, manipulaArquivo, manipulaDevs, webdriver, Keys
from bootcamps import driver, By
from diolog import todos_devs, devs_lista
getTopPage(driver)
getXpath(driver, todos_devs)
try:
    for i in range(1,376):
        if i == 1:
            sleep(1)
            html = driver.find_element_by_tag_name('html')
            for i in range(2):
                html.send_keys(Keys.PAGE_DOWN)
                sleep(1)
            sleep(4)
        sleep(2)
        lista_devs = getText(driver, devs_lista)
        sleep(1)
        devs = [dev.text for dev in lista_devs]
        sleep(0.5)
        manipulaDevs(devs, 'devs.txt')
        sleep(2)
        b_text = i+1    
        print('i - ', i)
        numero = driver.find_element(By.XPATH, value=f'//button[text()="{b_text}"]')
        sleep(0.5)
        print('numero --- ', numero.text)
        sleep(0.5)
        numero.click()
except Exception as error:
    print('erro ---- ', error)
finally:
    print('done')
    #lista2 = driver.find_element_by_css_selector('[href^=https://web.dio.me/track/users/]')
    #manipulaArquivo(lista2, 'devs2.txt')