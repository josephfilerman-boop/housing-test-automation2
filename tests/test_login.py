from selenium import webdriver
from selenium.webdriver.common.by import By  # <--- NEW: Needed to find elements
import time

def test_login_flow():
    """
    DHK-7: Verifies valid login using Standard User credentials.
    """
    print("--- 1. Initialize Driver ---")
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    print("--- 2. Navigate to Login Page ---")
    driver.get("https://www.saucedemo.com/")

    print("--- 3. LOCATING ELEMENTS & INTERACTING ---")
    
    # Strategy 1: Find by ID (Best Practice)
    # We ask the driver: "Find the element where ID equals 'user-name'"
    username_box = driver.find_element(By.ID, "user-name")
    
    # Strategy 2: Find by ID (for Password)
    password_box = driver.find_element(By.ID, "password")
    
    # Strategy 3: Find by Name or XPath (just to show you how)
    # This says: Find the <input> tag where the 'name' attribute is 'login-button'
    login_btn = driver.find_element(By.NAME, "login-button")

    # ACTION: Type into the boxes
    print("Typing credentials...")
    username_box.send_keys("standard_user")  # Valid user from the site
    password_box.send_keys("secret_sauce")   # Valid password
    
    time.sleep(1) # Just so you can see it happen (remove in real production code)
    
    # ACTION: Click the button
    print("Clicking login...")
    login_btn.click()
    
    time.sleep(2) # Wait for page load

    print("--- 4. ASSERTION (Did it work?) ---")
    # If login works, URL changes to 'inventory.html'
    current_url = driver.current_url
    
    if "inventory.html" in current_url:
        print("✅ PASS: Successfully logged in!")
    else:
        print(f"❌ FAIL: Still on {current_url}")

    driver.quit()

if __name__ == "__main__":
    test_login_flow()