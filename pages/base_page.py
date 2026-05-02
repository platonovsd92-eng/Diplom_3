from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Клик по элементу {locator}")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Получение текста элемента {locator}")
    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    @allure.step("Проверка видимости элемента {locator}")
    def is_element_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False

    @allure.step("Ожидание URL, содержащего '{expected_url_part}'")
    def wait_for_url_contains(self, expected_url_part):
        return self.wait.until(EC.url_contains(expected_url_part))

    @allure.step("Ввод текста '{text}' в поле {locator}")
    def send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Поиск элемента по локатору")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Проверка, что элемент не отображается")
    def is_element_invisible(self, locator):
        try:
            return self.wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            return False

    @allure.step("Закрыть элемент, если он виден")
    def click_if_visible(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            if element.is_displayed():
                element.click()
                return True
        except:
            pass
        return False

    @allure.step("Получить текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Проверить, виден ли элемент по локатору (без ожидания)")
    def is_element_displayed(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except:
            return False

    @allure.step("Найти элемент по локатору (без ожидания)")
    def find_element_now(self, locator):
        return self.driver.find_element(*locator)
    