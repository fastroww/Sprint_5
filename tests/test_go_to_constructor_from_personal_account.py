import pytest
import Locators

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

url_login ="https://stellarburgers.nomoreparties.site/login"
url = "https://stellarburgers.nomoreparties.site/"
def test_go_to_constructor_button_constraction(Email, Password, driver):

    driver.get(url_login)

    driver.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(Email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Password)
    driver.find_element(*Locators.BUTTON_LOGIN).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON))
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(Locators.PROFILE_BUTTON))
    driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
    assert driver.current_url == url

def test_go_to_constructor_click_on_stellar_burgers(Email, Password, driver):

    driver.get(url_login)

    driver.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(Email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Password)
    driver.find_element(*Locators.BUTTON_LOGIN).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON))
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(Locators.PROFILE_BUTTON))
    driver.find_element(*Locators.LOGO_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
    assert driver.current_url == url
    driver.quit()