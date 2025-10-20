import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.mark.smoke
@pytest.mark.carrito_POM
def test_carrito(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login()

    # Inventario
    inventory = InventoryPage(driver)
    assert inventory.esta_en_pagina_inventario(), "No se cargó la página de inventario."

    inventory.agregar_producto_por_indice(0)
    inventory.esperar_conteo_carrito("1")
    badge = inventory.obtener_conteo_carrito()
    assert badge == "1"
    print(f"Carrito incrementado correctamente → {badge}")

    inventory.ir_al_carrito()
    cart = CartPage(driver)
    cart.esperar_productos_en_carrito()
    items = cart.contar_items()
    assert items >= 1
    print(f"Producto visible en carrito ({items} encontrado/s).")

    # Captura de pantalla
    archivo = f"screenshot_{badge}_badge.png"
    driver.save_screenshot(archivo)
    print(f"Captura de pantalla guardada: {archivo}")
