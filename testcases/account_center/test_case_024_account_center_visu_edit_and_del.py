import csv
import unittest

from automate_driver.automate_driver_server import AutomateDriverServer
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.account_center_visual_account_page import AccountCenterVisualAccountPage

from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.login.login_page import LoginPage


# 账户中心-虚拟账户管理-编辑、删除
# author:孙燕妮

class TestCase024AccountCenterVisuEditAndDel(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_visual_account = AccountCenterVisualAccountPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_visu_edit_and_del(self):
        '''通过csv测试虚拟账户管理-编辑、删除功能'''
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()
        # 进入虚拟账户管理
        self.account_center_page_visual_account.enter_visual_account()
        csv_file = self.account_center_page_read_csv.read_csv('add_visual_account.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            acc_to_add = {
                "account": row[0],
                "passwd": row[1]
            }
            # 添加虚拟账户
            self.account_center_page_visual_account.add_visual_account(acc_to_add["account"], acc_to_add["passwd"])
            # 取消添加
            self.account_center_page_visual_account.dis_save_add_info()
            self.driver.wait()
            # 编辑列表中的虚拟账户
            self.account_center_page_visual_account.edit_visu_account(acc_to_add["passwd"])
            # 验证是否保存成功
            save_status = self.account_center_page_visual_account.get_save_status()
            self.assertIn("操作成功", save_status, "保存成功")
            self.account_center_page_visual_account.dis_edit()
            self.driver.wait(1)
            # 删除列表中的虚拟账户
            self.account_center_page_visual_account.del_visu_account()
            # 验证是否操作成功
            save_status = self.account_center_page_visual_account.get_save_status()
            self.assertIn("操作成功", save_status, "操作成功")
            self.driver.wait()
        csv_file.close()
        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
