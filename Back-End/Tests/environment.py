from behave.runner import Context
from selenium.webdriver.safari.webdriver import WebDriver
from selenium.webdriver.edge.webdriver import WebDriver
from Tests.POMs.CategoryPOMs import CategoryPOMs
from Tests.POMs.DepositPOMs import DepositPOMs
from Tests.POMs.ExpensePOMs import ExpensePOMs


def before_all(context: Context):
    context.driver = WebDriver()
    context.category_poms = CategoryPOMs(context.driver)
    context.deposit_poms = DepositPOMs(context.driver)
    context.expense_poms = ExpensePOMs(context.driver)
    context.driver.implicitly_wait(1)

def after_all(context: Context):
    context.driver.close()