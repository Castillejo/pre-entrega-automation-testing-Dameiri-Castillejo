from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    _ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    _ITEM_DESC = (By.CLASS_NAME, "inventory_item_desc") 


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def esperar_productos_en_carrito(self):
        self.wait.until(EC.presence_of_all_elements_located(self._CART_ITEMS))

    #def esperar_productos_en_carrito(self):
        #self.wait.until(EC.presence_of_element_located(self._CART_ITEMS))

    #def esperar_productos_en_carrito(self):
       # print(f"[DEBUG] Esperando productos en carrito, URL actual: {self.driver.current_url}")
       # self.wait.until(EC.visibility_of_all_elements_located(self._CART_ITEMS))

    def obtener_items(self):
        return self.driver.find_elements(*self._CART_ITEMS)

    def contar_items(self):
        return len(self.obtener_items())
    
    def obtener_producto_por_nombre(self, nombre):
        items = self.driver.find_elements(*self._CART_ITEMS)
        for item in items:
            nombre_item = item.find_element(*self._ITEM_NAME).text
            if nombre_item == nombre:
                precio = item.find_element(*self._ITEM_PRICE).text
                descripcion = item.find_element(*self._ITEM_DESC).text
                return {"nombre": nombre_item, "precio": precio, "descripcion": descripcion}
        return None
    
    

