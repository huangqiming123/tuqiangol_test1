import csv
import unittest
from time import sleep

import pymysql

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.alarm_info.alarm_info_page import AlarmInfoPage
from pages.base.base_page import BasePage
from pages.base.base_paging_function import BasePagingFunction
from pages.base.lon_in_base import LogInBase
from pages.command_management.command_management_page import CommandManagementPage
from pages.login.login_page import LoginPage
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv


class TestCase140AlarmDetailSearch(unittest.TestCase):
    '''
    用例第140条，告警详情页面搜索
    author:zhangAo
    '''

    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.log_in_page = LoginPage(self.driver, self.base_url)
        self.command_management_page = CommandManagementPage(self.driver, self.base_url)
        self.base_paging_function = BasePagingFunction(self.driver, self.base_url)
        self.alarm_info_page = AlarmInfoPage(self.driver, self.base_url)
        self.statistical_form_page_read_csv = StatisticalFormPageReadCsv()
        self.log_in_base = LogInBase(self.driver,self.base_url)
        self.statistical_form_page = StatisticalFormPage(self.driver, self.base_url)
        self.connect_sql = ConnectSql()

        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.driver.clear_cookies()
        self.log_in_base.log_in_jimitest()
        # 登录之后点击控制台，然后点击指令管理
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        sleep(3)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_140_alarm_detail_search(self):
        # 断言url
        expect_url = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url, self.alarm_info_page.actual_url_click_alarm())
        # 点击告警详情
        self.alarm_info_page.click_alarm_detail_list()
        # 断言
        self.driver.switch_to_frame('x,//*[@id="alarmDdetailsFrame"]')
        self.assertEqual('告警详情', self.alarm_info_page.actual_text_after_click_alarm_detail())
        self.driver.default_frame()
        sleep(3)
        # 读数据
        csv_file = self.statistical_form_page_read_csv.read_csv('alarm_detail_search_data.csv')
        csv_data = csv.reader(csv_file)

        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            data = {
                'user_name': row[0],
                'type': row[1],
                'status': row[2],
                'alarm_begin_time': row[3],
                'alarm_end_time': row[4],
                'push_begin_time': row[5],
                'push_end_time': row[6],
                'next_user': row[7]
            }
            self.alarm_info_page.add_data_to_search_alarm_detail(data)
            self.driver.switch_to_frame('x,//*[@id="alarmDdetailsFrame"]')

            # 连接数据库
            connect = self.connect_sql.connect_tuqiang_sql()
            # 创建游标
            cursor = connect.cursor()
            # 查询搜索用户的uesrID
            get_user_id_sql = "SELECT user_organize.userId FROM user_organize WHERE user_organize.account ='" + data[
                'user_name'] + "';"
            # 执行sql
            cursor.execute(get_user_id_sql)
            get_user_id = cursor.fetchall()
            user_id = get_user_id[0][0]

            # 当前用户下设置
            get_current_user_all_equipment = "SELECT a.imei FROM assets_device AS a WHERE a.userId = " + user_id + " and a.expiration > CURDATE();"
            cursor.execute(get_current_user_all_equipment)
            all_equipment = cursor.fetchall()

            all_equipment_list = []
            for range1 in all_equipment:
                for range2 in range1:
                    all_equipment_list.append(range2)

            current_user_all_equipment = tuple(all_equipment_list)

            cursor.close()
            connect.close()

            # 连接另一个数据库
            connect_02 = self.connect_sql.connect_tuqiang_form()
            # 创建游标
            cursor_02 = connect_02.cursor()
            '''# 判断查询条件
            if data['alarm_begin_time'] != '' and data['alarm_end_time'] != '' and data['push_begin_time'] != '' and \
                                data['push_end_time'] != '' and data['next_user'] == '1':
                    # 条件1，告警时间和定位时间都不为空，且勾选包含下级
                self.get_total_sql = "SELECT count(*) FROM alarm_info AS a WHERE a.CREATETIME BETWEEN '" + self.alarm_info.get_alarm_first_time() + "' AND '" + self.alarm_info.get_alarm_second_time() + "' AND a.PUSHTIME BETWEEN '" + self.alarm_info.get_push_first_time() + "' AND '" + self.alarm_info.get_push_second_time() + "' AND a.USER_ID IN " + str(
                        current_user_next) + " and a.imei in " + str(all_next_user_epuipment) + ";"

            elif data['alarm_begin_time'] != '' and data['alarm_end_time'] != '' and data[
                    'push_begin_time'] != '' and \
                                data['push_end_time'] != '' and data['next_user'] == '0':
                    # 条件2，告警时间和定位时间都不为空，不勾选包含下级
                self.get_total_sql = "SELECT count(*) FROM alarm_info AS a WHERE a.CREATETIME BETWEEN " + self.alarm_info.get_alarm_first_time() + " AND " + self.alarm_info.get_alarm_second_time() + " AND a.PUSHTIME BETWEEN " + self.alarm_info.get_push_first_time() + " AND " + self.alarm_info.get_push_second_time() + " AND a.USER_ID = " + user_id + " and a.imei in " + str(
                        current_user_all_equipment) + ";"

            elif data['alarm_begin_time'] != '' and data['alarm_end_time'] != '' and data[
                    'push_begin_time'] == '' and \
                                data['push_end_time'] == '' and data['next_user'] == '1':
                    # 条件3，告警时间不为空，定位时间为空，且勾选包含下级
                self.get_total_sql = "SELECT count(*) FROM alarm_info AS a WHERE a.CREATETIME BETWEEN " + self.alarm_info.get_alarm_first_time() + " AND " + self.alarm_info.get_alarm_second_time() + " AND a.USER_ID IN " + str(
                        current_user_next) + " and a.imei in " + str(all_next_user_epuipment) + ";"

            elif data['alarm_begin_time'] != '' and data['alarm_end_time'] != '' and data[
                    'push_begin_time'] == '' and \
                                data['push_end_time'] == '' and data['next_user'] == '0':
                    # 条件4，告警时间不为空、定位时间为空，且不勾选包含下级
                self.get_total_sql = "SELECT count(*) FROM alarm_info AS a WHERE a.CREATETIME BETWEEN " + self.alarm_info.get_alarm_first_time() + " AND " + self.alarm_info.get_alarm_second_time() + " AND a.USER_ID = " + user_id + " and a.imei in " + str(
                        current_user_all_equipment) + ";"

            elif data['alarm_begin_time'] == '' and data['alarm_end_time'] == '' and data[
                    'push_begin_time'] != '' and \
                                data['push_end_time'] != '' and data['next_user'] == '1':
                    # 条件5，告警时间为空、定位时间不为空，且勾选包含下级
                self.get_total_sql = "SELECT count(*) FROM alarm_info AS a WHERE a.PUSHTIME BETWEEN " + self.alarm_info.get_push_first_time() + " AND " + self.alarm_info.get_push_second_time() + " AND a.USER_ID IN " + str(
                        current_user_next) + " and a.imei in " + str(all_next_user_epuipment) + ";"

            elif data['alarm_begin_time'] == '' and data['alarm_end_time'] == '' and data[
                    'push_begin_time'] != '' and \
                                data['push_end_time'] != '' and data['next_user'] == '0':
                    # 条件6，告警时间为空、定位时间为不空，且不勾选包含下级
                self.get_total_sql = "SELECT count(*) FROM alarm_info AS a WHERE a.PUSHTIME BETWEEN " + self.alarm_info.get_push_first_time() + " AND " + self.alarm_info.get_push_second_time() + " AND a.USER_ID = " + user_id + " and a.imei in " + str(
                        current_user_all_equipment) + ";"

            elif data['alarm_begin_time'] == '' and data['alarm_end_time'] == '' and data[
                    'push_begin_time'] == '' and \
                                data['push_end_time'] == '' and data['next_user'] == '1':
                    # 条件7，告警时间为空、定位时间为空，且勾选包含下级
                self.get_total_sql = "SELECT count(*) FROM alarm_info AS a WHERE a.USER_ID IN " + str(current_user_next) + " and a.imei in " + str(all_next_user_epuipment) + ";"


            elif data['alarm_begin_time'] == '' and data['alarm_end_time'] == '' and data[
                    'push_begin_time'] == '' and \
                                data['push_end_time'] == '' and data['next_user'] == '0':
                    # 条件8，告警时间为空、定位时间为空，且不勾选包含下级
                self.get_total_sql = "SELECT count(*) FROM alarm_info AS a WHERE a.USER_ID = " + user_id + " and a.imei in " + str(
                        current_user_all_equipment) + ";"'''
            # 判断查询条件
            if data['alarm_begin_time'] != '' and data['alarm_end_time'] != '' and data['push_begin_time'] != '' and \
                            data['push_end_time'] != '' and data['next_user'] == '0':
                # 条件1，告警时间不为空，定位时间不为空，不包含下级用户
                self.get_total_sql = "SELECT a.imei FROM alarm_info_user AS a WHERE a.CREATETIME BETWEEN '" + self.alarm_info_page.get_alarm_first_time() + "' AND '" + self.alarm_info_page.get_alarm_second_time() + "' AND a.PUSHTIME BETWEEN '" + self.alarm_info_page.get_push_first_time() + "' AND '" + self.alarm_info_page.get_push_second_time() + "' and a.imei in " + str(
                    current_user_all_equipment) + " and a.USER_ID = " + user_id + ";"

            elif data['alarm_begin_time'] == '' and data['alarm_end_time'] == '' and data['push_begin_time'] == '' and \
                            data['push_end_time'] == '' and data['next_user'] == '0':
                #条件2，告警时间为空，定位时间为空，不包含下级用户
                self.get_total_sql = "SELECT a.imei FROM alarm_info_user AS a WHERE a.imei in " + str(
                    current_user_all_equipment) + " and a.USER_ID=" + user_id + ";"

            elif data['alarm_begin_time'] != '' and data['alarm_end_time'] != '' and data['push_begin_time'] == '' and \
                            data['push_end_time'] == '' and data['next_user'] == '0':
                #条件3，告警时间不为空，定位时间为空，不包含下级用户
                self.get_total_sql = "SELECT a.imei FROM alarm_info_user AS a WHERE a.CREATETIME BETWEEN '" + self.alarm_info_page.get_alarm_first_time() + "' AND '" + self.alarm_info_page.get_alarm_second_time() + "' and a.imei in " + str(
                    current_user_all_equipment) + " and a.USER_ID = " + user_id + ";"

            elif data['alarm_begin_time'] == '' and data['alarm_end_time'] == '' and data['push_begin_time'] != '' and \
                            data['push_end_time'] != '' and data['next_user'] == '0':
                # 条件4，告警时间为空，定位时间不为空，不包含下级用户
                self.get_total_sql = "SELECT a.imei FROM alarm_info_user AS a WHERE a.PUSHTIME BETWEEN '" + self.alarm_info_page.get_push_first_time() + "' AND '" + self.alarm_info_page.get_push_second_time() + "' and a.imei in " + str(
                    current_user_all_equipment) + " and a.USER_ID = " + user_id + ";"

            elif data['alarm_begin_time'] != '' and data['alarm_end_time'] != '' and data['push_begin_time'] != '' and \
                            data['push_end_time'] != '' and data['next_user'] == '1':
                # 条件5，告警时间不为空，定位时间不为空，包含下级用户
                self.get_total_sql = "SELECT a.imei FROM alarm_info_user AS a WHERE a.CREATETIME BETWEEN '" + self.alarm_info_page.get_alarm_first_time() + "' AND '" + self.alarm_info_page.get_alarm_second_time() + "' AND a.PUSHTIME BETWEEN '" + self.alarm_info_page.get_push_first_time() + "' AND '" + self.alarm_info_page.get_push_second_time() + "' and a.imei in " + str(
                    current_user_all_equipment) + ";"

            elif data['alarm_begin_time'] == '' and data['alarm_end_time'] == '' and data['push_begin_time'] == '' and \
                            data['push_end_time'] == '' and data['next_user'] == '1':
                # 条件6，告警时间为空，定位时间为空，包含下级用户
                self.get_total_sql = "SELECT a.imei FROM alarm_info_user AS a WHERE a.imei in " + str(
                    current_user_all_equipment) + ";"

            elif data['alarm_begin_time'] != '' and data['alarm_end_time'] != '' and data['push_begin_time'] == '' and \
                            data['push_end_time'] == '' and data['next_user'] == '1':
                # 条件7，告警时间不为空，定位时间为空，包含下级用户
                self.get_total_sql = "SELECT a.imei FROM alarm_info_user AS a WHERE a.CREATETIME BETWEEN '" + self.alarm_info_page.get_alarm_first_time() + "' AND '" + self.alarm_info_page.get_alarm_second_time() + "' and a.imei in " + str(
                    current_user_all_equipment) + ";"

            elif data['alarm_begin_time'] == '' and data['alarm_end_time'] == '' and data['push_begin_time'] != '' and \
                            data['push_end_time'] != '' and data['next_user'] == '1':
                # 条件8，告警时间为空，定位时间不为空，不包含下级用户
                self.get_total_sql = "SELECT a.imei FROM alarm_info_user AS a WHERE a.PUSHTIME BETWEEN '" + self.alarm_info_page.get_push_first_time() + "' AND '" + self.alarm_info_page.get_push_second_time() + "' and a.imei in " + str(
                    current_user_all_equipment) + ";"

            # 执行sql
            print(self.get_total_sql)
            cursor_02.execute(self.get_total_sql)
            get_total = cursor_02.fetchall()
            total_list = []
            for range1 in get_total:
                for range2 in range1:
                    total_list.append(range2)
            total = len(total_list)
            print(total)
            web_total = self.alarm_info_page.get_search_total()
            self.assertEqual(total, web_total)
            self.driver.default_frame()

            cursor_02.close()
            connect_02.close()
        csv_file.close()