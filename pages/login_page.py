import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import LoginPageLocators

class LoginPage(BasePage):
    
    @allure.step("Ввести email")
    def enter_email(self, email):
        element = self.wait.until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_INPUT))
        element.clear()
        element.send_keys(email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        element = self.wait.until(EC.element_to_be_clickable(LoginPageLocators.PASSWORD_INPUT))
        element.clear()
        element.send_keys(password)

    @allure.step("Нажать кнопку Войти")
    def click_login_submit(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)
        # Ждём, пока авторизация завершится (появление кнопки "Оформить заказ")
        from locators import MainPageLocators
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
        