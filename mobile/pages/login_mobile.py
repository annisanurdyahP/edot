from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginMobile:
    def __init__(self, driver):
        self.driver = driver

    def input_company_id(self, company_id):
      wait = WebDriverWait(self.driver, 10)
      input_field = wait.until(EC.presence_of_element_located((AppiumBy.ID, "id.edot.ework.debug:id/tv_company_id")))
      input_field.send_keys(company_id)

    def input_username(self, username):
        self.driver.find_element(AppiumBy.ID, "id.edot.ework.debug:id/tv_username").send_keys(username)

    def input_password(self, password):
        self.driver.find_element(AppiumBy.ID, "id.edot.ework.debug:id/tv_password").send_keys(password)

    def tap_login_button(self):
        self.driver.find_element(AppiumBy.ID, "id.edot.ework.debug:id/button_text").click()

