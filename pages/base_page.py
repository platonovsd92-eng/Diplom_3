from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # Увеличиваем таймаут для Firefox
        self.wait = WebDriverWait(driver, 20)

    def click(self, locator):
        with allure.step(f"Клик по элементу {locator}"):
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()

    def get_text(self, locator):
        with allure.step(f"Получение текста элемента {locator}"):
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text

    def is_element_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False

    def wait_for_url_contains(self, expected_url_part):
        with allure.step(f"Ожидание URL, содержащего '{expected_url_part}'"):
            return self.wait.until(EC.url_contains(expected_url_part))

    def send_keys(self, locator, text):
        with allure.step(f"Ввод текста в поле {locator}"):
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            