class TestLogin:
    def test_login(self,setup):
     setup.find_element('class name',"ico-login").click()
    def test_email(self,setup):
     setup.find_element('class name',"email").send_keys("deva@gmail.com")
    def test_password(self,setup):
     setup.find_element('class name',"password").send_keys("34141")