import csv
import unittest

from automate_driver.automate_driver_server import AutomateDriverServer
from model.connect_sql import ConnectSql
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.cust_manage.cust_manage_basic_info_and_add_cust_page import CustManageBasicInfoAndAddCustPage
from pages.cust_manage.cust_manage_cust_list_page import CustManageCustListPage
from pages.cust_manage.cust_manage_lower_account_page import CustManageLowerAccountPage
from pages.cust_manage.cust_manage_my_dev_page import CustManageMyDevPage
from pages.cust_manage.cust_manage_page_read_csv import CustManagePageReadCsv
from pages.cust_manage.search_sql import SearchSql

from pages.login.login_page import LoginPage


# 客户管理-我的设备-搜索

# author:孙燕妮

class TestCase071CustManageDevSearch(unittest.TestCase):
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
        self.cust_manager_page_read_csv = CustManagePageReadCsv()
        self.search_sql = SearchSql()
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_cust_manage_dev_search(self):
        '''客户管理-我的设备-搜索'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()

        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()

        csv_file = self.cust_manager_page_read_csv.read_csv('dev_search_data.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'account': row[0],
                'group': row[1],
                'active': row[2],
                'bound': row[3],
                'sim_or_imei': row[4],
                'info': row[5]
            }
            self.cust_manage_cust_list_page.add_data_to_search_dev(search_data)

            # 连接数据库查询
            connect = self.connect_sql.connect_tuqiang_sql()
            cursor = connect.cursor()
            get_id_sql = "select userId from user_organize where account = '" + search_data['account'] + "';"
            cursor.execute(get_id_sql)
            account_id = cursor.fetchall()
            user_id = account_id[0][0]

            get_total_sql = self.search_sql.search_dev_sql(user_id, search_data)

            print(get_total_sql)
            cursor.execute(get_total_sql)
            # 读取数据
            total_data = cursor.fetchall()
            # 从数据tuple中获取最终查询记录统计条数
            total_list = []
            for range1 in total_data:
                for range2 in range1:
                    total_list.append(range2)
            total = len(total_list)
            print('本次查询数据库的条数为：%s' % total)
            web_total = self.cust_manage_cust_list_page.get_equipment_number()
            print('本次查询页面的条数是：%s' % web_total)
            self.assertEqual(total, web_total)

            cursor.close()
            connect.close()
        # 进入账户中心页面
        self.cust_manage_basic_info_and_add_cust_page.enter_account_center()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
