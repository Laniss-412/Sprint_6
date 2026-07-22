import pytest
import allure
from Pages.main_page import MainPage
from Pages.order_page import OrderPage
from data import OrderData

class TestOrder:
    @allure.title("Проверка оформления заказа")
    @pytest.mark.parametrize("order_button, name, surname, address, phone, period", OrderData.ORDER_DETAILS)
    def test_order_scooter(self, driver, order_button, name, surname, address, phone, period):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_site()
        main_page.accept_cookies()

        if order_button == "top":
            main_page.click_top_order_button()
        else:
            main_page.click_bottom_order_button()

        order_page.fill_first_form(name, surname, address, phone)
        order_page.fill_second_form(period)

        success_text = order_page.get_succes_message()
        assert "Заказ оформлен" in success_text

