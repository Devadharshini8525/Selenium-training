from selenium import webdriver
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver=webdriver.Chrome(option)
driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")
driver.find_element(By.XPATH,"/html/body/div[6]/main/div/section/div/div[2]/div[1]/div/form/div[3]/button").click()
act_title=driver.title
exp_title="Just a moment..."
if act_title==exp_title:
 print("Login Test Passed")
else:
 print("Login Test Failed")
driver.close()
