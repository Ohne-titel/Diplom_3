import allure
from seletools.actions import drag_and_drop
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("переход по клику на «Конструктор»")
    def go_to_constructor(self):
        self.wait_and_find_element_located(MainPageLocators.CONSTRUCTOR_LINK).click()

    @allure.step("переход по клику на «Лента заказов»")
    def go_to_order_feed(self):
        self.wait_and_find_element_located(MainPageLocators.ORDER_FEED).click()

    @allure.step("Видимость элемента «Флюоресцентная булка»")
    def visibility_of_bun(self):
        self.visibility_of_element(MainPageLocators.BUN_BUTTON)

    @allure.step("Открытие модального окна ингредиента")
    def open_bun_details(self):
        self.wait_and_find_element_located(MainPageLocators.BUN_BUTTON).click()

    @allure.step("Видимость элемента модального окна")
    def visibility_of_ingredient_details(self):
        return self.wait_and_find_element_located(MainPageLocators.INGREDIENT_DETAILS).text

    @allure.step("Закрытие окна нажатием на крестик")
    def closing_cross_button(self):
        return self.wait_and_find_element_located(MainPageLocators.CLOSE_BUTTON_CROSS).click()

    @allure.step("Отсутсвие элемента на странице")
    def invisibility_cross_button(self):
        self.invisibility_of_element(MainPageLocators.CLOSE_BUTTON_CROSS)
        return True

    @allure.step("Добавление ингредиента в корзину")
    def add_ingredient_in_basket(self):
        source = self.wait_and_find_element_located(MainPageLocators.BUN_BUTTON)
        target = self.wait_and_find_element_located(MainPageLocators.BASKET_AREA)
        drag_and_drop(self.driver, source, target)

    @allure.step("Получение счетчика ингредиента")
    def get_ingredient_counter(self):
        return self.wait_and_find_element_located(MainPageLocators.INGREDIENT_COUNTER).text

    @allure.step("Нажатие кнопки «Оформить заказ»")
    def click_create_order_button(self):
        self.wait_and_find_element_located(MainPageLocators.PLACE_ORDER).click()

    @allure.step("Получение строки «Ваш заказ начали готовить»")
    def order_identifier(self):
        return self.wait_and_find_element_located(MainPageLocators.ORDER_CREATING).text
