from selenium.webdriver.common.by import By

class MainPageLocators:
    # ===== НАВИГАЦИЯ =====
    CONSTRUCTOR_BUTTON = By.XPATH, "//a[@href='/']"
    ORDER_FEED_BUTTON = By.XPATH, "//a[@href='/feed']"
    
    # ===== ИНГРЕДИЕНТЫ =====
    FIRST_INGREDIENT = By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]"
    
    # ===== МОДАЛЬНОЕ ОКНО =====
    INGREDIENT_DETAILS_MODAL = By.XPATH, "//div[contains(@class, 'Modal_modal')]"
    INGREDIENT_DETAILS_CLOSE_BUTTON = By.XPATH, "//button[contains(@class, 'Modal_modal__close')]"
    
    # ===== СЧЁТЧИК ИНГРЕДИЕНТА =====
    INGREDIENT_COUNTER_SIMPLE = By.XPATH, "//p[contains(@class, 'counter_counter__num_')]"
    
    # ===== КОНСТРУКТОР =====
    CONSTRUCTOR_BASKET = By.XPATH, "//section[contains(@class, 'BurgerConstructor')]"
    PLACE_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"
    DROP_TARGET = By.XPATH, "//div[contains(@class, 'constructor-element_pos_top')]"
    
    # ===== АВТОРИЗАЦИЯ =====
    LOGIN_BUTTON_ON_MAIN = By.XPATH, "//button[text()='Войти в аккаунт']"


class FeedPageLocators:
    FEED_TITLE = By.XPATH, "//h1[text()='Лента заказов']"
    
    # Надёжные локаторы через текст метки
    COMPLETED_TOTAL_COUNTER = By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"
    COMPLETED_TODAY_COUNTER = By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    
    # Заказы в работе
    ORDERS_IN_PROGRESS = By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li[1]"


class LoginPageLocators:
    # На основе присланных атрибутов
    EMAIL_INPUT = By.CSS_SELECTOR, "input[name='name']"
    PASSWORD_INPUT = By.CSS_SELECTOR, "input[name='Пароль']"
    LOGIN_BUTTON = By.CSS_SELECTOR, "button[class*='button_button_type_primary']"
    