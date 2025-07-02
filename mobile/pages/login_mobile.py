from appium.webdriver.common.appiumby import AppiumBy

class LoginMobile:
    def __init__(self, driver):
        self.driver = driver

    def input_username(self,username):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "username").send_keys(username)

    def input_password(self, password):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "password").send_keys(password)

    def tap_login_button(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "login_button").click()