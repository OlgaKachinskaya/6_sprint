import allure
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains

class MainPage(BasePage):

    @allure.step('ждем загрузки кнопки Заказать в хэдер')
    def wait_visibility_of_order_button_in_header(self):
        self.wait_visibility_of_element(MainPageLocators.order_button_in_header)

    @allure.step('жмем на кнопку заказать в хедере')
    def click_on_order_button_in_header(self):
        self.click_on_element(MainPageLocators.order_button_in_header)

    @allure.step('ждем загрузки лого "Самокат" в хедере')
    def wait_visibility_of_header_logo_scooter(self):
        self.wait_visibility_of_element(MainPageLocators.header_logo_scooter)

    @allure.step('ждем загрузки лого "яндекс" в хедере')
    def wait_visibility_of_header_logo_yandex(self):
        self.wait_visibility_of_element(MainPageLocators.header_logo_yandex)

    @allure.step('Кликнуть по лого Самакат в хэдере')
    def click_on_header_logo_scooter(self):
        self.click_on_element(MainPageLocators.header_logo_scooter)

    @allure.step('Кликнуть по лого Самакат в yandex')
    def click_on_header_logo_yandex(self):
        self.click_on_element(MainPageLocators.header_logo_yandex)

    @allure.step('ждем загрузки отобраения заголовка главной стр')
    def wait_visibility_of_main_header(self):
        self.wait_visibility_of_element(MainPageLocators.main_header)

    @allure.step('Проверяем отобразился ли заголовок главной стр')
    def check_display_main_header(self):
        return self.check_displaying_of_element(MainPageLocators.main_header)

    @allure.step('Скроллим до секции Вопросы о важном')
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.faq_section)

    @allure.step('Ждем прогрузки вопросов в секции Вопросы о важном')
    def wait_visibility_of_faq_items(self,data):
        self.wait_visibility_of_element(MainPageLocators.faq_questions_items[data])

    @allure.step('Нажать на нужный номер вопроса в секции в вопросы о важном')
    def click_on_faq_items(self, data):
        element = self.driver.find_element(*MainPageLocators.faq_questions_items[data])
        actions = ActionChains(self.driver)
        actions.move_to_element(element).pause(0.5).click().perform()

    @allure.step('ждем прогрузки необходимого номера ответа в Вопросах о важном')
    def wait_visibility_of_faq_answer(self, data):
        self.wait_visibility_of_element(MainPageLocators.faq_answer_items[data])

    @allure.step('Получить текст нужного номера ответа в секции вопросы о важном')
    def get_display_text_from_faq_answer(self, data):
        return self.get_text_on_element(MainPageLocators.faq_answer_items[data])