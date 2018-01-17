import csv
import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.connect_sql import ConnectSql
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
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


class TestCase402CustomerManageMentLowerUserSearch(unittest.TestCase):
    # 测试客户管理 搜索 客户
    def setUp(self):
        self.driver = AutomateDriverServer(choose='chrome')
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.cust_manage_basic_info_and_add_cust_page = CustManageBasicInfoAndAddCustPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.cust_manage_cust_list_page = CustManageCustListPage(self.driver, self.base_url)
        self.cust_manage_my_dev_page = CustManageMyDevPage(self.driver, self.base_url)
        self.cust_manage_lower_account_page = CustManageLowerAccountPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.cust_manage_page_read_csv = CustManagePageReadCsv()
        self.search_sql = SearchSql()
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.close_window()
        self.driver.quit_browser()

    def test_customer_management_lower_user_search(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.log_in_base.log_in()
        # 点击账户中心
        # self.account_center_page_navi_bar.click_account_center_button()
        # current_account = self.log_in_base.get_log_in_account()

        # 进入客户管理页面
        current_handle = self.driver.get_current_window_handle()
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()
        self.base_page.change_windows_handle(current_handle)

        csv_file = self.cust_manage_page_read_csv.read_csv('acc_search.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'account': row[0],
                "account_type": row[1],
                "info": row[2]
            }
            print(search_data)
            sleep(1)
            self.cust_manage_lower_account_page.add_data_to_search_account(search_data)
            connect = self.connect_sql.connect_tuqiang_sql()
            # 创建数据库游标
            cur = connect.cursor()

            # 执行sql脚本查询当前登录账号的userId,fullParent
            get_id_sql = "select o.account,o.userId,o.fullParentId from user_info o where o.account = '" + search_data[
                'account'] + "' ;"
            cur.execute(get_id_sql)
            # 读取数据
            user_relation = cur.fetchall()

            # 遍历数据
            for row in user_relation:
                user_relation_id = {
                    "account": row[0],
                    "userId": row[1],
                    "fullParent": row[2]
                }
                # 执行sql脚本，根据当前登录账号的userId,fullParent查询出当前账户的所有下级账户
                get_lower_account_sql = "select userId from user_info where fullParentId = " + \
                                        "'" + user_relation_id["fullParent"] + user_relation_id[
                                            "userId"] + ",'" + ";"

                cur.execute(get_lower_account_sql)
                # 读取数据
                lower_account = cur.fetchall()

                print(lower_account)

                lower_account_list = []
                for range1 in lower_account:
                    for range2 in range1:
                        lower_account_list.append(range2)
                lower_account_tuple = tuple(lower_account_list)
                print(lower_account_tuple)

                get_total_sql = self.search_sql.search_account_sql(lower_account_tuple, search_data)
                print(get_total_sql)
                cur.execute(get_total_sql)
                # 读取数据
                total_data = cur.fetchall()
                # 从数据tuple中获取最终查询记录统计条数
                total_list = []
                for range1 in total_data:
                    for range2 in range1:
                        total_list.append(range2)
                total = len(total_list)
                print('本次查询数据库的条数为：%s' % total)
                web_total = self.cust_manage_lower_account_page.get_account_number()
                print('本次查询页面的条数是：%s' % web_total)
                self.assertEqual(total, web_total)

            cur.close()
            connect.close()

        csv_file.close()
