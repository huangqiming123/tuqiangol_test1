from time import sleep

from pages.base.base_page_server import BasePageServer


class AccountCenterChangePage(BasePageServer):
    def switch_fast_sale_enable(self):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="fastSellDiv"]/div/div/div[1]/b'))
        sleep(2)

    def switch_to_fast_sale_frame(self):
        self.driver.switch_to_frame('x,//*[@id="fastSellFrame"]')

    def switch_kucun_dev_enable(self):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="stockStatDiv"]/div/div/div[1]/b'))
        sleep(2)

    def switch_to_kucun_dev_frame(self):
        self.driver.switch_to_frame('x,//*[@id="stockStatFrame"]')

    def get_account_in_kuncun_frame(self):
        return self.driver.get_element('x,')

    def switch_to_add_account_frame(self):
        self.driver.switch_to_frame('x,/html/body/div[9]/div[2]/iframe')
