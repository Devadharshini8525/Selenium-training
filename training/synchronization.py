#import time
#from selenium import webdriver
#opts = webdriver.ChromeOptions()
#opts.add_experimental_option("detach", True)
#driver = webdriver.Chrome(opts)
#driver.get(r'E:\Qspider\Selenium\loading.html')
#time.sleep(20)
#driver.find_element('xpath','//input[@name="fname"]').send_keys("deva")
#driver.find_element('xpath','//input[@name="lname"]').send_keys("deva")


#############           xpath using implicit_wait       ############


#from selenium import webdriver
#opts = webdriver.ChromeOptions()
#opts.add_experimental_option("detach", True)
#driver = webdriver.Chrome(opts)
#driver.get(r'E:\Qspider\Selenium\loading.html')
#driver.implicitly_wait(20)
#driver.find_element('xpath','//input[@name="fname"]').send_keys("deva")
#driver.find_element('xpath','//input[@name="lname"]').send_keys("deva")



#############           xpath using explicit_wait       ############

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
wait=WebDriverWait(driver,10)
driver.get(r'E:\Qspider\Selenium\loading.html')
driver.find_element('xpath','//input[@name="fname"]').send_keys("standard_user")
driver.find_element('xpath','//input[@name="lname"]').send_keys("secret_sauceeeeeeeee")
driver.find_element('xpath','//input[@name="login"]').click()
try:
    wait.until(expected_conditions.visibility_of_element_located(('xpath', '//span[text()="Products"]')))
    print("successfully login")
except:
    print("Unsuccessfully login")

