import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    @staticmethod
    @allure.step('Кликаем на элемент по локатору {locator}')
    def click_element(driver, locator):
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(locator)).click()

    @staticmethod
    @allure.step('Получаем текст элемента по локатору {locator}')
    def get_text_from_visible_element(driver, locator):
        return WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locator)).text

    @staticmethod
    @allure.step('Заполняем поле {locator_with_text[0]} текстом {locator_with_text[1]}')
    def input_text(driver, locator_with_text):
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(locator_with_text[0])).send_keys(locator_with_text[1])

    @staticmethod
    @allure.step('Кликаем на поле дропдауна {elements[0]} и на сам элемент дропауна {elements[1]}')
    def click_dropdown_and_element(driver, elements):
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(elements[0])).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(elements[1])).click()

    @staticmethod
    @allure.step('Переключаем вкладку')
    def switch_browser_tab(driver):
        driver.switch_to.window(driver.window_handles[1])

    @staticmethod
    @allure.step('Ожидаем загрузку страницы "Дзен"')
    def waiting_dzen_loaded(driver):
        WebDriverWait(driver, 5).until(expected_conditions.title_is('Дзен'))

    @staticmethod
    @allure.step('Проверяем на какой странице находимся')
    def check_current_url(driver):
        return driver.current_url
