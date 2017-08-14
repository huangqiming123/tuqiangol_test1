import csv
import unittest

from automate_driver.automate_driver_server import AutomateDriverServer
from model.connect_sql import ConnectSql
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_operation_log_page import AccountCenterOperationLogPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.search_sql import SearchSql
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer


# 账户中心招呼栏业务日志-设备管理日志查询

class TestCase38AccountCenterOperDeviceLog(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.account_center_page_operation_log = AccountCenterOperationLogPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.connect_sql = ConnectSql()
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.search_sql = SearchSql()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_oper_device_log(self):
        self.base_page.open_page()
        self.log_in_base.log_in()
        self.log_in_base.click_account_center_button()
        # 获取登录账号的用户名
        current_account = self.log_in_base.get_log_in_account()

        # 点击招呼栏-业务日志
        self.account_center_page_operation_log.click_help_button()
        self.account_center_page_operation_log.click_business_log()
        # 判断当前页面是否正确跳转至业务日志页面
        expect_url = self.base_url + "/userFeedback/toHelp"
        self.assertEqual(expect_url, self.driver.get_current_url(), "当前页面跳转错误")
        i = 0

        csv_file = self.account_center_page_read_csv.read_csv('search_equipment_manager_log_data.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'type': row[0],
                'begin_time': row[1],
                'end_time': row[2],
                'more': row[3]
            }
            self.account_center_page_operation_log.add_data_to_search_equipment_manager_log(search_data)

            connect = self.connect_sql.connect_tuqiang_sql()
            # 创建数据库游标
            cur = connect.cursor()

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
                lower_account_tuple = tuple(lower_account_list)

                get_total_sql = self.search_sql.search_equipment_manager_sql(lower_account_tuple, search_data)
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
                b = i + 1
                print('第%s次查询数据库的条数为：%s' % (b, total))
                web_total = self.account_center_page_operation_log.count_curr_busi_log_num()
                print('第%s次查询页面的条数是：%s' % (b, web_total))
                self.assertEqual(total, web_total)

            cur.close()
            connect.close()

        csv_file.close()