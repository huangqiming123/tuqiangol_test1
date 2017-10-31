import csv
import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.account_center_visual_account_page import AccountCenterVisualAccountPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer


# 账户中心-虚拟账户管理---添加异常处理
# author:戴招利
class TestCase29AccountCenterVisualAccountException(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer(choose='chrome')
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.visual_account_page = AccountCenterVisualAccountPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def test_visual_account_exception(self):
        '''虚拟账户管理，异常错误提示'''

        # 登录
        self.log_in_base.log_in()
        self.account_center_page_navi_bar.click_account_center_button()
        # 进入虚拟账户管理
        self.visual_account_page.enter_visual_account()
        # 点击添加
        self.visual_account_page.click_add_button()

        csv_file = self.account_center_page_read_csv.read_csv('visual_account_exception.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            data = {
                "name": row[0],
                "new_password": row[1],
                "new_password2": row[2],
                "name_prompt": row[3],
                "new_pwd_prompt": row[4],
                "new_pwd2_prompt": row[5]
            }
            # 虚拟账号添加与编辑方法
            prompt = self.visual_account_page.get_visu_account_error_prompt("add", data["new_password"],
                                                                            data["new_password2"], data["name"])
            self.assertEqual(data["name_prompt"], prompt["name_error_prompt"], "虚拟账号,登陆名称错误提示语显示不一致")

            self.assertEqual(data["new_pwd_prompt"], prompt["pwd_error_prompt"], "虚拟账号,密码错误提示语显示不一致")

            self.assertEqual(data["new_pwd2_prompt"], prompt["pwd2_error_prompt"], "虚拟账号,确认密码错误提示语显示不一致")

        # 验证密码输入长度
        self.assertEqual(16, self.visual_account_page.get_visual_add_and_edit_len(), "密码限制长度显示不一致")
        # 点取消
        self.visual_account_page.dis_save_add_info()
        csv_file.close()
        self.driver.wait(1)
        # 退出登录
        # self.account_center_page_navi_bar.usr_logout()

    def tearDown(self):
        self.driver.quit_browser()
