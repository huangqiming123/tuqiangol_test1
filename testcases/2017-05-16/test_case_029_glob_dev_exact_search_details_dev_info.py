import csv
import unittest
from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_pages import AccountCenterNaviBarPages
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.global_search.global_dev_search_page import GlobalDevSearchPage
from pages.global_search.global_search_page_read_csv import GlobleSearchPageReadCsv


# 全局搜索-精确查找设备结果唯一设备详情页面-设备信息-基本信息模块的操作
# author:孙燕妮

class TestCase029GlobDevExactSearchDetailsDevInfo(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.global_dev_search_page = GlobalDevSearchPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.global_search_page_read_csv = GlobleSearchPageReadCsv()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_glob_dev_exact_search_details_dev_info(self):
        '''通过csv测试全局搜索-精确查找设备结果唯一设备详情页面-设备信息-基本信息模块的操作功能'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()
        self.global_dev_search_page.click_equipment_button()

        csv_file = self.global_search_page_read_csv.read_csv('dev_info_modify.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            dev_info = {
                "keyword": row[0],
                "dev_name": row[1],
                "dev_group": row[2],
                "use_range": row[3],
                "dev_SIM": row[4],
                "dev_remark": row[5]
            }
            # 全局搜索栏输入搜索关键词进行设备搜索
            self.global_dev_search_page.device_easy_searchs(dev_info["keyword"])
            # 点击搜索结果-设备信息(基本信息)的操作
            self.global_dev_search_page.click_dev_info()
            self.driver.switch_to_frame('x,//*[@id="complex_editDevice_iframe"]')
            # 修改设备名称
            self.global_dev_search_page.dev_name_modify(dev_info["dev_name"])
            # 移动设备分组
            self.global_dev_search_page.dev_group_modify(dev_info["dev_group"])
            # 选择使用范围
            self.global_dev_search_page.dev_use_range_choose(dev_info["use_range"])
            # 填写设备SIM卡号
            self.global_dev_search_page.dev_SIM_edit(dev_info["dev_SIM"])
            # 填写设备备注
            self.global_dev_search_page.dev_remark_edit(dev_info["dev_remark"])

            # 保存编辑
            self.global_dev_search_page.dev_basic_info_save()
            # 验证保存状态是否成功
            save_status = self.global_dev_search_page.dev_basic_info_save_status()
            self.assertIn("操作成功", save_status, "保存失败")
            self.driver.default_frame()
        # 关闭当前设备搜索对话框
        self.global_dev_search_page.close_dev_search()
        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
        csv_file.close()
