from conftest import *
from pages.main_page import *
from data import *


class TestAccordion:

    @allure.title('Проверка функционала «Вопросы о важном»')
    @allure.description('Кликаем на вопрос и сверяем ответ')
    @pytest.mark.parametrize('accordion_item_heading, accordion_item_panel_text, expected_text', accordion_data)
    def test_question_click_check_text(self, driver, accordion_item_heading, accordion_item_panel_text, expected_text):
        page = MainPage(driver)
        page.open_main_page()
        page.confirm_rcc()
        page.click_question(accordion_item_heading)
        assert page.get_text_from_question(accordion_item_panel_text) == expected_text
