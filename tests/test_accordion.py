from conftest import *
from pages.main_page import *


class TestAccordion:

    @allure.title('Проверка функционала «Вопросы о важном»')
    @allure.description('Кликаем на вопрос и сверяем ответ')
    @pytest.mark.parametrize('accordion_item_heading, accordion_item_panel_text, expected_text', MainPage.accordion_data)
    def test_accordion_item_click_show_text(self, driver, accordion_item_heading, accordion_item_panel_text, expected_text):
        MainPage.open_main_page(driver)
        MainPage.confirm_rcc(driver)
        MainPage.click_question(driver, accordion_item_heading)
        assert MainPage.get_text_from_question(driver, accordion_item_panel_text) == expected_text
