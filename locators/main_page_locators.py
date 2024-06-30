from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//a[.='Конструктор']")  # кнопка "Конструктор"
    ORDER_FEED = (By.XPATH, "//a[.='Лента Заказов']")   # кнопка "Лента заказов"
    BUN_BUTTON = (By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']")   # кнопка "Флюоресцентная булка"
    INGREDIENT_DETAILS = (By.XPATH, ".//h2[text()='Детали ингредиента']")    # строка "Детали ингредиента"
    CLOSE_BUTTON_CROSS = (By.XPATH, "(.//button[@type='button' and contains(@class, 'modal__close')])[1]")    # кнопка закрытия модального окна "крестик"
    BASKET_AREA = (By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket__list')]")  # область корзины
    INGREDIENT_COUNTER = (By.XPATH, './/p[contains(@class, "counter_counter__num__3nue1")]')  # Счетчик ингредиента
    PLACE_ORDER = (By.XPATH, "//button[contains(.,'Оформить')]")  # кнопка "Оформить заказ"
    ORDER_CREATING = (By.XPATH, ".//p[contains (text(),  'Ваш заказ начали готовить')]") # строка "Ваш заказ начали готовить"
