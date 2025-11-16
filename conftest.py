import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import os
import re

URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# -------------------------
# FUNCIONES AUXILIARES MEJORADAS
# -------------------------
def limpiar_nombre_archivo(nombre, max_len=100):
    """Eliminar caracteres inválidos para nombres de archivo en Windows y limitar longitud"""
    nombre_limpio = re.sub(r'[^a-zA-Z0-9_-]', '_', nombre)
    if len(nombre_limpio) > max_len:
        nombre_limpio = nombre_limpio[:max_len]
    return nombre_limpio

def tomar_screenshot(driver, nombre, estado="pass"):
    """Guardar screenshot en carpeta pass/fail con ruta absoluta y nombre seguro"""
    # Carpeta absoluta dentro del proyecto
    carpeta_base = os.path.join(os.getcwd(), "screenshots")
    carpeta = os.path.join(carpeta_base, estado)
    os.makedirs(carpeta, exist_ok=True)

    # Nombre del archivo con timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_limpio = limpiar_nombre_archivo(nombre)
    nombre_archivo = f"{nombre_limpio}_{timestamp}.png"

    # Ruta completa
    ruta = os.path.join(carpeta, nombre_archivo)
    driver.save_screenshot(ruta)
    print(f"[INFO] Screenshot guardada en {estado}: {ruta}")
    return ruta

# -------------------------
# HOOK PARA SCREENSHOTS AUTOMÁTICOS
# -------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Captura automáticamente screenshots en pass/fail"""
    outcome = yield
    result = outcome.get_result()

    if result.when != "call":
        return

    driver = item.funcargs.get("driver", None)
    if not driver:
        return

    nombre_test = item.name

    try:
        if result.failed:
            tomar_screenshot(driver, nombre_test, estado="fail")
        elif result.passed:
            tomar_screenshot(driver, nombre_test, estado="pass")
    except Exception as e:
        print(f"[ERROR] No se pudo tomar screenshot: {e}")

        
"""
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    # Solo capturar screenshot cuando falla en la fase "call"
    if result.when == "call" and result.failed:

        driver = item.funcargs.get("driver", None)
        if driver:

            # Crear carpeta si no existe
            carpeta = "screenshots"
            if not os.path.exists(carpeta):
                os.makedirs(carpeta)

            # Nombre: testname_YYYYmmdd_HHMMSS.png
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_archivo = f"{item.name}_{timestamp}.png"
            ruta = os.path.join(carpeta, nombre_archivo)

            # Guardar screenshot
            driver.save_screenshot(ruta)

            print(f"\n[ERROR]  Screenshot guardada en: {ruta}\n")

"""           
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import datetime

URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre = f"{item.name}_{timestamp}.png"
            driver.save_screenshot(nombre)
            print(f"[ERROR] Screenshot guardada: {nombre}")
"""