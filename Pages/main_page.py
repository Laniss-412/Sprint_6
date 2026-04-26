import allure
from Pages.base_page import BasePage
from locators import MainPageLocators, HeaderLocators

class MainPage(BasePage):
    @allure.step("Принятие куки")
    def accept_cookies(self):
        self.click_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Клик на вопрос")
    def click_to_question(self, question_text):
        method, locator = MainPageLocators.QUESTION_LOCATOR
        formatted_locator = (method, locator.format(question_text))
        element = self.driver.find_element(*formatted_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click_element(formatted_locator)

    @allure.step("Получение текста ответа для вопроса")
    def get_answer_text(self, answer_text):
        method, locator = MainPageLocators.ANSWER_LOCATOR
        formatted_locator = (method, locator.format(answer_text))
        return self.get_text_from_element(formatted_locator)
    
    @allure.step("Клик на верхнюю кнопку 'Заказать'")
    def click_top_order_button(self):
        self.click_element(HeaderLocators.TOP_ORDER_BUTTON)

