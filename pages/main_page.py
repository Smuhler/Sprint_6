from data import *
from pages.base_page import *
from urls import main_page_url


class MainPage(BasePage):

    @allure.step(f'Открываем страницу {main_page_url}')
    def open_main_page(self):
        self.driver.get(main_page_url)

    @allure.step('Соглашаемся на куки')
    def confirm_rcc(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(rcc_confirm_button)).click()

    @allure.step('Кликаем на вопрос')
    def click_question(self, locator):
        self.click_element(locator)

    @allure.step('Проверяем текст под вопросом')
    def get_text_from_question(self, locator):
        return self.get_text_from_visible_element(locator)

    @allure.step('Кликаем на кнопку "Заказать" и переходим к первому шагу')
    def click_order_button(self, start_button):
        self.click_element(start_button)
