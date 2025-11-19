## Customise Marker

# import pytest
# @pytest.mark.xfail
# class TestMarker:
#  @pytest.mark.sanity
#  @pytest.mark.training
#  def test_login(self):
#     print("login")
#
#  @pytest.mark.sanity
#  def test_reg(self):
#     print("reg")
#
#  @pytest.mark.fell
#  @pytest.mark.training
#  def test_testreg(self):
#     print("testreg")
#
#  @pytest.mark.well
#  def test_logout(self):
#     print("logout")


## In-build Marker
# skip

#
# import pytest
# @pytest.mark.xfail
# class TestMarker:
#  @pytest.mark.sanity
#  @pytest.mark.training
#  def test_login(self):
#     print("login")
#
#  @pytest.mark.skip
#  def test_reg(self):
#     print("reg")
#
#  @pytest.mark.fell
#  @pytest.mark.training
#  def test_testreg(self):
#     print("testreg")
#
#  @pytest.mark.well
#  def test_logout(self):
#     print("logout")


### skip with reason

# import pytest
# @pytest.mark.xfail
# class TestMarker:
#  @pytest.mark.sanity
#  @pytest.mark.training
#  def test_login(self):
#     print("login")
#
#  @pytest.mark.skip(reason="not needed")
#  def test_reg(self):
#     print("reg")
#
#  @pytest.mark.fell
#  @pytest.mark.training
#  def test_testreg(self):
#     print("testreg")
#
#  @pytest.mark.well
#  def test_logout(self):
#     print("logout")


## skip class
import pytest


# @pytest.mark.skip
# class TestMarker:
#
#  def test_login(self):
#     print("login")
#
#  def test_reg(self):
#     print("reg")
#
#  def test_testreg(self):
#     print("testreg")



##### skipif

# @pytest.mark.skipif(True, reason="This test is skipped for now")
# def test_reg():
#     print("reg")
# @pytest.mark.skipif(False,reason="This test is not skipped for now")
# def test_testreg():
#     print("testreg")


### xfail
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# option=webdriver.ChromeOptions()
# option.add_experimental_option("detach",True)
# driver=webdriver.Chrome(option)
# wait=WebDriverWait(driver,3)
# driver.get("https://www.saucedemo.com/")
# @pytest.mark.xfail
# def test_login():
#     driver.find_element('id', 'user-name').send_keys('standard_user')
#     driver.find_element('id', 'password').send_keys('secret_sauce')
#     driver.find_element('id', 'login-button').click()
#     time.sleep(2)
#     wait.until(expected_conditions.visibility_of_element_located(('xpath', '//span[text()="Products"]')))

# def test_login():
#     print("login executed")
# @pytest.mark.xfail
# def test_signup():
#     print("signup executed")
# def test_logout():
#     print("logout executed")

#### 3.Prametrize
import pytest
@pytest.mark.parametrize("a,b",[(9,7),(98,90),(100,120)])
def test_marker(a,b):
    print(a + b)
