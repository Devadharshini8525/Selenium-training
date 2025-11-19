# import time
# import pytest
# from selenium import webdriver
# opt=webdriver.ChromeOptions()
# opt.add_experimental_option("detach",True)
#
#
#
# @pytest.fixture(scope='class', params=['chrome', 'firefox', 'edge'])
# def setup(request):
#     parameter = request.param       ## parameter = edge
#
#     if parameter == 'chrome':
#         driver = webdriver.Chrome(opt)
#     elif parameter == 'firefox':
#         driver = webdriver.Firefox()
#     elif parameter == 'edge':
#         driver = webdriver.Edge()
#
#     driver.get("https://demowebshop.tricentis.com/")
#     time.sleep(2)
#     yield driver
#     driver.close()
#
# class TestRegister:
#   def test_register(self,setup):
#     setup.find_element("xpath",'//a[text()="Register"]').click()
#   def test_gender(self,setup):
#     setup.find_element("xpath",'//label[@for="gender-female"]').click()
#   def test_firstname(self,setup):
#    setup.find_element("xpath",'//input[@id="FirstName"]').send_keys('John')
#   def test_lastname(self,setup):
#     setup.find_element("xpath",'//input[@id="LastName"]').send_keys("Doe")
#   def test_email(self,setup):
#     setup.find_element("xpath",'//input[@id="Email"]').send_keys("deva@gmail.com")
#
# class TestLogin:
#  def test_login(self,setup):
#   setup.find_element("xpath",'//a[text()="Log in"]').click()
#  def test_em(self,setup):
#   setup.find_element("xpath",'//input[@name="Email"]').send_keys("deva@gmail.com")
#  def test_password(self,setup):
#   setup.find_element("xpath",'//input[@id="Password"]').send_keys("deva123")
#
# # import pytest
# # @pytest.fixture(autouse=True,scope="class")
# # def content():
# #  print("hi")
# #  yield
# #  print("bye")
# #
# # @pytest.fixture()
# # def sum():
# #   print("GM")
# #   yield
# #   print("GN")
# #
# # class TestSuma:
# #  def test_login(self):
# #   print("login")
# #
# # class Testlogout():
# #  def test_logout(self):
# #   print("logout")
#
# # import pytest
# # @pytest.mark.sanity
# # class TestSuma:
# #    @pytest.mark.san
# #    def test_login(self):
# #       print("login")
# #
# # @pytest.mark.sanity
# # @pytest.mark.saan
# # class Testlogout():
# #    def test_logout(self):
# #      print("logout")

# import pytest
# @pytest.mark.parametrize("a,b",[[10,20],[50,60]])
# def test_add(a,b):
#   print(a+b)

# import time
# import pytest
# from selenium import webdriver
# opt=webdriver.ChromeOptions()
# opt.add_experimental_option("detach",True)
#
# @pytest.mark.parametrize("un,pwd",[['ss222','ss2222@gamil.com'],['dd2222','ddEmbf6@gamil.com']])
# def test_demo(un,pwd):
#  driver = webdriver.Chrome(opt)
#  driver.get("https://demowebshop.tricentis.com/")
#  driver.maximize_window()
#  driver.implicitly_wait(5)
#  driver.find_element("xpath",'//a[text()="Log in"]').click()
#  driver.find_element("xpath",'//input[@name="Email"]').send_keys(un)
#  driver.find_element("xpath",'//input[@id="Password"]').send_keys(pwd)
#  driver.find_element("xpath",'//input[@value="Log in"]').click()
#  logout_btn = driver.find_element("xpath", '//a[text()="Log out"]')
#  if logout_btn.is_displayed():
#   print(driver.title)
#   logout_btn.click()
#  else:
#   print(driver.title)
#  driver.close()

# import pytest
# class TestSuma:
#  @pytest.mark.dependency()
#  def test_login(self):
#     print("Logging")
#
#  @pytest.mark.dependency(depends=["TestSuma::test_login"])
#  def test_reg(self):
#     print("registered")
#
#  @pytest.mark.dependency(depends=[":TestSuma:test_reg"])
#  def test_logout(self):
#     print("logout")

import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
act_obj=WebDriverWait(driver,10)
driver.get("https://www.saucedemo.com/")
time.sleep(1)
@pytest.mark.dependency()
def test_suma():
    driver.find_element('id', 'user-name').send_keys('standard_user')
    driver.find_element('id', 'password').send_keys('secret_sauceeeee')
    driver.find_element('id', 'login-button').click()
    time.sleep(2)
    act_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//span[text()="Products"]')))




