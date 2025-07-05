from appium import webdriver
from appium.options.android import UiAutomator2Options

def create_capabilities(apk_path):
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("appium:automationName", "UiAutomator2")
    options.set_capability("appium:app", apk_path)
    options.set_capability("appium:deviceName", "R9CX500YF0Y")
    options.set_capability("appium:appPackage", "id.edot.ework.debug")
    options.set_capability("appium:appActivity", "id.edot.onboarding.ui.splash.SplashScreenActivity")
    # options.set_capability("appium:appActivity", "id.edot.onboarding.OnBoardingActivity")
    options.set_capability("appium:newCommandTimeout", 300)
    options.set_capability("appium:adbExecTimeout", 20000)
    options.set_capability("appium:uiautomator2ServerInstallTimeout", 20000)
    options.set_capability("appium:autoGrantPermissions", True)
    options.set_capability("appium:noReset", False)
    return options

def create_driver(apk_path):
    options = create_capabilities(apk_path)
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    return driver