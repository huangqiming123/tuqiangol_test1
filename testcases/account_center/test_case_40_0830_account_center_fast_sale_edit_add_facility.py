import csv
import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.login.login_page import LoginPage


# 账户详情-快捷销售--编辑设备名称和设备sim卡号
# author:戴招利
class TestCase400830AccountCenterFastSaleEditAddFaility(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.assert_text = AssertText()
        self.driver.set_window_max()
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_fast_sale_edit_add_faility_succeed(self):
        '''通过csv测试账户详情-快捷销售-编辑设备名称和设备sim卡号'''
        csv_file = self.account_center_page_read_csv.read_csv('fast_sale_edit_dev_data.csv')
        csv_data = csv.reader(csv_file)

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        self.log_in_base.log_in_with_csv("dzltest", "jimi123")
        self.driver.wait(1)
        self.account_center_page_navi_bar.click_account_center_button()

        for row in csv_data:
            data = {
                "account": row[0],
                "device_imei": row[1],
                "selected_dev": row[2],
                "dev_name": row[3],
                "sim": row[4],
                "old_dev_name": row[5],
                "old_sim": row[6]
            }
            # 进入快捷销售页面
            self.account_center_page_details.account_center_iframe()
            self.account_center_page_details.fast_sales()

            # 查找账户
            self.account_center_page_details.fast_sales_find_account(data["account"])

            # 输入设备imei精确查找设备并添加
            self.account_center_page_details.fast_sales_find_and_add_device(data["device_imei"])
            self.driver.default_frame()
            self.driver.wait()
            # 关闭消息提示框
            try:
                self.account_center_page_details.click_prompt_close()
            except:
                print("没有消息弹框提示")

            # self.account_center_page_details.account_center_iframe()
            # 获取列表设备imei,名称和sim卡号
            info = self.account_center_page_details.get_list_add_equipment_user_and_sim()

            # 验证设备名称和sim卡的元素长度
            self.assertEqual(50, self.account_center_page_details.get_fast_sale_dev_name_len(), "设备名称长度不一致")
            self.assertEqual(20, self.account_center_page_details.get_fast_sale_dev_sim_len(), "设备sim卡长度不一致")

            # 编辑设备名称和sim卡号
            self.account_center_page_details.edit_list_add_equipment(info["imei"], data["dev_name"], data["sim"])

            # 点击用户到期时间
            self.account_center_page_details.account_center_iframe()
            self.account_center_page_details.choose_account_expired_time(data["selected_dev"])
            sleep(1)
            # 销售
            self.account_center_page_details.sale_button()
            # 通过弹出框状态验证是否销售成功
            sale_status_text = self.account_center_page_details.get_sale_status()
            self.assertIn(self.assert_text.account_center_page_operation_done(), sale_status_text, "销售失败")
            self.driver.default_frame()
            sleep(2)

            # 点击设备管理
            dev_data = self.account_center_page_details.get_dev_manage_equipment_user_and_sim(info["imei"])
            for i in range(len(dev_data["dev_imei"])):
                if data["dev_name"] != "":
                    self.assertEqual(info["imei"][i] + data["dev_name"], dev_data["dev_name"][i], "设备名称与期望不一致")
                else:
                    self.assertIn(info["imei"][i][10:], dev_data["dev_name"][i], "为空时，设备名称不存在后五位imei")

                self.assertEqual(data["sim"], dev_data["dev_sim"][i], "sim卡与期望不一致")

            # 改设备数据
            self.account_center_page_details.dev_manage_edit_equipment_user_and_sim(data["old_dev_name"],
                                                                                    data["old_sim"])
            sleep(2)
            self.account_center_page_navi_bar.click_account_center_button()
            sleep(2)
