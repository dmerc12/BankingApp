from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.safari.webdriver import WebDriver
# from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POM for register page
class RegisterPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # POM for entering register username input
    def enter_username_input(self, username):
        element: WebElement = self.driver.find_element(By.ID, 'username')
        return element.send_keys(username)
    
    # POM for entering register first name input
    def enter_first_name_input(self, first_name):
        element: WebElement = self.driver.find_element(By.ID, 'first_name')
        return element.send_keys(first_name)

    # POM for entering register last name input
    def enter_last_name_input(self, last_name):
        element: WebElement = self.driver.find_element(By.ID, 'last_name')
        return element.send_keys(last_name)

    # POM for entering register email input
    def enter_email_input(self, email):
        element: WebElement = self.driver.find_element(By.ID, 'email')
        return element.send_keys(email)
    
    # POM for entering register phone number input
    def enter_phone_number_input(self, phone_number):
        element: WebElement = self.driver.find_element(By.ID, 'phone_number')
        return element.send_keys(phone_number)

    # POM for entering register password1 input
    def enter_password1_input(self, password1):
        element: WebElement = self.driver.find_element(By.ID, 'password1')
        return element.send_keys(password1)
    
    # POM for entering register password2 input
    def enter_password2_input(self, password2):
        element: WebElement = self.driver.find_element(By.ID, 'password2')
        return element.send_keys(password2)

    # POM for clicking register button
    def click_register_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'registerButton')
        return element.click()
    