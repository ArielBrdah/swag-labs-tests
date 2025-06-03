import pytest
from pages.login_page import LoginPage
from utils.browser_manager import BrowserManager
from config.settings import settings

class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self):
        """Configuration avant chaque test"""
        self.driver = BrowserManager.get_driver()
        self.login_page = LoginPage(self.driver)
        yield
        # Nettoyage après chaque test
        self.driver.quit()

    def test_successful_login(self):
        """Test une connexion réussie avec des identifiants valides"""
        # Données de test
        username = "standard_user"
        password = "secret_sauce"
        
        # Exécution du test
        self.login_page.load().login(username, password)
        
        # Vérification
        assert settings.INVENTORY_PAGE in self.driver.current_url, "Connection failed"
        assert "Products" in self.driver.page_source, "Products page not loaded"

    @pytest.mark.parametrize("username,password,expected_error", [
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
        ("invalid", "invalid", "Username and password do not match")
    ])
    def test_failed_login(self, username, password, expected_error):
        """Test les scénarios d'échec de connexion"""
        # Exécution du test
        self.login_page.load().login(username, password)
        
        # Vérification
        assert expected_error.lower() in self.driver.page_source.lower(), \
            f"Le message d'erreur attendu n'est pas affiché: {expected_error}"