import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.connect_sql import ConnectSql
from pages.account_center.account_center_msg_center_page import AccountCenterMsgCenterPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.search_sql import SearchSql
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer


# 账户中心-消息中心-编辑设备异常操作
# author:戴招利
class TestCase32AccountCenterMsgEdit_Exception(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_msg_center = AccountCenterMsgCenterPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.connect_sql = ConnectSql()
        self.search_sql = SearchSql()
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.base_page.open_page()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def test_account_center_msg_exception_prompt(self):
        """ 消息中心，验证编辑中的错误提示 """

        self.log_in_base.log_in()
        self.account_center_page_navi_bar.click_account_center_button()
        self.driver.wait(1)
        # 点击进入消息中心
        self.account_center_page_msg_center.enter_msg_center()
        # self.account_center_page_msg_center.message_center_iframe()
        # sleep(10)
        sleep(25)

        # 取元素长度
        len = self.account_center_page_msg_center.get_message_edit_element_len()
        # 基本信息
        self.assertEqual(50, len["device_name"], "设备名称长度不相同")
        self.assertEqual(20, len["sim"], "设备SIM卡号长度不相同")
        self.assertEqual(500, len["remark"], "备注长度不相同")
        # 客户信息
        self.assertEqual(20, len["driver_name"], "司机名称长度不相同")
        self.assertEqual(50, len["vehicle_number"], "车牌号长度不相同")
        self.assertEqual(50, len["sn"], "SN长度不相同")
        self.assertEqual(100, len["engine_number"], "电机/发动机号长度不相同")
        self.assertEqual(20, len["phone"], "车架号长度不相同")
        # self.assertEqual(18, len["id_card"], "电话长度不相同")
        self.assertEqual(50, len["car_frame"], "身份证号长度不相同")
        # 安装信息
        self.assertEqual(100, len["install_company"], "安装公司长度不相同")
        self.assertEqual(50, len["install_personnel"], "安装人员长度不相同")
        self.assertEqual(200, len["install_address"], "安装地址长度不相同")
        self.assertEqual(200, len["install_position"], "安装位置长度不相同")

        # 退出登录
        self.driver.wait()
        self.account_center_page_navi_bar.usr_logout()

    def tearDown(self):
        self.driver.quit_browser()
