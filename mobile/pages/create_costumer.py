import random
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreateCostumer:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click_create_new_costumer(self):
      element_register_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ID, "id.edot.ework.debug:id/tvRegister")))
      assert element_register_btn.text == "Registrasi Pelanggan Baru"
      element_register_btn.click()

    def step_one_register_new_costumer(self, outlet_name, outlet_email, contact_person, generated_phone):
      outlet_name_input = self.driver.find_element(AppiumBy.ID, "id.edot.ework.debug:id/et_outlet_name")
      outlet_name_input.send_keys(outlet_name)
      get_outlet_name = outlet_name_input.get_attribute("text")

      self.driver.find_element(AppiumBy.ID, "id.edot.ework.debug:id/et_outlet_phone").send_keys(generated_phone)
      self.driver.find_element(AppiumBy.ID, "id.edot.ework.debug:id/et_outlet_email").send_keys(outlet_email)
      self.driver.find_element(AppiumBy.ID, "id.edot.ework.debug:id/et_contact_person").send_keys(contact_person)

      self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("id.edot.ework.debug:id/et_channel"))').click()
      time.sleep(2)

      tipe_saluran = random.choice(["Modern Trade (MT)", "General Trade (GT)"])
      self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH,f'//android.widget.TextView[@resource-id="id.edot.ework.debug:id/tvName" and @text="{tipe_saluran}"]'))).click()

      self.driver.find_element(AppiumBy.ID, "id.edot.ework.debug:id/et_outlet_type").click()
      tipe_toko = random.choice(["Grosir", "Semi Grosir"])
      self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH,f'//android.widget.TextView[@resource-id="id.edot.ework.debug:id/tvName" and @text="{tipe_toko}"]'))).click()

      self.driver.find_element(AppiumBy.ID, "id.edot.ework.debug:id/button_text").click()

      return get_outlet_name


    def step_two_register_new_costumer(self, address, province_name = "DKI JAKARTA", city_name = "JAKARTA TIMUR", sub_district_name= "KRAMATJATI", village_name = "CAWANG"):
      self.driver.find_element(AppiumBy.ID, "id.edot.ework.debug:id/et_address_type").click()
      self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.TextView[@resource-id="id.edot.ework.debug:id/tvName" and @text="Delivery Address"]'))).click()
      self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("id.edot.ework.debug:id/etAddress"))')
      self.wait.until(EC.presence_of_element_located((AppiumBy.ID, "id.edot.ework.debug:id/etAddress"))).send_keys(address)

      self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Pilih Provinsi"]').click()
      self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[@text="{province_name}"]'))).click()

      self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Pilih Kota"]').click()
      self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[@text="{city_name}"]'))).click()

      self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Pilih Kecamatan"]').click()
      self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[@text="{sub_district_name}"]'))).click()

      self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Pilih Kelurahan"]').click()
      self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[@text="{village_name}"]'))).click()

      self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Pilih Kode pos"]').click()
      self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.TextView[@resource-id="id.edot.ework.debug:id/txt_name"]'))).click()

      self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.Button[@text="Lanjutkan"]'))).click()


    def step_three_upload_docs(self):
      dokumen_title = self.wait.until(EC.presence_of_element_located((AppiumBy.ID, "id.edot.ework.debug:id/tv_title_payment")))
      assert dokumen_title.text.strip() == "Dokumen"

      # input KTP
      id_card_number = ''.join([str(random.randint(0, 9)) for _ in range(16)])
      self.driver.find_element(AppiumBy.ID, "id.edot.ework.debug:id/etInput").send_keys(id_card_number)

      # upload file and take a photo
      self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="id.edot.ework.debug:id/button_text" and @text="Unggah Berkas"]').click()
      self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "id.edot.ework.debug:id/btn_capture"))).click()

      preview_image = self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, "id.edot.ework.debug:id/img_preview")))
      assert preview_image.is_displayed()

      self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Daftar"]').click()
      time.sleep(3)

    def submit_signature(self, get_outlet_name):
      self.wait.until(EC.text_to_be_present_in_element((AppiumBy.ID, "id.edot.ework.debug:id/tv_title"), "Tanda Tangan Persetujuan"))
      signature_view = self.driver.find_element(AppiumBy.ID, "id.edot.ework.debug:id/signature_view")
      rect = signature_view.rect
      start_x = rect['x'] + 10
      start_y = rect['y'] + rect['height'] // 2
      end_x = start_x + 100
      end_y = start_y

        # Simulasi tanda tangan
      self.driver.execute_script("mobile: dragGesture", {
            "startX": start_x,
            "startY": start_y,
            "endX": end_x,
            "endY": end_y,
            "speed": 100
        })
      self.driver.execute_script("mobile: dragGesture", {
            "startX": end_x,
            "startY": end_y,
            "endX": start_x,
            "endY": start_y + 50,
            "speed": 100
        })
      time.sleep(2)
      self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Daftar"]').click()

# Popup konfirmasi
      self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Anda yakin untuk menyimpan data ini?"]')))
      save_data_popup = self.driver.find_element(AppiumBy.ID, "id.edot.ework.debug:id/dialog_body")
      yes_btn = save_data_popup.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ya")')
      yes_btn.click()