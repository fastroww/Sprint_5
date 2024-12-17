import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_jumps_to_sauces(Email, Password, locator_email_login, locator_password_login, locator_button_login):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(By.XPATH, locator_email_login).send_keys(Email)
    driver.find_element(By.XPATH, locator_password_login).send_keys(Password)
    driver.find_element(By.XPATH, locator_button_login).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text() = 'Соберите бургер']")))
    driver.find_element(By.XPATH, "//span[text() = 'Соусы']").click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text() = 'Соусы']")))
    assert driver.find_element(By.XPATH, "//h2[text() = 'Соусы']").text == "Соусы"
    driver.quit()

def test_jumps_to_fillings(Email, Password, locator_email_login, locator_password_login, locator_button_login):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(By.XPATH, locator_email_login).send_keys(Email)
    driver.find_element(By.XPATH, locator_password_login).send_keys(Password)
    driver.find_element(By.XPATH, locator_button_login).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text() = 'Соберите бургер']")))
    driver.find_element(By.XPATH, "//span[text() = 'Начинки']").click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text() = 'Начинки']")))
    assert driver.find_element(By.XPATH, "//h2[text() = 'Начинки']").text == "Начинки"
    driver.quit()

def test_jumps_to_rolls(Email, Password, locator_email_login, locator_password_login, locator_button_login):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(By.XPATH, locator_email_login).send_keys(Email)
    driver.find_element(By.XPATH, locator_password_login).send_keys(Password)
    driver.find_element(By.XPATH, locator_button_login).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text() = 'Соберите бургер']")))
    driver.find_element(By.XPATH, "//span[text() = 'Начинки']").click()
    driver.find_element(By.XPATH, "//span[text() = 'Булки']").click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text() = 'Булки']")))
    assert driver.find_element(By.XPATH, "//h2[text() = 'Булки']").text == "Булки"
    driver.quit()