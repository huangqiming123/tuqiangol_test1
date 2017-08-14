import csv
import unittest

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.account_center.account_center_navi_bar_pages import AccountCenterNaviBarPages
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages
from pages.dev_manage.search_sql import SearchSql


# 设备管理-设备搜索-by imei+设备名称+设备型号+车牌号+车架号+SIM

# author:孙燕妮

class TestCase75DevManageDevComplexSearch(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePages(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPages(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.dev_manage_page_read_csv = DevManagePageReadCsv()
        self.connect_sql = ConnectSql()
        self.search_sql = SearchSql()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_dev_manage_dev_complex_search(self):
        '''测试设备管理-设备搜索-by imei+设备名称+设备型号+车牌号+车架号+SIM'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.base_page.click_chinese_button()
        # 登录
        self.log_in_base.log_in()
        self.dev_manage_page.click_account_center_button()
        current_account = self.log_in_base.get_log_in_account()

        self.dev_manage_page.enter_dev_manage()
        self.dev_manage_page.click_more_button()

        csv_file = self.dev_manage_page_read_csv.read_csv('dev_search_info.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'dev_name': row[0],
                'dev_type': row[1],
                'past_due': row[2],
                'plate_numbers': row[3],
                'frame_number': row[4],
                'sim': row[5],
                'active': row[6],
                'choose_time': row[7],
                'begin_time': row[8],
                'end_time': row[9],
                'next': row[10],
                'band_status': row[11],
                'dev_mold': row[12],
                'dev_group': row[13],
                'sn': row[14]
            }
            self.dev_manage_page.add_data_to_search_dev(search_data)
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
                cur.execute(get_lower_account_sql)
                # 读取数据
                lower_account = cur.fetchall()
                lower_account_list = [user_relation_id["userId"]]
                for range1 in lower_account:
                    for range2 in range1:
                        lower_account_list.append(range2)
                lower_account_tuple = tuple(lower_account_list)
                get_total_sql = self.search_sql.search_dev_sql(user_relation_id['userId'], lower_account_tuple,
                                                               search_data)
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
                web_total = self.dev_manage_page.get_dev_number()
                print('本次查询页面的条数是：%s' % web_total)
                self.assertEqual(total, web_total)

            cur.close()
            connect.close()
        csv_file.close()
