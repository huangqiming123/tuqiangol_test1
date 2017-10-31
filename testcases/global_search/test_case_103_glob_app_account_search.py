import csv
import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.account_center.account_center_navi_bar_pages import AccountCenterNaviBarPages
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.global_search.global_account_search_page import GlobalAccountSearchPage
from pages.global_search.global_dev_search_page import GlobalDevSearchPage
from pages.global_search.global_search_page_read_csv import GlobleSearchPageReadCsv
from pages.global_search.search_sql import SearchSql


class TestCase103GlobAppAccountSearch(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.global_dev_search_page = GlobalDevSearchPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.global_account_search_page = GlobalAccountSearchPage(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.global_search_page_read_csv = GlobleSearchPageReadCsv()
        self.search_sql = SearchSql()
        self.driver.wait(1)
        self.connect_sql = ConnectSql()
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_global_app_account_search(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.log_in_base.log_in_jimitest()
        self.log_in_base.click_account_center_button()
        self.log_in_base.click_account_center_button()
        current_account = self.log_in_base.get_log_in_account()
        self.global_dev_search_page.click_easy_search()
        # 关闭
        self.global_dev_search_page.close_search()
        sleep(2)

        self.global_dev_search_page.click_easy_search()
        self.global_dev_search_page.click_app_account_search()

        # 度数据
        csv_file = self.global_search_page_read_csv.read_csv('global_search_app_account_data.csv')
        csv_data = csv.reader(csv_file)

        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'account_info': row[0]
            }
            self.global_dev_search_page.swith_to_search_frame()
            self.global_dev_search_page.app_account_easy_search(search_data)

            connect = self.connect_sql.connect_tuqiang_sql()
            # 创建数据库游标
            cur = connect.cursor()

            # 执行sql脚本查询当前登录账号的userId,fullParent
            get_id_sql = "select o.account,o.userId,o.fullParentId from user_info o where o.account = '" + current_account + "' ;"
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
                print(get_lower_account_sql)
                cur.execute(get_lower_account_sql)
                # 读取数据
                lower_account = cur.fetchall()
                lower_account_list = [user_relation_id["userId"]]
                for range1 in lower_account:
                    for range2 in range1:
                        lower_account_list.append(range2)
                set_list = list(set(lower_account_list))
                lower_account_tuple = tuple(set_list)

                # 搜索下级用户绑定的所有app用户
                get_app_account_sql = "SELECT m.bindUserId FROM equipment_mostly m WHERE m.userId in %s and m.bindUserId is not NULL " % str(
                    lower_account_tuple)
                print(get_app_account_sql)
                cur.execute(get_app_account_sql)
                # 读取数据
                lower_app_account = cur.fetchall()
                lower_app_account_list = []
                for range1 in lower_app_account:
                    for range2 in range1:
                        lower_app_account_list.append(range2)
                set_lists = list(set(lower_app_account_list))
                lower_app_account_tuple = tuple(set_lists)

                get_total_sql = self.search_sql.search_account_sql(lower_app_account_tuple, search_data)
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
                web_total = self.global_account_search_page.app_easy_search_results()
                print('本次查询页面的条数是：%s' % web_total)
                self.assertEqual(total, web_total)
                self.driver.default_frame()
            cur.close()
            connect.close()

        csv_file.close()
        self.global_dev_search_page.close_search()
