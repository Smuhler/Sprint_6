from urls import main_page_url
from pages.base_page import *


class MainPage(BasePage):

    @allure.step(f'Открываем страницу {main_page_url}')
    def open_main_page(self):
        self.driver.get(main_page_url)

    @allure.step('Кликаем на вопрос')
    def click_question(self, locator):
        self.click_element(locator)

    @allure.step('Проверяем текст под вопросом')
    def get_text_from_question(self, locator):
        return self.get_text_from_visible_element(locator)

    @allure.step('Кликаем на кнопку "Заказать" и переходим к первому шагу')
    def click_order_button(self, start_button):
        self.click_element(start_button)
