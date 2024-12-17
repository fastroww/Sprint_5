import pytest

import Locators

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

url_register = "https://stellarburgers.nomoreparties.site/register"
def test_successful_registration(email_random, Password, driver):
    driver.get(url_register)

    driver.find_element(*Locators.NAME_INPUT).send_keys("Вадим")
    driver.find_element(*Locators.EMAIL_INPUT_REGISTER).send_keys(email_random)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Password)
    driver.find_element(*Locators.BUTTON_REGISTER).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.TITLE_LOGIN)))
    assert driver.find_element(*Locators.TITLE_LOGIN).text == "Вход"


def test_incorrect_password_registration(email_random, driver):
    driver.get(url_register)

    driver.find_element(*Locators.NAME_INPUT).send_keys("Вадим")
    driver.find_element(*Locators.EMAIL_INPUT_REGISTER).send_keys(email_random)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys("12345")
    driver.find_element(*Locators.BUTTON_REGISTER).click()
    WebDriverWait(driver, 3)
    assert driver.find_element(*Locators.INCORRECT_PASSWORD_MESSAGE).text == "Некорректный пароль"



