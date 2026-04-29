from selenium.webdriver.common.by import By
from pages.base import BasePage

class LoginPage(BasePage):
    user_name =(By.ID, 'username')
    password =(By.ID, 'password')
    # Change btton to button
    login_button = (By.XPATH, "//button[@type='submit' and contains(., 'Login')]")

    def pass_keys(self, username_text, password_text):
        self.type(self.user_name, username_text)
        self.type(self.password, password_text)
    def click_login(self):
        self.click_element(self.login_button)
    def right_input(self):
        try:
            self.type(self.user_name,self.password)
            print("right input")
        except Exception as e:
            print(e)



