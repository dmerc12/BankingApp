from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.safari.webdriver import WebDriver
# from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POM for navbar
class SideNavbarPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # POM for toggling side navbar
    def toggle_side_navbar(self):
        element = self.driver.find_element(By.ID, 'sidebarToggle')
        return element.click()
    
    # POM for clicking home button in the side navbar
    def click_home_button(self):
        element = self.driver.find_element(By.ID, 'sideNavHomeButton')
        return element.click()
    
    # POM for clicking the create account button in the side navbar
    def click_create_account_button(self):
        element = self.driver.find_element(By.ID, 'sideNavCreateAccountButton')
        return element.click()
    
    # POM for toggling the manage profile dropdown in the side navbar
    def toggle_manage_profile_dropdown(self):
        element = self.driver.find_element(By.ID, 'sideNavManageProfileToggle')
        return element.click()
    
    # POM for clicking the update user button in the side navbar
    def click_update_user_button(self):
        element = self.driver.find_element(By.ID, 'sideNavUpdateUserButton')
        return element.click()
    
    # POM for clicking the change password button in the side navbar
    def click_change_password_button(self):
        element = self.driver.find_element(By.ID, 'sideNavChangePasswordButton')
        return element.click()
    