import time

import allure

import urls
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.order_page import OrderPage
from conftest import driver


class TestOrderFeed:
    @allure.step("Проверка открытия всплывающего окно с деталями по клику на заказ")
    def test_check_opening_popup_with_details(self, driver):
        order_page = OrderPage(driver)
        order_page.wait_for_url(urls.URL)
        main_page = MainPage(driver)
        main_page.go_to_order_feed()
        order_page.open_an_order_card()
        order_card_element = order_page.get_an_order_card()

        assert order_card_element == 'Cостав'

    @allure.step("Проверка отображения заказов пользователя из раздела «История заказов» на странице «Лента заказов»")
    def test_checking_the_display_of_users_orders(self, driver):
        order_page = OrderPage(driver)
        order_page.wait_for_url(urls.URL)
        order_page.go_in_to_personal_account()
        account_page = AccountPage(driver)
        account_page.email_entry()
        account_page.password_entry()
        account_page.click_entry_button()
        main_page = MainPage(driver)
        main_page.add_ingredient_in_basket()
        main_page.click_create_order_button()
        order_page.wait_for_order_modal()
        order_page.wait_for_visibility_of_cross()
        order_page.click_order_cross_button()
        order_number = order_page.get_order_number()
        main_page.go_to_order_feed()
        order_list = order_page.get_order_list()

        assert order_number in order_list

    @allure.step("Проверка увеличения счетчика 'Выполнено за всё время' при создании нового заказа")
    def test_check_the_counter_increment(self, driver):
        order_page = OrderPage(driver)
        order_page.wait_for_url(urls.URL)
        order_page.go_in_to_personal_account()
        account_page = AccountPage(driver)
        account_page.email_entry()
        account_page.password_entry()
        account_page.click_entry_button()
        order_page.wait_for_url(urls.URL)
        main_page = MainPage(driver)
        main_page.go_to_order_feed()
        order_page.wait_for_url(urls.ORDER_FEED_URL)
        current_number = order_page.get_number_of_all_orders()
        main_page.go_to_constructor()
        main_page.add_ingredient_in_basket()
        main_page.click_create_order_button()
        order_page.wait_for_order_modal()
        order_page.wait_for_visibility_of_cross()
        order_page.click_order_cross_button()
        main_page.go_to_order_feed()

        assert order_page.get_number_of_all_orders() > current_number

    @allure.step("Проверка увеличения счетчика 'Выполнено за сегодня' при создании нового заказа")
    def test_check_the_counter_increment_today(self, driver):
        order_page = OrderPage(driver)
        order_page.wait_for_url(urls.URL)
        order_page.go_in_to_personal_account()
        account_page = AccountPage(driver)
        account_page.email_entry()
        account_page.password_entry()
        account_page.click_entry_button()
        order_page.wait_for_url(urls.URL)
        main_page = MainPage(driver)
        main_page.go_to_order_feed()
        order_page.wait_for_url(urls.ORDER_FEED_URL)
        current_number = order_page.get_number_of_todays_orders()
        main_page.go_to_constructor()
        main_page.add_ingredient_in_basket()
        main_page.click_create_order_button()
        order_page.wait_for_order_modal()
        order_page.wait_for_visibility_of_cross()
        order_page.click_order_cross_button()
        main_page.go_to_order_feed()
        now = order_page.get_number_of_todays_orders()

        assert now > current_number

    def test_order_number_appears_in_progress(self, driver):
        order_page = OrderPage(driver)
        order_page.wait_for_url(urls.URL)
        order_page.go_in_to_personal_account()
        account_page = AccountPage(driver)
        account_page.email_entry()
        account_page.password_entry()
        account_page.click_entry_button()
        main_page = MainPage(driver)
        main_page.add_ingredient_in_basket()
        main_page.click_create_order_button()
        order_page.wait_for_order_modal()
        order_page.wait_for_visibility_of_cross()
        order_page.click_order_cross_button()
        order_number = order_page.get_order_number()
        main_page.go_to_order_feed()
        time.sleep(5)
        in_progress = order_page.get_number_order_in_progress()

        assert order_number in in_progress
