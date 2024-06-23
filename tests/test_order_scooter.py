from conftest import *
from pages.main_page import *
from pages.order_page import *
from data import *


class TestOrderScooter:

    @allure.title('Проверка функционала заказа самоката')
    @allure.description(
        'Проходим весь флоу заказа самоката от главной страницы и проверяем, что появилось всплывающее окно с сообщением об успешном создании заказа')
    @pytest.mark.parametrize(
        'start_button, name, surname, address, metro_station, phone, date, period, colour, comment',
        order_data)
    def test_order_scooter(self, driver, start_button, name, surname, address, metro_station, phone, date, period,
                           colour, comment):
        page = MainPage(driver)
        page.open_main_page()
        page.confirm_rcc()
        page.click_order_button(start_button)
        page = OrderPage(driver)
        page.fill_inputs_step_one(name, surname, address, metro_station, phone)
        page.next_step()
        page.fill_inputs_step_two(date, period, colour, comment)
        page.order_done_click()
        page.order_agree_click()
        assert page.get_order_done_text()

    @allure.title('Проверка ссылки на логотипе «Самоката»')
    @allure.description('Кликаем по лого и проверяем куда попали')
    def test_click_logo_scooter(self, driver):
        page = OrderPage(driver)
        page.open_order_page()
        page.logo_scooter_click()
        assert page.check_current_url() == main_page_url

    @allure.title('Проверка ссылки на логотипе «Яндекс»')
    @allure.description('Кликаем по лого и проверяем куда попали')
    def test_click_logo_yandex(self, driver):
        page = OrderPage(driver)
        page.open_order_page()
        page.logo_yandex_click()
        page.switch_browser_tab()
        page.waiting_dzen_loaded()
        assert page.check_current_url() == dzen_redirect_url
