import pytest
import Locators

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

url_login = "https://stellarburgers.nomoreparties.site/login"
def test_jumps_to_sauces(Email, Password, driver):

    driver.get(url_login)

    driver.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(Email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Password)
    driver.find_element(*Locators.BUTTON_LOGIN).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))
    driver.find_element(*Locators.SAUCE_TAB).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((Locators.SAUCE_TITLE)))
    assert driver.find_element(*Locators.SAUCE_TITLE).text == "Соусы"

def test_jumps_to_fillings(Email, Password, driver):

    driver.get(url_login)

    driver.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(Email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Password)
    driver.find_element(*Locators.BUTTON_LOGIN).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))
    driver.find_element(*Locators.FILLINGS_TAB).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(Locators.FILLINGS_TITLE))
    assert driver.find_element(*Locators.FILLINGS_TITLE).text == "Начинки"

def test_jumps_to_rolls(Email, Password, driver):

    driver.get(url_login)

    driver.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(Email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Password)
    driver.find_element(*Locators.BUTTON_LOGIN).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))
    driver.find_element(*Locators.FILLINGS_TAB).click()
    driver.find_element(*Locators.BUN_TAB).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((Locators.BUN_TITLE)))
    assert driver.find_element(*Locators.BUN_TITLE).text == "Булки"