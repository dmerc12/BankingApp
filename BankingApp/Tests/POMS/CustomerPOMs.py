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

    def login_tab(self):
        element: WebElement = self.driver.find_element(By.ID, "loginTab")
        return element

    def register_tab(self):
        element: WebElement = self.driver.find_element(By.ID, "registerTab")
        return element

    def home_tab(self):
        element: WebElement = self.driver.find_element(By.ID, "homeTab")
        return element

    def manage_accounts_tab(self):
        element: WebElement = self.driver.find_element(By.ID, "manageAccountsTab")
        return element

    def manage_customer_tab(self):
        element: WebElement = self.driver.find_element(By.ID, "manageCustomerTab")
        return element

    def logout_button(self):
        element: WebElement = self.driver.find_element(By.ID, "logoutButton")
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
        element: WebElement = self.driver.find_element(By.ID, "registerPasswordConfirmation")
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

    def update_first_name_input(self):
        element: WebElement = self.driver.find_element(By.ID, "updatedFirstName")
        return element

    def update_last_name_input(self):
        element: WebElement = self.driver.find_element(By.ID, "updatedLastName")
        return element

    def update_email_input(self):
        element: WebElement = self.driver.find_element(By.ID, "updatedEmail")
        return element

    def update_phone_number_input(self):
        element: WebElement = self.driver.find_element(By.ID, "updatedPhoneNumber")
        return element

    def update_street_address_input(self):
        element: WebElement = self.driver.find_element(By.ID, "updatedStreetAddress")
        return element

    def update_city_input(self):
        element: WebElement = self.driver.find_element(By.ID, "updatedCity")
        return element

    def update_state_input(self):
        element: WebElement = self.driver.find_element(By.ID, "updatedState")
        return element

    def update_zip_code_input(self):
        element: WebElement = self.driver.find_element(By.ID, "updatedZipCode")
        return element

    def update_button(self):
        element: WebElement = self.driver.find_element(By.ID, "updateButton")
        return element

    def delete_button(self):
        element: WebElement = self.driver.find_element(By.ID, "deleteButton")
        return element

    def change_password_input(self):
        element: WebElement = self.driver.find_element(By.ID, "newPassword")
        return element

    def change_password_confirmation_input(self):
        element: WebElement = self.driver.find_element(By.ID, "confirmationPassword")
        return element

    def change_password_button(self):
        element: WebElement = self.driver.find_element(By.ID, "changePasswordButton")
        return element

    def update_customer_navigation(self):
        element: WebElement = self.driver.find_element(By.ID, "updateCustomerNavigation")
        return element

    def delete_customer_navigation(self):
        element: WebElement = self.driver.find_element(By.ID, "deleteCustomerNavigation")
        return element

    def change_password_navigation(self):
        element: WebElement = self.driver.find_element(By.ID, "changePasswordNavigation")
        return element

    def manage_customer_navigation(self):
        element: WebElement = self.driver.find_element(By.ID, "manageCustomerNavigation")
        return element
