from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from web.pages.login_page import LoginPage  # ini harus benar path-nya

# Setup driver
options = Options()
# options.add_argument("--headless=new")  # kalau mau headless, bisa tambahin ini
driver = webdriver.Chrome(options=options)
driver.get("https://esuite.edot.id")

# Gunakan LoginPage
login_page = LoginPage(driver)
login_page.login("your@email.com", "your_password")

# Misalnya cek setelah login
print(driver.current_url)

# Jangan lupa close
driver.quit()
