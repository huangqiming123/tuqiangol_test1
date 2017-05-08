from time import sleep

from pages.base.base_page import BasePage
from pages.base.base_page_server import BasePageServer


class LogInBaseServer(BasePageServer):
    def log_in(self):
        self.driver.operate_input_element("account", 'test_007')
        self.driver.operate_input_element("password", 'jimi123')
        self.driver.click_element('x,//*[@id="checkbox"]')
        self.driver.click_element("logins")
        sleep(2)

    def log_in_with_csv(self, account, password):
        self.driver.operate_input_element("account", account)
        self.driver.operate_input_element("password", password)
        self.driver.click_element('x,//*[@id="checkbox"]')
        self.driver.click_element("logins")
        sleep(2)

    def get_log_in_account(self):
        return self.driver.get_text('x,//*[@id="userAccount"]')

    def log_in_jimitest(self):
        self.driver.operate_input_element("account", 'jimitest')
        self.driver.operate_input_element("password", 'jimi123')
        self.driver.click_element('x,//*[@id="checkbox"]')
        self.driver.click_element("logins")
        sleep(2)
