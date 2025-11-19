import time
from selenium import webdriver
a=webdriver.ChromeOptions()
a.add_experimental_option('detach',True)
b=webdriver.Chrome(a)
b.get('https://demowebshop.tricentis.com/')
time.sleep(2)
b.find_element('link text',"Register").click()
b.find_element('link text','Log in').click()
time.sleep(3)
b.find_element('partial link text','Books').click()