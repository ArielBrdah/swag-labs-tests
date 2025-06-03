import time
import os
from datetime import datetime
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from config.settings import settings

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.highlight_color = "yellow" 

    def highlight_element(self, element, color=None):
        color = color or self.highlight_color
        original_style = element.get_attribute("style")
        style = f"background-color: {color}; border: 2px solid red;"
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);", element, style
        )
        time.sleep(0.5)
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);", element, original_style
        )

    def click(self, locator):
        try:
            element = self.wait.until(ec.element_to_be_clickable(locator))
            self.highlight_element(element)
            element.click()
        except Exception:
            self.take_screenshot(custom_name=f"error_click_on_{locator[0].replace('.', '_')}_{locator[1]}")
            raise Exception(f"Element {locator} is not clickable")

    def type(self, locator, text):
        try:
            element = self.wait.until(ec.visibility_of_element_located(locator))
            self.highlight_element(element)
            element.send_keys(text)
        except Exception:
            self.take_screenshot(custom_name=f"error_type_in_{locator[0].replace('.', '_')}_{locator[1]}")
            raise Exception(f"Element {locator} is not visible")

    def is_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def get_text(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator)).text

    def take_screenshot(self, custom_name="screenshot"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{settings.BASE_SCREENSHOT_PATH}/{custom_name}_{timestamp}.png"
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.driver.save_screenshot(filename)

    def wait_for_url_contains(self, text):
        self.wait.until(ec.url_contains(text))