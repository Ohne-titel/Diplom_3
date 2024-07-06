import allure
import urls
from pages.account_page import AccountPage
from pages.main_page import MainPage
from conftest import driver


class TestMainPage:
    @allure.step("Проверка перехода по клику на «Конструктор»")
    def test_go_to_constructor(self, driver):
        account_page = AccountPage(driver)
        account_page.go_in_to_personal_account()
        main_page = MainPage(driver)
        main_page.go_to_constructor()

        assert main_page.get_current_url() == urls.URL

    @allure.step("Проверка перехода по клику на «Лента заказов»")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_order_feed()
        main_page.wait_for_url(urls.ORDER_FEED_URL)

        assert main_page.get_current_url() == urls.ORDER_FEED_URL

    @allure.step("Проверка клика на ингредиент, должно появиться всплывающее окно с деталями")
    def test_get_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.visibility_of_bun()
        main_page.open_bun_details()
        ingredient_details = main_page.visibility_of_ingredient_details()

        assert ingredient_details == 'Детали ингредиента'

    @allure.step("Проверка закрытия всплывающего окна кликом по крестику")
    def test_closing_cross_button(self, driver):
        main_page = MainPage(driver)
        main_page.visibility_of_bun()
        main_page.open_bun_details()
        main_page.closing_cross_button()

        assert main_page.invisibility_cross_button() is True

    @allure.step("Проверка добавлении ингредиента в заказ, увеличения счётчика этого ингридиента")
    def test_add_ingredient_in_basket(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_url(urls.URL)
        main_page.add_ingredient_in_basket()
        counter = main_page.get_ingredient_counter()

        assert counter == '2'

    @allure.step("Проверка успешного оформления заказа залогиненным пользователем")
    def test_create_order_logged_in_user(self, driver):
        account_page = AccountPage(driver)
        account_page.go_in_to_account()
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        account_page.email_entry()
        account_page.password_entry()
        account_page.click_entry_button()
        main_page.add_ingredient_in_basket()
        main_page.click_create_order_button()
        created_order = main_page.order_identifier()

        assert created_order == 'Ваш заказ начали готовить'
