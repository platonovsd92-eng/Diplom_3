import allure
from pages.base_page import BasePage
from locators import FeedPageLocators
import re
import time

class FeedPage(BasePage):
    
    @allure.step("Получить значение счётчика 'Выполнено за всё время'")
    def get_total_completed_orders(self):
        time.sleep(2)
        try:
            text = self.get_text(FeedPageLocators.COMPLETED_TOTAL_COUNTER)
            numbers = re.findall(r'\d+', text)
            return int(numbers[0]) if numbers else 0
        except:
            return 0

    @allure.step("Получить значение счётчика 'Выполнено за сегодня'")
    def get_today_completed_orders(self):
        time.sleep(2)
        try:
            text = self.get_text(FeedPageLocators.COMPLETED_TODAY_COUNTER)
            numbers = re.findall(r'\d+', text)
            return int(numbers[0]) if numbers else 0
        except:
            return 0

    @allure.step("Получить номер заказа в разделе 'В работе'")
    def get_order_number_in_progress(self):
        time.sleep(3)
        try:
            text = self.get_text(FeedPageLocators.ORDERS_IN_PROGRESS)
            numbers = re.findall(r'\d+', text)
            return numbers[0] if numbers else ""
        except:
            return ""
        