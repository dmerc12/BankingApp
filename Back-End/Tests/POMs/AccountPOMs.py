from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.safari.webdriver import WebDriver
# from selenium.webdriver.edge.webdriver import WebDriver


class AccountPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def manage_accounts_nav_button(self):
        element: WebElement = self.driver.find_element(By.ID, "manageAccountsNav")
        return element

    def manage_accounts_button(self):
        element: WebElement = self.driver.find_element(By.ID, "manageAccountsButton")
        return element
