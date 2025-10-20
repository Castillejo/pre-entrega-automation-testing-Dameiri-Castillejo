# Proyecto de Automatización QA - SauceDemo

## Propósito del proyecto

Este proyecto tiene como objetivo **automatizar pruebas funcionales básicas** sobre la web (https://www.saucedemo.com/), utilizando **Selenium WebDriver** y **pytest**.

Se validan tres flujos principales del sistema:

1. **Login correcto:** autenticación del usuario y redirección al inventario.  
2. **Catálogo de productos:** verificación del listado de productos y elementos clave de la interfaz.  
3. **Carrito de compras:** validación de la adición de productos y contenido correcto en el carrito.

---

## Tecnologías utilizadas

- **Python 3.13.17** (python --version)
- **pytest** (prara realizar pruebas)
- **webdriver-manager** (para realizar pruebas automatizadas ChromeDriver, detecta la ultima versión del navegador)
- **pytest-html** (para generar reportes HTML de ejecución)
- **Git** (para control de versionados)

---

## Instrucciones de instalación

### Clonar el repositorio o copiar los archivos

bash
git clone https://github.com/Castillejo/pre-entrega-automation-testing-Dameiri-Castillejo.git
cd pre-entrega-automation-testing-Dameiri-Castillejo

### Instalar dependecias 
pip install pytest pytest-html selenium (instalación de pytest, pytest-html y selenium)
- **Pytest** maco de pruebas
- **pytest-htmal** generador de reporte
- **selenium** automatización web
pip install selenium pytest webdriver-manager pytest-html

---

## Comando para ejecutar pruebas 
- **pytest -v** (Ejecutar todas las pruebas con salida detallada)
- **pytest -v -s** (Deshabilita la captura de salida estándar y de errores por parte de pytest. Esta opción permite que los print() se muestren en la consola en tiempo real.)
- **pytest -v -m** (Para correr solo el test marcado)
- **pytest -v --html=reporte.html --self-contained-html** (Generar un reporte HTML de los resultados)
- **pytest -m smoke --html=preentrega_pom.html** (Generar un reporte HTML marcado smoke de los resultados)



