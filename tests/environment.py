from selenium.webdriver.safari.webdriver import WebDriver
# from selenium.webdriver.edge.webdriver import WebDriver
from poms.users.change_password import ChangePasswordPage
from poms.users.register import RegisterPage
from poms.side_navbar import SideNavbarPOMs
from poms.users.login import LoginPage
from poms.navbar import NavbarPOMs
from behave.runner import Context

# Setup for webdriver and POM files before selenium tests
def before_all(context: Context):
    context.driver = WebDriver()

    ## register POM files below
    # users poms
    context.login_poms = LoginPage(context.driver)
    context.register_poms = RegisterPage(context.driver)
    context.change_password_poms = ChangePasswordPage(context.driver)

    # banking poms

    # navigation poms
    context.navbar_poms = NavbarPOMs(context.driver)
    context.side_navbar_poms = SideNavbarPOMs(context.driver)

    context.driver.implicitly_wait(1)

# Cleanup for webdriver after selenium tests
def after_all(context: Context):
    context.driver.close()
