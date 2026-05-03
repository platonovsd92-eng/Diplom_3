import allure
from pages.base_page import BasePage
from locators import FeedPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import re

class FeedPage(BasePage):
    
    @allure.step("Получить значение счётчика 'Выполнено за всё время'")
    def get_total_completed_orders(self):
        element = self.wait.until(EC.visibility_of_element_located(FeedPageLocators.COMPLETED_TOTAL_COUNTER))
        text = element.text
        numbers = re.findall(r'\d+', text)
        return int(numbers[0]) if numbers else 0

    @allure.step("Получить значение счётчика 'Выполнено за сегодня'")
    def get_today_completed_orders(self):
        element = self.wait.until(EC.visibility_of_element_located(FeedPageLocators.COMPLETED_TODAY_COUNTER))
        text = element.text
        numbers = re.findall(r'\d+', text)
        return int(numbers[0]) if numbers else 0

    @allure.step("Ожидать увеличения счётчика 'Выполнено за всё время'")
    def wait_for_total_counter_increase(self, expected_value):
        def condition(driver):
            try:
                element = self.find_element(FeedPageLocators.COMPLETED_TOTAL_COUNTER)
                text = element.text
                numbers = re.findall(r'\d+', text)
                current_value = int(numbers[0]) if numbers else 0
                return current_value > expected_value
            except:
                return False
        wait = WebDriverWait(self.driver, 30)
        wait.until(condition)

    @allure.step("Ожидать увеличения счётчика 'Выполнено за сегодня'")
    def wait_for_today_counter_increase(self, expected_value):
        def condition(driver):
            try:
                element = self.find_element(FeedPageLocators.COMPLETED_TODAY_COUNTER)
                text = element.text
                numbers = re.findall(r'\d+', text)
                current_value = int(numbers[0]) if numbers else 0
                return current_value > expected_value
            except:
                return False
        wait = WebDriverWait(self.driver, 30)
        wait.until(condition)

    @allure.step("Ожидать появления номера заказа в работе")
    def wait_for_order_number_in_progress(self):
        def condition(driver):
            try:
                element = self.find_element(FeedPageLocators.ORDERS_IN_PROGRESS)
                text = element.text
                numbers = re.findall(r'\d+', text)
                return numbers[0] != ""
            except:
                return False
        wait = WebDriverWait(self.driver, 30)
        wait.until(condition)

    @allure.step("Получить номер заказа в разделе 'В работе'")
    def get_order_number_in_progress(self):
        try:
            element = self.wait.until(EC.visibility_of_element_located(FeedPageLocators.ORDERS_IN_PROGRESS))
            text = element.text
            numbers = re.findall(r'\d+', text)
            return numbers[0] if numbers else ""
        except TimeoutException:
            return ""
        