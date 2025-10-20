from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    _TITLE = (By.CLASS_NAME, "title")
    _PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    _PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    _ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='add-to-cart']")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_titulo_pagina(self):
        return self.driver.find_element(*self._TITLE).text

    def obtener_titulo_navegador(self):
        return self.driver.title

    def esta_en_pagina_inventario(self):
        return "inventory.html" in self.driver.current_url

    def obtener_productos(self):
        return self.driver.find_elements(*self._PRODUCTS)

    def contar_productos(self):
        return len(self.obtener_productos())

    def obtener_nombre_producto(self, index=0):
        productos = self.obtener_productos()
        return productos[index].find_element(*self._PRODUCT_NAMES).text

    def obtener_precio_producto(self, index=0):
        productos = self.obtener_productos()
        return productos[index].find_element(*self._PRODUCT_PRICES).text

    def agregar_producto_por_indice(self, index=0):
        botones = self.driver.find_elements(*self._ADD_TO_CART_BUTTONS)
        botones[index].click()

    def obtener_conteo_carrito(self):
        badge = self.driver.find_element(*self._CART_BADGE)
        return badge.text

    def esperar_conteo_carrito(self, valor_esperado):
        self.wait.until(EC.text_to_be_present_in_element(self._CART_BADGE, valor_esperado))

    def ir_al_carrito(self):
        self.driver.find_element(*self._CART_LINK).click()
