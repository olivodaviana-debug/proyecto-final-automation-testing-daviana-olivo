import pytest
from pages.login_page import LoginPage

def test_saucedemo_login(driver):
    login_page = LoginPage(driver)
    
    # Usamos los métodos del Page Object
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

def test_saucedemo_login_fail(driver):
    login_page = LoginPage(driver)
    
    # Escenario negativo utilizando POM
    login_page.login("user_invalido", "clave_invalida")
    error_text = login_page.get_error_message()
    assert "Username and password do not match" in error_text