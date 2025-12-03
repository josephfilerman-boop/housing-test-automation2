from selenium.webdriver.common.by import By
from pages.BasePage import BasePage  # <--- Import the Parent

class LoginPage(BasePage):  # <--- Inherit from BasePage
    """
    Page Object for the Login Page.
    """

    # LOCATORS
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON   = (By.NAME, "login-button")

    # INITIALIZER
    def __init__(self, driver):
        # Initialize the Parent (BasePage) so we get the 'self.wait' tools
        super().__init__(driver)

    # ACTIONS (Simpler now!)
    def enter_username(self, username):
        # We use the smart 'do_send_keys' from BasePage
        self.do_send_keys(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.do_send_keys(self.PASSWORD_FIELD, password)

    def click_login(self):
        self.do_click(self.LOGIN_BUTTON)