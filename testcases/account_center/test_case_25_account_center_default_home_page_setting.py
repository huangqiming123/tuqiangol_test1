import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.assert_text2 import AssertText2
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.account_center_setting_home_page import AccountCenterSettingHomePage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer


# 账户中心--默认首页设置
# author:戴招利
class TestCase25AccountCenterDefaultHomePageSetting(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_home_page_setting = AccountCenterSettingHomePage(self.driver, self.base_url)
        self.assert_text2 = AssertText2()
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.assert_text = AssertText()
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_setting_default_home_page_success(self):
        '''默认设置首页成功'''

        self.log_in_base.log_in_with_csv("dzltest", "jimi123")
        self.account_center_page_navi_bar.click_account_center_button()
        # 点击默认首页设置
        self.account_center_page_home_page_setting.click_home_page_setting()
        # 取列表数据
        all_state = self.account_center_page_home_page_setting.get_home_page_list_all_state()
        self.driver.default_frame()

        for i in range(len(all_state)):
            # 点击账户中心
            self.account_center_page_navi_bar.click_account_center_button()
            self.account_center_page_navi_bar.click_account_center_button()
            # 点击默认首页设置
            self.account_center_page_home_page_setting.click_home_page_setting()
            # 已默认
            is_default = self.assert_text2.account_center_home_page_setting_state()

            text = self.account_center_page_home_page_setting.get_default_setting_text(i + 1)
            if text["state"] == is_default:
                self.driver.default_frame()
                continue
            else:

                # 点击设置默认页面、获取状态
                prompt = self.account_center_page_home_page_setting.click_setting_default(i + 1)
                self.assertEqual(self.assert_text2.account_center_home_page_setting_prompt(), prompt,
                                 "预期设置默认后的提示语与实际提示语不一致")

                print(prompt)
                self.driver.wait()
                setting_text = self.account_center_page_home_page_setting.get_default_setting_text(i + 1)
                self.assertEqual(is_default, setting_text["state"],
                                 "设置默认后，状态未改变")

                default_list = []
                for a in all_state:
                    if a == is_default:
                        default_list.append(a)
                self.assertEqual(1, len(default_list), "列表设置默认中存在多个已默认")
                del (default_list[:])
                print("删除后：", default_list)

                self.driver.default_frame()
                # 退出
                sleep(2)
                self.account_center_page_navi_bar.usr_logout()
                # 登录
                self.log_in_base.log_in_with_csv("dzltest", "jimi123")
                actual_url = self.driver.get_current_url()
                # 获取默认设置的首页地址
                expect_url = self.account_center_page_home_page_setting.get_expect_url(setting_text["page_name"])
                self.assertEqual(expect_url, actual_url, "登录后，默认主页显示错误")
                sleep(2)
            break
        sleep(2)
        # self.account_center_page_navi_bar.usr_logout()
