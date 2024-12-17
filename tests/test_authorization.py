import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_authorization_login_account_button(Email, Password, locator_email_login, locator_password_login, locator_button_login):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    driver.find_element(By.XPATH, "//button[text() = 'Войти в аккаунт']").click()
    WebDriverWait(driver, 5)
    driver.find_element(By.XPATH, locator_email_login).send_keys(Email)
    driver.find_element(By.XPATH, locator_password_login).send_keys(Password)
    driver.find_element(By.XPATH, locator_button_login).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text() = 'Оформить заказ']")))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
    driver.quit()

def test_authorization_personal_account_button(Email, Password, locator_email_login, locator_password_login, locator_button_login):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    driver.find_element(By.XPATH, "//p[text() = 'Личный Кабинет']").click()
    WebDriverWait(driver, 5)
    driver.find_element(By.XPATH, locator_email_login).send_keys(Email)
    driver.find_element(By.XPATH, locator_password_login).send_keys(Password)
    driver.find_element(By.XPATH, locator_button_login).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text() = 'Оформить заказ']")))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
    driver.quit()

def test_authorization_register_page_login(Email, Password, locator_email_login, locator_password_login, locator_button_login):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(By.XPATH, "//a[text() = 'Войти']").click()
    WebDriverWait(driver, 5)
    driver.find_element(By.XPATH, locator_email_login).send_keys(Email)
    driver.find_element(By.XPATH, locator_password_login).send_keys(Password)
    driver.find_element(By.XPATH, locator_button_login).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[text() = 'Оформить заказ']")))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
    driver.quit()

def test_authorization_forgot_password_page(Email, Password, locator_email_login, locator_password_login, locator_button_login):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

    driver.find_element(By.XPATH, "//a[text() = 'Войти']").click()
    WebDriverWait(driver, 5)
    driver.find_element(By.XPATH, locator_email_login).send_keys(Email)
    driver.find_element(By.XPATH, locator_password_login).send_keys(Password)
    driver.find_element(By.XPATH, locator_button_login).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[text() = 'Оформить заказ']")))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
    driver.quit()
