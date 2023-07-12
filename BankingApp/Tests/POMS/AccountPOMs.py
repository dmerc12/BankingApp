from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class AccountPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def manage_accounts_navigation(self):
        element: WebElement = self.driver.find_element(By.ID, "manageAccountsNavigation")
        return element

    def create_account_navigation(self):
        element: WebElement = self.driver.find_element(By.ID, "createAccountNavigation")
        return element

    def view_accounts_navigation(self):
        element: WebElement = self.driver.find_element(By.ID, "viewAccountsNavigation")
        return element

    def deposit_navigation(self):
        element: WebElement = self.driver.find_element(By.ID, "depositNavigation")
        return element

    def withdraw_navigation(self):
        element: WebElement = self.driver.find_element(By.ID, "withdrawNavigation")
        return element

    def transfer_navigation(self):
        element: WebElement = self.driver.find_element(By.ID, "transferNavigation")
        return element

    def delete_account_navigation(self):
        element: WebElement = self.driver.find_element(By.ID, "deleteAccountNavigation")
        return element

    def create_account_amount_input(self):
        element: WebElement = self.driver.find_element(By.ID, "starting_balance")
        return element

    def create_account_button(self):
        element: WebElement = self.driver.find_element(By.ID, "createAccountButton")
        return element

    def deposit_account_dropdown(self):
        element: WebElement = self.driver.find_element(By.ID, "depositAccountId")
        return element

    def deposit_amount_input(self):
        element: WebElement = self.driver.find_element(By.ID, "depositAmount")
        return element

    def deposit_button(self):
        element: WebElement = self.driver.find_element(By.ID, "depositButton")
        return element

    def withdraw_account_dropdown(self):
        element: WebElement = self.driver.find_element(By.ID, "withdrawAccountId")
        return element

    def withdraw_amount_input(self):
        element: WebElement = self.driver.find_element(By.ID, "withdrawAmount")
        return element

    def withdraw_button(self):
        element: WebElement = self.driver.find_element(By.ID, "withdrawButton")
        return element

    def transfer_withdraw_account_dropdown(self):
        element: WebElement = self.driver.find_element(By.ID, "transferWithdrawAccountId")
        return element

    def transfer_deposit_account_dropdown(self):
        element: WebElement = self.driver.find_element(By.ID, "transferDepositAccountId")
        return element

    def transfer_amount_input(self):
        element: WebElement = self.driver.find_element(By.ID, "transferAmount")
        return element

    def transfer_button(self):
        element: WebElement = self.driver.find_element(By.ID, "transferButton")
        return element

    def delete_account_dropdown(self):
        element: WebElement = self.driver.find_element(By.ID, "deleteAccountId")
        return element

    def delete_account_button(self):
        element: WebElement = self.driver.find_element(By.ID, "deleteAccountButton")
        return element
