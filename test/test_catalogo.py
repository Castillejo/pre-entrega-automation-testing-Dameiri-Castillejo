import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.support.ui import WebDriverWait
from conftest import URL, tomar_screenshot
from utils.productos_json import get_productos_json

@pytest.mark.smoke
@pytest.mark.catalogo_POM
def test_catalogo_todos_productos(driver):
    # Iniciar sesión una sola vez
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_carrito_catalogo()
    
    # Instanciar inventario
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

    # Iterar sobre todos los productos del JSON
    for producto in get_productos_json():
        nombre, precio, descripcion = producto
        producto_pagina = inventory.buscar_producto_por_nombre(nombre)
        assert producto_pagina is not None, f"No se encontró el producto '{nombre}' en el catálogo."

        nombre_web = producto_pagina["nombre"]
        precio_web = producto_pagina["precio"]
        descripcion_web = producto_pagina["descripcion"]

        # Validar datos del producto
        assert nombre_web == nombre, f"Nombre distinto. Esperado: {nombre}, obtenido: {nombre_web}"
        assert float(precio_web) == float(precio), f"Precio distinto. Esperado: {precio}, obtenido: {precio_web}"
        assert descripcion_web == descripcion, f"Descripción distinta para {nombre}"

        print(f"Producto validado → {nombre_web} | Precio: {precio_web} | Descripción: {descripcion_web[:60]}...")
        tomar_screenshot(driver, f"{nombre_web}_{precio_web}", estado="pass")

    # Logout confiable al final
    inventory.logout()
    WebDriverWait(driver, 10).until(lambda d: URL in d.current_url)
    assert URL in driver.current_url, "No se redirigió al login después del logout."
    print("Logout exitoso de todos los productos")



# ============================================================
# TEST Login por cada producto
# ============================================================

"""

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.support.ui import WebDriverWait
from conftest import URL
from utils.productos_json import get_productos_json
from conftest import URL, tomar_screenshot

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
  
    tomar_screenshot(driver, f"{nombre_web}_{precio_web}", estado="pass")

    # Logout confiable
    inventory.logout()
    WebDriverWait(driver, 10).until(lambda d: URL in d.current_url)
    assert URL in driver.current_url, "No se redirigió al login después del logout."
    print("Logout exitoso")

"""