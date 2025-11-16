import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.smoke
@pytest.mark.checkout_POM
def test_checkout(driver):

    # --- LOGIN ---
    login = LoginPage(driver)
    login.open()
    login.login_carrito_catalogo()

    # --- INVENTORY ---
    inventory = InventoryPage(driver)
    inventory.agregar_producto_por_indice(0)
    inventory.ir_al_carrito()

    # --- CART ---
    cart = CartPage(driver)
    cart.esperar_productos_en_carrito()

    # --- CHECKOUT ---
    checkout = CheckoutPage(driver)
    checkout.iniciar_checkout()
    checkout.completar_formulario("Test", "User", "12345")
    checkout.continuar_checkout()
    checkout.finalizar_checkout()

    # --- VALIDAR ---
    mensaje = checkout.obtener_mensaje_final()
    assert "THANK YOU FOR YOUR ORDER!" in mensaje.upper(), f"Mensaje esperado no encontrado, se obtuvo: {mensaje}"
