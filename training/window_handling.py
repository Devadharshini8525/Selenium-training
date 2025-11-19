import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver=webdriver.Chrome(option)
action=ActionChains(driver)
driver.get("https://demowebshop.tricentis.com/")
handle1=driver.window_handles
print(handle1)
action.send_keys(Keys.END).perform()
driver.find_element('link text','Google+').click()
handles2=driver.window_handles
print(handles2)
driver.switch_to.window(handles2[0])
print(handles2[0])
driver.find_element('xpath','//input[@placeholder="Search blog"]').send_keys("youtube")
driver.switch_to.window(handles2[1])
driver.find_element('link text','YouTube').click()
handles3=driver.window_handles
print(handles3)
driver.find_element('xpath','//input[@name="search_query"]').send_keys("dragon tailer")


