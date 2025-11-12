import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

@pytest.mark.smoke
@pytest.mark.checkout_POM
def test_checkout(driver):
    # --- LOGIN ---
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_carrito_catalogo()  # tu método de login

    # --- INVENTARIO: agregar producto ---
    inventory = InventoryPage(driver)
    inventory.agregar_producto_por_indice(0)
    inventory.ir_al_carrito()

    # Esperar página carrito
    WebDriverWait(driver, 10).until(EC.url_contains("cart.html"))

    # --- CHECKOUT ---
    checkout = CheckoutPage(driver)
    checkout.iniciar_checkout()

    # Esperar página checkout-step-one
    WebDriverWait(driver, 10).until(EC.url_contains("checkout-step-one.html"))

    # Completar formulario usando React-friendly inputs
    checkout.completar_formulario("Juan", "Tester", "1234")

    # Verificar que los campos estén realmente completados
    first_val = driver.find_element(*checkout._FIRST_NAME).get_attribute("value")
    last_val = driver.find_element(*checkout._LAST_NAME).get_attribute("value")
    zip_val = driver.find_element(*checkout._ZIP_CODE).get_attribute("value")

    assert first_val == "Juan", f"Expected 'Juan', got '{first_val}'"
    assert last_val == "Tester", f"Expected 'Tester', got '{last_val}'"
    assert zip_val == "1234", f"Expected '1234', got '{zip_val}'"

    # Continuar al resumen
    checkout.continuar_checkout()

    # Finalizar checkout
    checkout.finalizar_checkout()

    # Verificación final: mensaje de confirmación
    assert "THANK YOU FOR YOUR ORDER" in driver.page_source
