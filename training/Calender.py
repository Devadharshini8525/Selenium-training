import time
from calendar import month

from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(option)
driver.get('https://www.makemytrip.com/')
time.sleep(2)
option.add_argument('--disable-notifications')
driver.maximize_window()
driver.find_element('xpath', '//span[@class="commonModal__close"]').click()
driver.find_element('xpath', '//span[text()="Departure"]').click()
time.sleep(2)


#########################       try and except         ###########
# def select_date(month, date):
#     while True:
#         try:
#             driver.find_element('xpath', f'//div[text()="{month}"]/../..//p[text()="{date}"]').click()
#             break
#         except:
#             driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()
#
# select_date('August 2026', 19)

#########################       IF ELSE        ###########


