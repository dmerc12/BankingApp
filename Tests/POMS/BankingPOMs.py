from datetime import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait


class BankingPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def manage_accounts_logout_button(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/button[1]")
        return element

    def create_and_manage_accounts_button(self):
        element: WebElement = self.driver.find_element(By.ID, "navigateToManageAccountsButton")
        return element

    def create_new_account_collapse_button(self):
        element: WebElement = self.driver.find_element(By.ID, "createAccountCollapseButton")
        return element

    def account_starting_balance_input(self):
        element: WebElement = self.driver.find_element(By.ID, "startingAmountInput")
        return element

    def create_account_button(self):
        element: WebElement = self.driver.find_element(By.ID, "createAccountButton")
        return element

    def view_all_accounts_collapse_button(self):
        element: WebElement = self.driver.find_element(By.ID, "viewAllAccountsCollapseButton")
        return element

    def deposit_collapse_button(self):
        element: WebElement = self.driver.find_element(By.ID, "depositCollapseButton")
        return element

    def deposit_account_input(self):
        element: WebElement = self.driver.find_element(By.ID, "depositAccountIdInput")
        return element

    def deposit_amount_input(self):
        element: WebElement = self.driver.find_element(By.ID, "depositAmountInput")
        return element

    def deposit_button(self):
        element: WebElement = self.driver.find_element(By.ID, "depositButton")
        return element

    def withdraw_collapse_button(self):
        element: WebElement = self.driver.find_element(By.ID, "withdrawCollapseButton")
        return element

    def withdraw_account_input(self):
        element: WebElement = self.driver.find_element(By.ID, "withdrawAccountIdInput")
        return element

    def withdraw_amount_input(self):
        element: WebElement = self.driver.find_element(By.ID, "withdrawAmountInput")
        return element

    def withdraw_button(self):
        element: WebElement = self.driver.find_element(By.ID, "withdrawButton")
        return element

    def transfer_collapse_button(self):
        element: WebElement = self.driver.find_element(By.ID, "transferCollapseButton")
        return element

    def transfer_withdraw_account_input(self):
        element: WebElement = self.driver.find_element(By.ID, "transferWithdrawIdInput")
        return element

    def transfer_deposit_account_input(self):
        element: WebElement = self.driver.find_element(By.ID, "transferDepositIdInput")
        return element

    def transfer_amount_input(self):
        element: WebElement = self.driver.find_element(By.ID, "transferAmountInput")
        return element

    def transfer_button(self):
        element: WebElement = self.driver.find_element(By.ID, "transferButton")
        return element

    def delete_account_collapse_button(self):
        element: WebElement = self.driver.find_element(By.ID, "deleteAccountCollapseButton")
        return element

    def delete_account_input(self):
        element: WebElement = self.driver.find_element(By.ID, "deleteAccountIdInput")
        return element

    def delete_button(self):
        element: WebElement = self.driver.find_element(By.ID, "deleteAccountButton")
        return element

    def press_ok_on_alert(self):
        alert: Alert = Alert(self.driver)
        return alert
