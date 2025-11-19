import time
from selenium import webdriver
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver=webdriver.Chrome(option)
driver.get("https://www.saucedemo.com/")
time.sleep(3)
driver.find_element('id',"user-name").send_keys("standard_user")
driver.find_element('id',"password").send_keys("secret_sauce")
driver.find_element('id',"login-button").click()
driver.find_element('id',"react-burger-menu-btn").click()
driver.find_element('id','logout_sidebar_link').click()


