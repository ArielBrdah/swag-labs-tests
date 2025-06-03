# Swag Labs UI Automation Tests

This project contains automated User Interface (UI) tests for the [Swag Labs](https://www.saucedemo.com/) demo application. It is developed in Python using Selenium WebDriver and Pytest.

## Current Status and Features

*   **Login Page Tests**:
    *   Successful login scenarios.
    *   Failed login scenarios with error message verification (empty or incorrect credentials).
*   **Page Object Model (POM)**:
    *   `BasePage`: Contains common methods for element interaction (click, type), wait management, screenshot capture, and visual element highlighting.
    *   `LoginPage`: Models the login page and its specific actions.
*   **Configuration Management**:
    *   URLs, paths (screenshots, local ChromeDriver), and browser arguments are centralized in `config/settings.py`.
*   **Browser Management**:
    *   `BrowserManager` (`utils/browser_manager.py`) configures and instantiates the Chrome driver.
    *   Supports using a local `chromedriver` (via `settings.py`) and automatic detection of `chromedriver` in the system `PATH` (for CI).
*   **Screenshots**:
    *   Automatic screenshot capture on error during interactions.
    *   Specific screenshots after key actions (e.g., after login).
    *   Dynamic naming of screenshot files including a custom name and timestamp, stored in `reports/screenshots/`.
*   **Visual Highlighting**:
    *   Elements are briefly highlighted (yellow background, red border) before click and type actions for better visibility during execution.
*   **Continuous Integration (CI/CD)**:
    *   A GitHub Actions workflow (`.github/workflows/main.yml`) is configured to:
        *   Install Python 3.8 and dependencies.
        *   Install Chrome and ChromeDriver.
        *   Run login page smoke tests.
        *   Upload screenshots as artifacts in case of test failure.
*   **Code Quality**:
    *   Ruff is used for linting to maintain clean and consistent code.

## Tech Stack

*   **Language**: Python 3.8
*   **Test Framework**: Pytest
*   **UI Automation**: Selenium WebDriver
*   **Target Browser**: Google Chrome
*   **Linting**: Ruff
*   **CI/CD**: GitHub Actions

## Prerequisites

*   Python 3.8 or higher
*   Pip (Python package manager)
*   Google Chrome (for local execution)
*   ChromeDriver (for local execution, the path must be configured in `config/settings.py` or ChromeDriver must be in the system PATH)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ArielBrdah/swag-labs-tests.git
    cd swag-labs-tests
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Local Configuration (if necessary):**
    *   Ensure Google Chrome is installed.
    *   Download the ChromeDriver version corresponding to your Chrome version.
    *   Update the `CHROME_DRIVER_PATH` variable in `config/settings.py` to point to your `chromedriver.exe` executable, or ensure `chromedriver` is accessible via your system `PATH`.

## Running Tests

To run all tests:
```bash
pytest
```

To run tests with more details (verbose):
```bash
pytest -v
```

To run a specific test file (e.g., login tests):
```bash
pytest tests/ui/smoke/test_login.py -v
```

Test reports (if configured with plugins like `pytest-html` or `allure-pytest`) and screenshots will be generated in their respective directories (e.g., `reports/screenshots/`).

## Continuous Integration

Tests are automatically run via GitHub Actions on every `push` or `pull_request` to the `main`, `master`, and `develop` branches. Results and artifacts (screenshots on failure) are available in the "Actions" tab of the GitHub repository.

## Future Planned Improvements

*   **Extend Test Coverage**:
    *   Add tests for other key features: inventory, add to cart, checkout process, logout.
    *   Develop more comprehensive end-to-end test scenarios.
*   **Advanced Test Reporting**:
    *   Integrate Allure Framework (`allure-pytest`) for interactive and detailed HTML test reports.
*   **Data-Driven Tests**:
    *   Explore reading test data from external files (CSV, JSON) for parameterized tests.
*   **Cross-Browser Testing**:
    *   Adapt `BrowserManager` to support running tests on other browsers (e.g., Firefox, Edge).
*   **Enhanced Logging**:
    *   Integrate a more robust logging system for better tracking and debugging.
*   **CI Enhancements**:
    *   Publish Allure reports as build artifacts.
    *   Optimize CI execution times.

## Contribution

Contributions are welcome. Please open an issue to discuss major changes or submit a pull request.
