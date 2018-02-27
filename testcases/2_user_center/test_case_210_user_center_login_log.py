import csv
import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.connect_es import ConnectEs
from model.connect_sql import ConnectSql
from pages.account_center.account_center_operation_log_page import AccountCenterOperationLogPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.help.help_page import HelpPage
from pages.help.help_page_sql import HelpPageSql
from pages.login.login_page import LoginPage

__author__ = ''

class TestCase210UserCenterLoginLog(unittest.TestCase):
    # 测试登录日志查询
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.help_page = HelpPage(self.driver, self.base_url)
        self.account_center_page_operation_log = AccountCenterOperationLogPage(self.driver, self.base_url)
        self.help_page_sql = HelpPageSql()
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.connect_sql = ConnectSql()
        self.connect_es = ConnectEs()
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_user_center_login_log(self):
        self.base_page.open_page()
        self.log_in_base.log_in()
        sleep(3)
        current_handle = self.driver.get_current_window_handle()
        self.log_in_base.click_account_center_button()
        self.base_page.change_windows_handle(current_handle)

        # 获取登录账号的用户名
        current_account = self.log_in_base.get_log_in_account()

        # 点击招呼栏-业务日志
        self.account_center_page_operation_log.click_help_button()
        self.help_page.click_log_in_log()
        # 判断当前页面是否正确跳转至业务日志页面
        expect_url = self.base_url + "/userFeedback/toHelp"
        self.assertEqual(expect_url, self.driver.get_current_url(), "当前页面跳转错误")

        i = 0
        csv_file = self.account_center_page_read_csv.read_csv('search_log_in_log_data.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'account': row[0],
                'begin_time': row[1],
                'end_time': row[2]
            }
            self.help_page.search_login_log(search_data)

            # 获取当前登录账号和下级账号全部的userid
            all_user_id = self.help_page.get_all_user_id(current_account)
            print(all_user_id)

            '''connect = self.connect_sql.connect_tuqiang_sql()
            cursor = connect.cursor()
            get_total_sql = self.help_page_sql.search_log_in_sql(all_user_id, search_data)
            cursor.execute(get_total_sql)
            total_list = cursor.fetchall()
            cursor.close()
            connect.close()'''
            # 连接Elastic search
            es = self.connect_es.connect_es()
            # 搜索的数据
            query_data = self.help_page.get_search_log_in_log_query_data(all_user_id, search_data)
            res_01 = es.search(index='userlogin_log_2', body={'query': query_data, 'size': 20000})
            res_02 = es.search(index='userlogin_log_12', body={'query': query_data, 'size': 20000})
            res_03 = es.search(index='userlogin_log_1', body={'query': query_data, 'size': 20000})
            total = len(res_01['hits']['hits']) + len(res_02['hits']['hits']) + len(res_03['hits']['hits'])
            i += 1
            print('第%s次查询数据库的条数为：%s' % (i, total))
            web_total = self.help_page.get_current_login_log()
            print('第%s次查询页面的条数是：%s' % (i, web_total))
            if total != 0:
                total += 10
            self.assertEqual(total, web_total)

        csv_file.close()
