import os
from appium import webdriver
from dotenv import load_dotenv
from mobile.pages.login_mobile import LoginMobile
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

load_dotenv()

def test_login():
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../test_data/company_id.txt'))
    with open(file_path, "r") as f:
      company_id = f.read().strip()
    apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../test_data/ework_1.20.5.apk'))

    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("appium:app", apk_path)
    options.set_capability("appium:deviceName", "RR8MA0EZPPN")
    options.set_capability("appium:appPackage", "id.edot.ework.debug")
    options.set_capability("appium:appActivity", "id.edot.onboarding.OnBoardingActivity")
    options.set_capability("appium:newCommandTimeout", 300)
    options.set_capability("appium:adbExecTimeout", 20000)
    options.set_capability("appium:uiautomator2ServerInstallTimeout", 20000)
    options.set_capability("appium:autoGrantPermissions", True)
    options.set_capability("appium:noReset", False)

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    login_page = LoginMobile(driver)

    login_page.input_company_id(company_id)
    login_page.input_username(os.getenv("USERNAME"))
    login_page.input_password(os.getenv("PASSWORD"))
    login_page.tap_login_button()

    time.sleep(5)
    driver.quit()
