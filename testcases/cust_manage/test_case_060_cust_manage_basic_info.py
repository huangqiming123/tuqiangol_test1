import csv
import unittest

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.cust_manage.cust_manage_basic_info_and_add_cust_page import CustManageBasicInfoAndAddCustPage
from pages.cust_manage.cust_manage_cust_list_page import CustManageCustListPage
from pages.cust_manage.cust_manage_my_dev_page import CustManageMyDevPage

from pages.login.login_page import LoginPage


# 客户管理-客户及其设备基本信息验证

# author:孙燕妮

class TestCase060CustManageBasicInfo(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.cust_manage_basic_info_and_add_cust_page = CustManageBasicInfoAndAddCustPage(self.driver, self.base_url)
        self.cust_manage_cust_list_page = CustManageCustListPage(self.driver, self.base_url)
        self.cust_manage_my_dev_page = CustManageMyDevPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_cust_manege_basic_info(self):
        '''测试客户管理-客户及其设备基本信息验证'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.log_in_base.log_in()
        current_account = self.log_in_base.get_log_in_account()
        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()

        # 获取客户管理页面当前账号
        cus_page_current_account = self.cust_manage_cust_list_page.get_cus_page_current_account()
        self.assertEqual(current_account, cus_page_current_account)
        connect = self.connect_sql.connect_tuqiang_sql()
        cursor = connect.cursor()
        get_account_user_info_sql = "SELECT o.type,o.phone,o.nickName from user_organize o INNER JOIN user_relation r ON o.userId = r.userId WHERE o.account = '" + \
                                    cus_page_current_account + "';"
        cursor.execute(get_account_user_info_sql)
        get_account_user_info = cursor.fetchall()
        current_user_info = []
        for range1 in get_account_user_info:
            for range2 in range1:
                current_user_info.append(range2)
        cursor.close()
        connect.close()
        print(current_user_info)
        if current_user_info[0] == 8:
            self.type = "代理商"
        elif current_user_info[0] == 9:
            self.type = "用户"
        usr_info_type = self.cust_manage_cust_list_page.usr_info_type()
        self.assertEqual(self.type, usr_info_type, "账户总览左下方显示的客户类型错误")

        self.assertEqual(current_user_info[1], self.cust_manage_cust_list_page.get_cus_page_account_phone())
        self.assertEqual(current_user_info[2], self.cust_manage_cust_list_page.get_cus_page_account_name())

        # 获取左侧客户列表中当前用户库存和总数
        stock_number = self.cust_manage_cust_list_page.get_account_stock_number()
        total_number = self.cust_manage_cust_list_page.get_account_total_number()

        # 获取总览的库存
        overview_stock_number = self.cust_manage_cust_list_page.get_cus_page_overview_stock_number()
        overview_total_number = self.cust_manage_cust_list_page.get_cus_page_overview_total_number()
        self.assertEqual(stock_number, overview_stock_number)
        self.assertEqual(total_number, overview_total_number)

        # 获取当前用户下库存的设备数量
        equipment_list_stock_number = self.cust_manage_cust_list_page.get_equipment_number()
        # 断言
        self.assertEqual(stock_number, str(equipment_list_stock_number))

        # 进入账户中心页面
        self.cust_manage_basic_info_and_add_cust_page.enter_account_center()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
