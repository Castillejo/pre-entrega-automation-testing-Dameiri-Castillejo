import pytest
import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from selenium.webdriver.common.by import By
from utils.helpers import login_saucedeme, get_driver, USERNAME
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture # Reutilización. Evitar escribir el mismo código de configuración una y otra vez en cada prueba.
def driver():
    # Configuracion para consultar a selenium web driver
    driver = get_driver()
    yield driver # Devuelve el driver a las pruebas
    driver.quit () # Cierra el navegador al finalizar

# ============================================================
# TEST 1: ACTIVIDAD 1 - Login
# ============================================================

@pytest.mark.login # Ejecutar solo un subconjunto específico de tus pruebas
def test_login(driver):
    login_saucedeme(driver)
    """
    Verifica:
    - Que la URL contenga /inventory.html.
    - Que el título de la página sea 'Swag Labs'.
    - Capture de pantalla.
    """
    # Verificación de redirección a /inventory.html
    current_url = driver.current_url
    assert '/inventory.html' in current_url, f"No se redirigió correctamente: {current_url}"
    print(f"Redirección correcta a {current_url}")

    # Validación del título justo después del login en title
    assert "Swag Labs" in driver.title, f"Título inesperado: {driver.title}"
    print(f"Título de ventana: {driver.title}")

    # Captura opcional de pantalla
    driver.save_screenshot(f"screenshot_{USERNAME}.png")
    print(f"Capture de pantalla: screenshot_{USERNAME}.png")

# ============================================================
# TEST 2: ACTIVIDAD 2 - Explorar inventario
# ============================================================

@pytest.mark.catalogo # Ejecutar solo un subconjunto específico de tus pruebas
def test_catalogo(driver):
    login_saucedeme(driver)

    """
    Tras el login:
    - Verifica que el título de catálogo sea 'Products'.
    - Confirma que haya al menos un producto visible.
    - Imprime nombre y precio del primer producto.
    """

    # Validar título de catálogo
    titulo = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert titulo == 'Products', f"Título incorrecto: {titulo}"
    print(f"Título de catálogo: {titulo}")

    # Validar existencia de productos
    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(productos) > 0, "No hay productos visibles en el catálogo."
    print(f"Se encontraron {len(productos)} productos.")

    # Mostrar nombre y precio del primer producto
    primer_producto = productos[0]
    nombre = primer_producto.find_element(By.CLASS_NAME, 'inventory_item_name').text
    precio = primer_producto.find_element(By.CLASS_NAME, 'inventory_item_price').text
    print(f"Primer producto → {nombre} | Precio: {precio}")

# ============================================================
# TEST 3: ACTIVIDAD 3 - Carrito 
# ============================================================

@pytest.mark.carrito # Ejecutar solo un subconjunto específico de tus pruebas
def test_carrito(driver):
    login_saucedeme(driver)

    """
    - Añade el primer producto al carrito.
    - Verifica que el contador del carrito sea 1.
    - Entra al carrito y confirma que el producto esté listado.
    """

    # Verificar que haya productos
    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(productos) > 0, "No se encontraron productos en el inventario."

    # Añadir el primer producto al carrito
    # Otra opción... productos[0].find_element(By.TAG_NAME, 'button').click()
    productos[0] =  driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    
    # Espera a que el badge del carrito muestre "1"
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'shopping_cart_badge'), '1')
    )

    # Confirmar que el ícono del carrito muestre "1"
    badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert badge == '1', f"El carrito no muestra el valor esperado: {badge}"
    print(f"Carrito incrementado correctamente → {badge}")

    # Ir al carrito
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    # Verificar que el producto añadido esté listado
    items = driver.find_elements(By.CLASS_NAME, 'cart_item')
    assert len(items) == 1, f"El carrito no contiene el producto esperado ({len(items)} encontrados)"
    print(f"Producto visible en carrito: {items[0].text[:40]}...")


  