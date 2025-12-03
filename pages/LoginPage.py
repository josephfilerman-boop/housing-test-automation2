from selenium.webdriver.common.by import By

class LoginPage:
    """
    Page Object for the Login Page.
    Contains all Locators and Actions for this specific page.
    """

    # 1. LOCATORS (The "Map")
    # We store them here as class variables so they are easy to change.
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON   = (By.NAME, "login-button")

    # 2. INITIALIZER
    def __init__(self, driver):
        self.driver = driver

    # 3. ACTIONS (The "Logic")
    def enter_username(self, username):
        """Finds the username box and types the name."""
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        """Finds the password box and types the password."""
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login(self):
        """Clicks the login button."""
        self.driver.find_element(*self.LOGIN_BUTTON).click()