from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.safari.webdriver import WebDriver
# from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POM for create account page
class CreateAccountPagePOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # POM for clicking create account navigation button
    def click_create_account_navigation_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'createAccountNavigation')
        return element.click()
        
    # POM for inputting account number
    def enter_account_number_input(self, account_number):
        element: WebElement = self.driver.find_element(By.ID, 'account_number')
        return element.send_keys(account_number)
        
    # POM for inputting bank name
    def enter_bank_name_input(self, bank_name):
        element: WebElement = self.driver.find_element(By.ID, 'bank_name')
        return element.send_keys(bank_name)
        
    # POM for inputting bank location
    def enter_location_input(self, location):
        element: WebElement = self.driver.find_element(By.ID, 'location')
        return element.send_keys(location)
        
    # POM for inputting timestamp
    def enter_timestamp_input(self, timestamp):
        element: WebElement = self.driver.find_element(By.ID, 'timestamp')
        return element.send_keys(timestamp)
        
    # POM for inputting opening balance
    def enter_opening_balance_input(self, opening_balance):
        element: WebElement = self.driver.find_element(By.ID, 'opening_balance')
        return element.send_keys(opening_balance)
        
    # POM for inputting notes
    def enter_opening_notes_input(self, opening_notes):
        element: WebElement = self.driver.find_element(By.ID, 'opening_notes')
        return element.send_keys(opening_notes)
        
    # POM for clicking create account button
    def click_create_account_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'createAccountButton')
        return element.click()
        