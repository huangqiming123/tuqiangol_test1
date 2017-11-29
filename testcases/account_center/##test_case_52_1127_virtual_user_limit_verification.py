import csv
import unittest

from automate_driver.automate_driver_server import AutomateDriverServer
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.virtual_user_limits_page import VirtualUserLimitsPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer


class TestCase52VirtualUserLimitVerification(unittest.TestCase):
    # 虚拟账号权限
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.virtual_user_limit_page = VirtualUserLimitsPage(self.driver, self.base_url)
        self.read_csv = AccountCenterPageReadCsv()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.base_page.open_page()

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_52_virtual_user_limit_verification(self):
        csv_file = self.read_csv.read_csv('virtual_user_limits.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            data = {
                'v_account': row[0],
                'v_password': row[1],
                'v_limit': row[2]
            }
            self.log_in_base.log_in()
            # 点击工作台，进入首页
            self.virtual_user_limit_page.click_workbench_button()
            # 点击进入设置-虚拟账号管理
            self.virtual_user_limit_page.click_set_up_and_virtual_user_management()
            # 点击添加按钮
            self.virtual_user_limit_page.click_add_virtual_user_button()
            # 填写账号、密码、确认密码
            self.virtual_user_limit_page.input_virtual_account_password(data)
            # 选择虚拟账号的权限
            self.virtual_user_limit_page.select_virtual_user_limit(data['v_limit'])
            # 点击确定
            self.virtual_user_limit_page.click_ensure_add_virtual_user_button()
            # 退出
            self.virtual_user_limit_page.logout()
            # 登录创建的虚拟账号
            self.log_in_base.log_in_with_csv(data['v_account'], data['v_password'])
            self.virtual_user_limit_page.click_workbench_button()
            # 获取抬头列表个数
            name_list = []
            list_number = self.virtual_user_limit_page.get_list_number_in_look_up()
            for n in range(list_number):
                name_list.append(self.virtual_user_limit_page.get_per_name_in_list(n).split(' ')[1])
            print(name_list)
            self.assertNotIn(data['v_limit'], name_list)
            self.virtual_user_limit_page.logout()
            self.log_in_base.log_in()
            # 点击虚拟账号管理
            self.virtual_user_limit_page.click_set_up_and_virtual_user_management()
            # 点击删除-确定
            self.virtual_user_limit_page.click_delete_button_and_ensure()
            # 再次退出
            self.virtual_user_limit_page.logout()
        csv_file.close()
