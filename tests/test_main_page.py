import sys
import os
import allure
import pytest
from data import TestData
from pages.main_page import MainPage
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestMainPageFaq:
    @allure.title('проверка Вопросы о важном')
    @allure.description('Проверка появления правильного текста при нажании на иконки')
    @pytest.mark.parametrize('questions_number,expected_answer', TestData.test_data_question_answer)
    def test_click_faq_expand_icons_text_is_expected(self, driver, questions_number, expected_answer):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        main_page.wait_visibility_of_faq_items(questions_number)
        main_page.click_on_faq_items(questions_number)
        main_page.wait_visibility_of_faq_answer(questions_number)
        assert main_page.get_display_text_from_faq_answer(questions_number) == expected_answer
