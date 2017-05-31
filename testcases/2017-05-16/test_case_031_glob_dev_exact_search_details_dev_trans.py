import csv
import unittest

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_pages import AccountCenterNaviBarPages
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.global_search.global_dev_search_page import GlobalDevSearchPage
from pages.global_search.global_search_page_read_csv import GlobleSearchPageReadCsv


# 全局搜索-精确查找设备结果唯一设备详情页面-设备转移模块的操作
# author:孙燕妮

class TestCase030GlobDevExactSearchDetailsDevTrans(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.global_dev_search_page = GlobalDevSearchPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPages(self.driver, self.base_url)
        self.global_search_page_read_csv = GlobleSearchPageReadCsv()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_glob_dev_exact_search_details_dev_trans(self):
        '''通过csv测试全局搜索-精确查找设备结果唯一设备详情页面-设备转移模块的操作功能'''
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()
        self.global_dev_search_page.click_equipment_button()

        csv_file = self.global_search_page_read_csv.read_csv('dev_trans_info.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            dev_trans_info = {
                "keyword": row[0],
                "user_name": row[1],
                "imei": row[2],
                "trans_user": row[3]
            }
            # 全局搜索栏输入搜索关键词进行设备搜索
            self.global_dev_search_page.device_easy_searchs(dev_trans_info["keyword"])
            # 点击搜索结果-设备转移下的操作
            self.global_dev_search_page.click_dev_trans()
            # 搜索转移用户
            self.global_dev_search_page.dev_trans_cust(dev_trans_info["user_name"])
            self.driver.wait()
            # 点击转移
            self.global_dev_search_page.click_trans_btn()
            # 验证是否转移成功
            status = self.global_dev_search_page.get_dev_trans_status()
            self.assertIn("操作成功", status, "设备转移操作失败")

            self.driver.wait(1)

            # 添加设备imei
            self.global_dev_search_page.dev_imei_input(dev_trans_info["imei"])
            self.global_dev_search_page.dev_add()
            self.driver.wait()

            # 验证是否添加成功
            add_num01 = self.global_dev_search_page.dev_sele_num()
            self.assertEqual("1", add_num01, "设备添加失败")
            self.driver.wait(1)
            # 删除当前已选设备
            self.global_dev_search_page.del_curr_dev()
            # 验证是否已删除
            del_num = self.global_dev_search_page.dev_sele_num()
            self.assertEqual("0", del_num, "当前已选设备删除失败")

            # 添加设备imei
            self.global_dev_search_page.dev_imei_input(dev_trans_info["imei"])
            self.global_dev_search_page.dev_add()
            self.driver.wait()

            # 验证是否添加成功
            add_num02 = self.global_dev_search_page.dev_sele_num()
            self.assertEqual("1", add_num02, "设备添加失败")

            self.driver.wait(1)

            # 重置
            self.global_dev_search_page.reset_dev_trans()

            # 验证是否重置成功
            reset_num = self.global_dev_search_page.dev_sele_num()
            self.assertEqual("0", reset_num, "设备重置失败")

            self.driver.wait(1)

            # 添加设备imei
            self.global_dev_search_page.dev_imei_input(dev_trans_info["imei"])
            self.global_dev_search_page.dev_add()

            self.driver.wait()

            # 验证是否添加成功
            add_num02 = self.global_dev_search_page.dev_sele_num()
            self.assertEqual("1", add_num02, "设备添加失败")

            self.driver.wait(1)

            # 搜索转移用户
            self.global_dev_search_page.dev_trans_cust(dev_trans_info["trans_user"])

            # 点击转移
            self.global_dev_search_page.click_trans_btn()

            # 验证是否转移成功
            status = self.global_dev_search_page.get_dev_trans_status()
            self.assertIn("操作成功", status, "设备转移操作失败")

            self.driver.wait(1)

            # 取消转移设备
            self.global_dev_search_page.click_dis_trans_btn()

            self.driver.wait(1)

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()

        csv_file.close()
