import allure

from locators.main_page_locators import *
from urls import main_page_url
from pages.base_page import *


class MainPage(BasePage):
    accordion_data = [[accordion_item_headings[0], accordion_item_panel_texts[0], expected_texts[0]],
                      [accordion_item_headings[1], accordion_item_panel_texts[1], expected_texts[1]],
                      [accordion_item_headings[2], accordion_item_panel_texts[2], expected_texts[2]],
                      [accordion_item_headings[3], accordion_item_panel_texts[3], expected_texts[3]],
                      [accordion_item_headings[4], accordion_item_panel_texts[4], expected_texts[4]],
                      [accordion_item_headings[5], accordion_item_panel_texts[5], expected_texts[5]],
                      [accordion_item_headings[6], accordion_item_panel_texts[6], expected_texts[6]],
                      [accordion_item_headings[7], accordion_item_panel_texts[7], expected_texts[7]]]

    @staticmethod
    @allure.step(f'Открываем страницу {main_page_url}')
    def open_main_page(driver):
        driver.get(main_page_url)

    @staticmethod
    @allure.step('Соглашаемся на куки')
    def confirm_rcc(driver):
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(rcc_confirm_button)).click()

    @staticmethod
    @allure.step('Кликаем на вопрос')
    def click_question(driver, locator):
        MainPage.click_element(driver, locator)

    @staticmethod
    @allure.step('Проверяем текст под вопросом')
    def get_text_from_question(driver, locator):
        return MainPage.get_text_from_visible_element(driver, locator)

    @staticmethod
    @allure.step('Кликаем на кнопку "Заказать" и переходим к первому шагу')
    def click_order_button(driver, start_button):
        MainPage.click_element(driver, start_button)
