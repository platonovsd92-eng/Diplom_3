import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import LoginPageLocators
import time

class LoginPage(BasePage):
    
    @allure.step("Ввести email")
    def enter_email(self, email):
        time.sleep(1)
        element = self.wait.until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_INPUT))
        element.clear()
        element.send_keys(email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        time.sleep(1)
        element = self.wait.until(EC.element_to_be_clickable(LoginPageLocators.PASSWORD_INPUT))
        element.clear()
        element.send_keys(password)

    @allure.step("Нажать кнопку Войти")
    def click_login_submit(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)
        time.sleep(3)
        