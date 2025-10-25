import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.support.ui import WebDriverWait
from conftest import URL


@pytest.mark.smoke
@pytest.mark.catalogo_POM
def test_catalogo(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login()
    
    # Verificar que se está en la página de inventario
    inventory = InventoryPage(driver)
    assert inventory.esta_en_pagina_inventario(), "No se cargó la página de inventario."

    # Verificar título de la página
    titulo = inventory.obtener_titulo_pagina()
    assert titulo == "Products", f"Título incorrecto: {titulo}"
    print(f"Título de catálogo: {titulo}")

    # Verificar que haya productos visibles
    cantidad = inventory.contar_productos()
    assert cantidad > 0, "No hay productos visibles en el catálogo."
    print(f"Se encontraron {cantidad} productos.")

    # Mostrar información del primer producto
    nombre = inventory.obtener_nombre_producto(0)
    precio = inventory.obtener_precio_producto(0)
    print(f"Primer producto → {nombre} | Precio: {precio}")

    # Cerrar sesión de manera confiable
    inventory.logout()

    # Esperar a que la URL vuelva a la de login
    WebDriverWait(driver, 10).until(lambda d: URL in d.current_url)
    assert URL in driver.current_url, "No se redirigió al login después del logout."
    print("Logout exitoso")

   