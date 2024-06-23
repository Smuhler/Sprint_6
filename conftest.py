import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('-headless')
    firefox_driver = webdriver.Firefox(options=options)
    firefox_driver.set_window_size(1920, 1080)
    yield firefox_driver
    firefox_driver.quit()
