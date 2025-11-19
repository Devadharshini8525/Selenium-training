import pytest
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
@pytest.fixture(scope="class")
def setup():
 driver = webdriver.Chrome(options)
 driver.get("https://demowebshop.tricentis.com/")
 yield driver
 driver.close()