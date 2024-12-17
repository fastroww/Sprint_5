import pytest
import random as r

@pytest.fixture
def Email():
    email = "vadim_akimov_16_999@yandex.ru"
    return email

@pytest.fixture
def email_random():
    email = f"vadim_akimov_16_{r.randint(100, 999)}@yandex.ru"
    return email

@pytest.fixture
def Password():
    password = "python"
    return password

@pytest.fixture
def locator_email_login():
    locator = "//input[@name = 'name']"
    return locator

@pytest.fixture
def locator_password_login():
    locator = "//input[@name = 'Пароль']"
    return locator
@pytest.fixture
def locator_button_login():
    locator = "//button[text() = 'Войти']"
    return locator
