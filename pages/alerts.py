from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Alerts(Page):

    COUNTRY_LABEL = (By.CSS_SELECTOR, "div[lang='en'] .country-selection .us-link")
    POP_WINDOW_CLOSE = (By.CSS_SELECTOR, "button[type='button'].close:not(.modal-close)")

    def choose_country(self):
        self.wait_for_element_appear(*self.COUNTRY_LABEL)
        self.click(*self.COUNTRY_LABEL)

    def close_pop_up(self):
        self.wait_for_element_appear(*self.POP_WINDOW_CLOSE)
        self.click(*self.POP_WINDOW_CLOSE)

    def create_alert(self):
        self.driver.execute_script('window.alert(\'Hello world\')')
        sleep(1)

    def create_prompt(self):
        self.driver.execute_script('window.prompt(\'Hello world!!!\')')
        sleep(1)

    def create_confirm(self):
        self.driver.execute_script('window.confirm(\'Hello world!!\')')
        sleep(1)

    def close_alert(self):
        alert = self.wait_until_alert_is_present()
        # self.driver.switch_to.alert
        alert.accept()

    def close_prompt(self):
        alert = self.wait_until_alert_is_present()
        alert.send_keys("Selenium")
        alert.accept()

    def close_confirm(self):
        alert = self.wait_until_alert_is_present()
        print(alert.text)
        alert.dismiss()
