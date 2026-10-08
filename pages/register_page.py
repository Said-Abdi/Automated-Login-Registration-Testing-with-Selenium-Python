from selenium.webdriver.common.by import By
from .base_page import BasePage


class RegisterPage(BasePage):
    NAME = (By.ID, "name")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "confirm_password")
    REGISTER_BUTTON = (By.ID, "register_btn")
    MESSAGE = (By.ID, "message")

    def register(self, name, email, password, confirm_password):
        self.type(self.NAME, name)
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.type(self.CONFIRM_PASSWORD, confirm_password)
        self.click(self.REGISTER_BUTTON)

    def get_message(self):
        return self.text_of(self.MESSAGE)
