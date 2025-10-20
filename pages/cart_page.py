from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def esperar_productos_en_carrito(self):
        self.wait.until(EC.presence_of_element_located(self._CART_ITEMS))

    def obtener_items(self):
        return self.driver.find_elements(*self._CART_ITEMS)

    def contar_items(self):
        return len(self.obtener_items())
