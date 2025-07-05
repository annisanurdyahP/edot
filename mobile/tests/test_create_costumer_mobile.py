import os
import random
import time
from faker import Faker
from dotenv import load_dotenv
from mobile.pages.create_costumer import CreateCostumer
from mobile.pages.login_mobile import LoginMobilePage
from mobile.pages.home_page_mobile import HomePage
from mobile.utils.login_setup import create_driver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()
fake = Faker()

def generate_indonesian_phone():
    prefix = random.choice(["812", "813", "815", "816"])
    suffix = ''.join([str(random.randint(0, 9)) for _ in range(7)])
    return prefix + suffix

def test_create_new_customer():
    outlet_name = fake.word().capitalize() + " Shop"
    outlet_email = fake.email()
    contact_person = "JOHN ALEXANDER"
    address = "Jl Alternatif Cibubur"
    phone = generate_indonesian_phone()

    apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../test_data/ework_1.20.5.apk'))
    driver = create_driver(apk_path)

    login = LoginMobilePage(driver)
    login.login()

    homepage = HomePage(driver)
    homepage.menu_in_homepage("Pelanggan Baru").click()
    time.sleep(3)
    create_customer = CreateCostumer(driver)
    create_customer.click_create_new_costumer()
    registration_page_title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ID, "id.edot.ework.debug:id/tv_title_reg_customer")))
    assert "Informasi Toko" in registration_page_title.text

    create_customer.step_one_register_new_costumer(outlet_name, outlet_email, contact_person, phone)
    create_customer.step_two_register_new_costumer(address)
    create_customer.step_three_upload_docs()
    create_customer.submit_signature(outlet_name)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ID, "id.edot.ework.debug:id/tv_address")))
    address_elements = driver.find_elements(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="id.edot.ework.debug:id/tv_address"]')
    address_texts = [el.text for el in address_elements]
    assert address in address_texts

    outlet_name_list = driver.find_elements(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="id.edot.ework.debug:id/tv_name"]')
    outlet_name_data = [el.text for el in outlet_name_list]
    assert outlet_name in outlet_name_data



