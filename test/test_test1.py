import sys
import os
import time

# Asegura que podamos importar desde la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browser_setup import start_browser
from pages.login import LoginPage

def test_login_page_elements():
    driver = start_browser()
    login_page = LoginPage(driver)

    # Cargar la página de login
    login_page.load("https://www.saucedemo.com/")
    

    # Verificar que el título de la página es correcto
    assert driver.title == "Swag Labs", "El título de la página no es el esperado"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))  # Asegúrate de que el selector sea correcto
    )   

    # Verificar que los elementos de la página están presentes
    assert login_page.is_username_field_present(), "El campo de nombre de usuario no está presente"
    assert login_page.is_password_field_present(), "El campo de contraseña no está presente"
    assert login_page.is_login_button_present(), "El botón de login no está presente"

    time.sleep(2)
    driver.quit()

# Test case 2: Verificar login con credenciales correctas
def test_login_success():
    driver = start_browser()
    login_page = LoginPage(driver)

    # Cargar página de login
    login_page.load("https://www.saucedemo.com/")

    # Login con usuario correcto
    login_page.login("standard_user", "secret_sauce")

    # Verificar si la URL cambió (indicando login exitoso)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "URL no es la esperada"

    # Verificar si se cargó la lista de productos
    assert login_page.is_inventory_page_loaded(), "La página de inventario no se cargó correctamente"

    time.sleep(2)
    driver.quit()

# Test case 3: Verificar login con credenciales incorrectas
def test_login_failure():
    driver = start_browser()
    login_page = LoginPage(driver)

    # Cargar página de login
    login_page.load("https://www.saucedemo.com/")

    # Login con credenciales incorrectas
    login_page.login("invalid_user", "wrong_password")

    # Verificar que se muestra un mensaje de error
    error_message = login_page.get_error_message()
    assert error_message == "Epic sadface: Username and password do not match any user in this service", "Mensaje de error no es el esperado"

    time.sleep(2)
    driver.quit()

# Test case 4: Verificar que el campo de usuario esté vacío al inicio
def test_empty_username_field():
    driver = start_browser()
    login_page = LoginPage(driver)

    # Cargar página de login
    login_page.load("https://www.saucedemo.com/")

    # Verificar que el campo de usuario esté vacío
    username_value = login_page.get_username_field_value()
    assert username_value == "", "El campo de usuario no está vacío"

    time.sleep(2)
    driver.quit()

# Más casos de prueba...
if __name__ == "__main__":
    import pytest
    pytest.main(["-q", "--tb=short"])  # Puedes agregar más opciones si las necesitas
