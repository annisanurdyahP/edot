from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginWeb:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_use_email_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Use Email or Username')]"))
        ).click()

    def enter_email(self, email):
        self.wait.until(EC.visibility_of_element_located(
            (By.NAME, "username"))).send_keys(email)

    def login_button(self):
       return self.driver.find_element(By.XPATH, "//button[contains(text(), 'Log In')]")

    def click_next(self):
        self.login_button().click()

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(
            (By.NAME, "password"))).send_keys(password)

    def login_with_email_password(self, email, password):
        self.click_use_email_button()
        self.enter_email(email)
        self.click_next()
        self.enter_password(password)
        self.click_next()