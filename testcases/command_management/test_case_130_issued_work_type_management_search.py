import csv
import unittest
from time import sleep

import pymysql

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.command_management.command_management_page import CommandManagementPage
from pages.command_management.command_management_page_read_csv import CommandManagementPageReadCsv
from pages.login.login_page import LoginPage


class TestCase130IssuedWorkTypeManagementSearch(unittest.TestCase):
    '''
    用例第130条，下发工作模式管理页面搜索
    author：zhangAo
    '''
    driver = None
    base_url = None
    base_page = None
    log_in_page = None
    command_management_page = None

    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.log_in_page = LoginPage(self.driver, self.base_url)
        self.command_management_page = CommandManagementPage(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.command_management_page_read_csv = CommandManagementPageReadCsv()
        self.connect_sql = ConnectSql()

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

    def test_case_130_issued_work_type_management_search(self):
        # 断言url
        expect_url_after_click_command_management = self.base_url + '/custom/toTemplate'
        self.assertEqual(expect_url_after_click_command_management,
                         self.command_management_page.actual_url_click_command_management())
        # 断言左侧列表的title文本
        expect_title_text_after_click_command_management = '指令类型'
        self.assertEqual(expect_title_text_after_click_command_management,
                         self.command_management_page.actual_title_text_after_click_command_management())
        # 点击下发工作模式管理
        self.command_management_page.click_lift_list('issued_work_type_management')
        # 断言
        expect_title_text_click_issued_work_type = '下发工作模式'
        self.assertEqual(expect_title_text_click_issued_work_type,
                         self.command_management_page.actual_text_click_look_equipment())

        # 读取数据
        csv_file = self.command_management_page_read_csv.read_csv('issused_work_template.csv')
        csv_data = csv.reader(csv_file)

        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'batch': row[0],
                'execute_state': row[1],
                'state': row[2],
                'imei': row[3]
            }

            # 传入数据
            self.command_management_page.add_data_to_search(search_data)

            # 创建数据库连接
            connect = self.connect_sql.connect_tuqiang_sql()
            # 创建游标
            cursor = connect.cursor()
            # 获取登录账号的ID
            get_current_user_id_sql = "select o.account,o.userId from user_organize o where o.account = '" + self.current_account + "';"
            cursor.execute(get_current_user_id_sql)
            user_relation = cursor.fetchall()
            for row in user_relation:
                user_id = {
                    'user_account': row[0],
                    'user_id': row[1]
                }

                # 查询数据库有多少条记录
                # 判断查询的条件
                if search_data['batch'] != '' and search_data['state'] == '' and search_data['imei'] == '' and \
                                search_data['execute_state'] == '':
                    self.get_total_count_sql = "select c.id from command_issued_stage c where c.createdBy = " + \
                                               user_id[
                                                   'user_id'] + " and c.issuedTemplateId= " + search_data['batch'] + ";"

                elif search_data['batch'] == '' and search_data['state'] == '' and search_data['imei'] == '' and \
                                search_data['execute_state'] != '':
                    self.get_total_count_sql = "select c.id from command_issued_stage c where c.createdBy = " + \
                                               user_id[
                                                   'user_id'] + " and c.exectueState= " + search_data[
                                                   'execute_state'] + ";"

                elif search_data['batch'] == '' and search_data['state'] == '1' and search_data['imei'] == '' and \
                                search_data['execute_state'] == '':
                    self.get_total_count_sql = "select c.id from command_issued_stage c where c.createdBy = " + \
                                               user_id[
                                                   'user_id'] + " and DATEDIFF(c.endTime,CURDATE())<0;"
                elif search_data['batch'] == '' and search_data['state'] == '2' and search_data['imei'] == '' and \
                                search_data['execute_state'] == '':
                    self.get_total_count_sql = "select c.id from command_issued_stage c where c.createdBy = " + \
                                               user_id[
                                                   'user_id'] + " AND DATEDIFF(c.endTime,CURDATE()) < 7 AND DATEDIFF(c.endTime,CURDATE()) >= 0;"

                elif search_data['batch'] == '' and search_data['state'] == '' and search_data['imei'] != '' and \
                                search_data['execute_state'] == '':
                    self.get_total_count_sql = "select c.id from command_issued_stage c where c.createdBy = " + \
                                               user_id[
                                                   'user_id'] + " and c.imei= " + search_data['imei'] + ";"

                elif search_data['batch'] == '' and search_data['state'] == '1' and search_data['imei'] != '' and \
                                search_data['execute_state'] == '':
                    self.get_total_count_sql = "select c.id from command_issued_stage c where c.createdBy = " + \
                                               user_id[
                                                   'user_id'] + " and DATEDIFF(c.endTime,CURDATE())<0 and c.imei= " + \
                                               search_data[
                                                   'imei'] + ";"
                elif search_data['batch'] == '' and search_data['state'] == '2' and search_data['imei'] != '' and \
                                search_data['execute_state'] == '':
                    self.get_total_count_sql = "select c.id from command_issued_stage c where c.createdBy = " + \
                                               user_id[
                                                   'user_id'] + " AND DATEDIFF(c.endTime,CURDATE()) < 7 AND DATEDIFF(c.endTime,CURDATE()) >= 0 and c.imei= " + \
                                               search_data[
                                                   'imei'] + ";"

                elif search_data['batch'] == '' and search_data['state'] == '' and search_data['imei'] != '' and \
                                search_data['execute_state'] != '':
                    self.get_total_count_sql = "select c.id from command_issued_stage c where c.createdBy = " + \
                                               user_id[
                                                   'user_id'] + " and c.exectueState=" + search_data[
                                                   'execute_state'] + " and c.imei= " + \
                                               search_data[
                                                   'imei'] + ";"

                elif search_data['batch'] == '' and search_data['state'] == '1' and search_data['imei'] == '' and \
                                search_data['execute_state'] != '':
                    self.get_total_count_sql = "select c.id from command_issued_stage c where c.createdBy = " + \
                                               user_id[
                                                   'user_id'] + " and c.exectueState=" + search_data[
                                                   'execute_state'] + " and DATEDIFF(c.endTime,CURDATE())<0;"
                elif search_data['batch'] == '' and search_data['state'] == '2' and search_data['imei'] == '' and \
                                search_data['execute_state'] != '':
                    self.get_total_count_sql = "select c.id from command_issued_stage c where c.createdBy = " + \
                                               user_id[
                                                   'user_id'] + " and c.exectueState=" + search_data[
                                                   'execute_state'] + " AND DATEDIFF(c.endTime,CURDATE()) < 7 AND DATEDIFF(c.endTime,CURDATE()) >= 0;"

                elif search_data['batch'] != '' and search_data['state'] == '' and search_data['imei'] != '' and \
                                search_data['execute_state'] == '':
                    self.get_total_count_sql = "select c.id from command_issued_stage c where c.createdBy = " + \
                                               user_id[
                                                   'user_id'] + " and c.issuedTemplateId=" + search_data[
                                                   'batch'] + " and c.imei= " + search_data[
                                                   'imei'] + ";"

                elif search_data['batch'] != '' and search_data['state'] == '1' and search_data['imei'] == '' and \
                                search_data['execute_state'] == '':
                    self.get_total_count_sql = "select c.id from command_issued_stage c where c.createdBy = " + \
                                               user_id[
                                                   'user_id'] + " and c.issuedTemplateId=" + search_data[
                                                   'batch'] + " and DATEDIFF(c.endTime,CURDATE()) < 0;"
                elif search_data['batch'] != '' and search_data['state'] == '2' and search_data['imei'] == '' and \
                                search_data['execute_state'] == '':
                    self.get_total_count_sql = "select c.id from command_issued_stage c where c.createdBy = " + \
                                               user_id[
                                                   'user_id'] + " and c.issuedTemplateId=" + search_data[
                                                   'batch'] + " AND DATEDIFF(c.endTime,CURDATE()) < 7 AND DATEDIFF(c.endTime,CURDATE()) >= 0;"

                elif search_data['batch'] != '' and search_data['state'] == '' and search_data['imei'] == '' and \
                                search_data['execute_state'] != '':
                    self.get_total_count_sql = "select c.id from command_issued_stage c where c.createdBy =" + \
                                               user_id['user_id'] + " and c.issuedTemplateId=" + search_data[
                                                   'batch'] + " and c.exectueState=" + search_data[
                                                   'execute_state'] + ";"

                elif search_data['batch'] == '' and search_data['state'] == '1' and search_data['imei'] != '' and \
                                search_data['execute_state'] != '':
                    self.get_total_count_sql = "select c.id from command_issued_stage c where c.createdBy = " + \
                                               user_id[
                                                   'user_id'] + " and c.exectueState=" + search_data[
                                                   'execute_state'] + " and DATEDIFF(c.endTime,CURDATE())<0 and c.imei=" + \
                                               search_data['imei'] + ";"
                elif search_data['batch'] == '' and search_data['state'] == '2' and search_data['imei'] != '' and \
                                search_data['execute_state'] != '':
                    self.get_total_count_sql = "select c.id from command_issued_stage c where c.createdBy = " + \
                                               user_id[
                                                   'user_id'] + " and c.exectueState=" + search_data[
                                                   'execute_state'] + " AND DATEDIFF(c.endTime,CURDATE()) < 7 AND DATEDIFF(c.endTime,CURDATE()) >= 0 and c.imei=" + \
                                               search_data['imei'] + ";"

                elif search_data['batch'] != '' and search_data['state'] == '' and search_data['imei'] != '' and \
                                search_data['execute_state'] != '':
                    self.get_total_count_sql = "select c.id from command_issued_stage c where c.createdBy = " + \
                                               user_id[
                                                   'user_id'] + " and c.exectueState=" + search_data[
                                                   'execute_state'] + " and c.issuedTemplateId= " + \
                                               search_data['batch'] + " and c.imei=" + search_data['imei'] + ";"

                elif search_data['batch'] != '' and search_data['state'] == '1' and search_data['imei'] == '' and \
                                search_data['execute_state'] != '':
                    self.get_total_count_sql = "select c.id from command_issued_stage c where c.createdBy = " + \
                                               user_id[
                                                   'user_id'] + " and c.exectueState=" + search_data[
                                                   'execute_state'] + " and c.issuedTemplateId= " + \
                                               search_data['batch'] + " and DATEDIFF(c.endTime,CURDATE())<0;"
                elif search_data['batch'] != '' and search_data['state'] == '2' and search_data['imei'] == '' and \
                                search_data['execute_state'] != '':
                    self.get_total_count_sql = "select c.id from command_issued_stage c where c.createdBy = " + \
                                               user_id[
                                                   'user_id'] + " and c.exectueState=" + search_data[
                                                   'execute_state'] + " and c.issuedTemplateId= " + \
                                               search_data[
                                                   'batch'] + " AND DATEDIFF(c.endTime,CURDATE()) < 7 AND DATEDIFF(c.endTime,CURDATE()) >= 0;"

                elif search_data['batch'] != '' and search_data['state'] == '1' and search_data['imei'] != '' and \
                                search_data['execute_state'] == '':
                    self.get_total_count_sql = "select c.id from command_issued_stage c where c.createdBy = " + \
                                               user_id[
                                                   'user_id'] + " and c.imei=" + search_data[
                                                   'imei'] + " and c.issuedTemplateId= " + \
                                               search_data['batch'] + " and DATEDIFF(c.endTime,CURDATE())<0;"

                elif search_data['batch'] != '' and search_data['state'] == '2' and search_data['imei'] != '' and \
                                search_data['execute_state'] == '':
                    self.get_total_count_sql = "select c.id from command_issued_stage c where c.createdBy = " + \
                                               user_id[
                                                   'user_id'] + " and c.imei=" + search_data[
                                                   'imei'] + " and c.issuedTemplateId= " + \
                                               search_data[
                                                   'batch'] + " AND DATEDIFF(c.endTime,CURDATE()) < 7 AND DATEDIFF(c.endTime,CURDATE()) >= 0;"
                else:
                    self.get_total_count_sql = "select c.id from command_issued_stage c where c.createdBy = " + \
                                               user_id[
                                                   'user_id'] + " and c.imei=" + search_data[
                                                   'imei'] + " and c.issuedTemplateId= " + \
                                               search_data['batch'] + " and c.exectueState=" + search_data[
                                                   'execute_state'] + " and DATEDIFF(c.endTime,CURDATE())<0;"
                cursor.execute(self.get_total_count_sql)
                current_total = cursor.fetchall()
                total_list = []
                for range1 in current_total:
                    for range2 in range1:
                        total_list.append(range2)
                total = len(total_list)
                web_total = self.command_management_page.search_total_number_issued_work_type()
                self.assertEqual(total, web_total)

            cursor.close()
            connect.close()
