from conftest import *
from pages.main_page import *
from pages.order_page import *


class TestOrderScooter:

    @allure.title('Проверка функционала заказа самоката')
    @allure.description(
        'Проходим весь флоу заказа самоката от главной страницы и проверяем, что появилось всплывающее окно с сообщением об успешном создании заказа')
    @pytest.mark.parametrize(
        'start_button, name, surname, address, metro_station, phone, date, period, colour, comment',
        OrderPage.order_data)
    def test_order_scooter(self, driver, start_button, name, surname, address, metro_station, phone, date, period,
                           colour, comment):
        MainPage.open_main_page(driver)
        MainPage.confirm_rcc(driver)
        MainPage.click_order_button(driver, start_button)
        OrderPage.fill_inputs_step_one(driver, name, surname, address, metro_station, phone)
        OrderPage.next_step(driver)
        OrderPage.fill_inputs_step_two(driver, date, period, colour, comment)
        OrderPage.order_done_click(driver)
        OrderPage.order_agree_click(driver)
        assert 'Заказ оформлен' in OrderPage.get_order_done_text(driver)

    @allure.title('Проверка ссылки на логотипе «Самоката»')
    @allure.description('Кликаем по лого и проверяем куда попали')
    def test_click_logo_scooter(self, driver):
        OrderPage.open_order_page(driver)
        OrderPage.logo_scooter_click(driver)
        assert OrderPage.check_current_url(driver) == main_page_url

    @allure.title('Проверка ссылки на логотипе «Яндекс»')
    @allure.description('Кликаем по лого и проверяем куда попали')
    def test_click_logo_yandex(self, driver):
        OrderPage.open_order_page(driver)
        OrderPage.logo_yandex_click(driver)
        OrderPage.switch_browser_tab(driver)
        OrderPage.waiting_dzen_loaded(driver)
        assert OrderPage.check_current_url(driver) == dzen_redirect_url
