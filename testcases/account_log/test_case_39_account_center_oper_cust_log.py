import csv
import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from model.connect_sql import ConnectSql
from pages.account_center.account_center_operation_log_page import AccountCenterOperationLogPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.help.help_page import HelpPage
from pages.help.help_page_sql import HelpPageSql
from pages.login.login_page import LoginPage


class TestCase39AccountCenterOperCustLog(unittest.TestCase):
    """ 帮助--业务日志 """

    # author:邓肖斌
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
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_oper_cust_log(self):
        self.base_page.open_page()
        self.log_in_base.log_in()
        self.log_in_base.click_account_center_button()
        # 获取登录账号的用户名
        current_account = self.log_in_base.get_log_in_account()

        # 点击招呼栏-业务日志
        self.account_center_page_operation_log.click_help_button()
        self.help_page.click_business_log()
        # 判断当前页面是否正确跳转至业务日志页面
        expect_url = self.base_url + "/userFeedback/toHelp"
        self.assertEqual(expect_url, self.driver.get_current_url(), "当前页面跳转错误")

        i = 0

        csv_file = self.account_center_page_read_csv.read_csv('search_cus_manager_log_data.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'search_type': row[0],
                'begin_time': row[1],
                'end_time': row[2],
                'more': row[3]
            }
            self.help_page.search_business_log(search_data)

            connect = self.connect_sql.connect_tuqiang_sql()
            # 创建数据库游标
            cur = connect.cursor()

            # 执行sql脚本查询当前登录账号的userId,fullParent
            get_id_sql = \
                "select o.account,o.userId,o.fullParentId from user_info o where o.account = " \
                "'" + current_account + "' ;"
            cur.execute(get_id_sql)
            # 读取数据
            user_relation = cur.fetchall()
            # 遍历数据
            for row1 in user_relation:
                user_relation_id = {
                    "account": row1[0],
                    "userId": row1[1],
                    "fullParent": row1[2]
                }

                # 执行sql脚本，根据当前登录账号的userId,fullParent查询出当前账户的所有下级账户
                get_lower_account_sql = "select userId from user_info where fullParentId like" + \
                                        "'" + user_relation_id["fullParent"] + user_relation_id["userId"] + "%'" + ";"
                cur.execute(get_lower_account_sql)
                # 读取数据
                lower_account = cur.fetchall()
                lower_account_list = [user_relation_id["userId"]]
                for range1 in lower_account:
                    for range2 in range1:
                        lower_account_list.append(range2)
                lower_account_tuple = tuple(lower_account_list)
                get_total_sql = self.help_page_sql.business_log_sql(lower_account_tuple, search_data)
                print(get_total_sql)
                cur.execute(get_total_sql)
                # 读取数据
                total_data = cur.fetchall()
                # 从数据tuple中获取最终查询记录统计条数
                total_list = []
                for range3 in total_data:
                    for range4 in range3:
                        total_list.append(range4)
                total = len(total_list)
                i += 1
                print('第%s次查询数据库的条数为：%s' % (i, total))
                web_total = self.help_page.get_current_customer_log()
                print('第%s次查询页面的条数是：%s' % (i, web_total))
                self.assertEqual(total, web_total)

            cur.close()
            connect.close()

        csv_file.close()
