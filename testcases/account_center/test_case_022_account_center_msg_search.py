import csv
import unittest

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.account_center.account_center_msg_center_page import AccountCenterMsgCenterPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_operation_log_page import AccountCenterOperationLogPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.search_sql import SearchSql
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.login.login_page import LoginPage


# 账户中心-消息中心-根据搜索条件来搜索消息
# author:孙燕妮

class TestCase022AccountCenterMsgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_operation_log = AccountCenterOperationLogPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_msg_center = AccountCenterMsgCenterPage(self.driver, self.base_url)
        self.assert_text = AssertText()
        self.driver.set_window_max()
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.connect_sql = ConnectSql()
        self.search_sql = SearchSql()
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_msg_search(self):
        self.base_page.open_page()
        self.log_in_base.log_in()
        self.account_center_page_navi_bar.click_account_center_button()

        self.driver.switch_to_frame('x,//*[@id="usercenterFrame"]')
        # 获取登录账号的用户名
        current_account = self.log_in_base.get_log_in_account()
        self.driver.default_frame()

        # 进入消息中心
        self.account_center_page_msg_center.enter_msg_center()
        self.driver.wait(5)

        # 进入iframe
        self.account_center_page_msg_center.message_center_iframe()
        # 获取消息中心title
        msg_center_title = self.account_center_page_msg_center.get_msg_center_title()
        # 验证消息中心title是否正确显示
        self.assertIn(self.assert_text.account_center_page_message_center_text(), msg_center_title, "消息中心title有误!")

        csv_file = self.account_center_page_read_csv.read_csv('search_massage_data.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'imei': row[0],
                'type': row[1],
                'status': row[2]
            }
            self.account_center_page_operation_log.add_data_to_search_massages(search_data)
            connect1 = self.connect_sql.connect_tuqiang_sql()
            # 创建数据库游标
            cur = connect1.cursor()
            # 执行sql脚本查询当前登录账号的userId,fullParent
            get_id_sql = "select o.account,o.userId,o.fullParentId from user_info o where o.account = '" + current_account + "';"
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
                get_lower_account_sql = "select userId from user_info where fullParentId like" + \
                                        "'" + user_relation_id["fullParent"] + user_relation_id["userId"] + "%'" + ";"
                cur.execute(get_lower_account_sql)
                # 读取数据
                lower_account = cur.fetchall()
                lower_account_list = [user_relation_id["userId"]]
                for range1 in lower_account:
                    for range2 in range1:
                        lower_account_list.append(range2)
                self.lower_account_tuple = tuple(lower_account_list)
            cur.close()
            connect1.close()

            connect = self.connect_sql.connect_tuqiang_sql()
            # 创建数据库游标
            cur = connect.cursor()
            get_total_sql = self.search_sql.search_massage_sql(self.lower_account_tuple, search_data)
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
            web_total = self.account_center_page_operation_log.get_msg_number()
            print('本次查询页面的条数是：%s' % web_total)
            self.assertEqual(total, web_total)
            cur.close()
            connect.close()
        csv_file.close()
