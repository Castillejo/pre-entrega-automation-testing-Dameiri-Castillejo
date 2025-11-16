import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage

@pytest.mark.smoke
@pytest.mark.checkout_POM1111
def test_checkout(driver):

    # LOGIN
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_carrito_catalogo()

    # Agregar producto
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Ir al carrito
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    # Iniciar Checkout
    driver.find_element(By.ID, "checkout").click()

    # Completar formulario
    driver.find_element(By.ID, 'first-name').send_keys('Test')
    driver.find_element(By.ID, 'last-name').send_keys('User')
    driver.find_element(By.ID, 'postal-code').send_keys('12345')

    # Botón continue
    driver.find_element(By.ID, 'continue').click()

    # Esperar el botón finish
    finish_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "finish"))
    )
    finish_btn.click()

    # Validar mensaje final
    mensaje = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    assert 'Thank you for your order!' in mensaje.text
