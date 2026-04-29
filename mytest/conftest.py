import pytest
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # On GitHub Actions (Linux), Chrome is already installed.
    # You don't need the service path or binary_location!
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


