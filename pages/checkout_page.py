from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SHORT = 10
LONG = 30

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    # --------- SELECTORES ----------
    btn_checkout = (By.ID, "checkout")
    input_first = (By.ID, "first-name")
    input_last = (By.ID, "last-name")
    input_zip = (By.ID, "postal-code")
    btn_continue = (By.ID, "continue")
    btn_finish = (By.ID, "finish")
    msg_complete = (By.CLASS_NAME, "complete-header")

    # --------- MÉTODOS ----------
    def iniciar_checkout(self):
        WebDriverWait(self.driver, SHORT).until(
            EC.element_to_be_clickable(self.btn_checkout)
        ).click()

    def completar_formulario(self, nombre, apellido, cp):
        WebDriverWait(self.driver, SHORT).until(
            EC.visibility_of_element_located(self.input_first)
        ).send_keys(nombre)

        self.driver.find_element(*self.input_last).send_keys(apellido)
        self.driver.find_element(*self.input_zip).send_keys(cp)

    def continuar_checkout(self):
        WebDriverWait(self.driver, SHORT).until(
            EC.element_to_be_clickable(self.btn_continue)
        ).click()
        # Esperar que aparezca el botón FINISH
        WebDriverWait(self.driver, SHORT).until(
            EC.element_to_be_clickable(self.btn_finish)
        )

    def finalizar_checkout(self):
        finish_button = WebDriverWait(self.driver, SHORT).until(
            EC.element_to_be_clickable(self.btn_finish)
        )
        # Click robusto con JavaScript
        self.driver.execute_script("arguments[0].click();", finish_button)

    def obtener_mensaje_final(self):
        # Esperar que el botón Finish desaparezca (seguridad)
        WebDriverWait(self.driver, LONG).until(
            EC.invisibility_of_element_located(self.btn_finish)
        )
        # Esperar mensaje final
        mensaje_elem = WebDriverWait(self.driver, LONG).until(
            EC.visibility_of_element_located(self.msg_complete)
        )
        return mensaje_elem.text
    

"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SHORT = 10

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    # --------- SELECTORES ----------
    btn_checkout = (By.ID, "checkout")
    input_first = (By.ID, "first-name")
    input_last = (By.ID, "last-name")
    input_zip = (By.ID, "postal-code")
    btn_continue = (By.ID, "continue")
    btn_finish = (By.ID, "finish")
    msg_complete = (By.CLASS_NAME, "complete-header")

    # --------- MÉTODOS ----------
    def iniciar_checkout(self):
        WebDriverWait(self.driver, SHORT).until(
            EC.element_to_be_clickable(self.btn_checkout)
        ).click()

    def completar_formulario(self, nombre, apellido, cp):
        WebDriverWait(self.driver, SHORT).until(
            EC.visibility_of_element_located(self.input_first)
        ).send_keys(nombre)

        self.driver.find_element(*self.input_last).send_keys(apellido)
        self.driver.find_element(*self.input_zip).send_keys(cp)

    def continuar_checkout(self):
        # Hacer click en continue
        WebDriverWait(self.driver, SHORT).until(
            EC.element_to_be_clickable(self.btn_continue)
        ).click()

        # Esperar que aparezca el botón FINISH (igual que tu test que funciona)
        WebDriverWait(self.driver, SHORT).until(
            EC.element_to_be_clickable(self.btn_finish)
        )

    def finalizar_checkout(self):
        WebDriverWait(self.driver, SHORT).until(
            EC.element_to_be_clickable(self.btn_finish)
        ).click()

    def obtener_mensaje_final(self):
        return WebDriverWait(self.driver, SHORT).until(
            EC.visibility_of_element_located(self.msg_complete)
        ).text
"""