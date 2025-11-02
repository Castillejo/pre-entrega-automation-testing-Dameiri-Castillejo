from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from conftest import URL, USERNAME, PASSWORD

class LoginPage:
    _INPUT_NAME = (By.NAME, "user-name")
    _INPUT_PASSWORD = (By.NAME, "password")
    _LOGIN_BUTTON = (By.NAME, "login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self):
        """Abre la URL definida en conftest"""
        self.driver.get(URL)

    def login(self, username, password):
        """Realiza el login con las credenciales proporcionadas."""
        self.wait.until(EC.element_to_be_clickable(self._INPUT_NAME)).clear()
        self.wait.until(EC.element_to_be_clickable(self._INPUT_NAME)).send_keys(username)

        self.wait.until(EC.element_to_be_clickable(self._INPUT_PASSWORD)).clear()
        self.wait.until(EC.element_to_be_clickable(self._INPUT_PASSWORD)).send_keys(password)

        self.wait.until(EC.element_to_be_clickable(self._LOGIN_BUTTON)).click()

    def mensaje_error_visible(self, timeout=3):
        """
        Verifica si el mensaje de error de login está visible.
        Retorna True si lo encuentra, False si no.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self._ERROR_MESSAGE)
            )
            return True
        except:
            return False
        
    def login_carrito_catalogo(self, username=USERNAME, password=PASSWORD):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self._INPUT_NAME)).send_keys(username)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self._INPUT_PASSWORD)).send_keys(password)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self._LOGIN_BUTTON)).click()
    

