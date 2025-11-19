import time
from turtledemo.paint import switchupdown

from selenium import webdriver
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
# driver.get("https://testautomationpractice.blogspot.com/")


############## Confirmation Alert ############
# driver.find_element('xpath', '//button[@id="confirmBtn"]').click()
# obj = driver.switch_to.alert
# obj.accept()
# time.sleep(1)
# driver.find_element('xpath','//button[@id="confirmBtn"]').click()
# time.sleep(1)
# obj.dismiss()

############## Simple Alert ############
# driver.find_element('xpath','//button[text()="Simple Alert"]').click()
# simple_alert=driver.switch_to.alert
# simple_alert.accept()

############## Prompt Alert ############
# driver.find_element('xpath','//button[text()="Prompt Alert"]').click()
# Prompt_Alert=driver.switch_to.alert
# Prompt_Alert.send_keys("deva")
# time.sleep(1)
# Prompt_Alert.accept()

############## Authentication pop-ups ############

# driver.get("https://the-internet.herokuapp.com/basic_auth")
# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")


############## Authentication pop-ups ############

# driver.get("https://testautomationpractice.blogspot.com/")
# singe_choose=driver.find_element('xapth','//input[@id="singleFileInput"]').click()

############## file-upload pop-up ############

# single_choose=driver.find_element('xpath','//input[@id="singleFileInput"]')
# single_choose.send_keys(r'E:\Qspider\Selenium\alerts_.py')
# multiple_choose=driver.find_element('xpath','//input[@id="multipleFilesInput"]')
# f1=r'E:\Qspider\Selenium\actionchains__.py'
# f2=r'E:\Qspider\Selenium\alerts_.py'
# multiple_choose.send_keys(f'{f1}\n{f2}')

############## file-upload pop-up ############
# option.add_argument("--disable-notifications")
# driver=webdriver.Chrome(option)
# driver.get('https://www.irctc.co.in/nget/train-search')