from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

def test_browser_launch():
    """
    DHK-7: Verifies that the browser can open and navigate to the Housing Portal.
    """
    print("--- 1. Initializing the Robot (Driver) ---")
    # This initializes the Chrome Browser
    driver = webdriver.Chrome()
    
    # Best Practice: Maximize window so all buttons are visible
    driver.maximize_window()

    print("--- 2. Navigating to the Portal ---")
    # dummy login site to simulate the DoD Portal
    url = "https://www.saucedemo.com/"
    driver.get(url)

    print(f"--- 3. Verifying we are at the right place ---")
    # check the 'Title' or 'URL' to confirm navigation worked
    actual_title = driver.title
    current_url = driver.current_url
    
    print(f"Page Title: {actual_title}")
    print(f"Current URL: {current_url}")

    # A simple assertion (Test)
    if "Swag Labs" in actual_title:
        print("TEST PASSED: Landed on the login page.")
    else:
        print("TEST FAILED: Wrong page loaded.")

    # Sleep for 5 seconds so you can physically see the browser (otherwise it closes too fast)
    time.sleep(5)

    print("--- 4. Cleanup ---")
    # CRITICAL: Always close the browser to prevent memory leaks on the server
    driver.quit()

if __name__ == "__main__":
    test_browser_launch()