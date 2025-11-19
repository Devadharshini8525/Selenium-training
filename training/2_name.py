from selenium import webdriver
a=webdriver.ChromeOptions()
a.add_experimental_option("detach",True)
b=webdriver.Chrome(a)
#b.get("https://www.facebook.com/r.php?entry_point=login")
#b.find_element('name',"firstname").send_keys("Deva")
#b.find_element('name','lastname').send_keys('raj')
#b.find_element('name','reg_email__').send_keys('deva@gmail.com')
#b.find_element('name','reg_passwd__').send_keys('deva123')
b.get(r'file:///E:/Qspider/Selenium/css_selector.html')
b.find_element('name','fname').send_keys("deva")
b.find_element('name','fname').send_keys('dharshini')

