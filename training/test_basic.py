import pytest
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


@pytest.fixture(scope="class",params=['chrome','edge'])
def setup(request):
    driver=request.param
    if driver=="chrome":
        driver = webdriver.Chrome(options)
    elif driver=="edge":
        driver=webdriver.Edge()

    driver.get("https://demowebshop.tricentis.com/")
    yield driver
    driver.close()


class TestRegisteration:
   def test_register(self,setup):
    setup.find_element('xpath','//a[@class="ico-register"]').click()
   def test_gender(self,setup):
    setup.find_element('xpath','//input[@name="Gender"]').click()
   def test_firstname(self,setup):
    setup.find_element('xpath','//input[@id="FirstName"]').send_keys("deva")
   def test_lastname(self,setup):
    setup.find_element('xpath','//input[@id="LastName"]').send_keys("R")
   def test_email(self,setup):
     setup.find_element('xpath','//input[@id="Email"]').send_keys("deva@gmail.com")
   def test_password(self,setup):
    setup.find_element('name',"Password").send_keys("341414")
   def test_password2(self,setup):
    setup.find_element('name','ConfirmPassword').send_keys("341414")


class TestLogin:
    def test_login(self,setup):
     setup.find_element('class name',"ico-login").click()
    def test_email(self,setup):
     setup.find_element('class name',"email").send_keys("deva@gmail.com")
    def test_password(self,setup):
     setup.find_element('class name',"password").send_keys("34141")