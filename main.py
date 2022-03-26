import time

ini = time.time()
print(ini)

if __name__ == "__main__":
    try:    
        from bootcamps import *
        #from buscadevs import *
    except Exception as error:
        print('Erro Main: ', error)
    finally:
        from buscapontos import *
        driver.close()
        fim = time.time()
        print('Tempo de execução: ', fim-ini)
        print(fim)
