import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import MainPageLocators
from config import MAIN_PAGE
import time
import re

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(MAIN_PAGE)
        time.sleep(2)

    @allure.step("Кликнуть на Конструктор")
    def click_constructor(self):
        self.close_modal_if_exists()
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)
        time.sleep(1)

    @allure.step("Кликнуть на Ленту заказов")
    def click_order_feed(self):
        self.close_modal_if_exists()
        self.click(MainPageLocators.ORDER_FEED_BUTTON)
        time.sleep(1)
    
    @allure.step("Закрыть модальное окно, если оно открыто")
    def close_modal_if_exists(self):
        try:
            close_button = self.driver.find_element(*MainPageLocators.INGREDIENT_DETAILS_CLOSE_BUTTON)
            if close_button.is_displayed():
                close_button.click()
                time.sleep(0.5)
        except:
            pass

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self):
        time.sleep(1)
        self.click(MainPageLocators.FIRST_INGREDIENT)
        time.sleep(1)

    @allure.step("Закрыть всплывающее окно")
    def close_ingredient_modal(self):
        self.click(MainPageLocators.INGREDIENT_DETAILS_CLOSE_BUTTON)
        time.sleep(1)

    @allure.step("Проверить видимость модального окна")
    def is_ingredient_modal_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_DETAILS_MODAL)

    @allure.step("Получить счётчик ингредиента")
    def get_ingredient_counter(self):
        try:
            time.sleep(1)
            element = self.wait.until(EC.presence_of_element_located(MainPageLocators.INGREDIENT_COUNTER_SIMPLE))
            text = element.text
            numbers = re.findall(r'\d+', text)
            if numbers:
                return int(numbers[0])
            return 0
        except Exception as e:
            print(f"Ошибка получения счётчика: {e}")
            return 0

    @allure.step("Перетащить ингредиент в заказ (Drag-and-Drop) - JavaScript для Firefox")
    def drag_and_drop_ingredient_to_basket(self):
        time.sleep(1)
        ingredient = self.driver.find_element(*MainPageLocators.FIRST_INGREDIENT)
        target = self.driver.find_element(*MainPageLocators.DROP_TARGET)
        
        # JavaScript drag-and-drop (работает в Chrome и Firefox)
        js_script = """
        function createEvent(typeOfEvent) {
            var event = document.createEvent("CustomEvent");
            event.initCustomEvent(typeOfEvent, true, true, null);
            event.dataTransfer = {
                data: {},
                setData: function(key, value) {
                    this.data[key] = value;
                },
                getData: function(key) {
                    return this.data[key];
                }
            };
            return event;
        }
        
        function dragAndDrop(dragElement, dropElement) {
            var dragStartEvent = createEvent('dragstart');
            dragElement.dispatchEvent(dragStartEvent);
            
            var dropEvent = createEvent('drop');
            dropElement.dispatchEvent(dropEvent);
            
            var dragEndEvent = createEvent('dragend');
            dragElement.dispatchEvent(dragEndEvent);
        }
        
        var dragElement = arguments[0];
        var dropElement = arguments[1];
        dragAndDrop(dragElement, dropElement);
        """
        
        self.driver.execute_script(js_script, ingredient, target)
        time.sleep(2)

    @allure.step("Оформить заказ")
    def place_order(self):
        self.click(MainPageLocators.PLACE_ORDER_BUTTON)
        time.sleep(3)

    @allure.step("Кликнуть на кнопку 'Войти в аккаунт'")
    def click_login_button_on_main(self):
        self.click(MainPageLocators.LOGIN_BUTTON_ON_MAIN)
        time.sleep(2)

    @allure.step("Авторизация пользователя")
    def login(self, email, password):
        from pages.login_page import LoginPage
        
        self.open()
        self.click_login_button_on_main()
        time.sleep(2)
        
        login_page = LoginPage(self.driver)
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login_submit()
        
        time.sleep(3)

    @allure.step("Проверить видимость конструктора")
    def is_constructor_visible(self):
        return self.is_element_visible(MainPageLocators.CONSTRUCTOR_BASKET)
    