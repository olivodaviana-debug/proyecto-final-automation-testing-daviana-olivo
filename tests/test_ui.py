import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

# Caso 1: Login Exitoso estándar
def test_saucedemo_login(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

# Caso 2: Escenario Negativo (Credenciales inválidas requeridas por la consigna)
def test_saucedemo_login_fail(driver):
    login_page = LoginPage(driver)
    login_page.login("user_invalido", "clave_invalida")
    error_text = login_page.get_error_message()
    assert "Username and password do not match" in error_text

# Caso 3: Navegación interna a la página de detalles de un producto
def test_navigate_to_product_details(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    # Navegamos haciendo click al título de la mochila
    driver.find_element(By.ID, "item_4_title_link").click()
    assert "id=4" in driver.current_url

# Caso 4: Agregar un artículo al carrito de compras
def test_add_item_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    # Añadimos la mochila usando el botón
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    badge_text = driver.find_element(By.CLASS_SELECTOR, ".shopping_cart_badge").text
    assert badge_text == "1"

# Caso 5: Quitar un artículo del carrito (Flujo complementario)
def test_remove_item_from_cart(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    
    # Validamos que el indicador numérico desaparezca al estar vacío
    badges = driver.find_elements(By.CLASS_SELECTOR, ".shopping_cart_badge")
    assert len(badges) == 0