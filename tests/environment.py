from behave.runner import Context
from selenium.webdriver.safari.webdriver import WebDriver
from selenium.webdriver.edge.webdriver import WebDriver
from poms.users.login import LoginPage

# Setup for webdriver and POM files before selenium tests
def before_all(context: Context):
    context.driver = WebDriver()
    # register POM files below
    context.login_poms = LoginPage(context.driver)
    
    context.driver.implicitly_wait(1)

# Cleanup for webdriver after selenium tests
def after_all(context: Context):
    context.driver.close()
