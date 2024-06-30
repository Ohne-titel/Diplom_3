import allure

import urls
from conftest import driver
from pages.account_page import AccountPage


class TestAccountPage:
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_reset_password_page(self, driver):
        account_page = AccountPage(driver)
        account_page.go_in_to_account()
        account_page.transition_to_reset_password()

        assert account_page.get_current_url() == urls.FORGOT_PASSWORD_URL

    @allure.title('Проверка ввода почты и клик по кнопке «Восстановить»')
    def test_reset_password_page(self, driver):
        account_page = AccountPage(driver)
        account_page.go_in_to_account()
        account_page.transition_to_reset_password()
        account_page.reset_password()
        account_page.wait_for_url(urls.RESET_PASSWORD_URL)

        assert account_page.get_current_url() == urls.RESET_PASSWORD_URL

    @allure.title('Проверка клика по кнопке показать/скрыть пароль (делает поле активным — подсвечивает его)')
    def test_reset_password(self, driver):
        account_page = AccountPage(driver)
        account_page.go_in_to_account()
        account_page.transition_to_reset_password()
        account_page.reset_password()
        account_page.set_new_passsword()
        account_page.click_eye_button()
        account_page.get_eye_button()

        assert account_page.get_eye_button() == account_page.assign_parent_class()

    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    def test_go_in_to_personal_account(self, driver):
        account_page = AccountPage(driver)
        account_page.go_in_to_personal_account()
        entry_button = account_page.visibility_of_entry_field()

        assert entry_button == 'Вход'

    def test_go_in_to_order_history(self, driver):
        account_page = AccountPage(driver)
        account_page.go_in_to_account()
        account_page.email_entry()
        account_page.password_entry()
        account_page.click_entry_button()
        account_page.wait_for_url(urls.URL)
        account_page.go_in_to_personal_account()
        account_page.go_to_order_history_page()
        account_page.wait_for_url(urls.ORDER_HISTORY_URL)

        assert urls.ORDER_HISTORY_URL == account_page.get_current_url()

    def test_logout_account(self, driver):
        account_page = AccountPage(driver)
        account_page.go_in_to_account()
        account_page.email_entry()
        account_page.password_entry()
        account_page.click_entry_button()
        account_page.wait_for_url(urls.URL)
        account_page.go_in_to_personal_account()
        account_page.logout_account()
        account_page.wait_for_url(urls.LOGIN_URL)

        assert account_page.get_current_url() == urls.LOGIN_URL
