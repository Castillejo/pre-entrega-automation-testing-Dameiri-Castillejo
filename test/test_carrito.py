import pytest
import re
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.productos_json import get_productos_json

def limpiar_nombre_archivo(nombre):
    """Eliminar caracteres que no se pueden usar en nombres de archivo"""
    return re.sub(r'[^a-zA-Z0-9_-]', '_', nombre)

@pytest.mark.smoke
@pytest.mark.carrito_POM
@pytest.mark.parametrize("nombre,precio,descripcion", get_productos_json())
def test_carrito(driver, nombre, precio, descripcion):
    # Login
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_carrito_catalogo()

    # Inventario
    inventory = InventoryPage(driver)
    assert inventory.esta_en_pagina_inventario(), "No se cargó la página de inventario."

    # Agregar producto específico por nombre
    productos = inventory.obtener_productos()
    agregado = False
    for idx, p in enumerate(productos):
        nombre_item = p.find_element(*inventory._PRODUCT_NAMES).text
        if nombre_item == nombre:
            inventory.agregar_producto_por_indice(idx)
            agregado = True
            break

    assert agregado, f"Producto '{nombre}' no encontrado en inventario."

    # Validar badge del carrito
    inventory.esperar_conteo_carrito("1")
    badge = inventory.obtener_conteo_carrito()
    assert badge == "1", f"Badge esperado 1, obtenido {badge}"
    print(f"[INFO] Carrito incrementado correctamente → {badge}")

    # Ir al carrito
    inventory.ir_al_carrito()
    cart = CartPage(driver)
    cart.esperar_productos_en_carrito()

    # Validar que haya al menos 1 producto en el carrito
    items = cart.contar_items()
    assert items >= 1, f"No se encontraron productos en el carrito para '{nombre}'"
    print(f"[INFO] Producto visible en carrito ({items} encontrado/s).")

    # Captura de pantalla con nombre del producto
    nombre_archivo = limpiar_nombre_archivo(nombre)
    archivo = f"screenshot_{nombre_archivo}_badge{badge}.png"
    driver.save_screenshot(archivo)
    print(f"[INFO] Captura de pantalla guardada: {archivo}")








