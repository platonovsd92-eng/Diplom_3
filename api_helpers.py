import requests
import random
import string
import allure
from config import API_REGISTER

def generate_random_string(length=10):
    """Генерирует случайную строку из букв нижнего регистра"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def register_new_user_and_return_data():
    """Регистрирует нового пользователя через API и возвращает его данные"""
    with allure.step("Создание нового пользователя через API"):
        email = f"{generate_random_string(8)}@test.com"
        password = generate_random_string(10)
        name = generate_random_string(8)
        
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        
        response = requests.post(API_REGISTER, json=payload)
        
        if response.status_code == 200:
            return {
                "email": email, 
                "password": password, 
                "name": name, 
                "accessToken": response.json().get("accessToken")
            }
        else:
            return {}
        