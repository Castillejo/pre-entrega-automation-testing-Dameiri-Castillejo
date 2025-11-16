import pytest
import re
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.productos_json import get_productos_json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import tomar_screenshot

def limpiar_nombre_archivo(nombre):
    """Eliminar caracteres que no se pueden usar en nombres de archivo"""
    return re.sub(r'[^a-zA-Z0-9_-]', '_', nombre)

@pytest.mark.smoke
@pytest.mark.carrito_POM
@pytest.mark.parametrize("nombre,precio,descripcion", get_productos_json())
def test_carrito(driver, nombre, precio, descripcion):
    # --- Login ---
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_carrito_catalogo()

    # --- Inventario ---
    inventory = InventoryPage(driver)
    assert inventory.esta_en_pagina_inventario(), "No se cargó la página de inventario."

    # --- Agregar producto específico ---
    productos = inventory.obtener_productos()
    agregado = False
    for idx, p in enumerate(productos):
        nombre_item = p.find_element(*inventory._PRODUCT_NAMES).text
        if nombre_item == nombre:
            inventory.agregar_producto_por_indice(idx)
            agregado = True
            break

    assert agregado, f"Producto '{nombre}' no encontrado en inventario."

    # --- Validar badge del carrito ---
    inventory.esperar_conteo_carrito("1")
    badge = inventory.obtener_conteo_carrito()
    assert badge == "1", f"Badge esperado 1, obtenido {badge}"
    print(f"[INFO] Carrito incrementado correctamente → {badge}")

    # --- Captura de pantalla después de agregar ---
    tomar_screenshot(driver, f"producto_agregado_{limpiar_nombre_archivo(nombre)}")

    # --- Ir al carrito ---
    inventory.ir_al_carrito()

    # --- Esperar a que los productos estén visibles en el carrito ---
    cart = CartPage(driver)
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
    )
    cart.esperar_productos_en_carrito()

    # --- Validar que haya al menos 1 producto en el carrito ---
    items = cart.contar_items()
    assert items >= 1, f"No se encontraron productos en el carrito para '{nombre}'"
    print(f"[INFO] Producto visible en carrito ({items} encontrado/s).")

    # --- Captura de pantalla en carrito ---
    tomar_screenshot(driver, f"producto_en_carrito_{limpiar_nombre_archivo(nombre)}")


"""
    # Captura de pantalla con nombre del producto
    nombre_archivo = limpiar_nombre_archivo(nombre)
    archivo = f"screenshot_{nombre_archivo}_badge{badge}.png"
    driver.save_screenshot(archivo)
    print(f"[INFO] Captura de pantalla guardada: {archivo}")

"""














