from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.safari.webdriver import WebDriver
from selenium.webdriver.edge.webdriver import WebDriver


class UniversalPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def toast_notification(self):
        element: WebElement = self.driver.find_element(By.ID, "toast")
        return element
