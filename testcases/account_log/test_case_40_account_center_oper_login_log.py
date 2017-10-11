import csv
import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from model.connect_sql import ConnectSql
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.help.help_page import HelpPage
from pages.help.help_page_sql import HelpPageSql
from pages.login.login_page import LoginPage


# 账户中心招呼栏业务日志-登录日志查询
# author:邓肖斌
class TestCase40AccountCenterOperLoginLog(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.help_page = HelpPage(self.driver, self.base_url)
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

    def test_account_center_login_log(self):
        self.base_page.open_page()
        self.log_in_base.log_in()
        self.log_in_base.click_account_center_button()
        # 获取登录账号的用户名
        current_account = self.log_in_base.get_log_in_account()

        # 点击招呼栏-业务日志
        self.help_page.click_help()
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

            connect = self.connect_sql.connect_tuqiang_sql()
            # 创建数据库游标
            cur = connect.cursor()

            # 执行sql脚本查询当前登录账号的userId,fullParent
            get_id_sql = "select o.userId from user_info o where o.account = '" + current_account + "' ;"
            cur.execute(get_id_sql)
            # 读取数据
            user_relation = cur.fetchall()
            # 遍历数据
            for row1 in user_relation:
                user_relation_id = {
                    "userId": row1[0]
                }
                get_total_sql = self.help_page_sql.search_log_in_sql(user_relation_id['userId'], search_data)
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
                i += 1
                print('第%s次查询数据库的条数为：%s' % (i, total))
                web_total = self.help_page.get_current_login_log()
                print('第%s次查询页面的条数是：%s' % (i, web_total))
                self.assertEqual(total, web_total)

            cur.close()
            connect.close()

        csv_file.close()
