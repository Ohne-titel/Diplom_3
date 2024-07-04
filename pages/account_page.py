import allure

import data
from data import email, password
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик по кнопке «Войти в аккаунт»")
    def go_in_to_account(self):
        self.wait_and_find_element_located(AccountPageLocators.GO_IN_TO_ACCOUNT_BUTTON).click()

    @allure.step("Переход на страницу восстановления пароля по ссылке «Восстановить пароль»")
    def transition_to_reset_password(self):
        self.wait_and_find_element_located(AccountPageLocators.RESET_PASSWORD).click()

    @allure.step("Ввод имэйла для восстановления пароля, нажатие кнопки «Восстановить» ")
    def reset_password(self):
        self.wait_and_find_element_located(AccountPageLocators.EMAIL_FIELD).send_keys(data.email)
        self.wait_and_find_element_located(AccountPageLocators.RESET_PASSWORD_BUTTON).click()

    @allure.step("Ввод нового пароля")
    def set_new_passsword(self):
        self.wait_and_find_element_located(AccountPageLocators.PASSWORD_FIELD).send_keys(data.new_password)

    @allure.step('Нажимаем  кнопку "Показать/Скрыть" пароль')
    def click_eye_button(self):
        self.wait_and_find_element_located(AccountPageLocators.VISIBILITY_PASSWORD_BUTTON).click()

    @allure.step('Получаем родительский класс')
    def get_eye_button(self):
        return self.wait_and_find_element_located(AccountPageLocators.PASSWORD_FIELD_PARENT)

    @allure.step('Присваиваем переменной родительский класс')
    def assign_parent_class(self):
        return self.wait_and_find_element_located(AccountPageLocators.VISIBLE_PASSWORD_FIELD)

    @allure.title('Получаем значение строки «Войти»')
    def visibility_of_entry_field(self):
        return self.wait_and_find_element_located(AccountPageLocators.ENTRY_FIELD).text

    @allure.title('Ввод имэйла при логине')
    def email_entry(self):
        self.wait_and_find_element_located(AccountPageLocators.EMAIL_FIELD).send_keys(email)

    @allure.title('Ввод пароля при логине')
    def password_entry(self):
        self.wait_and_find_element_located(AccountPageLocators.PASSWORD_FIELD).send_keys(password)

    @allure.title('Нажатие кнопки «Войти»')
    def click_entry_button(self):
        self.wait_and_find_element_located(AccountPageLocators.LOG_IN_BUTTON).click()

    @allure.title('Переход в «Историю заказов»')
    def go_to_order_history_page(self):
        self.wait_and_find_element_located(AccountPageLocators.ORDER_HISTORY).click()

    @allure.title('Логаут')
    def logout_account(self):
        self.wait_and_find_element_located(AccountPageLocators.LOGOUT_BUTTON).click()

    @allure.title('Переход по клику на «Личный кабинет»')
    def go_in_to_personal_account(self):
        self.wait_and_find_element_located(AccountPageLocators.PERSONAL_ACCOUNT).click()

    @allure.step("Клик по кнопке «Войти в аккаунт»")
    def go_in_to_account(self):
        self.wait_and_find_element_located(AccountPageLocators.GO_IN_TO_ACCOUNT_BUTTON).click()