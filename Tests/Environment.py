from behave.runner import Context
from selenium.webdriver.chrome.webdriver import WebDriver
from Tests.POMS.BankingPOMs import BankingPOMs

def before_all(context: Context):
    context.driver = WebDriver()
    context.secret_page_poms = BankingPOMs(context.driver)
    context.driver.implicitly_wait(1)

def after_all(context: Context):
    context.driver.close()
