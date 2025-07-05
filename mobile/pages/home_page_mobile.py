from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def menu_in_homepage(self, name_menu):
        locator = (AppiumBy.XPATH, f'//android.widget.TextView[@resource-id="id.edot.ework.debug:id/txt_menu" and @text="{name_menu}"]')
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))