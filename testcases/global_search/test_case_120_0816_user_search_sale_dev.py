import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.account_center.account_center_navi_bar_pages import AccountCenterNaviBarPages
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.global_search.global_account_search_page import GlobalAccountSearchPage
from pages.global_search.global_dev_search_page import GlobalDevSearchPage
from pages.global_search.global_search_page_read_csv import GlobleSearchPageReadCsv
from pages.global_search.search_sql import SearchSql


class TestCase120UserSearchSaleDev(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.global_dev_search_page = GlobalDevSearchPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.global_account_search_page = GlobalAccountSearchPage(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.global_search_page_read_csv = GlobleSearchPageReadCsv()
        self.search_sql = SearchSql()
        self.driver.wait(1)
        self.connect_sql = ConnectSql()
        self.assert_text = AssertText()
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_user_search_sale_dev(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.log_in_base.log_in()
        # 点击设备管理 获取imei号
        self.global_account_search_page.click_dev_manage_page()
        first_imei = self.global_account_search_page.get_frist_imei_in_dev_manage_page()
        second_imei = self.global_account_search_page.get_second_imei_in_dev_manage_page()
        third_imei = self.global_account_search_page.get_third_imei_in_dev_manage_page()
        fourth_imei = self.global_account_search_page.get_fourth_imei_in_dev_manage_page()
        fifth_imei = self.global_account_search_page.get_fifth_imei_in_dev_manage_page()

        # 点击账号中心
        self.log_in_base.click_account_center_button()
        self.global_dev_search_page.click_easy_search()
        # 关闭
        self.global_dev_search_page.close_search()
        sleep(2)

        self.global_dev_search_page.click_easy_search()

        # 选择用户搜索
        self.global_dev_search_page.click_dev_search()
        self.global_dev_search_page.click_search_buttons()

        # 获取列表中第二个用户的账号
        self.global_dev_search_page.swith_to_search_frame()
        get_second_user_account = self.global_account_search_page.get_second_user_account_after_search_user()
        # 点击详情
        self.global_account_search_page.click_user_detail_button()
        # 点击销售设备
        self.global_account_search_page.clcik_sale_dev_button_in_user_detail_button()
        # 输入不存在的imei进行添加
        self.global_account_search_page.add_imei_to_sale_dev_in_user_detail(first_imei + '123456')
        # 获取失败的状态
        failure_statues = self.global_account_search_page.get_failure_statue_text_in_user_detail()
        self.assertEqual(self.assert_text.dev_page_fail_text(), failure_statues)
        failure_reason = self.global_account_search_page.get_failure_reason_text_in_user_detail()
        self.assertEqual(self.assert_text.dev_page_inexistence_text(), failure_reason)

        # 关闭失败的弹窗
        self.global_account_search_page.close_failure_windows()

        # 输入与 IMEI 列表中相同、存在的IMEI,点击添加
        self.global_account_search_page.add_imei_to_sale_dev_in_user_detail(first_imei)
        self.global_account_search_page.add_imei_to_sale_dev_in_user_detail(first_imei)

        # 获取失败的状态
        failure_statues = self.global_account_search_page.get_failure_statue_text_in_user_detail()
        self.assertEqual(self.assert_text.dev_page_fail_text(), failure_statues)
        failure_reason = self.global_account_search_page.get_failure_reason_text_in_user_detail()
        self.assertEqual(self.assert_text.dev_page_repetition_text(), failure_reason)

        # 关闭失败的弹窗
        self.global_account_search_page.close_failure_windows()

        # 输入与 IMEI 列表中不相同、存在的IMEI,点击添加
        self.global_account_search_page.add_imei_to_sale_dev_in_user_detail(second_imei)
        get_imei_after_add = self.global_account_search_page.get_imei_after_add_in_user_detail()
        self.assertEqual(second_imei, get_imei_after_add)

        # 输入多个设备的IMEI,其中部分不存在，其中部分与列表中IMEI重复
        self.global_account_search_page.add_imei_to_sale_dev_in_user_detail(
            second_imei + ',' + first_imei + '123456' + ',' + third_imei)
        # 获取失败的状态
        failure_statues = self.global_account_search_page.get_failure_statue_text_in_user_detail()
        self.assertEqual(self.assert_text.dev_page_fail_text(), failure_statues)
        failure_reason = self.global_account_search_page.get_failure_reason_text_in_user_detail()
        self.assertEqual(self.assert_text.dev_page_inexistence_text(), failure_reason)

        second_failure_statues = self.global_account_search_page.get_second_failure_statue_text_in_user_detail()
        self.assertEqual(self.assert_text.dev_page_fail_text(), second_failure_statues)
        second_failure_reason = self.global_account_search_page.get_second_failure_reason_text_in_user_detail()
        self.assertEqual(self.assert_text.dev_page_repetition_text(), second_failure_reason)

        # 关闭失败的弹窗
        self.global_account_search_page.close_failure_windows()

        # 输入多个设备的IMEI,与列表中IMEI不重复，点击添加
        self.global_account_search_page.add_imei_to_sale_dev_in_user_detail(fourth_imei + ',' + fifth_imei)
        total_dev_number = self.global_account_search_page.get_total_dev_number_after_add_in_sale_dev()
        self.assertEqual(5, total_dev_number)
