from pages.base_page import *
from locators.order_page_locators import *
from locators.main_page_locators import home_order_button
from locators.base_page_locators import *
from urls import *


class OrderPage(BasePage):
    names = [[name_input, 'Василий'], [name_input, 'Ащьф']]
    surnames = [[surname_input, 'Пупкин'], [surname_input, 'Фштшфум']]
    addresses = [[address_input, 'хттпс--куа-скутер.практикум-сервисес.ру--ордер'], [address_input, 'Москва СССР']]
    metro_stations = [[metro_station_input, metro_station_buttons[0]], [metro_station_input, metro_station_buttons[1]]]
    phones = [[phone_input, '+79999999999'], [phone_input, '80000000000']]
    datepikers = [[datepicker_input, datepicker_day_selects[0]], [datepicker_input, datepicker_day_selects[1]]]
    rental_period_listboxes = [[rental_period_listbox, rental_period_listbox_items[0]],
                               [rental_period_listbox, rental_period_listbox_items[1]]]
    comments = [[comment_input, ''], [comment_input, 'Инкогнито, пожалуйста']]

    order_data = [[order_header_button, names[0], surnames[0], addresses[0],
                   metro_stations[0], phones[0], datepikers[0], rental_period_listboxes[0],
                   black_pearl_checkbox, comments[0]],
                  [home_order_button, names[1], surnames[1], addresses[1],
                   metro_stations[1], phones[1], datepikers[1], rental_period_listboxes[1],
                   gray_hopelessness_checkbox, comments[1]]]

    @staticmethod
    @allure.step(f'Открываем страницу {order_page_url}')
    def open_order_page(driver):
        driver.get(order_page_url)

    @staticmethod
    @allure.step(f'Кликаем "Далее" и переходим на второй шаг')
    def next_step(driver):
        OrderPage.click_element(driver, next_step_button)

    @staticmethod
    @allure.step(f'Завершаем заказ по клику "Заказать"')
    def order_done_click(driver):
        OrderPage.click_element(driver, complete_order_button)

    @staticmethod
    @allure.step(f'Подтверждаем заказ')
    def order_agree_click(driver):
        OrderPage.click_element(driver, agree_order_button)

    @staticmethod
    @allure.step('Получаем текст подтверждения заказа')
    def get_order_done_text(driver):
        return WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(order_done_text)).text

    @staticmethod
    @allure.step(f'Кликаем на логотип "Самокат"')
    def logo_scooter_click(driver):
        OrderPage.click_element(driver, scooter_logo_link_locator)

    @staticmethod
    @allure.step(f'Кликаем на логотип "Яндекс"')
    def logo_yandex_click(driver):
        OrderPage.click_element(driver, yandex_logo_link_locator)

    @staticmethod
    @allure.step(f'Заполняем поля первого шага для заказа самоката')
    def fill_inputs_step_one(driver, name, surname, address, metro_station, phone):
        OrderPage.input_text(driver, name)
        OrderPage.input_text(driver, surname)
        OrderPage.input_text(driver, address)
        OrderPage.click_dropdown_and_element(driver, metro_station)
        OrderPage.input_text(driver, phone)

    @staticmethod
    @allure.step(f'Заполняем поля первого шага для заказа самоката')
    def fill_inputs_step_two(driver, date, period, colour, comment):
        OrderPage.click_dropdown_and_element(driver, date)
        OrderPage.click_dropdown_and_element(driver, period)
        OrderPage.click_element(driver, colour)
        OrderPage.input_text(driver, comment)
