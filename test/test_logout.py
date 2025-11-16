import pytest
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from conftest import URL  # tu URL base

@pytest.mark.smoke
@pytest.mark.logout_POM
def test_logout(driver, username="standard_user", password="secret_sauce"):
    # Login
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)

    # Logout
    logout_page = LogoutPage(driver)
    logout_page.logout()

    # Verificación
    assert URL in driver.current_url, "No se redirigió al login después del logout."
    print("Logout exitoso")

