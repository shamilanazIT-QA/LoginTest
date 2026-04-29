# login_test.py
from pages.Login_Page import LoginPage  # Make sure this import is correct


def test_valid_login(driver):
    login_pg = LoginPage(driver)
    driver.get("https://the-internet.herokuapp.com/login")

    # Use the base 'type' method directly or update pass_keys to accept strings
    login_pg.type(login_pg.user_name, "tomsmith")
    login_pg.type(login_pg.password, "SuperSecretPassword!")
    login_pg.click_login()

    # This part is crucial!
    assert "secure" in driver.page_source



