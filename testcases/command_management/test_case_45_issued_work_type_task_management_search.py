import csv
import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.command_management.command_management_page import CommandManagementPage
from pages.command_management.command_management_page_read_csv import CommandManagementPageReadCsv
from pages.command_management.search_sql import SearchSql


class TestCase45IssuedWorkTypetTaskManagementSearch(unittest.TestCase):
    """ 发工作模式任务管理搜索功能 """
    # author:邓肖斌
    driver = None
    base_url = None
    base_page = None
    log_in_page = None
    command_management_page = None

    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver(choose='firefox')
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.command_management_page = CommandManagementPage(self.driver, self.base_url)
        self.command_management_page_read_csv = CommandManagementPageReadCsv()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.connect_sql = ConnectSql()
        self.assert_text = AssertText()
        self.search_sql = SearchSql()

        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.driver.clear_cookies()
        self.log_in_base.log_in()
        self.log_in_base.click_account_center_button()
        self.current_account = self.log_in_base.get_log_in_account()

        # 登录之后点击控制台，然后点击指令管理
        self.command_management_page.click_control_after_click_command_management()
        sleep(3)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_issued_work_type_task_management_search(self):
        # 断言url
        expect_url_after_click_command_management = self.base_url + '/custom/toTemplate'
        self.assertEqual(expect_url_after_click_command_management,
                         self.command_management_page.actual_url_click_command_management())
        # 断言左侧列表的title文本
        expect_title_text_after_click_command_management = self.assert_text.command_manager_page_command_type()
        self.assertEqual(expect_title_text_after_click_command_management,
                         self.command_management_page.actual_title_text_after_click_command_management())

        # 点击工作模式模板管理
        self.command_management_page.click_lift_list('issued_work_type_task_management')
        # 断言
        expect_title_text_after_click_issued_work_type_task_mangagement = \
            self.assert_text.command_manager_page_work_type_task_manager_text()
        self.assertEqual(expect_title_text_after_click_issued_work_type_task_mangagement,
                         self.command_management_page.actual_title_text_click_issued_work_type_task_management())

        csv_file = self.command_management_page_read_csv.read_csv('search_work_type_task_manage_data.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'number': row[0],
                'name': row[1]
            }
            self.command_management_page.issued_work_type_task_management_search(search_data['number'],
                                                                                 search_data['name'])
            # 创建连接
            connect = self.connect_sql.connect_tuqiang_sql()
            # 创建游标
            cursor = connect.cursor()
            # 获取当前登录账号的usedID
            get_current_user_id_sql = \
                "select o.account,o.userId from user_info o where o.account = '" + self.current_account + "';"
            cursor.execute(get_current_user_id_sql)

            user_relation = cursor.fetchall()
            for row1 in user_relation:
                user_id = {
                    'user_account': row1[0],
                    'user_id': row1[1]
                }
                get_total_sql = self.search_sql.search_work_task_manager_sql(user_id['user_id'], search_data)
                print(get_total_sql)
                cursor.execute(get_total_sql)
                # 读取数据
                total_data = cursor.fetchall()
                # 从数据tuple中获取最终查询记录统计条数
                total_list = []
                for range1 in total_data:
                    for range2 in range1:
                        total_list.append(range2)
                print(total_list)
                total = len(total_list)
                print('本次查询数据库的条数为：%s' % total)
                web_total = self.command_management_page.search_total_number_work_task_manage()
                print('本次查询页面的条数是：%s' % web_total)
                self.assertEqual(total, web_total)
            cursor.close()
            connect.close()
        csv_file.close()


if __name__ == "__main__":
    unittest.main()
