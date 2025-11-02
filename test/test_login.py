import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.login_csv import get_login_csv

@pytest.mark.smoke
@pytest.mark.login_POM
@pytest.mark.parametrize("username,password,login_bool", get_login_csv())
def test_login(driver, username, password, login_bool):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)

    if login_bool:
        # Si el login debe funcionar
        inventory = InventoryPage(driver)
        assert inventory.esta_en_pagina_inventario(), f"No se redirigió correctamente: {driver.current_url}"
        print(f"Redirección correcta a {driver.current_url}")
        assert inventory.obtener_titulo_navegador() == "Swag Labs", f"Título inesperado: {driver.title}"
        print(f"Título de ventana: {driver.title}. Inicio de sesión exitoso")
    else:
        # Si el login debe fallar
        assert login_page.mensaje_error_visible(), f"Se esperaba error de login para usuario {username}"
        print(f"Login fallido correctamente para usuario {username}")

    # Captura siempre
    driver.save_screenshot(f"screenshot_{username}.png")
    print(f"Captura de pantalla: screenshot_{username}.png")
