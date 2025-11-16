from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutPage:
    _MENU_BUTTON = (By.ID, 'react-burger-menu-btn')  # botón del menú
    _LINK_LOGOUT = (By.ID, 'logout_sidebar_link')   # link de logout

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def logout(self):
        # Click en el menú usando JS para evitar overlay
        menu_btn = self.wait.until(EC.element_to_be_clickable(self._MENU_BUTTON))
        self.driver.execute_script("arguments[0].click();", menu_btn)

        # Click en logout link
        logout_link = self.wait.until(EC.element_to_be_clickable(self._LINK_LOGOUT))
        self.driver.execute_script("arguments[0].click();", logout_link)

        # Esperar que se redirija al login
        self.wait.until(lambda d: "saucedemo.com" in d.current_url)
