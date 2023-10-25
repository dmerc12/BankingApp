from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.safari.webdriver import WebDriver
from selenium.webdriver.edge.webdriver import WebDriver


class CustomerPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_register_nav_button(self):
        element: WebElement = self.driver.find_element(By.ID, "registerNav")
        return element.click()

    def click_login_nav_button(self):
        element: WebElement = self.driver.find_element(By.ID, "loginNav")
        return element.click()

    def click_logout_nav_button(self):
        element: WebElement = self.driver.find_element(By.ID, "logoutNav")
        return element.click()

    def click_manage_info_nav_button(self):
        element: WebElement = self.driver.find_element(By.ID, "manageInformationNav")
        return element.click()

    def click_home_nav_button(self):
        element: WebElement = self.driver.find_element(By.ID, "homeNav")
        return element.click()

    def click_manage_info_button(self):
        element: WebElement = self.driver.find_element(By.ID, "manageInformationButton")
        return element.click()

    def click_update_profile_modal(self):
        element: WebElement = self.driver.find_element(By.ID, "updateInformationModal")
        return element.click()

    def click_change_password_modal(self):
        element: WebElement = self.driver.find_element(By.ID, "changePasswordModal")
        return element.click()

    def click_delete_profile_modal(self):
        element: WebElement = self.driver.find_element(By.ID, "deleteProfileModal")
        return element.click()

    def input_register_first_name(self, first_name):
        element: WebElement = self.driver.find_element(By.ID, "registerFirstName")
        return element.send_keys(first_name)

    def input_register_last_name(self, last_name):
        element: WebElement = self.driver.find_element(By.ID, "registerLastName")
        return element.send_keys(last_name)

    def input_register_email(self, email):
        element: WebElement = self.driver.find_element(By.ID, "registerEmail")
        return element.send_keys(email)

    def input_register_password(self, password):
        element: WebElement = self.driver.find_element(By.ID, "registerPassword")
        return element.send_keys(password)

    def input_register_confirmation_password(self, confirmation_password):
        element: WebElement = self.driver.find_element(By.ID, "registerConfirmationPassword")
        return element.send_keys(confirmation_password)

    def input_register_phone_number(self, phone_number):
        element: WebElement = self.driver.find_element(By.ID, "registerPhoneNumber")
        return element.send_keys(phone_number)

    def input_register_street_address(self, street_address):
        element: WebElement = self.driver.find_element(By.ID, "registerStreetAddress")
        return element.send_keys(street_address)

    def input_register_city(self, city):
        element: WebElement = self.driver.find_element(By.ID, "registerCity")
        return element.send_keys(city)

    def input_register_state(self, state):
        element: WebElement = self.driver.find_element(By.ID, "registerState")
        return element.send_keys(state)

    def input_register_zip_code(self, zip_code):
        element: WebElement = self.driver.find_element(By.ID, "registerZipCode")
        return element.send_keys(zip_code)

    def register_button(self):
        element: WebElement = self.driver.find_element(By.ID, "registerButton")
        return element.click()

    def input_login_email(self, email):
        element: WebElement = self.driver.find_element(By.ID, "loginEmail")
        return element.send_keys(email)

    def input_login_password(self, password):
        element: WebElement = self.driver.find_element(By.ID, "loginPassword")
        return element.send_keys(password)

    def click_login_button(self):
        element: WebElement = self.driver.find_element(By.ID, "loginButton")
        return element.click()

    def input_update_first_name(self, first_name):
        element: WebElement = self.driver.find_element(By.ID, "updateFirstName")
        return element.send_keys(first_name)

    def input_update_last_name(self, last_name):
        element: WebElement = self.driver.find_element(By.ID, "updateLastName")
        return element.send_keys(last_name)

    def input_update_email(self, email):
        element: WebElement = self.driver.find_element(By.ID, "updateEmail")
        return element.send_keys(email)

    def input_update_phone_number(self, phone_number):
        element: WebElement = self.driver.find_element(By.ID, "updatePhoneNumber")
        return element.send_keys(phone_number)

    def input_update_street_address(self, street_address):
        element: WebElement = self.driver.find_element(By.ID, "updateStreetAddress")
        return element.send_keys(street_address)

    def input_update_city(self, city):
        element: WebElement = self.driver.find_element(By.ID, "updateCity")
        return element.send_keys(city)

    def input_update_state(self, state):
        element: WebElement = self.driver.find_element(By.ID, "updateState")
        return element.send_keys(state)

    def input_update_zip_code(self, zip_code):
        element: WebElement = self.driver.find_element(By.ID, "updateZipCode")
        return element.send_keys(zip_code)

    def click_update_button(self):
        element: WebElement = self.driver.find_element(By.ID, "updateInformationButton")
        return element.click()

    def input_change_password(self, password):
        element: WebElement = self.driver.find_element(By.ID, "newPassword")
        return element.send_keys(password)

    def input_change_confirmation_password(self, confirmation_password):
        element: WebElement = self.driver.find_element(By.ID, "newConfirmationPassword")
        return element.send_keys(confirmation_password)

    def click_change_password_button(self):
        element: WebElement = self.driver.find_element(By.ID, "changePasswordButton")
        return element.click()

    def click_delete_profile_button(self):
        element: WebElement = self.driver.find_element(By.ID, "deleteProfileButton")
        return element.click()
