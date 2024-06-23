import pytest
from selenium import webdriver
import time


@pytest.fixture(scope="function")
# def driver():
#     options = webdriver.FirefoxOptions()
#     options.add_argument('--ignore-certificate-errors')
#     options.add_argument('--ignore-ssl-errors')
#     options.add_argument('-headless')
#     firefox_driver = webdriver.Firefox(options=options)
#     firefox_driver.set_window_size(1920, 1080)
#     yield firefox_driver
#     firefox_driver.quit()


def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    time.sleep(3)
    chrome_driver.close()
