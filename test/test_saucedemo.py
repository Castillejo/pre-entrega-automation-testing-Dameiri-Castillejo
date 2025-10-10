import pytest


@pytest.fixture # reutilización. Evitar escribir el mismo código de configuración una y otra vez en cada prueba.
def driver():
    # configuracion para consultar a selenium web driver


def test_login():
    # logeo de usuario con username y password
    # click al boton de login 
    # rediriga a la pagina de inventario
    # verifixar el titulo de la pagina(ventanita)

def test_catalogo():

    # logeo de usuario con username y password
    # click al boton de login 
    # podamos verificar el titulo pero del html
    # comprobar si existen productos en la pagina viosibles (len())
    # verificar elementos importantes de la pagina.

def test_carrito():

    # logeo de usuario con username y password
    # click al boton de login 
    # llevarme a la pagina de carrito de compras
    # incremento de carrito al agregar un producto
    # comprobar que el carrito aparezca el produto correcto