import allure
from pages.main_page import MainPage



class TestLogo:
    @allure.title('Проверка клика на логотип Яндекс и перехода на страницу Дзена')
    def test_logo_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_header_logo_yandex()
        main_page.switch_to_new_tab()
        assert main_page.verify_dzen_url()

    @allure.title('Проверка клика на логотип Самоката')
    def test_logo_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_order_button_in_header()
        main_page.click_on_order_button_in_header()
        main_page.wait_visibility_of_header_logo_scooter()
        main_page.click_on_header_logo_scooter()
        main_page.wait_visibility_of_main_header()
        assert main_page.check_display_main_header()