from selenium import webdriver
import time
import sys
import os

# Add root folder to path so we can import 'config' and 'pages'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.config import TestData
from pages.LoginPage import LoginPage  # <--- IMPORT THE NEW CLASS

def test_login_pom():
    """
    DHK-9: Login test using Page Object Model.
    """
    print("--- 1. Initialize Driver ---")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(TestData.BASE_URL)

    print("--- 2. Initialize Page Object ---")
    # We hand the driver to the LoginPage class
    login_page = LoginPage(driver)

    print("--- 3. Perform Actions using POM ---")
    # Notice how readable this is? No messy "driver.find_element..." here!
    print(f"Typing User: {TestData.USERNAME}")
    login_page.enter_username(TestData.USERNAME)
    login_page.enter_password(TestData.PASSWORD)
    
    time.sleep(1)
    login_page.click_login()
    
    time.sleep(2)

    # Assertion
    if "inventory.html" in driver.current_url:
        print("✅ PASS: POM Login successful!")
    else:
        print("❌ FAIL: Login failed.")

    driver.quit()

if __name__ == "__main__":
    test_login_pom()