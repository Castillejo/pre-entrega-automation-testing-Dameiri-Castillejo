import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.support.ui import WebDriverWait
from conftest import URL
from utils.productos_json import get_productos_json

@pytest.mark.smoke
@pytest.mark.catalogo_POM
@pytest.mark.parametrize("nombre,precio,descripcion", get_productos_json())
def test_catalogo(driver, nombre, precio, descripcion):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_carrito_catalogo()
    
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

    # Buscar producto por nombre
    producto_pagina = inventory.buscar_producto_por_nombre(nombre)
    assert producto_pagina is not None, f"No se encontró el producto '{nombre}' en el catálogo."

    nombre_web = producto_pagina["nombre"]
    precio_web = producto_pagina["precio"]
    descripcion_web = producto_pagina["descripcion"]

    # Validar datos del producto contra el JSON
    assert nombre_web == nombre, f"Nombre distinto. Esperado: {nombre}, obtenido: {nombre_web}"
    assert float(precio_web) == float(precio), f"Precio distinto. Esperado: {precio}, obtenido: {precio_web}"
    assert descripcion_web == descripcion, f"Descripción distinta para {nombre}"

    print(f"Producto validado → {nombre_web} | Precio: {precio_web} | Descripción: {descripcion_web[:60]}...")

    # Logout confiable
    inventory.logout()
    WebDriverWait(driver, 10).until(lambda d: URL in d.current_url)
    assert URL in driver.current_url, "No se redirigió al login después del logout."
    print("Logout exitoso")
