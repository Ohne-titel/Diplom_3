from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_FEED_BUTTON = (By.XPATH, "//a[.='Лента Заказов']")  # кнопка "Лента заказов"
    ORDER_CARD = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__2x95r mb-6')][1]")   # карточка заказа
    ORDER_CARD_ELEMENT = (By.XPATH, ".//p[contains(text(), 'Cостав')]")   # элемент карточки заказа
    ORDER_HISTORY = (By.XPATH, ".//a[contains(text(), 'История заказов')]")  # кнопка "История заказов"
    ORDER_CROSS_BUTTON = (By.XPATH, './/button[contains(@class, "modal__close")]')  # кнопка "крестик" на модальном коне
    ORDER_NUMBER = (By.XPATH, ".//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text "
                              "text_type_digits-large mb-8']") # номер заказа
    ORDERS_LIST = (By.XPATH, ".//p[@class='text text_type_digits-default']") # список заказов
    ORDER_MODAL = (By.XPATH, ".//div[contains(@class, 'Modal_modal__contentBox')]")  # модальное окно заказа
    CREATED_FOR_ALL_TIME = (By.XPATH, ".//p[@class= 'OrderFeed_number__2MbrQ text text_type_digits-large']")  # строка Выполнено за все время
    CREATED_TODAY = (By.XPATH, "(.//p[@class= 'OrderFeed_number__2MbrQ text text_type_digits-large'])[2]")  # строка Выполнено за сегодня
    IN_PROGRESS_NUMBER = (By.XPATH, ".//ul[@class = 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']")  # номер заказа в работе
    IN_PROGRESS = (By.XPATH, "//p[contains(text(), 'В работе:')]")  # список в работе
    COMPLETED_ORDER = (By.XPATH, "//p[contains(text(), 'Готовы:')]")   # список готовы



