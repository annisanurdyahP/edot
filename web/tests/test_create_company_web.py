import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from web.pages.login_web import LoginWeb
from web.pages.create_company import CreateCompany
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import time


load_dotenv()
fake = Faker()

company_name = fake.company()
email = fake.email()

data_register_company = [
    { "title": "Create Companies with Valid Data",
      "company_phone": "13000010",
      "industry_type": "Healthcare",
      "company_type": "Retailer",
      "language": "Indonesia",
      "address": "Jl Jalan Kenangan",
      "country": "Indonesia",
      "province": "DKI JAKARTA",
      "city": "JAKARTA SELATAN",
      "district": "SETIABUDI",
      "sub_district": "KARET",
      "city_branch": "JAKARTA PUSAT",
      "district_branch": "GAMBIR",
      "sub_district_branch": "CIDENG",
    },
]

def test_case_create_company():
  for data in data_register_company:
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.get(os.getenv("WEB_BASEURL"))
    login_page = LoginWeb(driver)
    login_page.login_with_email_password(os.getenv("USERNAME"), os.getenv("PASSWORD"))

    # Click Companies meny from homepage
    driver.implicitly_wait(10)
    company_page = CreateCompany(driver)
    company_page.click_company_menu()
    company_page.wait_until_element_text_visible("My Company")
    company_page.click_add_company_button()

# Step 1 - Register Company
    company_page.wait_until_element_text_visible("Register Company")
    company_page.fill_input_placeholder_by_text("Input Company Name", company_name)
    input_company_name_value = company_page.get_input_value_by_placeholder("Input Company Name")
    print("DEBUG: company_name =", company_name)
    print("DEBUG: input_company_name_value =", input_company_name_value)
    assert input_company_name_value == company_name
    company_page.fill_input_placeholder_by_text("Input Email", email)
    company_page.fill_input_placeholder_by_text("Input Phone", data["company_phone"])
    company_page.select_dropdown_option_by_label("Choose Industry Type", data["industry_type"])
    company_page.select_dropdown_option_by_label("Choose Company Type", data["company_type"])
    company_page.select_dropdown_option_by_label("Choose Language", data["language"])
    company_page.fill_input_placeholder_by_text("Input Address", data["address"])
    company_page.select_dropdown_option_by_label("Choose Country", data["country"])
    company_page.select_dropdown_option_by_label("Choose Province", data["province"])
    company_page.select_dropdown_option_by_label("Choose City", data["city"])
    company_page.select_dropdown_option_by_label("Choose District", data["district"])
    company_page.select_dropdown_option_by_label("Choose Sub District", data["sub_district"])
    company_page.click_button("Next")

# Step 2 - Register Legal & Bank
    company_page.wait_until_element_text_visible("Register Legal & Bank")
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../test_data/file_test.jpg'))
    company_page.fill_legal_document(file_path)
    company_page.click_button("Next")
    time.sleep(5)

# Step 3 - Create Your Branch
    company_page.wait_until_element_text_visible("Create Your Branch")
    company_page.fill_input_placeholder_by_text("Input Branch Name", f"Branch {company_name}")


# if data address branch is different
    company_page.fill_input_placeholder_by_text("Input Address", data["address"])
    company_page.select_dropdown_option_by_label("Choose Country", data["country"])
    company_page.select_dropdown_option_by_label("Choose Province", data["province"])
    company_page.select_dropdown_option_by_label("Choose City", data["city_branch"])
    company_page.select_dropdown_option_by_label("Choose District", data["district_branch"])
    company_page.select_dropdown_option_by_label("Choose Sub District", data["sub_district_branch"])
    checkbox_agreement_btn = driver.find_element(By.ID, "select-all")
    checkbox_agreement_btn.click()
    company_page.click_button("Register")
    company_page.wait_until_element_text_visible("My Company", 20)
    company_page.click_manage_button_by_company_name(input_company_name_value)

    assert company_page.get_input_value_by_placeholder("Input Company Name") == input_company_name_value
    assert company_page.get_selected_card_by_label("Industry Type") == data["industry_type"]
    assert company_page.get_selected_card_by_label("Company Type") == data["company_type"]
    company_id = company_page.get_company_id()
    print("DEBUG: company_id =", company_id)
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../test_data/company_id.txt'))
    with open(file_path, "w") as f:
      f.write(str(company_id))

