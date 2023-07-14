from behave.runner import Context
from selenium.webdriver.chrome.webdriver import WebDriver

from BankingApp.Tests.POMS.AccountPOMs import AccountPOMs
from BankingApp.Tests.POMS.CustomerPOMs import CustomerPOMs


def before_all(context: Context):
    context.driver = WebDriver()
    context.account_poms = AccountPOMs(context.driver)
    context.customer_poms = CustomerPOMs(context.driver)
    context.driver.implicitly_wait(1)

def after_all(context: Context):
    context.driver.close()
