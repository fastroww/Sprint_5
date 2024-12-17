import pytest
import random as r
from selenium import webdriver

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
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
