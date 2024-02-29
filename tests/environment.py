from selenium.webdriver.safari.webdriver import WebDriver
# from selenium.webdriver.edge.webdriver import WebDriver
from poms.users.register import RegisterPage
from poms.side_navbar import SideNavbarPOMs
from poms.users.login import LoginPage
from behave.runner import Context
from poms.navbar import NavbarPOMs

# Setup for webdriver and POM files before selenium tests
def before_all(context: Context):
    context.driver = WebDriver()

    # register POM files below
    context.login_poms = LoginPage(context.driver)
    context.register_poms = RegisterPage(context.driver)
    context.navbar_poms = NavbarPOMs(context.driver)
    context.side_navbar_poms = SideNavbarPOMs(context.driver)
    
    context.driver.implicitly_wait(1)

# Cleanup for webdriver after selenium tests
def after_all(context: Context):
    context.driver.close()
