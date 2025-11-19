# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# option=webdriver.ChromeOptions()
# option.add_experimental_option("detach",True)
# driver=webdriver.Chrome(option)
# driver.get(r'file:///E:/Qspider/Selenium/demo.html')
# time.sleep(2)

###############              Standarded_listbox    ############################

###############              Singleselect_listbox    ############################
#singleselect_listbox=driver.find_element('xpath','//select[@id="standard_cars"]')
#time.sleep(1)
#obj_select=Select(singleselect_listbox)
#obj_select.select_by_index(1)
#time.sleep(2)
#obj_select.select_by_value("jgr")
#time.sleep(2)
#obj_select.select_by_visible_text("BMW")
#time.sleep(2)


###############              Multiselect_listbox    ############################
#Multipleselect_listbox=driver.find_element('xpath','//select[@id="multiple_cars"]')
#obj_select=Select(Multipleselect_listbox)
#obj_select.select_by_index(3)
#obj_select.select_by_value('lr')
#obj_select.select_by_visible_text("Mini")


###############              Not Standarded_listbox    ############################

# import time
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument("--disable-notifications")
# driver = webdriver.Chrome(opts)
# driver.get('https://www.irctc.co.in/nget/train-search')
# time.sleep(2)
# driver.find_element('xpath','//div[@role="button"][1]').click()
# driver.find_element('xpath','//li[@aria-label="Anubhuti Class (EA)"]').click()
# driver.find_element('xpath','(//div[@role="button"])[2]').click()
# driver.find_element('xpath','//li[@aria-label="LADIES"]').click()


###############             Singleselect listbox  - with multi select    ############################
##########          wap to select all the elements of the dropdown one by one    ###########

import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
option.add_argument('--disable-notifications')
driver=webdriver.Chrome(option)
driver.get(r'file:///E:/Qspider/Selenium/demo.html')
singleselect_listbox = driver.find_element('xpath', '//select[@id="standard_cars"]')
select_obj = Select(singleselect_listbox)
time.sleep(2)
all_cars=driver.find_elements('xpath','//select[@id="standard_cars"]/option')
print(all_cars)
for car in range(0,len(all_cars)):
    select_obj.select_by_index(car)




