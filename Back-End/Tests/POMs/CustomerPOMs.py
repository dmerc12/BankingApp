from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.safari.webdriver import WebDriver
# from selenium.webdriver.edge.webdriver import WebDriver


class CustomerPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register_nav_button(self):
        element: WebElement = self.driver.find_element(By.ID, "registerNav")
        return element

    def login_nav_button(self):
        element: WebElement = self.driver.find_element(By.ID, "loginNav")
        return element

    def logout_nav_button(self):
        element: WebElement = self.driver.find_element(By.ID, "logoutNav")
        return element

    def manage_info_nav_button(self):
        element: WebElement = self.driver.find_element(By.ID, "manageInformationNav")
        return element

    def home_nav_button(self):
        element: WebElement = self.driver.find_element(By.ID, "homeNav")
        return element

    def register_first_name_input(self):
        element: WebElement = self.driver.find_element(By.ID, "registerFirstName")
        return element

    def register_last_name_input(self):
        element: WebElement = self.driver.find_element(By.ID, "registerLastName")
        return element

    def register_email_input(self):
        element: WebElement = self.driver.find_element(By.ID, "registerEmail")
        return element

    def register_password_input(self):
        element: WebElement = self.driver.find_element(By.ID, "registerPassword")
        return element

    def register_confirmation_password_input(self):
        element: WebElement = self.driver.find_element(By.ID, "registerConfirmationPassword")
        return element

    def register_phone_number_input(self):
        element: WebElement = self.driver.find_element(By.ID, "registerPhoneNumber")
        return element

    def register_street_address_input(self):
        element: WebElement = self.driver.find_element(By.ID, "registerStreetAddress")
        return element

    def register_city_input(self):
        element: WebElement = self.driver.find_element(By.ID, "registerCity")
        return element

    def register_state_input(self):
        element: WebElement = self.driver.find_element(By.ID, "registerState")
        return element

    def register_zip_code_input(self):
        element: WebElement = self.driver.find_element(By.ID, "registerZipCode")
        return element

    def register_button(self):
        element: WebElement = self.driver.find_element(By.ID, "registerButton")
        return element

    def login_email_input(self):
        element: WebElement = self.driver.find_element(By.ID, "loginEmail")
        return element

    def login_password_input(self):
        element: WebElement = self.driver.find_element(By.ID, "loginPassword")
        return element

    def login_button(self):
        element: WebElement = self.driver.find_element(By.ID, "loginButton")
        return element
