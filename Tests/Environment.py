from behave.runner import Context
from selenium.webdriver.chrome.webdriver import WebDriver
from Tests.POMS.BankingPOMs import BankingPOMs
from Tests.POMS.customer_POMs import CustomerPOMs

def before_all(context: Context):
    context.driver = WebDriver()
    context.banking_poms = BankingPOMs(context.driver)
    context.customer_poms = CustomerPOMs(context.driver)
    context.driver.implicitly_wait(1)

def after_all(context: Context):
    context.driver.close()
