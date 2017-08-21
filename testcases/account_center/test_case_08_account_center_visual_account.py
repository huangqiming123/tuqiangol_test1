import csv
import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.account_center_visual_account_page import AccountCenterVisualAccountPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.login.login_page import LoginPage


# 账户中心-虚拟账户管理--添加虚拟账号
# author:孙燕妮

class TestCase08AccountCenterVisualAccount(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_visual_account = AccountCenterVisualAccountPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.assert_text = AssertText()
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

        csv_file = self.account_center_page_read_csv.read_csv('add_visual_account.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            acc_to_add = {
                "account": row[0],
                "passwd": row[1]
            }
            # 登录
            self.log_in_base.log_in()
            self.account_center_page_navi_bar.click_account_center_button()
            # 进入虚拟账户管理
            self.account_center_page_visual_account.enter_visual_account()
            # 进入iframe
            self.account_center_page_visual_account.visual_account_iframe()
            # 获取虚拟账户管理title
            visual_account_title = self.account_center_page_visual_account.get_visual_account_title()
            # 验证消息中心title是否正确显示
            self.assertIn(self.assert_text.account_center_page_virtual_account_manager(), visual_account_title,
                          "虚拟账户管理title有误!")
            self.driver.default_frame()

            # 添加虚拟账户
            self.account_center_page_visual_account.add_visual_account(acc_to_add["account"], acc_to_add["passwd"])
            state = self.account_center_page_visual_account.get_visual_account_limits_state()
            self.assertEqual(False, state["edit_data"], "修改数据默认勾选了")
            self.assertEqual(False, state["instruction"], "下发指令默认勾选了")
            # 保存
            self.account_center_page_visual_account.save_add_info()

            # 验证是否保存成功
            save_status = self.account_center_page_visual_account.get_save_status()
            self.assertIn(self.assert_text.account_center_page_operation_done(), save_status, "保存成功")
            self.driver.wait()

            #退出登录验证虚拟账号
            self.account_center_page_navi_bar.usr_logout()
            self.log_in_base.log_in_with_csv(acc_to_add["account"], acc_to_add["passwd"])
            self.assertEqual(acc_to_add["account"], self.account_center_page_navi_bar.hello_user_account(),
                             "招呼栏登录账号显示不一致")
            self.account_center_page_navi_bar.usr_logout()

        csv_file.close()
