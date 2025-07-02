import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from web.pages.login_web import LoginWeb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


load_dotenv()

login_data = [
    {"title": "valid login", "email": os.getenv("USERNAME"), "password": os.getenv("PASSWORD")},
    {"title": "invalid password", "email": os.getenv("USERNAME"), "password": "salah123"},
    {"title": "invalid format email", "email": "it.qa@ed", "password": os.getenv("PASSWORD")},
    {"title": "unregistered email", "email": "it.abc@test.com", "password": os.getenv("PASSWORD")},
    {"title": "case-sensitive email", "email": os.getenv("USERNAME").upper(), "password": os.getenv("PASSWORD")},

]

def test_login_looping():
    for data in login_data:
        options = Options()
        # options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)

        driver.get(os.getenv("WEB_BASEURL"))
        login_page = LoginWeb(driver)

        login_page.click_use_email_button()
        login_page.enter_email(data["email"])

        # Wrong Invalid Format Email
        if data["title"] == "invalid format email":
          login_btn = login_page.login_button()
          is_disabled_btn = login_btn.get_attribute("disabled")
          assert is_disabled_btn == "true"
          error_format_email = driver.find_element(By.XPATH, "//p[contains(text(), 'Wrong email format')]").text
          assert "Wrong email format" in error_format_email
          driver.quit()
          continue

        #continue step if format email is valid
        login_page.click_next()


        # assertion unregistered and case-sensitive email
        if data["title"] in ["unregistered email", "case-sensitive email"]:
            error_email_unregistered = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Email Not Registered')]")))
            assert "Email Not Registered" in error_email_unregistered.text

            edit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Edit')]")
            assert edit_button.is_displayed()

            yes_register_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Yes, Register')]")
            assert yes_register_button.is_displayed()
            driver.quit()
            continue

#continue step if valid email
        login_page.enter_password(data["password"])
        login_page.click_next()
        driver.implicitly_wait(10)

        if data["title"] == "valid login":
            home_menu= driver.find_element(By.LINK_TEXT, "Home")
            assert home_menu.is_displayed()

            companies_menu = driver.find_element(By.LINK_TEXT, "Companies")
            assert companies_menu.is_displayed()

            settings_menu = driver.find_element(By.LINK_TEXT, "Settings")
            assert settings_menu.is_displayed()

            welcome_text = driver.find_element(By.XPATH, "//span[contains(text(), 'Welcome Back')]").text
            assert "Welcome Back" in welcome_text

        elif data["title"] == "invalid password":
            error_password = driver.find_element(By.XPATH, "//p[contains(text(), 'Incorrect password')]").text
            assert "Incorrect password" in error_password

        driver.quit()