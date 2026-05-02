import allure
import time
import pytest
import logging
from pages.feed_page import FeedPage
from pages.main_page import MainPage

logger = logging.getLogger(__name__)


@allure.epic("Stellar Burgers UI тесты")
@allure.feature("Основная функциональность")
class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    def test_constructor_click(self, main_page):
        main_page.click_order_feed()
        time.sleep(2)
        main_page.click_constructor()
        time.sleep(2)
        assert "feed" not in main_page.get_current_url()

    @allure.title("Переход по клику на «Лента заказов»")
    def test_feed_click(self, main_page):
        main_page.click_order_feed()
        time.sleep(2)
        assert "feed" in main_page.get_current_url()

    @allure.title("Клик на ингредиент → появляется всплывающее окно с деталями")
    def test_ingredient_modal_opens(self, main_page):
        main_page.click_ingredient()
        time.sleep(2)
        assert main_page.is_ingredient_modal_visible()

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_modal_closes_by_cross(self, main_page):
        main_page.click_ingredient()
        time.sleep(2)
        assert main_page.is_ingredient_modal_visible()
        main_page.close_ingredient_modal()
        time.sleep(2)
        assert not main_page.is_ingredient_modal_visible()

    @allure.title("При добавлении ингредиента в заказ счётчик увеличивается (Drag-and-Drop)")
    def test_counter_increases(self, main_page):
        initial_counter = main_page.get_ingredient_counter()
        logger.info(f"Начальный счётчик: {initial_counter}")
        
        main_page.drag_and_drop_ingredient_to_basket()
        time.sleep(3)
        
        new_counter = main_page.get_ingredient_counter()
        logger.info(f"Новый счётчик: {new_counter}")
        
        assert new_counter > initial_counter, \
            f"Счётчик не увеличился: было {initial_counter}, стало {new_counter}"


@allure.epic("Stellar Burgers UI тесты")
@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Счётчик «Выполнено за всё время» увеличивается после создания заказа")
    def test_total_completed_orders_increases(self, main_page, browser, created_user):
        assert created_user, "Пользователь не создан через API"
        
        main_page.login(created_user["email"], created_user["password"])
        time.sleep(3)
        
        main_page.click_order_feed()
        time.sleep(3)
        feed_page = FeedPage(browser)
        total_before = feed_page.get_total_completed_orders()
        logger.info(f"Выполнено за всё время ДО: {total_before}")
        
        main_page.click_constructor()
        time.sleep(2)
        main_page.drag_and_drop_ingredient_to_basket()
        time.sleep(2)
        main_page.place_order()
        time.sleep(4)
        
        main_page.click_order_feed()
        time.sleep(3)
        
        feed_page.wait_for_total_counter_increase(total_before)
        total_after = feed_page.get_total_completed_orders()
        logger.info(f"Выполнено за всё время ПОСЛЕ: {total_after}")
        
        assert total_after > total_before, \
            f"Счётчик 'Выполнено за всё время' не увеличился: было {total_before}, стало {total_after}"

    @allure.title("Счётчик «Выполнено за сегодня» увеличивается после создания заказа")
    def test_today_completed_orders_increases(self, main_page, browser, created_user):
        assert created_user, "Пользователь не создан через API"
        
        main_page.login(created_user["email"], created_user["password"])
        time.sleep(3)
        
        main_page.click_order_feed()
        time.sleep(3)
        feed_page = FeedPage(browser)
        today_before = feed_page.get_today_completed_orders()
        logger.info(f"Выполнено за сегодня ДО: {today_before}")
        
        main_page.click_constructor()
        time.sleep(2)
        main_page.drag_and_drop_ingredient_to_basket()
        time.sleep(2)
        main_page.place_order()
        time.sleep(4)
        
        main_page.click_order_feed()
        time.sleep(3)
        
        feed_page.wait_for_today_counter_increase(today_before)
        today_after = feed_page.get_today_completed_orders()
        logger.info(f"Выполнено за сегодня ПОСЛЕ: {today_after}")
        
        assert today_after > today_before, \
            f"Счётчик 'Выполнено за сегодня' не увеличился: было {today_before}, стало {today_after}"

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_order_number_appears_in_progress(self, main_page, browser, created_user):
        assert created_user, "Пользователь не создан через API"
        
        main_page.login(created_user["email"], created_user["password"])
        time.sleep(3)
        
        main_page.drag_and_drop_ingredient_to_basket()
        time.sleep(2)
        main_page.place_order()
        time.sleep(4)
        
        main_page.click_order_feed()
        time.sleep(4)
        feed_page = FeedPage(browser)
        
        feed_page.wait_for_order_number_in_progress()
        order_number = feed_page.get_order_number_in_progress()
        logger.info(f"Номер заказа в работе: {order_number}")
        
        assert order_number, "Номер заказа не отображается в разделе 'В работе'"
        assert order_number.isdigit(), f"Номер заказа '{order_number}' не является числом"
        assert int(order_number) > 0, "Номер заказа должен быть положительным числом"
        