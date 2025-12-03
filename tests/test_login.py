from selenium import webdriver
import sys
import os
import time

# 1. Path Setup: Tells Python where to look for 'config' and 'pages'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.config import TestData
from pages.LoginPage import LoginPage

def test_login_pom():
    """
    DHK-9: Login test using Page Object Model.
    """
    print("--- 1. Initialize Driver ---")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(TestData.BASE_URL)

    print("--- 2. Initialize Page Object ---")
    # Give the driver to the LoginPage
    login_page = LoginPage(driver)

    print("--- 3. Perform Actions using Smart Waits ---")
    print(f"Typing User: {TestData.USERNAME}")
    login_page.enter_username(TestData.USERNAME)
    login_page.enter_password(TestData.PASSWORD)
    
    print("Clicking Login...")
    # The Page Object handles the wait automatically
    login_page.click_login()
    
    # Optional: Short sleep just so you can visually confirm the login worked
    # (In a real CI/CD pipeline, we would remove this)
    time.sleep(3)

    print("--- 4. Assertion ---")
    if "inventory.html" in driver.current_url:
        print("✅ PASS: POM Login successful!")
    else:
        print(f"❌ FAIL: Still on {driver.current_url}")

    driver.quit()

# --- THE TRIGGER (This was missing!) ---
if __name__ == "__main__":
    test_login_pom()