from selenium.webdriver.common.by import By


class BasePageLocators:
    PERSONAL_ACCOUNT = (By.XPATH, "//a[.='Личный Кабинет']")  # кнопка "Личный кабинет"
    GO_IN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[.='Войти в аккаунт']")  # кнопка "Войти в аккаунт"





