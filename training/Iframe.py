import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(option)
act_obj=ActionChains(driver)
driver.get('https://in.linkedin.com/')
time.sleep(2)
frame1=driver.find_element('xpath','//iframe[@title="Sign in with Google Button"]')
driver.switch_to.frame(frame1)
driver.find_element('xpath','//span[text()="Continue with Google"]').click()
time.sleep(1)
driver.switch_to.parent_frame()
    
