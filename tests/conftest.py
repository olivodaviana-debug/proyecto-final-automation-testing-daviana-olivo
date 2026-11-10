import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ejecuta sin abrir ventana gráfica
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get("https://saucedemo.com")
    yield driver
    driver.quit()