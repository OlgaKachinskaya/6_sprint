import allure
from data import TestData
from locators.order_page_locators import OrderPageLocators
from .base_page import BasePage

class OrderPage(BasePage):

    @allure.step('Заполнение первой части полей формы и нажать Далее')
    def data_entry_first_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.name)
        self.send_key_to_input(OrderPageLocators.name, test_data[0])
        self.send_key_to_input(OrderPageLocators.lastname, test_data[1])
        self.send_key_to_input(OrderPageLocators.address, test_data[2])
        self.click_on_element(OrderPageLocators.metro)
        self.send_key_to_input(OrderPageLocators.metro, test_data[3])
        self.wait_visibility_of_element(OrderPageLocators.select_item_in_dropdown_metro)
        self.click_on_element(OrderPageLocators.select_item_in_dropdown_metro)
        self.send_key_to_input(OrderPageLocators.telephone, test_data[4])
        self.click_on_element(OrderPageLocators.button_next)

    @allure.step('Заполнение второй части полей формы и подтвердение')
    def data_entry_second_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.date)
        self.click_on_element(OrderPageLocators.date)
        self.send_key_to_input(OrderPageLocators.date, test_data[5])
        self.click_on_element(OrderPageLocators.checkbox_black_color_scooter)
        self.click_on_element(OrderPageLocators.field_rental_period)
        self.click_on_element(OrderPageLocators.dropdown_rental_period)
        self.click_on_element(OrderPageLocators.comment)
        self.send_key_to_input(OrderPageLocators.comment, test_data[6])
        self.click_on_element(OrderPageLocators.button_make_order)
        self.wait_visibility_of_element(OrderPageLocators.button_yes_confirm_order)
        self.click_on_element(OrderPageLocators.button_yes_confirm_order)

    @allure.step('Выбрать из выпадающего списка станцию метро')
    def select_station(self):
        self.click_on_element(OrderPageLocators.select_item_in_dropdown_metro)

    @allure.step('Ввести дату заказа в поле Когда привезти самокат')
    def send_keys_date_by_keyboard_input(self):
        self.send_key_to_input(OrderPageLocators.date, TestData.test_data_user1[5])

    @allure.step('Нажать на выбранную дату в выпадающем календаре поля ввода начала аренды')
    def click_date_in_calendar(self):
        self.click_on_element(OrderPageLocators.calendar_item)

    @allure.step('Проверить кнопку "посмотреть мстатус" после оформления заказа')
    def check_displaying_of_button_check_status_of_order(self):
        return self.check_displaying_of_element(OrderPageLocators.button_check_status_of_order)