from imports import By, WebDriverWait, expect,  Keys, sleep

class DadosSecretos():
        
        def __init__(self, driver: object, location: str, field: str, send='n') -> None:
            self.driver = driver
            self.entrada = self.__getData(self.driver, location)
            self.enviar = self.__sendData(self.entrada, field, send)
            return None

        def __getData(self, driver: object, data: str) -> object:
                dados = WebDriverWait(driver, 10, 1).until(
                        expect.visibility_of_element_located(
                        (By.XPATH, data)))
                return dados

        def __sendData(self, entrada: object, data: str, send:str) -> None:
                dados = entrada
                dados.send_keys(data)
                if send == 'y':
                        dados.send_keys(Keys.RETURN)
                        sleep(4)
                return None