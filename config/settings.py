class Settings:
    BASE_URL = "https://www.saucedemo.com/"
    LOGIN_PAGE = ""
    INVENTORY_PAGE = "inventory.html"
    CART_PAGE = "cart.html"
    CHROME_DRIVER_PATH = "C:\\Users\\ASUS\\workspace\\arielberdah.com\\swag-labs-tests\\drivers\\chromedriver.exe"
    BASE_SCREENSHOT_PATH = "reports/screenshots"
    CHROME_ARGS = {
        "no-sandbox": "--no-sandbox",
        "disable-dev-shm-usage": "--disable-dev-shm-usage",
        "window-size": "--window-size=1920,1080",
    }
settings = Settings()
