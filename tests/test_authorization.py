import pytest
import Locators

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

url_main_page = "https://stellarburgers.nomoreparties.site/"
url_register_page = "https://stellarburgers.nomoreparties.site/register"
url_forgot_password_page = "https://stellarburgers.nomoreparties.site/forgot-password"
def test_authorization_login_account_button(Email, Password, driver):

    driver.get(url_main_page)

    driver.find_element(*Locators.LOGIN_IN_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5)
    driver.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(Email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Password)
    driver.find_element(*Locators.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
    assert driver.current_url == url_main_page


def test_authorization_personal_account_button(Email, Password, driver):

    driver.get(url_main_page)

    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5)
    driver.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(Email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Password)
    driver.find_element(*Locators.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
    assert driver.current_url == url_main_page

def test_authorization_register_page_login(Email, Password, driver):

    driver.get(url_register_page)

    driver.find_element(*Locators.LOGIN_BUTTON_FORGOT_AND_REGISTER).click()
    WebDriverWait(driver, 5)
    driver.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(Email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Password)
    driver.find_element(*Locators.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
    assert driver.current_url == url_main_page


def test_authorization_forgot_password_page(Email, Password, driver):

    driver.get(url_forgot_password_page)

    driver.find_element(*Locators.LOGIN_BUTTON_FORGOT_AND_REGISTER).click()
    WebDriverWait(driver, 5)
    driver.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(Email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Password)
    driver.find_element(*Locators.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
    assert driver.current_url == url_main_page

