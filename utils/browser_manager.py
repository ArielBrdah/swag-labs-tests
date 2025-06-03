from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
from config.settings import settings

class BrowserManager:
    @staticmethod
    def get_driver():
        try:
            chrome_options = Options()
            for arg in settings.CHROME_ARGS.values():
                chrome_options.add_argument(arg)
            chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
            
            # Vérifier si CHROME_DRIVER_PATH est défini et valide
            if hasattr(settings, 'CHROME_DRIVER_PATH') and settings.CHROME_DRIVER_PATH and os.path.isfile(settings.CHROME_DRIVER_PATH):
                service = Service(executable_path=settings.CHROME_DRIVER_PATH)
            else:
                # Si non valide ou non défini, Selenium cherchera chromedriver dans le PATH
                service = Service()
            
            driver = webdriver.Chrome(service=service, options=chrome_options)
            
            driver.implicitly_wait(10)
            driver.set_page_load_timeout(30)
            
            return driver
            
        except Exception:
            raise
