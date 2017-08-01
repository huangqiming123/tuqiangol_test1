from time import sleep

from pages.base.base_page import BasePage


class LogInBase(BasePage):
    def log_in(self):
        self.driver.operate_input_element("account", 'web_autotest')
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
        self.driver.switch_to_frame('x,//*[@id="usercenterFrame"]')
        a = self.driver.get_text('x,//*[@id="userAccount"]')
        self.driver.default_frame()
        return a

    def log_in_jimitest(self):
        self.driver.operate_input_element("account", 'jimitest')
        self.driver.operate_input_element("password", 'jimi123')
        self.driver.click_element('x,//*[@id="checkbox"]')
        self.driver.click_element("logins")
        sleep(2)

    def log_in_hemi(self):
        self.driver.operate_input_element("account", 'hemi')
        self.driver.operate_input_element("password", 'jimi123')
        self.driver.click_element('x,//*[@id="checkbox"]')
        self.driver.click_element("logins")
        sleep(2)

    def click_account_center_button(self):
        self.driver.click_element('x,//*[@id="accountCenter"]/a')
        sleep(4)
