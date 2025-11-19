import time
from selenium import webdriver
a=webdriver.ChromeOptions()
a.add_experimental_option('detach',True)
b=webdriver.Chrome(a)
b.get(r'E:\Qspider\Selenium\css_selector.html')
time.sleep(2)
b.find_element('tag name',"input").send_keys("deva")
time.sleep(2)
b.find_element('tag name',"input").send_keys("dharshini")