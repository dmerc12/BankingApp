from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.safari.webdriver import WebDriver
# from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POM for delete user page
class DeleteUserPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # POM for clicking delete user button
    def click_delete_user_button(self, first_name):
        element: WebElement = self.driver.find_element(By.ID, 'deleteUserButton')
        return element.send_keys(first_name)

    # POM for clicking delete user confirmation button
    def click_delete_user_confirm_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'deleteUserConfirmButton')
        return element.click()
