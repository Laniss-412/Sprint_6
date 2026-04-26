import allure
from Pages.base_page import BasePage
from locators import MainPageLocators, HeaderLocators, OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    @allure.step("Принятие куки")
    def accept_cookies(self):
        self.click_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Клик на вопрос")
    def click_to_question(self, question_text):
        method, locator = MainPageLocators.QUESTION_LOCATOR
        formatted_locator = (method, locator.format(question_text))
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(formatted_locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(formatted_locator))
        self.click_element(formatted_locator)

    @allure.step("Получение текста ответа для вопроса")
    def get_answer_text(self, answer_text):
        method, locator = MainPageLocators.ANSWER_LOCATOR
        formatted_locator = (method, locator.format(answer_text))
        return self.get_text_from_element(formatted_locator)
    
    @allure.step("Клик на верхнюю кнопку 'Заказать'")
    def click_top_order_button(self):
        self.click_element(OrderPageLocators.TOP_ORDER_BUTTON)

    @allure.step("Клик на нижнюю кнопку 'Заказать'")
    def click_bottom_order_button(self):
        self.click_element(OrderPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Клик на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(HeaderLocators.SCOOTER_LOGO)

    @allure.step("Клик на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(HeaderLocators.YANDEX_LOGO)
