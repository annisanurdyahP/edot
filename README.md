# Result Take Home Test – QA Automation Engineer

## A simple UI automation framework built with:
- Python: 3.13.5
- pytest: 8.4.1
- Selenium: 4.34.0
- Appium v2
- Appium-Python-Client: 5.1.1
- UiAutomator2
- Faker: 37.4.0
- python-dotenv: 1.1.1  -> for load variabel from file .env


## Project Structure
automation_edot_task
   test_data/     --> this folder for APK & external data
     - ework_1.20.5.apk
     - company_ud.txt
     - file_test.jpg
   mobile/
     - pages
       - login_mobile.py
     - tests
       - test_login_mobile.py
   web/
     - pages
       - create_company.py
       - login_web.py
     - tests
       - test_create_company_web.py
       - test_login_web.py

## Running The Project
**1. Clone repository**
```bash
git clone https://github.com/annisanurdyahP/edot.git
```
**2. Create Virtual Environment**
```bash
python -m venv venv
```
```bash
source venv/bin/activate
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

***4. How to run**
- Mobile Automation (Appium)
  - Start the Appium server:
    ```bash
    appium
    ```
  - Run a specific mobile test:
    ```bash
    pytest <mobile/tests/name_file>
    ```
- Web Automation (Selenium):
  ```bash
  pytest <web/tests/name_file>
  ```

