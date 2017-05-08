import csv
import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.base_paging_function import BasePagingFunction
from pages.base.lon_in_base import LogInBase
from pages.command_management.command_management_page import CommandManagementPage
from pages.command_management.command_management_page_read_csv import CommandManagementPageReadCsv


class TestCase136IssuedCommandManagementSearch(unittest.TestCase):
    '''
    用例第136条，下发指令管理页面的搜索
    '''
    driver = None
    base_url = None
    base_page = None
    log_in_page = None
    command_management_page = None
    base_paging_function = None

    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.command_management_page = CommandManagementPage(self.driver, self.base_url)
        self.base_paging_function = BasePagingFunction(self.driver, self.base_url)
        self.command_management_page_read_csv = CommandManagementPageReadCsv()
        self.connect_sql = ConnectSql()
        self.log_in_base = LogInBase(self.driver, self.base_url)

        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.driver.clear_cookies()
        self.log_in_base.log_in_jimitest()
        self.current_account = self.log_in_base.get_log_in_account()

        # 登录之后点击控制台，然后点击指令管理
        self.command_management_page.click_control_after_click_command_management()
        sleep(3)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_136_issued_command_management_search(self):
        # 断言url
        expect_url_after_click_command_management = self.base_url + '/custom/toTemplate'
        self.assertEqual(expect_url_after_click_command_management,
                         self.command_management_page.actual_url_click_command_management())
        # 断言左侧列表的title文本
        expect_title_text_after_click_command_management = '指令类型'
        self.assertEqual(expect_title_text_after_click_command_management,
                         self.command_management_page.actual_title_text_after_click_command_management())

        # 点击下发指令管理
        self.command_management_page.click_lift_list('issued_command_management')
        # 断言
        expect_title_text = '下发指令管理'
        self.assertEqual(expect_title_text, self.command_management_page.actual_text_after_click_look_equipment())

        # 读csv
        csv_file = self.command_management_page_read_csv.read_csv('issued_command_management_search_data.csv')
        csv_data = csv.reader(csv_file)

        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'imei': row[0],
                'batch': row[1],
                'statue': row[2]
            }
            # 添加搜索添加搜索
            self.command_management_page.issued_command_management_search_data(search_data)

            # 连接数据库
            connect = self.connect_sql.connect_tuqiang_sql()
            # 建立游标
            cursor = connect.cursor()
            # 查询登录用户的ID 和 父ID
            get_current_user_id = "select o.userId,r.fullParent from user_relation r inner join user_organize o on r.userId = o.userId where o.account = '" + self.current_account + "';"
            # 执行
            cursor.execute(get_current_user_id)
            user = cursor.fetchall()
            for row in user:
                user_info = {
                    'id': row[0],
                    'fullparent': row[1]
                }
                # 查询当前登录用户的全部下级
                get_next_id_sql = "select userId from user_relation where fullParent like" + \
                                  "'" + user_info["fullparent"] + user_info["id"] + "%'" + ";"
                # 执行sql脚本
                cursor.execute(get_next_id_sql)
                current_account = cursor.fetchall()
                current_account_list = [user_info['id']]

                for range1 in current_account:
                    for range2 in range1:
                        current_account_list.append(range2)

                current_user_next = tuple(current_account_list)
                # 判断搜索条件
                get_sql = self.command_management_page.search_sql(current_user_next, search_data)
                # 执行sql
                print(get_sql)
                cursor.execute(get_sql)

                current_total = cursor.fetchall()
                total_list = []
                for range1 in current_total:
                    for range2 in range1:
                        total_list.append(range2)
                total = len(total_list)
                web_total = self.command_management_page.search_total_number_issued_command_management()
                self.assertEqual(total, web_total)

            cursor.close()
            connect.close()
