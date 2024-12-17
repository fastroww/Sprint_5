import pytest
import Locators

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

url_login = "https://stellarburgers.nomoreparties.site/login"
def test_logout(Email, Password, driver):
    driver.get(url_login)

    driver.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(Email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Password)
    driver.find_element(*Locators.BUTTON_LOGIN).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON))
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((Locators.PROFILE_BUTTON)))
    driver.find_element(*Locators.LOGOUT_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((Locators.TITLE_LOGIN)))
    assert driver.current_url == url_login
