import time
import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Открытие карточки заказа")
    def open_an_order_card(self):
        self.wait_and_find_element_located(OrderPageLocators.ORDER_CARD).click()

    @allure.step("Получение номера карточки заказа")
    def get_an_order_card(self):
        return self.wait_and_find_element_located(OrderPageLocators.ORDER_CARD_ELEMENT).text

    @allure.step("Ожидание модального окна")
    def wait_for_order_modal(self):
        return self.wait_and_find_element_located(OrderPageLocators.ORDER_MODAL)

    @allure.step("Закрытие модального окна")
    def click_order_cross_button(self):
        self.wait_and_find_element_located(OrderPageLocators.ORDER_CROSS_BUTTON).click()

    @allure.step("Ожидание элемента 'крестик' на модальном окне")
    def wait_for_visibility_of_cross(self):
        self.visibility_of_element(OrderPageLocators.ORDER_CROSS_BUTTON)

    @allure.step("Получение номера последнего заказа")
    def get_order_number(self):
        self.visibility_of_element(OrderPageLocators.ORDER_NUMBER)
        return self.wait_and_find_element_located(OrderPageLocators.ORDER_NUMBER).text

    @allure.step("Получение списка всех заказов")
    def get_order_list(self):
        self.visibility_of_element(OrderPageLocators.ORDERS_LIST)
        return self.wait_and_find_element_located(OrderPageLocators.ORDERS_LIST).text

    @allure.step("Получение списка заказов, выполненных за все время")
    def get_number_of_all_orders(self):
        self.visibility_of_element(OrderPageLocators.CREATED_FOR_ALL_TIME)
        return self.wait_and_find_element_located(OrderPageLocators.CREATED_FOR_ALL_TIME).text

    @allure.step("Получение списка заказов, выполненных за сегодня")
    def get_number_of_todays_orders(self):
        self.visibility_of_element(OrderPageLocators.CREATED_TODAY)
        return self.wait_and_find_element_located(OrderPageLocators.CREATED_TODAY).text

    @allure.step("Получение номера заказа в статусе в работе")
    def get_number_order_in_progress(self, timeout=8):
        start_time = time.time()
        while time.time() - start_time < timeout:
            order_in_progress = self.wait_and_find_element_located(OrderPageLocators.IN_PROGRESS_NUMBER).text
            if order_in_progress != 'Все текущие заказы готовы!':
                return order_in_progress
