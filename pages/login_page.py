from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import settings

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{settings.BASE_URL}{settings.LOGIN_PAGE}"
    
    def load(self):
        self.driver.get(self.url)
        return self

    def login(self, username, password):
        self.type((By.ID, "user-name"), username)
        self.type((By.ID, "password"), password)
        self.click((By.ID, "login-button"))
        self.take_screenshot(custom_name="login_action_completed")
        return self