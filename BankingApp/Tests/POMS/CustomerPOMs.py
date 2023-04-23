from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
class CustomerPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login_email_input(self):
        element: WebElement = self.driver.find_element(By.ID, "loginEmail")
        return element

    def login_password_input(self):
        element: WebElement = self.driver.find_element(By.ID, "loginPassword")
        return element

    def login_button(self):
        element: WebElement = self.driver.find_element(By.ID, "loginButton")
        return element

    def login_page(self):
        element: WebElement = self.driver.find_element(By.ID, "login")
        return element

    def register_page(self):
        element: WebElement = self.driver.find_element(By.ID, "register")
        return element

    def create_first_name_input(self):
        element: WebElement = self.driver.find_element(By.ID, "firstName")
        return element

    def create_last_name_input(self):
        element: WebElement = self.driver.find_element(By.ID, "lastName")
        return element

    def create_email_input(self):
        element: WebElement = self.driver.find_element(By.ID, "email")
        return element

    def create_password_input(self):
        element: WebElement = self.driver.find_element(By.ID, "password")
        return element

    def create_confirmation_password_input(self):
        element: WebElement = self.driver.find_element(By.ID, "passwordConfirmation")
        return element

    def create_phone_number_input(self):
        element: WebElement = self.driver.find_element(By.ID, "phoneNumber")
        return element

    def create_address_input(self):
        element: WebElement = self.driver.find_element(By.ID, "address")
        return element

    def register_button(self):
        element: WebElement = self.driver.find_element(By.ID, "registerButton")
        return element

    def home_nav_button(self):
        element: WebElement = self.driver.find_element(By.ID, "homeNavButton")
        return element

    def manage_accounts_nav_button(self):
        element: WebElement = self.driver.find_element(By.ID, "manageAccountsNavButton")
        return element

    def manage_customer_nav_button(self):
        element: WebElement = self.driver.find_element(By.ID, "manageCustomerNavButton")
        return element

    def logout_button(self):
        element: WebElement = self.driver.find_element(By.ID, "NavLogoutButton")
        return element
