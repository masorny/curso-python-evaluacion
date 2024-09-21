# Inicializar librerias y configuraciones.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from evento import insertarlog

# Configuracion
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")

# Ruta del chromedriver.exe
chromedriver_path = "C:\\Users\\Adrian MR\\Desktop\\Projects\\Python\\curso-evaluacion\\chromedriver.exe"

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

def initialize(url: str, matricula: str, clave: str):
    '''
    Inicializa el Web Scraping.
    '''

    driver.get(url)

    cingreso = driver.find_element(By.ID, "codigo")
    contrasena = driver.find_element(By.ID, "password")
    ingresar = driver.find_element(By.XPATH, """//*[@id="mod_alumno"]/button""")

    cingreso.send_keys(matricula)
    contrasena.send_keys(clave)

    ingresar.click()

    try:
        driver.find_element(By.XPATH, """//*[@id="mod_alumno"]/span""")
        print("No se ha podido iniciar sesion.")
    except Exception as e:
        print('Se ha iniciado sesion correctamente.')

        insertarlog(url, matricula)
        sleep(10)
        driver.quit()