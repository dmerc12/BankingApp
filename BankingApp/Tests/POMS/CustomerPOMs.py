from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
class CustomerPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login_username_input(self):
        element: WebElement = self.driver.find_element(By.ID, "usernameInput")
        return element

    def login_password_input(self):
        element: WebElement = self.driver.find_element(By.ID, "passwordInput")
        return element

    def login_button(self):
        element: WebElement = self.driver.find_element(By.ID, "submitInfo")
        return element

    def indicate_new_customer(self):
        element: WebElement = self.driver.find_element(By.ID, "indicateNewUser")
        return element

    def create_first_name_input(self):
        element: WebElement = self.driver.find_element(By.ID, "firstNameInput")
        return element

    def create_last_name_input(self):
        element: WebElement = self.driver.find_element(By.ID, "lastNameInput")
        return element

    def create_username_input(self):
        element: WebElement = self.driver.find_element(By.ID, "usernameInput")
        return element

    def create_password_input(self):
        element: WebElement = self.driver.find_element(By.ID, "passwordInput")
        return element

    def create_email_input(self):
        element: WebElement = self.driver.find_element(By.ID, "emailInput")
        return element

    def create_phone_number_input(self):
        element: WebElement = self.driver.find_element(By.ID, "phoneNumberInput")
        return element

    def create_address_input(self):
        element: WebElement = self.driver.find_element(By.ID, "addressInput")
        return element

    def create_new_customer_button(self):
        element: WebElement = self.driver.find_element(By.ID, "createCustomerButton")
        return element

    def update_customer_collapsable(self):
        element: WebElement = self.driver.find_element(By.ID, "updateCustomerCollapseButton")
        return element

    def update_first_name_input(self):
        element: WebElement = self.driver.find_element(By.ID, "updatedFirstNameInput")
        return element

    def update_last_name_input(self):
        element: WebElement = self.driver.find_element(By.ID, "updatedLastNameInput")
        return element

    def update_username_input(self):
        element: WebElement = self.driver.find_element(By.ID, "updatedUsernameInput")
        return element

    def update_password_input(self):
        element: WebElement = self.driver.find_element(By.ID, "updatedPasswordInput")
        return element

    def update_email_input(self):
        element: WebElement = self.driver.find_element(By.ID, "updatedEmailAddressInput")
        return element

    def update_phone_number_input(self):
        element: WebElement = self.driver.find_element(By.ID, "updatedPhoneNumberInput")
        return element

    def update_address_input(self):
        element: WebElement = self.driver.find_element(By.ID, "updatedAddressInput")
        return element

    def update_customer_button(self):
        element: WebElement = self.driver.find_element(By.ID, "updateCustomerButton")
        return element

    def manage_customer_information_button(self):
        element: WebElement = self.driver.find_element(By.ID, "navigateToManageCustomerButton")
        return element

    def delete_customer_collapse_button(self):
        element: WebElement = self.driver.find_element(By.ID, "deleteCustomerCollapseButton")
        return element

    def delete_customer_button(self):
        element: WebElement = self.driver.find_element(By.ID, "deleteCustomerButton")
        return element

    def home_log_out_button(self):
        element: WebElement = self.driver.find_element(By.ID, "logOutButton")
        return element

    def manage_customer_information_logout_button(self):
        element: WebElement = self.driver.find_element(By.ID, "logOutButton")
        return element