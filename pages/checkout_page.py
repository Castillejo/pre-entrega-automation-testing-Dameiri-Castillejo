from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

LONG_TIMEOUT = 15

class CheckoutPage:
    _FIRST_NAME = (By.ID, "first-name")
    _LAST_NAME = (By.ID, "last-name")
    _ZIP_CODE = (By.ID, "postal-code")
    _CONTINUE_BUTTON = (By.ID, "continue")
    _FINISH_BUTTON = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver

    def iniciar_checkout(self):
        checkout_btn = WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_btn.click()
        WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.url_contains("checkout-step-one.html")
        )

    def completar_formulario(self, first_name, last_name, zip_code):
        # Esperar los campos
        first_input = WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.visibility_of_element_located(self._FIRST_NAME)
        )
        last_input = WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.visibility_of_element_located(self._LAST_NAME)
        )
        zip_input = WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.visibility_of_element_located(self._ZIP_CODE)
        )

        # Función para React: setear valor y disparar evento change
        def react_input(element, value):
            self.driver.execute_script("""
                const input = arguments[0];
                const value = arguments[1];
                input.focus();
                input.value = value;
                input.dispatchEvent(new Event('input', { bubbles: true }));
                input.dispatchEvent(new Event('change', { bubbles: true }));
            """, element, value)

        react_input(first_input, first_name)
        react_input(last_input, last_name)
        react_input(zip_input, zip_code)

    def continuar_checkout(self):
        continue_btn = WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.element_to_be_clickable(self._CONTINUE_BUTTON)
        )
        ActionChains(self.driver).move_to_element(continue_btn).click().perform()
        WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.url_contains("checkout-step-two.html")
        )

    def finalizar_checkout(self):
        finish_btn = WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.element_to_be_clickable(self._FINISH_BUTTON)
        )
        ActionChains(self.driver).move_to_element(finish_btn).click().perform()
        WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.url_contains("checkout-complete.html")
        )

