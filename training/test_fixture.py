# import pytest
#
#
# @pytest.fixture(autouse=True,scope="module")
# def getup():
#     print("hello")
#     yield
#     print("tatan")
#
# @pytest.fixture(autouse=True,scope="class")
# def setup():
#     print("hiiiii")
#     yield
#     print("bye")
#
#
# class TestSample:
#  def test_login(self,setup):
#      print("login")
# class TestSample2:
#  def test_logout(self,getup):
#     print("logout")

import pytest
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options)
driver.get("https://demowebshop.tricentis.com/")

class TestRegisteration:
   def test_register(self):
    driver.find_element('xpath','//a[@class="ico-register"]').click()
   def test_gender(self):
    driver.find_element('xpath','//input[@name="Gender"]').click()
   def test_firstname(self):
    driver.find_element('xpath','//input[@id="FirstName"]').send_keys("deva")
   def test_lastname(self):
    driver.find_element('xpath','//input[@id="LastName"]').send_keys("R")
   def test_email(self):
    driver.find_element('xpath','//input[@id="Email"]').send_keys("deva@gmail.com")
   def test_password(self):
    driver.find_element('name',"Password").send_keys("341414")
   def test_password2(self):
    driver.find_element('name','ConfirmPassword').send_keys("341414")

class TestLogin:
    def test_login(self):
     driver.find_element('class name',"ico-login").click()
    def test_email(self):
     driver.find_element('class name',"email").send_keys("deva@gmail.com")
    def test_password(self):
     driver.find_element('class name',"password").send_keys("341414")



