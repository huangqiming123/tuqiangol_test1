import csv
import unittest

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.global_search.global_account_search_page import GlobalAccountSearchPage
from pages.global_search.global_search_page_read_csv import GlobleSearchPageReadCsv
from pages.login.login_page import LoginPage


# 全局搜索-精确查找设备结果唯一用户详情页面-转移用户的操作
# 运行前需修改csv中的转移账户
# author:孙燕妮

class TestCase041GlobAccountExactSearchDetailsAccTrans(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.global_acc_search_page = GlobalAccountSearchPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.global_search_page_read_csv = GlobleSearchPageReadCsv()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_glob_account_exact_search_details_acc_trans(self):
        '''通过csv测试全局搜索-精确查找设备结果唯一用户详情页面-转移用户模块的操作功能'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.log_in_base.log_in()

        csv_file = self.global_search_page_read_csv.read_csv('acc_trans.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            acc_trans = {
                "account": row[0],
                "trans_user": row[1]
            }

            # 全局搜索栏输入搜索关键词进行用户搜索
            self.global_acc_search_page.acc_easy_search(acc_trans["account"])

            # 点击搜索结果-转移客户
            self.global_acc_search_page.click_user_trans()

            # 搜索客户
            self.global_acc_search_page.user_trans_search(acc_trans["trans_user"])

            # 转移
            self.global_acc_search_page.click_trans()

            # 获取转移操作状态
            status = self.global_acc_search_page.get_trans_status()

            # 验证是否转移成功
            self.assertIn("操作成功", status, "操作失败")

            # 关闭当前设备搜索对话框
            self.global_acc_search_page.close_dev_search()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()

        csv_file.close()
