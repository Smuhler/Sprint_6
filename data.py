from locators.main_page_locators import *
from locators.base_page_locators import *
from locators.order_page_locators import *

expected_texts = ['Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
                  'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
                  'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
                  'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
                  'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
                  'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
                  'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
                  'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
accordion_data = [[accordion_item_headings[0], accordion_item_panel_texts[0], expected_texts[0]],
                      [accordion_item_headings[1], accordion_item_panel_texts[1], expected_texts[1]],
                      [accordion_item_headings[2], accordion_item_panel_texts[2], expected_texts[2]],
                      [accordion_item_headings[3], accordion_item_panel_texts[3], expected_texts[3]],
                      [accordion_item_headings[4], accordion_item_panel_texts[4], expected_texts[4]],
                      [accordion_item_headings[5], accordion_item_panel_texts[5], expected_texts[5]],
                      [accordion_item_headings[6], accordion_item_panel_texts[6], expected_texts[6]],
                      [accordion_item_headings[7], accordion_item_panel_texts[7], expected_texts[7]]]
names = [[name_input, 'Василий'], [name_input, 'Ащьф']]
surnames = [[surname_input, 'Пупкин'], [surname_input, 'Фштшфум']]
addresses = [[address_input, 'хттпс--куа-скутер.практикум-сервисес.ру--ордер'], [address_input, 'Москва СССР']]
metro_stations = [[metro_station_input, metro_station_buttons[0]], [metro_station_input, metro_station_buttons[1]]]
phones = [[phone_input, '+79999999999'], [phone_input, '80000000000']]
datepikers = [[datepicker_input, datepicker_day_selects[0]], [datepicker_input, datepicker_day_selects[1]]]
rental_period_listboxes = [[rental_period_listbox, rental_period_listbox_items[0]],
                           [rental_period_listbox, rental_period_listbox_items[1]]]
comments = [[comment_input, ''], [comment_input, 'Инкогнито, пожалуйста']]

order_data = [[order_header_button, names[0], surnames[0], addresses[0],
               metro_stations[0], phones[0], datepikers[0], rental_period_listboxes[0],
               black_pearl_checkbox, comments[0]],
              [home_order_button, names[1], surnames[1], addresses[1],
               metro_stations[1], phones[1], datepikers[1], rental_period_listboxes[1],
               gray_hopelessness_checkbox, comments[1]]]
