import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_logout(Email, Password, locator_email_login, locator_password_login, locator_button_login):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(By.XPATH, locator_email_login).send_keys(Email)
    driver.find_element(By.XPATH, locator_password_login).send_keys(Password)
    driver.find_element(By.XPATH, locator_button_login).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//p[text() = 'Личный Кабинет']")))
    driver.find_element(By.XPATH, "//p[text() = 'Личный Кабинет']").click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//a[text() = 'Профиль']")))
    driver.find_element(By.XPATH, "//button[text() = 'Выход']").click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text() = 'Вход']")))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
    driver.quit()