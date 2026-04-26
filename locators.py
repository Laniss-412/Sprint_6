from selenium.webdriver.common.by import By

class MainPageLocators:
    #Кнопка принятия куки 
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button") 
    
    #Шаблон для вопроса
    QUESTION_LOCATOR = (By.XPATH, ".//div[@class='accordion__button' and text()='{}']")

    #Шаблон для ответов
    ANSWER_LOCATOR = (By.XPATH, ".//div[@class='accordion__panel']//p[text()='{}']")
    
class OrderPageLocators:
    #Кнопки "Заказать"
    TOP_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]//button")

    #Форма "Для кого самокат"
    NAME_FIELD = (By.XPATH, ".//input[@placeholder='* Имя']") #Поле ввода Имя
    SURNAME_FIELD = (By.XPATH, ".//input[@placeholder='* Фамилия']") #Поле ввода Фамилия
    ADDRESS_FIELD = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']") #Поле ввода Адрес
    METRO_FIELD = (By.XPATH, ".//input[@placeholder='* Станция метро']") #Поле ввода Метро
    PHONE_FILED = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер]") #Поле ввода телефона
    METRO_STATION_OPTION = (By.XPATH, ".//div[@class='select-search__select']//li") #Выбора станции из списка
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']") #Кнопка "Далее"

    #Форма "Про аренду"
    DATE_FIELD = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']") #Поле выбора даты
    CURRENT_DATE = (By.XPATH, ".//div[contains(@class, 'react-datepicker__day--today')]") #Выбор текущей даты в календаре
    PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-control") #Поле для открытия списка срока аренды
    PERIOD_OPTION = (By.XPATH, ".//div[@class='Dropdown-menu']//div[text()='{}']") #Шаблон для срока аренды
    COLOR_BLACK = (By.ID, "black") #Выбор цвета чёрный жемчуг
    COLOR_GREY = (By.ID, "grey") #Выбор цвета серая безысходность
    COMMENT_FIELD = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']") #Поле ввода коментария для курьера
    FINAL_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']") #Кнопка "Заказать"
    CONFIRM_YES_BUTTON = (By.XPATH, ".//button[text()='Да']") # Кнопка "Да" в форме подтверждения заказа


class HeaderLocators:
    SCOOTER_LOGO = (By.XPATH, ".//img[@alt='Scooter']") #Логотип "Самокат"
    YANDEX_LOGO = (By.XPATH, ".//img[@alt='Yandex']") #Логотип "Яндекс"