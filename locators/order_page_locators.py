from selenium.webdriver.common.by import By

name_input = (By.XPATH, './/input[@placeholder="* Имя"]')
surname_input = (By.XPATH, './/input[@placeholder="* Фамилия"]')
address_input = (By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]')
metro_station_input = (By.XPATH, './/input[@placeholder="* Станция метро"]')
metro_station_buttons = [(By.XPATH, './/button[@value="177"]'),
                         (By.XPATH, './/button[@value="1"]')]
phone_input = (By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]')
next_step_button = (By.XPATH, './/button[text()="Далее"]')
datepicker_input = (By.XPATH, './/input[@placeholder="* Когда привезти самокат"]')
datepicker_day_selects = [(By.XPATH, './/div[@class="react-datepicker__day react-datepicker__day--028"]'),
                          (By.XPATH, './/div[@class="react-datepicker__day react-datepicker__day--013"]')]
rental_period_listbox = (By.XPATH, './/div[text()="* Срок аренды"]')
rental_period_listbox_items = [(By.XPATH, './/div[text()="сутки"]'),
                               (By.XPATH, './/div[text()="семеро суток"]')]
black_pearl_checkbox = (By.ID, 'black')
gray_hopelessness_checkbox = (By.ID, 'grey')
comment_input = (By.XPATH, './/input[@placeholder="Комментарий для курьера"]')
complete_order_button = (By.XPATH, './/div[@class="Order_Buttons__1xGrp"]//button[text()="Заказать"]')
agree_order_button = (By.XPATH, './/button[text()="Да"]')
order_done_text = (By.XPATH, './/div[text()[contains(.,"Заказ оформлен")]]')
