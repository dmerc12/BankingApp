from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class AccountPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def manage_accounts_navigation(self):
        element: WebElement = self.driver.find_element(By.ID, "manageAccountsNavigation")
