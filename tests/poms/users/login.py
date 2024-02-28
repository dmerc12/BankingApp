from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.safari.webdriver import WebDriver
# from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POM for login page
class LoginPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # POM for entering login username input
    def enter_username_input(self, username):
        element: WebElement = self.driver.find_element(By.ID, 'username')
        return element.send_keys(username)
    
    # POM for entering login password input
    def enter_password_input(self, password):
        element: WebElement = self.driver.find_element(By.ID, 'password')
        return element.send_keys(password)
    
    # POM for clicking login button
    def click_login_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'loginButton')
        return element.click()
