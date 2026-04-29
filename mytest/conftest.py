import pytest
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    options = Options()
    options.binary_location = r"C:\Users\shamila\AppData\Local\chrome\chrome.exe"
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("start-maximized")
    service = Service(r"C:\Users\shamila\AppData\Local\chromedriver\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()



