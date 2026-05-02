from selenium.webdriver.common.by import By

class MainPageLocators:
    # ===== НАВИГАЦИЯ =====
    CONSTRUCTOR_BUTTON = By.XPATH, "//a[@href='/']"
    ORDER_FEED_BUTTON = By.XPATH, "//a[@href='/feed']"
    
    # ===== ИНГРЕДИЕНТЫ =====
    FIRST_INGREDIENT = By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]"
    SECOND_INGREDIENT = By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[2]"
    
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
    
    # Твои точные локаторы
    COMPLETED_TOTAL_COUNTER = By.XPATH, "//*[@id='root']/div/main/div/div/div/div[2]/p[2]"
    COMPLETED_TODAY_COUNTER = By.XPATH, "//*[@id='root']/div/main/div/div/div/div[3]/p[2]"
    
    # Заказы в работе
    ORDERS_IN_PROGRESS = By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li[1]"


class LoginPageLocators:
    EMAIL_INPUT = By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input"
    PASSWORD_INPUT = By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input"
    LOGIN_BUTTON = By.XPATH, "//*[@id='root']/div/main/div/form/button"
    