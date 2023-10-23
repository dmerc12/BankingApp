from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.safari.webdriver import WebDriver
# from selenium.webdriver.edge.webdriver import WebDriver


class AccountPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_manage_accounts_nav_button(self):
        element: WebElement = self.driver.find_element(By.ID, "manageAccountsNav")
        return element.click()

    def click_manage_accounts_button(self):
        element: WebElement = self.driver.find_element(By.ID, "manageAccountsButton")
        return element.click()

    def click_create_account_modal(self):
        element: WebElement = self.driver.find_element(By.ID, "createAccountModal")
        return element.click()

    def click_deposit_modal(self, account_id: int):
        element: WebElement = self.driver.find_element(By.ID, f"depositModal{account_id}")
        return element.click()

    def click_withdraw_modal(self, account_id: int):
        element: WebElement = self.driver.find_element(By.ID, f"withdrawModal{account_id}")
        return element.click()

    def click_delete_account_modal(self, account_id: int):
        element: WebElement = self.driver.find_element(By.ID, f"deleteAccountModal{account_id}")
        return element.click()

    def click_transfer_modal(self):
        element: WebElement = self.driver.find_element(By.ID, "transferModal")
        return element.click()

    def input_create_account_starting_balance(self, starting_balance):
        element: WebElement = self.driver.find_element(By.ID, "startingBalance")
        return element.send_keys(starting_balance)

    def click_create_account_button(self):
        element: WebElement = self.driver.find_element(By.ID, "createAccountButton")
        return element.click()

    def input_deposit_amount(self, deposit_amount):
        element: WebElement = self.driver.find_element(By.ID, "depositAmount")
        return element.send_keys(deposit_amount)

    def click_deposit_button(self):
        element: WebElement = self.driver.find_element(By.ID, "depositButton")
        return element.click()

    def input_withdraw_amount(self, withdraw_amount):
        element: WebElement = self.driver.find_element(By.ID, "withdrawAmount")
        return element.send_keys(withdraw_amount)

    def click_withdraw_button(self):
        element: WebElement = self.driver.find_element(By.ID, "withdrawButton")
        return element.click()

    def click_delete_account_button(self):
        element: WebElement = self.driver.find_element(By.ID, "deleteAccountButton")
        return element.click()

    def click_transfer_withdraw_account_input(self):
        element: WebElement = self.driver.find_element(By.ID, "transferWithdrawAccountId")
        return element.click()

    def click_transfer_account(self, account_id):
        element: WebElement = self.driver.find_element(By.ID, f"{account_id}")
        return element.click()

    def click_transfer_deposit_account_input(self):
        element: WebElement = self.driver.find_element(By.ID, "transferDepositAccountId")
        return element.click()

    def input_transfer_amount(self, transfer_amount):
        element: WebElement = self.driver.find_element(By.ID, "transferAmount")
        return element.send_keys(transfer_amount)

    def click_transfer_button(self):
        element: WebElement = self.driver.find_element(By.ID, "transferButton")
        return element.click()
