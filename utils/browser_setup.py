#importa selenium
from selenium import webdriver
#importa la clase de service que se encarga de iniciar el servicio de Chromedriver 
from selenium.webdriver.chrome.service import Service
#Options permite configurar el navegador, por ejemplo: abrirlo maximizado, en modo headless (sin ventana), desactivar notificaciones, etc.
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os 
from dotenv import load_dotenv
def start_browser():
    #Creamos un objeto options que nos permite configurar Chrome antes de iniciarlo
    chrome_Options = Options()
    #Añadimos una opción para que Chrome se abra maximizado.
    chrome_Options.add_argument("--start-maximized")
   #Añadimos una opción para que Chrome se abra maximizado.
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_Options)
    #Añadimos una opción para que Chrome se abra maximizado.
    driver.implicitly_wait(10)
    return driver  