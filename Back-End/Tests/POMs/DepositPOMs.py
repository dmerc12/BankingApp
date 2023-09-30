from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.safari.webdriver import WebDriver
# from selenium.webdriver.edge.webdriver import WebDriver


class DepositPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver
