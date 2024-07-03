import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import *


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем на элемент по локатору {locator}')
    def click_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator)).click()

    @allure.step('Соглашаемся на куки')
    def confirm_rcc(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(rcc_confirm_button)).click()

    @allure.step('Получаем текст элемента по локатору {locator}')
    def get_text_from_visible_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator)).text

    @allure.step('Заполняем поле {locator_with_text[0]} текстом {locator_with_text[1]}')
    def input_text(self, locator_with_text):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator_with_text[0])).send_keys(locator_with_text[1])

    @allure.step('Кликаем на поле дропдауна {elements[0]} и на сам элемент дропауна {elements[1]}')
    def click_dropdown_and_element(self, elements):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(elements[0])).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(elements[1])).click()

    @allure.step('Переключаем вкладку')
    def switch_browser_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Ожидаем загрузку страницы "Дзен"')
    def waiting_dzen_loaded(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.title_is('Дзен'))

    @allure.step('Проверяем на какой странице находимся')
    def check_current_url(self):
        return self.driver.current_url

    @allure.step('Проверяем отображение элемента на экране')
    def is_visible_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
