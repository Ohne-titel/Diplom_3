import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop

from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание элемента')
    def wait_and_find_element_located(self, locator):
        WebDriverWait(self.driver, 6).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Получение текущего урла')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ожидание урла')
    def wait_for_url(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    @allure.step('Видимость элемента')
    def visibility_of_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.title('Переход по клику на «Личный кабинет»')
    def go_in_to_personal_account(self):
        self.wait_and_find_element_located(BasePageLocators.PERSONAL_ACCOUNT).click()

    @allure.step("Клик по кнопке «Войти в аккаунт»")
    def go_in_to_account(self):
        self.wait_and_find_element_located(BasePageLocators.GO_IN_TO_ACCOUNT_BUTTON).click()

    @allure.step('Отсутствие элемента')
    def invisibility_of_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Перетаскивание ингредиента в корзину')
    def drag_and_drop(self, source, target):
        drag_and_drop(self.driver, source, target)



