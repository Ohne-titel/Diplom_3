from selenium.webdriver.common.by import By


class AccountPageLocators:
    RESET_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")  # ссылка "Восстановить пароль"
    EMAIL_FIELD = (By.XPATH, ".//label[text() = 'Email']/../input")  # строка для ввода Email
    RESET_PASSWORD_BUTTON = (By.XPATH, "//button[contains(.,'Восстановить')]")  # кнопка "Восстановить"
    VISIBILITY_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class,'input__icon input__icon-action')]")  # кнопка видимости пароля
    PASSWORD_FIELD = (By.XPATH, ".//label[text() = 'Пароль']/../input") # строка для ввода нового пароля
    PASSWORD_FIELD_PARENT = (By.XPATH, ".//input[contains(@type,'text')]/parent::div")
    VISIBLE_PASSWORD_FIELD = (
        By.XPATH,
        ".//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")  # глаз

    ENTRY_FIELD = (By.XPATH,".//h2[text()='Вход']")  # кнопка
    ORDER_HISTORY = (By.XPATH,"//a[contains(.,'История заказов')]")  # кнопка "История заказов"
    LOG_IN_BUTTON = (By.XPATH, "//button[contains(.,'Войти')]")  # кнопка "Войти"
    LOGOUT_BUTTON = (By.XPATH,"//button[contains(.,'Выход')]")   # кнопка "Выход"
    PERSONAL_ACCOUNT = (By.XPATH, "//a[.='Личный Кабинет']")  # кнопка "Личный кабинет"
    GO_IN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[.='Войти в аккаунт']")  # кнопка "Войти в аккаунт"

