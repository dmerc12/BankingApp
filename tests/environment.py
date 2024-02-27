from behave.runner import Context
from selenium.webdriver.safari.webdriver import WebDriver
from selenium.webdriver.edge.webdriver import WebDriver
from poms import *

def before_all(context: Context):
    context.driver = WebDriver()
    # register POM files below

    context.driver.implicitly_wait(1)

def after_all(context: Context):
    context.driver.close()
    