import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from conftest import USERNAME

@pytest.mark.smoke
@pytest.mark.login_POM
def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login()

    inventory = InventoryPage(driver)
    assert inventory.esta_en_pagina_inventario(), f"No se redirigió correctamente: {driver.current_url}"
    print(f"Redirección correcta a {driver.current_url}")
    assert inventory.obtener_titulo_navegador() == "Swag Labs", f"Título inesperado: {driver.title}"
    print(f"Título de ventana: {driver.title}. Inicio de sesión exitoso")

    driver.save_screenshot(f"screenshot_{USERNAME}.png")
    print(f"Capture de pantalla: screenshot_{USERNAME}.png")
