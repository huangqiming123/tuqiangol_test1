import csv
import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.assert_text2 import AssertText2
from model.connect_sql import ConnectSql
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.cust_manage.cust_manage_basic_info_and_add_cust_page import CustManageBasicInfoAndAddCustPage
from pages.cust_manage.cust_manage_cust_list_page import CustManageCustListPage
from pages.cust_manage.cust_manage_lower_account_page import CustManageLowerAccountPage

from pages.cust_manage.cust_manage_my_dev_page import CustManageMyDevPage
from pages.cust_manage.cust_manage_page_read_csv import CustManagePageReadCsv
from pages.login.login_page import LoginPage


# 编辑客户--客户树操作

class TestCase66CustManageCustEditCustSearch(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.cust_manage_basic_info_and_add_cust_page = CustManageBasicInfoAndAddCustPage(self.driver, self.base_url)
        self.cust_manage_cust_list_page = CustManageCustListPage(self.driver, self.base_url)
        self.cust_manage_my_dev_page = CustManageMyDevPage(self.driver, self.base_url)
        self.cust_manage_lower_account_page = CustManageLowerAccountPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.cust_manage_page_read_csv = CustManagePageReadCsv()
        self.assert_text2 = AssertText2()
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.assert_text = AssertText()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_cust_manage_edit_cust_search(self):

        account = ["jianyigezh1", "csjianyigezh2"]
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()
        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()
        sleep(2)
        csv_file = self.cust_manage_page_read_csv.read_csv('edit_user_tree.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            info = {
                "username": row[0],
                "search_user": row[1]
            }

            # 搜索用户
            self.cust_manage_lower_account_page.input_search_info(info["username"])
            self.cust_manage_lower_account_page.click_search_btn()
            # self.cust_manage_lower_account_page.click_search_btn()
            self.assertEqual(info["username"], self.cust_manage_lower_account_page.get_search_result_account(),
                             "搜索结果账号不一致")
            # 获取类型
            type = self.cust_manage_lower_account_page.get_search_result_account_type()

            # 点击编辑用户
            self.cust_manage_basic_info_and_add_cust_page.click_edit_customer_process()
            sleep(1)
            search_user = info["search_user"].split("/")
            for user in search_user:
                #搜索用户
                self.cust_manage_basic_info_and_add_cust_page.search_cust(user)
                self.cust_manage_basic_info_and_add_cust_page.click_search_user()
                sleep(2)
                #获取提示
                self.cust_manage_basic_info_and_add_cust_page.locate_to_iframe()
                status = self.cust_manage_lower_account_page.edit_info_save_status()
                self.driver.default_frame()
                print(status)

                if type == " 销售":
                    try:
                        self.assertEqual(self.assert_text2.cust_manage_sell_shift_agent_prompt(), status,
                                         "销售转移给代理商时,提示不一致")
                    except:
                        self.assertEqual(self.assert_text2.cust_manage_sell_shift_user_prompt(), status,
                                         "销售转移给用户时,提示不一致")
                elif type == " 代理商":
                    self.assertEqual(self.assert_text2.cust_manage_agent_shift_user_prompt(), status, "代理商账号，转移客户时提示不一致")
            #取消
            self.cust_manage_basic_info_and_add_cust_page.click_cancel_edit()


        # 搜索用户
        self.cust_manage_lower_account_page.input_search_info(account[0])
        self.cust_manage_lower_account_page.click_search_btn()
        # 点击编辑用户
        self.cust_manage_basic_info_and_add_cust_page.click_edit_customer_process()

        #验证不能作为上级的验证
        for user in account:
            self.cust_manage_basic_info_and_add_cust_page.search_cust(user)
            self.cust_manage_basic_info_and_add_cust_page.click_search_user()
            sleep(2)
            self.cust_manage_basic_info_and_add_cust_page.locate_to_iframe()
            status = self.cust_manage_lower_account_page.edit_info_save_status()
            self.driver.default_frame()
            self.assertEqual(self.assert_text2.cust_manage_select_user_unable_superior(), status, "提示显示不一致")

        # 搜索无数据的内容
        self.cust_manage_basic_info_and_add_cust_page.search_cust('无数据')
        get_text = self.cust_manage_basic_info_and_add_cust_page.get_search_no_data_text()
        self.assertIn(self.assert_text.account_center_page_no_data_text(), get_text)
        self.cust_manage_basic_info_and_add_cust_page.click_cancel_edit()

        #验证循环点击五次
        self.cust_manage_lower_account_page.input_search_info("yonghu123")
        self.cust_manage_lower_account_page.click_search_btn()
        self.cust_manage_basic_info_and_add_cust_page.click_edit_customer_process()
        for n in range(5):
            self.cust_manage_basic_info_and_add_cust_page.locate_to_iframe()
            #self.driver.click_element('x,//*[@id="treeDemo2_%s_span"]' % str(n + 3))
            self.driver.click_element('x,//*[@id="treeDemo2_%s_span"]' % str(n + 2))
            sleep(2)
            text = self.driver.get_text('x,//*[@id="treeDemo2_%s_span"]' % str(n + 2))
            account_name = text.split('(')[0]
            value = self.driver.get_element('x,//*[@id="topUser"]').get_attribute('value')
            self.assertEqual(account_name, value)
            self.driver.default_frame()


        csv_file.close()
