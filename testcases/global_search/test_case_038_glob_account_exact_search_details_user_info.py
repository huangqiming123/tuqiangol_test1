import csv
import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_pages import AccountCenterNaviBarPages
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.global_search.global_account_search_page import GlobalAccountSearchPage
from pages.global_search.global_search_page_read_csv import GlobleSearchPageReadCsv


# 全局搜索-精确查找设备结果唯一用户详情页面-用户信息模块的操作
# author:孙燕妮

class TestCase038GlobAccountExactSearchDetailsUserInfo(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.global_acc_search_page = GlobalAccountSearchPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.global_search_page_read_csv = GlobleSearchPageReadCsv()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_glob_account_exact_search_details_user_info(self):
        '''通过csv测试全局搜索-精确查找设备结果唯一用户详情页面-用户信息模块的操作功能'''
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()

        csv_file = self.global_search_page_read_csv.read_csv('account_info_modify.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            acc_info = {
                "account": row[0],
                "acc_type": row[1],
                "acc_name": row[2],
                "phone": row[3],
                "email": row[4],
                "conn": row[5],
                "com": row[6],
                "keyword": row[7]
            }

            # 全局搜索栏输入搜索关键词进行用户搜索
            self.global_acc_search_page.acc_easy_search(acc_info["account"])
            sleep(2)
            # 点击搜索结果-用户信息的操作
            self.global_acc_search_page.click_acc_info()

            # 选择用户类型
            self.global_acc_search_page.acc_type_choose(acc_info["acc_type"])

            # 编辑用户信息
            self.global_acc_search_page.acc_input_info_edit(acc_info["acc_name"],
                                                            acc_info["phone"],
                                                            acc_info["email"],
                                                            acc_info["conn"],
                                                            acc_info["com"])

            # 修改登录权限
            self.global_acc_search_page.acc_login_limit_modi()

            # 选择指令权限
            self.global_acc_search_page.acc_instr_limit_modi()

            # 修改设备权限
            self.global_acc_search_page.acc_modi_limit_modi()

            # 保存编辑
            self.global_acc_search_page.acc_info_save()
            # 验证保存状态是否成功
            save_status = self.global_acc_search_page.acc_info_save_status()
            self.assertIn("操作成功", save_status, "保存失败")
            # 关闭当前设备搜索对话框
            self.global_acc_search_page.close_dev_search()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()

        csv_file.close()
