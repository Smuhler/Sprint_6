from locators.base_page_locators import *
from locators.order_page_locators import *
from pages.base_page import *
from urls import *


class OrderPage(BasePage):

    @allure.step(f'Открываем страницу {order_page_url}')
    def open_order_page(self):
        self.driver.get(order_page_url)

    @allure.step(f'Кликаем "Далее" и переходим на второй шаг')
    def next_step(self):
        self.click_element(next_step_button)

    @allure.step(f'Завершаем заказ по клику "Заказать"')
    def order_done_click(self):
        self.click_element(complete_order_button)

    @allure.step(f'Подтверждаем заказ')
    def order_agree_click(self):
        self.click_element(agree_order_button)

    @allure.step('Проверяем отображение на экране текста подтверждения заказа')
    def get_order_done_text(self):
        return self.is_visible_element(order_done_text)

    @allure.step(f'Кликаем на логотип "Самокат"')
    def logo_scooter_click(self):
        self.click_element(scooter_logo_link_locator)

    @allure.step(f'Кликаем на логотип "Яндекс"')
    def logo_yandex_click(self):
        self.click_element(yandex_logo_link_locator)

    @allure.step(f'Заполняем поля первого шага для заказа самоката')
    def fill_inputs_step_one(self, name, surname, address, metro_station, phone):
        self.input_text(name)
        self.input_text(surname)
        self.input_text(address)
        self.click_dropdown_and_element(metro_station)
        self.input_text(phone)

    @allure.step(f'Заполняем поля второго шага для заказа самоката')
    def fill_inputs_step_two(self, date, period, colour, comment):
        self.click_dropdown_and_element(date)
        self.click_dropdown_and_element(period)
        self.click_element(colour)
        self.input_text(comment)
