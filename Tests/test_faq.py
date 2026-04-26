import pytest
import allure
from Pages.main_page import MainPage

class TestFAQ:
    @allure.title("Проверка вопроса 'Сколько это стоит? И как оплатить?'")
    def test_faq_cost(self, driver):
        main_page = MainPage(driver)
        main_page.open_site()
        main_page.accept_cookies()
        
        question = "Сколько это стоит? И как оплатить?"
        answer = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        
        main_page.click_to_question(question)
        assert main_page.get_answer_text(answer) == answer

    @allure.title("Проверка вопроса 'Хочу сразу несколько самокатов! Так можно?'")
    def test_faq_multiple_scooters(self, driver):
        main_page = MainPage(driver)
        main_page.open_site()
        main_page.accept_cookies()
        
        question = "Хочу сразу несколько самокатов! Так можно?"
        answer = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        
        main_page.click_to_question(question)
        assert main_page.get_answer_text(answer) == answer

    @allure.title("Проверка вопроса 'Как рассчитывается время аренды?'")
    def test_faq_how_is_rental_time_calculated(self, driver):
        main_page = MainPage(driver)
        main_page.open_site()
        main_page.accept_cookies()
        
        question = "Как рассчитывается время аренды?"
        answer = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        
        main_page.click_to_question(question)
        assert main_page.get_answer_text(answer) == answer

    @allure.title("Проверка вопроса 'Можно ли заказать самокат прямо на сегодня?'")
    def test_faq_rental_today(self, driver):
        main_page = MainPage(driver)
        main_page.open_site()
        main_page.accept_cookies()
        
        question = "Можно ли заказать самокат прямо на сегодня?"
        answer = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        
        main_page.click_to_question(question)
        assert main_page.get_answer_text(answer) == answer

    @allure.title("Проверка вопроса 'Можно ли продлить заказ или вернуть самокат раньше?'")
    def test_faq_extend_an_order_or_return_the_scooter_earlier(self, driver):
        main_page = MainPage(driver)
        main_page.open_site()
        main_page.accept_cookies()
        
        question = "Можно ли продлить заказ или вернуть самокат раньше?"
        answer = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        
        main_page.click_to_question(question)
        assert main_page.get_answer_text(answer) == answer

    @allure.title("Проверка вопроса 'Вы привозите зарядку вместе с самокатом?'")
    def test_faq_charger(self, driver):
        main_page = MainPage(driver)
        main_page.open_site()
        main_page.accept_cookies()
        
        question = "Вы привозите зарядку вместе с самокатом?"
        answer = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        
        main_page.click_to_question(question)
        assert main_page.get_answer_text(answer) == answer

    @allure.title("Проверка вопроса 'Можно ли отменить заказ?'")
    def test_faq_order_cancellation(self, driver):
        main_page = MainPage(driver)
        main_page.open_site()
        main_page.accept_cookies()
        
        question = "Можно ли отменить заказ?"
        answer = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        
        main_page.click_to_question(question)
        assert main_page.get_answer_text(answer) == answer

    @allure.title("Проверка вопроса 'Я жизу за МКАДом, привезёте?'")
    def test_faq_delivery_outside_the_mkad(self, driver):
        main_page = MainPage(driver)
        main_page.open_site()
        main_page.accept_cookies()
        
        question = "Я жизу за МКАДом, привезёте?"
        answer = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        
        main_page.click_to_question(question)
        assert main_page.get_answer_text(answer) == answer