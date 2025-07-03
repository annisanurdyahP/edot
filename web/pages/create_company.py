from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CreateCompany:
      def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

      def company_menu(self):
        return self.driver.find_element(By.XPATH, "//a[contains(text(), 'Companies')]")

      def click_company_menu(self):
        self.company_menu().click()

      def wait_until_element_text_visible(self, element, timeout=15):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(), '{element}')]")))

      def click_add_company_button(self):
        add_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add Company')]")))
        add_button.click()

      def fill_input_placeholder_by_text(self, placeholder_text, value):
        input_field = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, f"//input[@placeholder='{placeholder_text}']")))
        input_field.clear()
        input_field.send_keys(value)

      def get_input_value_by_placeholder(self, placeholder_text, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        input_element = wait.until(EC.presence_of_element_located((By.XPATH, f"//input[@placeholder='{placeholder_text}']")))
        return input_element.get_attribute("value")

      def get_selected_card_by_label(self, label_text):
        xpath = f"//span[text()='{label_text}']/following::span[contains(@class, 'text-gray-700')][1]"
        element = self.driver.find_element(By.XPATH, xpath)
        return element.text

      def select_dropdown_option_by_label(self, field_name, option_list_text):
        dropdown_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, f"//button[.//span[text()='{field_name}']]")))
        dropdown_button.click()
# wait until option display
        option_xpath = f"//div[@role='option']//span[normalize-space(text())='{option_list_text}']"
        option = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
        option.click()

      def click_button(self, button_next):
        return WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//button[normalize-space()='{button_next}']"))).click()

      def fill_legal_document(self, file_path):
        wait = WebDriverWait(self.driver, 10)

        # click add document from step 2
        add_document_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Legal Document (optional)']/following::button[.='+ Add Document'][1]")))
        add_document_button.click()

        # Click field legal document option
        dropdown_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Choose Legal Document']]")))
        dropdown_button.click()

        # Choose type of Legal Document option
        legal_docs_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(., 'Identification Card')]")))
        legal_docs_option.click()

        # choose file docs button
        file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
        file_input.send_keys(file_path)

        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.='Submit Document']")))
        submit_button.click()


      def click_manage_button_by_company_name(self, companies_name: str):
        xpath_card_company_name = f"//div[@class='text-lg font-bold' and normalize-space()='{companies_name}']/ancestor::div[contains(@class, 'rounded-lg')]//button[normalize-space()='Manage']"
        self.driver.find_element(By.XPATH, xpath_card_company_name).click()

      def teardown_data_company(self, companies_name: str):
        delete_button = self.driver.find_element(By.XPATH, '//button[normalize-space()="Delete"]')
        delete_button.click()

        self.wait.until(EC.visibility_of_element_located((By.ID, "delete")))
        checkbox = self.driver.find_element(By.ID, "select-all")
        checkbox.click()

        confirm_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="dialog"]//button[normalize-space()="Confirm"]')))
        confirm_button.click()
        xpath_company_card = f"//div[@class='text-lg font-bold' and normalize-space()='{companies_name}']"
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, xpath_company_card)))

      def get_company_id(self):
        return self.driver.find_element(By.XPATH, '//input[@placeholder="Input Company ID"]').get_attribute("value")
