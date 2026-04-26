import allure
from Pages.base_page import BasePage
from locators import OrderPageLocators

class OrderPage(BasePage):
    @allure.step("Заполнение первой страницы формы заказа")
    def fill_first_form(self, name, surname, address, phone):
        self.enter_text(OrderPageLocators.NAME_FIELD, name)
        self.enter_text(OrderPageLocators.SURNAME_FIELD, surname)
        self.enter_text(OrderPageLocators.ADDRESS_FIELD, address)
        self.click_element(OrderPageLocators.METRO_FIELD)
        self.click_element(OrderPageLocators.METRO_STATION_OPTION)
        self.enter_text(OrderPageLocators.PHONE_FILED, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнение второй страницы (про аренду")
    def fill_second_form(self, period):
        self.click_element(OrderPageLocators.DATE_FIELD)
        self.click_element(OrderPageLocators.CURRENT_DATE)
        self.click_element(OrderPageLocators.PERIOD_DROPDOWN)
        method, locator = OrderPageLocators.PERIOD_OPTION
        formatted_period = (method, locator.format(period))
        self.click_element(formatted_period)
        self.click_element(OrderPageLocators.FINAL_ORDER_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_YES_BUTTON)

    @allure.step("Проверка появления окна успеха")
    def get_succes_message(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_SUCCESS_MODAL)