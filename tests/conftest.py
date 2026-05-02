import os
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import MainPage
from api_helpers import register_new_user_and_return_data

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption(
        "--browser", 
        action="store", 
        default="chrome", 
        help="Browser: chrome or firefox"
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")
    driver = None
    
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(10)
        logger.info("ChromeDriver инициализирован")
        
    elif browser_name == "firefox":
        current_dir = os.path.dirname(os.path.abspath(__file__))
        driver_path = os.path.join(current_dir, '..', 'drivers', 'geckodriver.exe')
        
        if not os.path.exists(driver_path):
            raise FileNotFoundError(
                f"geckodriver не найден по пути: {driver_path}\n"
                f"Скачайте geckodriver с https://github.com/mozilla/geckodriver/releases\n"
                f"и поместите в папку drivers/ (создайте папку drivers в корне проекта)"
            )
        
        logger.info(f"geckodriver найден: {driver_path}")
        
        options = FirefoxOptions()
        firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        if os.path.exists(firefox_path):
            options.binary_location = firefox_path
            logger.info(f"Firefox найден: {firefox_path}")
        
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        
        service = FirefoxService(driver_path)
        driver = webdriver.Firefox(service=service, options=options)
        driver.implicitly_wait(15)
        logger.info("FirefoxDriver инициализирован")
    
    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser_name}. Используйте 'chrome' или 'firefox'")
    
    driver.maximize_window()
    yield driver
    driver.quit()
    logger.info("Браузер закрыт")


@pytest.fixture(scope="function")
def main_page(browser):
    page = MainPage(browser)
    page.open()
    return page


@pytest.fixture(scope="function")
def created_user():
    user_data = register_new_user_and_return_data()
    yield user_data
    