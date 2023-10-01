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

    def create_account_modal(self):
        element: WebElement = self.driver.find_element(By.ID, "createAccountModal")
        return element

    def deposit_modal(self, account_id: int):
        element: WebElement = self.driver.find_element(By.ID, f"depositModal{account_id}")
        return element

    def withdraw_modal(self, account_id: int):
        element: WebElement = self.driver.find_element(By.ID, f"withdrawModal{account_id}")
        return element

    def delete_account_modal(self, account_id: int):
        element: WebElement = self.driver.find_element(By.ID, f"deleteAccountModal{account_id}")
        return element

    def transfer_modal(self):
        element: WebElement = self.driver.find_element(By.ID, "transferModal")
        return element

    def create_account_starting_balance_input(self):
        element: WebElement = self.driver.find_element(By.ID, "startingBalance")
        return element

    def create_account_button(self):
        element: WebElement = self.driver.find_element(By.ID, "createAccountButton")
        return element

    def deposit_amount_input(self):
        element: WebElement = self.driver.find_element(By.ID, "depositAmount")
        return element

    def deposit_button(self):
        element: WebElement = self.driver.find_element(By.ID, "depositButton")
        return element

    def withdraw_amount_input(self):
        element: WebElement = self.driver.find_element(By.ID, "withdrawAmount")
        return element

    def withdraw_button(self):
        element: WebElement = self.driver.find_element(By.ID, "withdrawButton")
        return element

    def delete_account_button(self):
        element: WebElement = self.driver.find_element(By.ID, "deleteAccountButton")
        return element

    def transfer_withdraw_account_input(self):
        element: WebElement = self.driver.find_element(By.ID, "transferWithdrawAccountId")
        return element

    def transfer_deposit_account_input(self):
        element: WebElement = self.driver.find_element(By.ID, "transferDepositAccountId")
        return element

    def transfer_amount_input(self):
        element: WebElement = self.driver.find_element(By.ID, "transferAmount")
        return element

    def transfer_button(self):
        element: WebElement = self.driver.find_element(By.ID, "transferButton")
        return element
