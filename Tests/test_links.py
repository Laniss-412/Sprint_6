import allure
from Pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestHeaderLinks:
    @allure.title("Проверка перехода на главную страницу при клике на логотип самоката")
    def test_click_csooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open_site()
        main_page.click_top_order_button()
        main_page.click_scooter_logo()

        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title("Проверка перехода на дзен при клике на логотип Яндекса")
    def test_click_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open_site()
        main_page.click_yandex_logo()
        driver.switch_to.window(driver.window_handles[1])

        WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in driver.current_url

        