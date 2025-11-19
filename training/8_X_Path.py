###########################                         X Path                 ########################
###########  Absolute X Path #############
# import time
# from selenium import webdriver
# a=webdriver.ChromeOptions()
# a.add_experimental_option('detach',True)
# b=webdriver.Chrome(a)
# b.get("https://www.saucedemo.com/")
# time.sleep(2)
# b.find_element('xpath','html/body/div/div/div[2]/div/div/div/form/div/input').send_keys('standard_user')
# time.sleep(2)
# b.find_element('xpath','html/body/div/div/div[2]/div/div/div/form/div[2]/input').send_keys('secret_sauce')
# time.sleep(2)
# b.find_element('xpath','html/body/div/div/div[2]/div/div/div/form/input').click()


###########  Relative X Path - Attribute name & value  #############

#                 //tagname[@attri_name="attri_values"]

# import time
# from selenium import webdriver
# a=webdriver.ChromeOptions()
# a.add_experimental_option('detach',True)
# b=webdriver.Chrome(a)
# b.get("https://www.instagram.com/accounts/emailsignup/")
# time.sleep(2)
# b.find_element('xpath','//input[@aria-label="Mobile Number or Email"]').send_keys('secret_sauce')
# time.sleep(1)
# b.find_element('xpath','//input[@aria-label="Password"]').send_keys('secret')
# time.sleep(1)
# b.find_element('xpath','//input[@name="fullName"]').send_keys('secret_sauce11111111111111')
# time.sleep(1)
# b.find_element('xpath','//input[@name="username"]').send_keys('s----9e')

###########  Relative X Path - Text #############

#                 //tagname[text()="text "]


#import time
#from selenium import webdriver
#a=webdriver.ChromeOptions()
#a.add_experimental_option('detach',True)
#b=webdriver.Chrome(a)
#b.get("https://www.flipkart.com/")
#time.sleep(2)
#b.find_element('xpath','//span[text()="Mobiles & Tablets"]').click()
#b.find_element('xpath','//span[text()="Become a Seller"]').click()
#b.find_element('xpath','//button[text()="Start Selling"]').click()



###########  Relative X Path - Group Indexing #############

#                 //tagname[@attri_name="attri_values"][IndexNo]

#import time
#from selenium import webdriver
#a=webdriver.ChromeOptions()
#a.add_experimental_option('detach',True)
#b=webdriver.Chrome(a)
#b.get(r'E:\Qspider\Selenium\css_selector.html')
#time.sleep(2)
#b.find_element('xpath','//input[@class="first_row"]').send_keys("Deva")
#b.find_element('xpath','//input[@class="first_row"][2]').send_keys("dharshini")


###########  Relative X Path - Text With Space - Contains #############

#                 //tagname[contains(text(),"Partial Text Content")]

#import time
#from selenium import webdriver
#a=webdriver.ChromeOptions()
#a.add_experimental_option('detach',True)
#b=webdriver.Chrome(a)
#b.get("https://www.giva.co/")
#time.sleep(2)
#b.find_element('xpath','//span[contains(text(),"Gold with Lab Diamonds")]').click()
#b.find_element('xpath','//span[contains(text(),"GIVA Gift Card")]').click()


###########  Relative X Path - Dependent-Independent X-Path #############

#                 //tagname[text()="Text Content"]/..//tagname[@attri_name="attri_values"]
#               /.. - one step back
#               /../.. - 2 step back

#import time
#from selenium import webdriver
#a=webdriver.ChromeOptions()
#a.add_experimental_option('detach',True)
#b=webdriver.Chrome(a)
#b.get(r'E:\Qspider\Selenium\demo.html')
#time.sleep(2)
#b.find_element('xpath','//td[text()="Ruby"]/..//input[@name="download"]').click()
#b.find_element('xpath','//td[text()="Java"]/..//input[@name="download"]').click()


###########  Relative X Path - Dependent Element is Changing #############


import time
from selenium import webdriver
a=webdriver.ChromeOptions()
a.add_experimental_option('detach',True)
b=webdriver.Chrome(a)
b.get("https://in.tradingview.com/")
time.sleep(2)
b.find_element('xpath', '//span[text()="Search"]').click()
time.sleep(1)
b.find_element('xpath', '//input[@name="query"]').send_keys("mrf")
b.find_element('xpath', '//span[@class="icon-KLRTYDjH"][1]').click()
mrf_price = b.find_element('xpath', '//span[text()="MRF"]/../../..//span[@class="priceWrapper-qWcO4bp9"]')
print(mrf_price.text)