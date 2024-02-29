from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.safari.webdriver import WebDriver
# from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POM for navbar
class NavbarPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # POM for toggling navbar dropdown
    def toggle_navbar_dropdown(self):
        element = self.driver.find_element(By.ID, 'navbarDropdown')
        return element.click()
    
    # POM for clicking update user button in the navbar
    def click_update_user_button(self):
        element = self.driver.find_element(By.ID, 'navUpdateUserButton')
        return element.click()
    
    # POM for clicking change password button in the navbar
    def click_change_password_button(self):
        element = self.driver.find_element(By.ID, 'navChangePasswordButton')
        return element.click()
    
    # POM for clicking logout button in the navbar
    def click_logout_button(self):
        element = self.driver.find_element(By.ID, 'navLogoutButton')
        return element.click()
    

    # POM for clicking register button in the navbar
    def click_register_button(self):
        element = self.driver.find_element(By.ID, 'navRegisterButton')
        return element.click()
    
    # POM for clicking login button in the navbar
    def click_login_button(self):
        element = self.driver.find_element(By.ID, 'navLoginButton')
        return element.click()
