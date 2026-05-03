import allure
import logging
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import MainPageLocators
from config import MAIN_PAGE
import re

logger = logging.getLogger(__name__)

class MainPage(BasePage):
    
    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(MAIN_PAGE)
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_BASKET))

    @allure.step("Кликнуть на Конструктор")
    def click_constructor(self):
        self.force_close_modals()
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_BASKET))

    @allure.step("Кликнуть на Ленту заказов")
    def click_order_feed(self):
        self.force_close_modals()
        self.click(MainPageLocators.ORDER_FEED_BUTTON)
        self.wait_for_url_contains("/feed")
    
    @allure.step("Принудительно закрыть все модальные окна и оверлеи")
    def force_close_modals(self):
        # Шаг 1: клик по крестику, если он виден
        try:
            close_button = self.driver.find_element(*MainPageLocators.INGREDIENT_DETAILS_CLOSE_BUTTON)
            if close_button.is_displayed():
                close_button.click()
        except:
            pass
        
        # Шаг 2: JavaScript для удаления оверлея
        try:
            self.execute_script("""
                var overlays = document.querySelectorAll('.Modal_modal_overlay__x2ZCr');
                for(var i = 0; i < overlays.length; i++) {
                    overlays[i].style.display = 'none';
                }
            """)
        except:
            pass
        
        # Шаг 3: ожидание, пока оверлей действительно исчезнет
        try:
            self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")))
        except:
            pass

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self):
        self.force_close_modals()
        self.click(MainPageLocators.FIRST_INGREDIENT)
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.INGREDIENT_DETAILS_MODAL))

    @allure.step("Закрыть всплывающее окно")
    def close_ingredient_modal(self):
        self.click(MainPageLocators.INGREDIENT_DETAILS_CLOSE_BUTTON)
        self.wait.until(EC.invisibility_of_element_located(MainPageLocators.INGREDIENT_DETAILS_MODAL))
        self.force_close_modals()

    @allure.step("Проверить видимость модального окна")
    def is_ingredient_modal_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_DETAILS_MODAL)

    @allure.step("Получить счётчик ингредиента")
    def get_ingredient_counter(self):
        try:
            element = self.wait.until(EC.presence_of_element_located(MainPageLocators.INGREDIENT_COUNTER_SIMPLE))
            text = element.text
            numbers = re.findall(r'\d+', text)
            if numbers:
                return int(numbers[0])
            return 0
        except Exception as e:
            logger.error(f"Ошибка получения счётчика: {e}")
            return 0

    @allure.step("Перетащить ингредиент в заказ (Drag-and-Drop)")
    def drag_and_drop_ingredient_to_basket(self):
        self.force_close_modals()
        ingredient = self.find_element(MainPageLocators.FIRST_INGREDIENT)
        target = self.find_element(MainPageLocators.DROP_TARGET)
        
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
        
        self.execute_script(js_script, ingredient, target)

    @allure.step("Оформить заказ")
    def place_order(self):
        self.click(MainPageLocators.PLACE_ORDER_BUTTON)
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))

    @allure.step("Кликнуть на кнопку 'Войти в аккаунт'")
    def click_login_button_on_main(self):
        self.force_close_modals()
        self.click(MainPageLocators.LOGIN_BUTTON_ON_MAIN)

    @allure.step("Проверить видимость конструктора")
    def is_constructor_visible(self):
        return self.is_element_visible(MainPageLocators.CONSTRUCTOR_BASKET)
    