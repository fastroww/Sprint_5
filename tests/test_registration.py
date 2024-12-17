import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_successful_registration(email_random, Password):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")


    driver.find_element(By.XPATH, "//fieldset[1]//input").send_keys("Вадим")
    driver.find_element(By.XPATH, "//fieldset[2]//input").send_keys(email_random)
    driver.find_element(By.XPATH, "//input[@name = 'Пароль']").send_keys(Password)
    driver.find_element(By.XPATH, "//button[text() = 'Зарегистрироваться']").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text() = 'Вход']")))
    assert driver.find_element(By.XPATH, "//h2[text() = 'Вход']").text == "Вход"
    driver.quit()

def test_incorrect_password_registration(email_random):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(By.XPATH, "//fieldset[1]//input").send_keys("Вадим")
    driver.find_element(By.XPATH, "//fieldset[2]//input").send_keys(email_random)
    driver.find_element(By.XPATH, "//input[@name = 'Пароль']").send_keys("12345")
    driver.find_element(By.XPATH, "//button[text() = 'Зарегистрироваться']").click()
    WebDriverWait(driver, 3)
    assert driver.find_element(By.XPATH, "//p[text() = 'Некорректный пароль']").text == "Некорректный пароль"

    driver.quit()

