import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver=webdriver.Chrome(option)
act_obj=ActionChains(driver)
# ## mouse hovering operation
# driver.get("https://www.myntra.com/")
# women=driver.find_element('xpath', '(//a[text()="Women"])[1]')
# act_obj.move_to_element(women).perform()
# boy=driver.find_element('xpath','(//a[text()="Genz"])[1]')
# act_obj.move_to_element(boy).perform()

# ## Double click

# driver.get("https://testautomationpractice.blogspot.com/")
# double_click=driver.find_element('xpath','//a[text()="Udemy Courses"]')
# act_obj.double_click(double_click).perform()

# ## Right Click

# driver.get('https://www.facebook.com/r.php?entry_point=login')
# right_click=driver.find_element('xpath','//div[text()="Create a new account"]')
# act_obj.context_click(right_click).perform()

# ## Scrolling Down and up

# driver.get('https://www.swarovski.com/')
# ## page-down operation
# act_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# act_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(1)
# act_obj.send_keys(Keys.PAGE_DOWN).perform()

# # ## page-up operation

# act_obj.send_keys(Keys.PAGE_UP).perform()
# time.sleep(1)
# act_obj.send_keys(Keys.PAGE_UP).perform()
# time.sleep(1)
# act_obj.send_keys(Keys.PAGE_UP).perform()

# ## Scroll down to the end of the application

# act_obj.send_keys(Keys.END).perform()
# time.sleep(1)
# act_obj.send_keys(Keys.HOME).perform()

# ## to scroll to a particular web-element

# ele = driver.find_element('xpath', '//h3[text()="Maximum brilliance"]')
# act_obj.scroll_to_element(ele).perform()
# # scroll=driver.find_element('xpath','//h3[text()="A celebration of joy"]')
# # act_obj.scroll_to_element(scroll).perform()

# ## Drag and drop


driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)

ele = driver.find_element('xpath', '//h2[text()="Drag and Drop"]')
act_obj.scroll_to_element(ele).perform()

draggable_ele = driver.find_element('xpath', '//div[@id="draggable"]')
droppable_ele = driver.find_element('xpath', '//div[@id="droppable"]')

act_obj.drag_and_drop(draggable_ele, droppable_ele).perform()