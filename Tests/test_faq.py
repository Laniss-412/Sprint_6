import pytest
import allure
from Pages.main_page import MainPage
from data import TestData

class TestFAQ:
    @allure.title("Проверка FAQ: {question}")
    @pytest.mark.parametrize("question, answer", TestData.FAQ_DATA)
    def test_faq_questions(self, driver, question, answer):
        main_page = MainPage(driver)
        main_page.open_site()
        main_page.accept_cookies()
        main_page.click_to_question(question)
        assert main_page.get_answer_text(answer) == answer