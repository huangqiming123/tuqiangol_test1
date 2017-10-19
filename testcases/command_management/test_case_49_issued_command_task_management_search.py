import csv
import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.base_paging_function import BasePagingFunction
from pages.base.lon_in_base import LogInBase
from pages.command_management.command_management_page import CommandManagementPage
from pages.command_management.command_management_page_read_csv import CommandManagementPageReadCsv
from pages.command_management.search_sql import SearchSql


class TestCase49IssuedCommandTaskManagementSearch(unittest.TestCase):
    """ 下发指令任务管理的搜索功能"""
    # author:邓肖斌

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
        self.search_sql = SearchSql()
        self.assert_text = AssertText()

        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.driver.clear_cookies()
        self.log_in_base.log_in()
        self.log_in_base.click_account_center_button()
        self.current_account = self.command_management_page.get_user_account_text()

        # 登录之后点击控制台，然后点击指令管理
        self.command_management_page.click_control_after_click_command_management()
        sleep(3)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_issued_command_task_management_search(self):
        # 断言url
        expect_url_after_click_command_management = self.base_url + '/custom/toTemplate'
        self.assertEqual(expect_url_after_click_command_management,
                         self.command_management_page.actual_url_click_command_management())
        # 断言左侧列表的title文本
        expect_title_text_after_click_command_management = self.assert_text.command_manager_page_command_type()
        self.assertEqual(expect_title_text_after_click_command_management,
                         self.command_management_page.actual_title_text_after_click_command_management())

        # 点击下发任务指令管理
        self.command_management_page.click_lift_list('issued_command_task_management')
        # 断言
        expect_title_text_after_click_issued_command_task_management = \
            self.assert_text.command_manager_page_issued_command_task()
        self.assertEqual(expect_title_text_after_click_issued_command_task_management,
                         self.command_management_page.actual_text_after_click_issued_command_task())

        csv_file = self.command_management_page_read_csv.read_csv('issued_command_task_management_serach_data.csv')
        csv_data = csv.reader(csv_file)

        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'batch': row[0],
                'name': row[1]
            }
            self.command_management_page.issued_command_task_add_data_to_search(search_data)

            # 建立数据库的连接
            connect = self.connect_sql.connect_tuqiang_sql()
            # 建立游标
            cursor = connect.cursor()
            # 查询登录用户的ID 和 父ID
            get_current_user_id = \
                "select o.userId,o.fullParentId from user_info o where o.account = '" + self.current_account + "';"
            # 执行
            cursor.execute(get_current_user_id)
            user = cursor.fetchall()
            for row1 in user:
                user_info = {
                    'id': row1[0],
                    'fullparent': row1[1]
                }
                # 查询当前登录用户的全部下级
                get_next_id_sql = "select userId from user_info where fullParentId like" + \
                                  "'" + user_info["fullparent"] + user_info["id"] + "%'" + ";"
                # 执行sql脚本
                cursor.execute(get_next_id_sql)
                current_account = cursor.fetchall()
                current_account_list = [user_info['id']]

                for range1 in current_account:
                    for range2 in range1:
                        current_account_list.append(range2)

                current_user_next = tuple(current_account_list)
                print(current_user_next)

                # 查询数据库
                # 执行sql
                search_sql = self.search_sql.search_issued_command_task_management_sql(current_user_next, search_data)
                print(search_sql)
                cursor.execute(search_sql)
                current_total = cursor.fetchall()
                total_list = []
                for range1 in current_total:
                    for range2 in range1:
                        total_list.append(range2)
                total = len(total_list)
                web_total = self.command_management_page.search_total_number_with_issued_command_task()
                sleep(3)
                # 断言
                self.assertEqual(total, web_total)

            cursor.close()
            connect.close()
