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
expected_texts = ['Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
                  'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
                  'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
                  'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
                  'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
                  'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
                  'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
                  'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
home_order_button = (By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button')
