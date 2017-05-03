'''import csv
import unittest
from time import sleep

import pymysql

from automate_driver.automate_driver import AutomateDriver
from pages.base.base_page import BasePage

from pages.login.login_page import LoginPage
from pages.statistical_form.statistical_form_page import StatisticalFormPage


class TestCase150SportStatisticalStayForm(unittest.TestCase):

    用例第150条，运动统计，停留报表
    author ： zhangAo


    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.log_in_page = LoginPage(self.driver, self.base_url)
        self.statistical_form_page = StatisticalFormPage(self.driver, self.base_url)
        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.driver.clear_cookies()
        self.log_in_page.account_input('jimitest')
        self.log_in_page.password_input('jimi123')
        self.log_in_page.remember_me()
        self.log_in_page.login_button_click()
        self.driver.implicitly_wait(5)

        # 登录之后点击控制台，然后点击设置
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        sleep(3)

    def tearDown(self):
        # 退出浏览器
        self.driver.quit_browser()

    def test_case_150_sport_statistical_stay_form(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/runReport/toReports'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())
        # 断言
        self.assertEqual('运动总览', self.statistical_form_page.actual_text_after_click_sport_overview())
        # 点击停留报表
        self.statistical_form_page.click_stay_form_button()
        # 断言
        self.assertEqual('停留报表', self.statistical_form_page.actual_text_after_click_stay_form_button())

        # 读数据
        # 读取查询数据
        csv_file = open('E:\git\\tuqiangol_test\data\statistical_form\sport_statistical_stay_search_data.csv',
                        'r', encoding='utf8')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'search_user': row[0],
                'choose_date': row[1],
                'begin_time': row[2],
                'end_time': row[3]
            }
            self.statistical_form_page.add_data_to_search_stay_form(search_data)

            # 连接数据库
            connect = pymysql.connect(
                host='172.16.0.100',
                port=3306,
                user='tracker',
                passwd='tracker',
                db='tracker-web-mimi',
                charset='utf8'
            )
            # 创建游标
            cursor = connect.cursor()
            # 查询搜索用户的uesrID
            get_user_id_sql = "SELECT user_organize.userId FROM user_organize WHERE user_organize.account ='" + \
                              search_data[
                                  'search_user'] + "';"
            # 执行sql
            cursor.execute(get_user_id_sql)
            get_user_id = cursor.fetchall()
            user_id = get_user_id[0][0]

            # 当前用户下设置
            get_current_user_all_equipment = "SELECT a.imei FROM assets_device AS a WHERE a.userId = " + user_id + ";"
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
            connect_02 = pymysql.connect(
                host='172.16.0.116',
                port=8066,
                user='jimi',
                passwd='jimi',
                db='his',
                charset='utf8'
            )
            # 创建游标
            cursor_02 = connect_02.cursor()

            # 判断查询条件
            if search_data['choose_date'] == 'today':
                self.get_total_sql = "SELECT s.IMEI,s.DURSECOND FROM report_stop_segment AS s WHERE s.IMEI in " + str(
                    current_user_all_equipment) + " AND (s.STARTTIME BETWEEN '" + self.statistical_form_page.get_today_begin_date() + "' and '" + self.statistical_form_page.get_today_end_time() + "' or s.ENDTIME BETWEEN '" + self.statistical_form_page.get_today_begin_date() + "' and '" + self.statistical_form_page.get_today_end_time() + "' or (s.STARTTIME <= '" + self.statistical_form_page.get_today_begin_date() + "' and s.ENDTIME >= '" + self.statistical_form_page.get_today_end_time() + "'));"

            elif search_data['choose_date'] == 'yesterday':
                self.get_total_sql = "SELECT s.IMEI,s.DURSECOND FROM report_stop_segment AS s WHERE s.IMEI in " + str(
                    current_user_all_equipment) + " AND (s.STARTTIME BETWEEN '" + self.statistical_form_page.get_yesterday_begin_time() + "' and '" + self.statistical_form_page.get_yesterday_end_time() + "' or s.ENDTIME BETWEEN '" + self.statistical_form_page.get_yesterday_begin_time() + "' and '" + self.statistical_form_page.get_yesterday_end_time() + "' or (s.STARTTIME <= '" + self.statistical_form_page.get_yesterday_begin_time() + "' and s.ENDTIME >= '" + self.statistical_form_page.get_yesterday_end_time() + "'));"

            elif search_data['choose_date'] == 'this_week':
                self.get_total_sql = "SELECT s.IMEI,s.DURSECOND FROM report_stop_segment AS s WHERE s.IMEI in " + str(
                    current_user_all_equipment) + " AND (s.STARTTIME BETWEEN '" + self.statistical_form_page.get_this_week_begin_time() + "' and '" + self.statistical_form_page.get_this_week_end_time() + "' or s.ENDTIME BETWEEN '" + self.statistical_form_page.get_this_week_begin_time() + "' and '" + self.statistical_form_page.get_this_week_end_time() + "' or (s.STARTTIME <= '" + self.statistical_form_page.get_this_week_begin_time() + "' and s.ENDTIME >= '" + self.statistical_form_page.get_this_week_end_time() + "'));"

            elif search_data['choose_date'] == 'last_week':
                self.get_total_sql = "SELECT s.IMEI,s.DURSECOND FROM report_stop_segment AS s WHERE s.IMEI in " + str(
                    current_user_all_equipment) + " AND (s.STARTTIME BETWEEN '" + self.statistical_form_page.get_last_week_begin_time() + "' and '" + self.statistical_form_page.get_last_week_end_time() + "' or s.ENDTIME BETWEEN '" + self.statistical_form_page.get_last_week_begin_time() + "' and '" + self.statistical_form_page.get_last_week_end_time() + "' or (s.STARTTIME <= '" + self.statistical_form_page.get_last_week_begin_time() + "' and s.ENDTIME >= '" + self.statistical_form_page.get_last_week_end_time() + "'));"

            elif search_data['choose_date'] == 'this_month':
                self.get_total_sql = "SELECT s.IMEI,s.DURSECOND FROM report_stop_segment AS s WHERE s.IMEI in " + str(
                    current_user_all_equipment) + " AND (s.STARTTIME BETWEEN '" + self.statistical_form_page.get_this_month_begin_time() + "' and '" + self.statistical_form_page.get_this_month_end_time() + "' or s.ENDTIME BETWEEN '" + self.statistical_form_page.get_this_month_begin_time() + "' and '" + self.statistical_form_page.get_this_month_end_time() + "' or (s.STARTTIME <= '" + self.statistical_form_page.get_this_month_begin_time() + "' and s.ENDTIME >= '" + self.statistical_form_page.get_this_month_end_time() + "'));"

            elif search_data['choose_date'] == 'last_month':
                self.get_total_sql = "SELECT s.IMEI,s.DURSECOND FROM report_stop_segment AS s WHERE s.IMEI in " + str(
                    current_user_all_equipment) + " AND (s.STARTTIME BETWEEN '" + self.statistical_form_page.get_last_month_begin_time() + "' and '" + self.statistical_form_page.get_last_month_end_time() + "' or s.ENDTIME BETWEEN '" + self.statistical_form_page.get_last_month_begin_time() + "' and '" + self.statistical_form_page.get_last_month_end_time() + "' or (s.STARTTIME <= '" + self.statistical_form_page.get_last_month_begin_time() + "' and s.ENDTIME >= '" + self.statistical_form_page.get_last_month_end_time() + "'));"

            elif search_data['choose_date'] == '':
                self.get_total_sql = "SELECT s.IMEI,s.DURSECOND FROM report_stop_segment AS s WHERE s.IMEI in " + str(
                    current_user_all_equipment) + " AND (s.STARTTIME BETWEEN '" + search_data[
                                         'begin_time'] + "' and '" + search_data[
                                         'end_time'] + "' or s.ENDTIME BETWEEN '" + search_data[
                                         'begin_time'] + "' and '" + search_data[
                                         'end_time'] + "' or (s.STARTTIME <= '" + search_data[
                                         'begin_time'] + "' and s.ENDTIME >= '" + search_data['end_time'] + "'));"

            cursor_02.execute(self.get_total_sql)
            get_total = cursor_02.fetchall()

            total_list = []
            for range1 in get_total:
                for range2 in range1:
                    total_list.append(range2)
            # 拆分列表
            total_number_list = []
            total_time_list = []
            for n in range(len(total_list)):
                if n % 2 == 0:
                    total_number_list.append(total_list[n])
                elif n % 2 == 1:
                    total_time_list.append(total_list[n])

            # 断言查询的条
            print(total_number_list)
            total = len(total_number_list)
            sleep(3)
            web_total = self.statistical_form_page.get_total_search_stay_form_number()
            self.assertEqual(total, web_total)

            # 断言查询的总的停留时间
            total_time = sum(total_time_list)
            chang_total_time_type = self.statistical_form_page.change_sec_time(total_time)
            web_total_time = self.statistical_form_page.get_total_stay_form_time()
            self.assertEqual(chang_total_time_type, web_total_time)

            # 点击导出停留报表
            self.statistical_form_page.click_export_stay_form()
            cursor_02.close()
            connect_02.close()
        csv_file.close()'''

