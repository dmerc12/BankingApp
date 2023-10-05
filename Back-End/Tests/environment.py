from behave.runner import Context
from selenium.webdriver.safari.webdriver import WebDriver
# from selenium.webdriver.edge.webdriver import WebDriver
from Tests.POMs.CustomerPOMs import CustomerPOMs
from Tests.POMs.AccountPOMs import AccountPOMs


def before_all(context: Context):
    context.driver = WebDriver()
    context.customer_poms = CustomerPOMs(context.driver)
    context.account_poms = AccountPOMs(context.driver)
    context.driver.implicitly_wait(1)

def after_all(context: Context):
    context.driver.close()
