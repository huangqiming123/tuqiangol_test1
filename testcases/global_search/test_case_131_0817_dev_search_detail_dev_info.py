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


class TestCase131DevSearchDetailDevInfo(unittest.TestCase):
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

    def test_case_dev_search_detail_dev_info(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.log_in_base.log_in()
        self.log_in_base.click_account_center_button()
        self.global_dev_search_page.click_easy_search()
        # 关闭
        self.global_dev_search_page.close_search()
        sleep(2)
        self.global_dev_search_page.click_easy_search()
        sleep(3)
        self.global_dev_search_page.swith_to_search_frame()
        self.global_dev_search_page.click_advanced_search_button()

        # 点击搜索按钮
        self.global_dev_search_page.click_search_buttons_in_dev_advanced_search_page()
        sleep(4)
        # 点击详情
        self.global_dev_search_page.click_detail_button_in_dev_advanced_search_page()
        sleep(2)
        get_imei_in_dev_advanced_detail_page = self.global_dev_search_page.get_imei_after_click_detail_button_in_dev_advanced()
        ## 点击设备信息
        self.global_dev_search_page.click_dev_info_in_dev_advancde_search_page()
        self.global_dev_search_page.switch_to_dev_info_frame()
        get_imei_in_dev_info = self.global_dev_search_page.get_imei_in_dev_info_after_click_dev_info_button()
        self.assertEqual(get_imei_in_dev_advanced_detail_page, get_imei_in_dev_info)

        ## 点击设备IMEI，修改设备IMEI
        get_imei_input_attribute = self.global_dev_search_page.get_imei_input_attribute_in_dev_info_page()
        self.assertEqual('true', get_imei_input_attribute)

        ## 点击设备设备名称输入框，修改设备的设备名称，点击保存
        self.global_dev_search_page.input_dev_name_modify_dev_info_in_dev_info_page('这是设备名称')
        # 点击保存
        self.global_dev_search_page.click_ensure_button_in_dev_info_page()

        # 点击设备设备分组下拉按钮，修改设备的设备分组（在控制台页面已新建分组），点击保存
        self.global_dev_search_page.select_dev_group_in_dev_info_page()
        self.global_dev_search_page.click_ensure_button_in_dev_info_page()

        # 修改使用范围选项（11类）
        self.global_dev_search_page.click_dev_range_of_use_in_dev_info_page('2')
        self.global_dev_search_page.click_ensure_button_in_dev_info_page()

        # 修改iccid
        get_iccid_input_attribute = self.global_dev_search_page.get_iccid_input_attribute_in_dev_info_page()
        self.assertEqual('true', get_iccid_input_attribute)

        # 修改销售时间
        get_sale_time_input_attribute = self.global_dev_search_page.get_sale_time_input_attribute_in_dev_info_page()
        self.assertEqual('true', get_sale_time_input_attribute)

        # 修改超速速度和超速时间
        self.global_dev_search_page.add_over_speed_and_over_speed_time_to_modify_dev_info('12', '10')
        self.global_dev_search_page.click_ensure_button_in_dev_info_page()

        # 点击备注输入框，修改设备的备注，点击保存
        self.global_dev_search_page.add_remark_to_modify_dev_info('这是备注')
        self.global_dev_search_page.click_ensure_button_in_dev_info_page()

        ## 点击设备类型，修改设备类型
        get_dev_type_input_attribute = self.global_dev_search_page.get_dev_type_input_attribute_in_dev_info_page()
        self.assertEqual('true', get_dev_type_input_attribute)

        ## 点击设备SIM卡号输入框，修改设备的设备SIM卡号，点击保存
        self.global_dev_search_page.add_sim_number_to_modify_dev_info_page('123456789')
        self.global_dev_search_page.click_ensure_button_in_dev_info_page()

        ## 点击激活时间，修改设备的激活时间
        get_active_time_input_attribute = self.global_dev_search_page.get_active_time_input_attribute_in_dev_info_page()
        self.assertEqual('true', get_active_time_input_attribute)

        ## 点击平台到期时间，修改设备平台到期时间
        get_platform_time_input_attribute = self.global_dev_search_page.get_platform_time_input_attribute_in_dev_info_page()
        self.assertEqual('true', get_platform_time_input_attribute)

        ##点击imsi，修改imsi
        get_imsi_input_attribute = self.global_dev_search_page.get_imsi_input_attribute_in_dev_info_page()
        self.assertEqual('true', get_imsi_input_attribute)

        ## 点击导入时间输入框，编辑时间
        get_export_time_attribute = self.global_dev_search_page.get_export_time_attribute_in_dev_info_page()
        self.assertEqual('true', get_export_time_attribute)