import csv
import unittest
from time import sleep

import pymysql

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase

from pages.login.login_page import LoginPage
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv


class TestCase150SportStatisticalStayForm(unittest.TestCase):
    '''
    用例第150条，运动统计，停留报表
    author ： zhangAo
    '''

    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.log_in_page = LoginPage(self.driver, self.base_url)
        self.statistical_form_page = StatisticalFormPage(self.driver, self.base_url)
        self.statistical_form_page_read_csv = StatisticalFormPageReadCsv()
        self.log_in_base = LogInBase(self.driver,self.base_url)
        self.connect_sql = ConnectSql()
        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.driver.clear_cookies()
        self.log_in_base.log_in_jimitest()

        # 登录之后点击控制台，然后点击设置
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        sleep(3)

    def tearDown(self):
        # 退出浏览器
        self.driver.quit_browser()

    def test_case_150_sport_statistical_stay_form(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())
        # 点击停留报表
        self.statistical_form_page.click_stay_form_button()
        # 断言
        self.driver.switch_to_frame('x,//*[@id="stayReportFrame"]')
        self.assertEqual('停留报表', self.statistical_form_page.actual_text_after_click_stay_form_button())
        self.driver.default_frame()
        # 读数据
        # 读取查询数据
        csv_file = self.statistical_form_page_read_csv.read_csv('sport_statistical_stay_search_data.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'search_user': row[0],
                'choose_date': row[1],
                'begin_time': row[2],
                'end_time': row[3]
            }
            self.statistical_form_page.add_data_to_search_stay_form(search_data)
            self.driver.switch_to_frame('x,//*[@id="stayReportFrame"]')
            # 连接数据库
            connect = self.connect_sql.connect_tuqiang_sql()
            # 创建游标
            cursor = connect.cursor()
            # 查询搜索用户的uesrID
            get_user_id_sql = "SELECT user_organize.userId FROM user_organize WHERE user_organize.account ='" + \
                              search_data[
                                  'search_user'] + "';"
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

            # 判断查询条件
            if search_data['choose_date'] == 'today':
                self.get_total_sql = "SELECT s.CREATETIME,s.DURSECOND FROM report_stop_segment AS s WHERE s.IMEI in " + str(
                    current_user_all_equipment) + " AND (s.STARTTIME BETWEEN '" + self.statistical_form_page.get_today_begin_date() + "' and '" + self.statistical_form_page.get_today_end_time() + "' or s.ENDTIME BETWEEN '" + self.statistical_form_page.get_today_begin_date() + "' and '" + self.statistical_form_page.get_today_end_time() + "' or (s.STARTTIME <= '" + self.statistical_form_page.get_today_begin_date() + "' and s.ENDTIME >= '" + self.statistical_form_page.get_today_end_time() + "')) GROUP BY s.CREATETIME;"

            elif search_data['choose_date'] == 'yesterday':
                self.get_total_sql = "SELECT s.CREATETIME,s.DURSECOND FROM report_stop_segment AS s WHERE s.IMEI in " + str(
                    current_user_all_equipment) + " AND (s.STARTTIME BETWEEN '" + self.statistical_form_page.get_yesterday_begin_time() + "' and '" + self.statistical_form_page.get_yesterday_end_time() + "' or s.ENDTIME BETWEEN '" + self.statistical_form_page.get_yesterday_begin_time() + "' and '" + self.statistical_form_page.get_yesterday_end_time() + "' or (s.STARTTIME <= '" + self.statistical_form_page.get_yesterday_begin_time() + "' and s.ENDTIME >= '" + self.statistical_form_page.get_yesterday_end_time() + "')) GROUP BY s.CREATETIME;"

            elif search_data['choose_date'] == 'this_week':
                self.get_total_sql = "SELECT s.CREATETIME,s.DURSECOND FROM report_stop_segment AS s WHERE s.IMEI in " + str(
                    current_user_all_equipment) + " AND (s.STARTTIME BETWEEN '" + self.statistical_form_page.get_this_week_begin_time() + "' and '" + self.statistical_form_page.get_this_week_end_time() + "' or s.ENDTIME BETWEEN '" + self.statistical_form_page.get_this_week_begin_time() + "' and '" + self.statistical_form_page.get_this_week_end_time() + "' or (s.STARTTIME <= '" + self.statistical_form_page.get_this_week_begin_time() + "' and s.ENDTIME >= '" + self.statistical_form_page.get_this_week_end_time() + "')) GROUP BY s.CREATETIME;"

            elif search_data['choose_date'] == 'last_week':
                self.get_total_sql = "SELECT s.CREATETIME,s.DURSECOND FROM report_stop_segment AS s WHERE s.IMEI in " + str(
                    current_user_all_equipment) + " AND (s.STARTTIME BETWEEN '" + self.statistical_form_page.get_last_week_begin_time() + "' and '" + self.statistical_form_page.get_last_week_end_time() + "' or s.ENDTIME BETWEEN '" + self.statistical_form_page.get_last_week_begin_time() + "' and '" + self.statistical_form_page.get_last_week_end_time() + "' or (s.STARTTIME <= '" + self.statistical_form_page.get_last_week_begin_time() + "' and s.ENDTIME >= '" + self.statistical_form_page.get_last_week_end_time() + "')) GROUP BY s.CREATETIME;"

            elif search_data['choose_date'] == 'this_month':
                self.get_total_sql = "SELECT s.CREATETIME,s.DURSECOND FROM report_stop_segment AS s WHERE s.IMEI in " + str(
                    current_user_all_equipment) + " AND (s.STARTTIME BETWEEN '" + self.statistical_form_page.get_this_month_begin_time() + "' and '" + self.statistical_form_page.get_this_month_end_time() + "' or s.ENDTIME BETWEEN '" + self.statistical_form_page.get_this_month_begin_time() + "' and '" + self.statistical_form_page.get_this_month_end_time() + "' or (s.STARTTIME <= '" + self.statistical_form_page.get_this_month_begin_time() + "' and s.ENDTIME >= '" + self.statistical_form_page.get_this_month_end_time() + "')) GROUP BY s.CREATETIME;"

            elif search_data['choose_date'] == 'last_month':
                self.get_total_sql = "SELECT s.CREATETIME,s.DURSECOND FROM report_stop_segment AS s WHERE s.IMEI in " + str(
                    current_user_all_equipment) + " AND (s.STARTTIME BETWEEN '" + self.statistical_form_page.get_last_month_begin_time() + "' and '" + self.statistical_form_page.get_last_month_end_time() + "' or s.ENDTIME BETWEEN '" + self.statistical_form_page.get_last_month_begin_time() + "' and '" + self.statistical_form_page.get_last_month_end_time() + "' or (s.STARTTIME <= '" + self.statistical_form_page.get_last_month_begin_time() + "' and s.ENDTIME >= '" + self.statistical_form_page.get_last_month_end_time() + "')) GROUP BY s.CREATETIME;"

            elif search_data['choose_date'] == '':
                self.get_total_sql = "SELECT s.CREATETIME,s.DURSECOND FROM report_stop_segment AS s WHERE s.IMEI in " + str(
                    current_user_all_equipment) + " AND (s.STARTTIME BETWEEN '" + search_data[
                                         'begin_time'] + "' and '" + search_data[
                                         'end_time'] + "' or s.ENDTIME BETWEEN '" + search_data[
                                         'begin_time'] + "' and '" + search_data[
                                         'end_time'] + "' or (s.STARTTIME <= '" + search_data[
                                         'begin_time'] + "' and s.ENDTIME >= '" + search_data['end_time'] + "')) GROUP BY s.CREATETIME;"

            cursor_02.execute(self.get_total_sql)
            get_total = cursor_02.fetchall()

            total_list = []
            for range1 in get_total:
                for range2 in range1:
                    total_list.append(range2)

            print(total_list)
            # 拆分列表
            total_number_list = []
            total_time_list = []
            for n in range(len(total_list)):
                if n % 2 == 0:
                    total_number_list.append(total_list[n])
                elif n % 2 == 1:
                    total_time_list.append(total_list[n])

            # 断言查询的条
            print(total_number_list)
            total = len(total_number_list)
            sleep(3)
            web_total = self.statistical_form_page.get_total_search_stay_form_number()
            self.assertEqual(total, web_total)

            # 断言查询的总的停留时间
            total_time = sum(total_time_list)
            chang_total_time_type = self.statistical_form_page.change_sec_time(total_time)
            web_total_time = self.statistical_form_page.get_total_stay_form_time()
            self.assertEqual(chang_total_time_type, web_total_time)

            # 点击导出停留报表
            self.driver.default_frame()
            self.statistical_form_page.click_export_stay_form()
            cursor_02.close()
            connect_02.close()
        csv_file.close()