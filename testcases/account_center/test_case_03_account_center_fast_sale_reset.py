import csv
import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.login.login_page import LoginPage


# 账户中心-账户详情-快捷销售-删除设备、重置
# author:孙燕妮
class TestCase016AccountCenterFastSaleReset(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_fast_sale_reset(self):
        '''通过csv测试账户详情-快捷销售-删除设备、重置功能'''
        csv_file = self.account_center_page_read_csv.read_csv('fast_sale_exact_find_and_sale.csv')
        csv_data = csv.reader(csv_file)

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        # self.log_in_base.log_in()
        self.log_in_base.log_in_with_csv("dzltest", "jimi123")
        self.driver.wait(1)
        self.account_center_page_navi_bar.click_account_center_button()

        for row in csv_data:
            search_account = {
                "account": row[0],
                "device_imei": row[1],
                "imei_count": row[2],
                "selected_dev": row[2]
            }
            # 进入快捷销售页面
            self.account_center_page_details.account_center_iframe()
            self.account_center_page_details.fast_sales()

            # 查找账户
            self.account_center_page_details.fast_sales_find_account(search_account["account"])
            #点取消
            self.account_center_page_details.fast_sales_find_and_dis_add_device("123123123")

            # 输入设备imei精确查找设备并添加
            self.account_center_page_details.fast_sales_find_and_add_device(search_account["device_imei"])
            self.driver.default_frame()
            self.driver.wait()

            #验证消息中的失败个数
            failure_count = self.account_center_page_details.get_device_prompt_failure_count()
            list_failure_count = self.account_center_page_details.get_device_list_failure_count()
            self.assertEqual(failure_count, list_failure_count, "显示的失败个数与列表中的失败数不一致")

            #验证消息中的成功个数
            all_data = self.account_center_page_details.get_prompt_list_data()
            succeed_count = self.account_center_page_details.get_device_prompt_succeed_count()
            self.account_center_page_details.click_prompt_close()
            self.account_center_page_details.account_center_iframe()
            list_count = self.account_center_page_details.get_list_succeed_count()
            self.assertEqual(succeed_count, list_count, "成功添加的设备数不一致")

            #断言失败提示中的信息
            for s in range(list_failure_count):
                self.assertIsNotNone(all_data["imei"][s], "sim卡号为空")
                self.assertEqual("失败", all_data["state"][s], "存在不是失败的数据")
                self.assertIsNotNone(all_data["cause"][s], "失败原因中存在空数据")


            # 验证已选设备计数是否准确
            dev_num = self.account_center_page_details.get_selected_device_num()
            self.assertEqual(list_count, dev_num, "已选设备个数不准确")
            # 删除列表中的设备
            self.account_center_page_details.delete_list_device()

            self.assertEqual(0, self.account_center_page_details.get_selected_device_num(), "删除设备后，已选设备数不是0")

            # 重置
            self.account_center_page_details.reset_device()
            self.driver.default_frame()
        csv_file.close()
        # 退出登录
        self.account_center_page_navi_bar.usr_logout()