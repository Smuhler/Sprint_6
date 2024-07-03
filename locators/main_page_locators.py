from selenium.webdriver.common.by import By

rcc_confirm_button = (By.ID, "rcc-confirm-button")
accordion_item_headings = [(By.ID, 'accordion__heading-0'),
                           (By.ID, 'accordion__heading-1'),
                           (By.ID, 'accordion__heading-2'),
                           (By.ID, 'accordion__heading-3'),
                           (By.ID, 'accordion__heading-4'),
                           (By.ID, 'accordion__heading-5'),
                           (By.ID, 'accordion__heading-6'),
                           (By.ID, 'accordion__heading-7')]
accordion_item_panel_texts = [(By.XPATH, './/div[@id="accordion__panel-0"]/p'),
                              (By.XPATH, './/div[@id="accordion__panel-1"]/p'),
                              (By.XPATH, './/div[@id="accordion__panel-2"]/p'),
                              (By.XPATH, './/div[@id="accordion__panel-3"]/p'),
                              (By.XPATH, './/div[@id="accordion__panel-4"]/p'),
                              (By.XPATH, './/div[@id="accordion__panel-5"]/p'),
                              (By.XPATH, './/div[@id="accordion__panel-6"]/p'),
                              (By.XPATH, './/div[@id="accordion__panel-7"]/p')]
home_order_button = (By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button')
