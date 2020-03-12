from pages.alerts import Alerts
from pages.base_page import Page


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.base_page = Page(self.driver)
        self.alerts = Alerts(self.driver)
