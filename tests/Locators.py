from selenium.webdriver.common.by import By

NAME_INPUT = (By.XPATH, "//fieldset[1]//input") # Поле для ввода имени в форме для регистрации
EMAIL_INPUT_REGISTER = (By.XPATH, "//fieldset[2]//input") # Поле для ввода email в форме для регистрации
BUTTON_REGISTER = (By.XPATH, "//button[text() = 'Зарегистрироваться']") # Кнопка "Зарегистрироваться"
TITLE_LOGIN = (By.XPATH, "//h2[text() = 'Вход']") # Заголовок "Вход" для проверки успешной регистрации
INCORRECT_PASSWORD_MESSAGE = (By.XPATH, "//p[text() = 'Некорректный пароль']") # Надпись 'Некорректный пароль' для проверки некорректного пароля
EMAIL_INPUT_LOGIN = (By.XPATH, "//input[@name = 'name']") # Поле для ввода email в форме для входа
PASSWORD_INPUT = (By.XPATH, "//input[@name = 'Пароль']") # Поле для ввода пароля
BUTTON_LOGIN = (By.XPATH, "//button[text() = 'Войти']") # Кнопка "Войти" в форме для входа
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']") # Кнопка "Личный Кабинет"
PROFILE_BUTTON = (By.XPATH, "//a[text() = 'Профиль']") # Кнопка "Профиль" в личном кабинете
CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text() = 'Конструктор']") # Кнопка "Конструктор"
ORDER_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']") # Кнопка оформить заказ
LOGO_BUTTON = (By.XPATH, "//div/a") # Кнопка логотипа
LOGOUT_BUTTON = (By.XPATH, "//button[text() = 'Выход']") # Кнопка "Выход"
CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text() = 'Соберите бургер']") # Кнопка "Соберите бургер" для проверки нахождения в конструкторе
FILLINGS_TAB = (By.XPATH, "//span[text() = 'Начинки']") # Кнопка "Начинки"
BUN_TAB = (By.XPATH, "//span[text() = 'Булки']") # Кнопка "Булки"
SAUCE_TAB = (By.XPATH, "//span[text() = 'Соусы']") # Кнопка "Соусы"
BUN_TITLE = (By.XPATH, "//h2[text() = 'Булки']") # Заголовок "Булки"
SAUCE_TITLE = (By.XPATH, "//h2[text() = 'Соусы']") # Заголовок "Соусы"
FILLINGS_TITLE = (By.XPATH, "//h2[text() = 'Начинки']") # Заголовок "Начинки"
LOGIN_IN_ACCOUNT_BUTTON = (By.XPATH, "//button[text() = 'Войти в аккаунт']") # Кнопка "Войти в аккаунт"
LOGIN_BUTTON_FORGOT_AND_REGISTER = (By.XPATH, "//a[text() = 'Войти']") # Кнопка "Войти" со страницы восстановления пароля и регистрации