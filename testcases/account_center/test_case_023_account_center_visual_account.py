import csv
import unittest
from time import sleep

from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.account_center_visual_account_page import AccountCenterVisualAccountPage

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.login.login_page import LoginPage


# 账户中心-虚拟账户管理
# author:孙燕妮

class TestCase023AccountCenterVisualAccount(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_visual_account = AccountCenterVisualAccountPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.log_in_base = LogInBase(self.driver, self.base_page)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_visual_account(self):
        '''通过csv测试虚拟账户管理功能'''
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        sleep(2)
        # 登录
        self.log_in_base.log_in()
        # 进入虚拟账户管理
        self.account_center_page_visual_account.enter_visual_account()
        # 获取虚拟账户管理title
        visual_account_title = self.account_center_page_visual_account.get_visual_account_title()
        # 验证消息中心title是否正确显示
        self.assertIn("虚拟账号管理", visual_account_title, "虚拟账户管理title有误!")
        csv_file = self.account_center_page_read_csv.read_csv('add_visual_account.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            acc_to_add = {
                "account": row[0],
                "passwd": row[1]
            }
            # 添加虚拟账户
            self.account_center_page_visual_account.add_visual_account(acc_to_add["account"], acc_to_add["passwd"])
            # 选择权限-修改数据
            self.account_center_page_visual_account.choose_assign_comm_limit()
            # 选择权限-下发指令
            self.account_center_page_visual_account.choose_assign_comm_limit()
            # 保存
            self.account_center_page_visual_account.save_add_info()
            # 验证是否保存成功
            save_status = self.account_center_page_visual_account.get_save_status()
            self.assertIn("操作成功", save_status, "保存成功")
            self.driver.wait()
        csv_file.close()
        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
