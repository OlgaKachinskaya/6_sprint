import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скролить до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Ждем загрузку элемента')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(locator))

    @allure.step('Нажать на элемент')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ввести значение в поле ввода')
    def send_key_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('получить текст на эл-те')
    def get_text_on_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('перейти на др вкладку')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('проверка отображение эл-та')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    def get_page_title(self):
        return self.driver.title

    @allure.step('Ожидать URL, содержащий "{text}"')
    def wait_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text)
        )

    @allure.step('Получить текущий URL')
    def current_url(self):
        return self.driver.current_url

    @allure.step('Проверка, что открылся Дзен')
    def verify_dzen_url(self):
        self.wait_url_contains("dzen.ru")
        return "dzen.ru" in self.current_url()

    @allure.step('Переключиться на новую вкладку')
    def switch_to_new_tab(self, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > 1
        )
        self.driver.switch_to.window(self.driver.window_handles[-1])

