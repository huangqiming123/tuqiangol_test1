from time import sleep

from pages.base.base_page_server import BasePageServer


class VirtualUserLimitsPage(BasePageServer):
    def click_workbench_button(self):
        # 点击工作台
        self.driver.click_element('x,//*[@id="accountCenter"]/a')
        sleep(3)

    def click_set_up_and_virtual_user_management(self):
        # 点击设置-虚拟账号管理
        self.driver.click_element('x,/html/body/header/div/div[2]/div[2]/div[2]/span[1]/a')
        sleep(2)
        self.driver.click_element('p,虚拟账号设置')
        sleep(3)

    def click_add_virtual_user_button(self):
        self.driver.click_element('x,//*[@id="ficAccAddBtn"]')
        sleep(3)

    def input_virtual_account_password(self, data):
        self.driver.operate_input_element('x,//*[@id="fictitiousAccountForm"]/div[1]/div/input', data['v_account'])
        self.driver.operate_input_element('x,//*[@id="fictitious_password"]', data['v_password'])
        self.driver.operate_input_element('x,//*[@id="password"]', data['v_password'])

    def select_virtual_user_limit(self, param):
        if param == '设备管理':
            self.driver.click_element('x,/html/body/div[7]/div[2]/div/form/div[4]/div/div/div/ul/li[2]/span[2]')
        elif param == '客户管理':
            self.driver.click_element('x,/html/body/div[7]/div[2]/div/form/div[4]/div/div/div/ul/li[3]/span[2]')
        elif param == '控制台':
            self.driver.click_element('x,/html/body/div[7]/div[2]/div/form/div[4]/div/div/div/ul/li[4]/span[2]')
        elif param == '统计报表':
            self.driver.click_element('x,/html/body/div[7]/div[2]/div/form/div[4]/div/div/div/ul/li[5]/span[2]')
        elif param == '安全区域':
            self.driver.click_element('x,/html/body/div[7]/div[2]/div/form/div[4]/div/div/div/ul/li[6]/span[2]')
        elif param == '设备分布':
            self.driver.click_element('x,/html/body/div[7]/div[2]/div/form/div[4]/div/div/div/ul/li[7]/span[2]')
        sleep(2)

    def click_ensure_add_virtual_user_button(self):
        self.driver.click_element('c,layui-layer-btn0')
        sleep(4)

    def logout(self):
        # 点击退出系统
        self.driver.float_element(self.driver.get_element('x,/html/body/header/div/div[2]/div[2]/div[2]/span[2]/a'))
        sleep(2)
        self.driver.click_element('p,退出系统')
        sleep(2)
        self.driver.click_element("c,layui-layer-btn0")
        self.driver.wait()

    def get_list_number_in_look_up(self):
        return len(list(self.driver.get_elements('x,//*[@id="navMenu"]/li')))

    def get_per_name_in_list(self, n):
        return self.driver.get_text('x,/html/body/header/div/div[2]/ul/li[%s]/a' % str(n + 1))

    def click_delete_button_and_ensure(self):
        self.driver.click_element('x,//*[@id="fictitiousAccount_tbody"]/tr[1]/td[4]/a[2]')
        sleep(2)
        self.driver.click_element('c,layui-layer-btn0')
        sleep(2)
