import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

ac_obj = ActionChains(driver)
driver.get('https://www.myntra.com/')
time.sleep(2)

women = driver.find_element('xpath', '(//a[text()="Women"])[1]')
ac_obj.move_to_element(women).perform()
time.sleep(2)

home = driver.find_element('xpath', '(//a[text()="Home"])[1]')
ac_obj.move_to_element(home).perform()
time.sleep(2)

genz = driver.find_element('xpath', '(//a[text()="Genz"])[1]')
ac_obj.move_to_element(genz).perform()