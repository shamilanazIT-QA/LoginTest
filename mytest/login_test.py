# login_test.py
from pages.Login_Page import LoginPage  # Make sure this import is correct


def test_valid_login(driver):  # 'driver' here comes from your fixture in driver_test.py
    login_pg = LoginPage(driver)
    driver.get("https://the-internet.herokuapp.com/login")

    # Corrected usage
    login_pg.type(login_pg.user_name, "tomsmith")
    login_pg.type(login_pg.password, "SuperSecretPassword!")
    login_pg.click_login()

    # Add an assertion to see if it worked!
    assert "secure" in driver.current_url



