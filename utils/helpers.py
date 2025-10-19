from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Credenciales y URL base
URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

# Lista de usuarios proporcionados
USERSLISTA = [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user"
]

def get_driver():

    """
    Configura y entrega un driver de Chrome para cada prueba.
    - Usa webdriver_manager para manejar el driver.
    - Maximiza la ventana y aplica un tiempo de espera implícito.
    """
    options = Options()
    options.add_argument('--start-maximized')

    # Instalación del driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Pausa la ejecución de un programa durante un número específico de segundos.
    driver.implicitly_wait(10)

    # Devuelve el driver ya logueado
    return driver 
   
def login_saucedeme(driver):
    """
    Realiza el login en saucedemo.com con las credenciales estándar.
    Deja al navegador en la página de inventario (si el login fue exitoso).
    """

    # Navega al sitio
    driver.get(URL)

    # Completa usuario y contraseña
    # Otra forma... driver.find_element(By.NAME, 'user-name').send_keys(USERNAME)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'user-name'))
    ).send_keys(USERNAME)

    # Otra forma... driver.find_element(By.NAME, 'password').send_keys(PASSWORD)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'password'))
    ).send_keys(PASSWORD)

    # Envía el formulario
    # Otra forma... driver.find_element(By.ID, 'login-button').click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'login-button'))
    ).click()

    # Pausa la ejecución de un programa durante un número específico de segundos.
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.header_secondary_container .title'))
    )

def loginlista(driver, usuario):
    """
    Realiza login con el usuario recibido por parámetro.
    Soporta usuarios bloqueados y verifica resultados esperados.
    """
    driver.get(URL)

       # Esperar a que el campo usuario esté visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'user-name'))
    )

    # Completar credenciales
    user_input = driver.find_element(By.NAME, 'user-name')
    pass_input = driver.find_element(By.NAME, 'password')

    user_input.clear()
    pass_input.clear()

    user_input.send_keys(usuario)
    pass_input.send_keys(PASSWORD)

    driver.find_element(By.ID, "login-button").click()
    
    """
    # Otra forma de realizar
    # Esperar a que el campo usuario, pass y botón estén visible y completa campos
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'user-name'))
    ).send_keys(usuario)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'password'))
    ).send_keys(PASSWORD)


    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'login-button'))
    ).click()

    """

    # Esperas condicionales según tipo de usuario
    if usuario == "locked_out_user":
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        )
        return "bloqueado"
    else:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.header_secondary_container .title'))
        )
        return "ok"