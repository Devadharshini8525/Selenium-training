import time
from selenium import webdriver
a=webdriver.ChromeOptions()
a.add_experimental_option('detach',True)
b=webdriver.Chrome(a)
b.get("https://demowebshop.tricentis.com/")
time.sleep(1)
b.find_element('css selector','a[class="ico-register"]').click()
time.sleep(1)
b.find_element('css selector','input[id="FirstName"]').send_keys("deva")
b.find_element('css selector','input[id="LastName"]').send_keys("dharshini")
b.find_element('css selector','input[id="Email"]').send_keys("Deva123@gamil.com")
b.find_element('css selector','input[id="Password"]').send_keys("1234")
b.find_element('css selector','input[id="ConfirmPassword"]').send_keys("1234")
