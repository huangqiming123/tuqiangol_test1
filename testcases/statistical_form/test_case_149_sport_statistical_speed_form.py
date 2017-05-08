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


class TestCase149SportStatisticalSpeedForm(unittest.TestCase):
    '''
    用例第149条，运动报表，超速报表
    author：zhangAo
    '''

    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
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

    def test_case_149_sport_statistical_speed_form(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())

        self.statistical_form_page.click_over_speed_button()
        # 断言
        self.driver.switch_to_frame('x,//*[@id="speedingReportFrame"]')
        self.assertEqual('超速报表', self.statistical_form_page.actual_text_after_click_over_speed_button())
        self.driver.default_frame()

        # 读取查询数据
        csv_file = self.statistical_form_page_read_csv.read_csv('sport_statistical_over_speed_search_dara.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'search_user': row[0],
                'speed': row[1],
                'choose_date': row[2],
                'begin_time': row[3],
                'end_time': row[4]
            }
            self.statistical_form_page.add_data_to_search_over_speed(search_data)
            self.driver.switch_to_frame('x,//*[@id="speedingReportFrame"]')

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
            # 判断查询的条件
            if search_data['choose_date'] == 'today':
                self.get_total_sql = "SELECT t.IMEI FROM report_track_segment AS t INNER JOIN day_run_summary AS r ON t.IMEI = r.IMEI WHERE r.OVERSPEEDTIMES IS NOT NULL AND t.AVGSPEED >= " + \
                                     search_data[
                                         'speed'] + " AND t.CREATETIME BETWEEN '" + self.statistical_form_page.get_today_begin_date() + "' AND '" + self.statistical_form_page.get_today_end_time() + "' and t.IMEI in " + str(
                    current_user_all_equipment) + ";"

            elif search_data['choose_date'] == 'yesterday':
                self.get_total_sql = "SELECT t.IMEI FROM report_track_segment AS t INNER JOIN day_run_summary AS r ON t.IMEI = r.IMEI WHERE r.OVERSPEEDTIMES IS NOT NULL AND t.AVGSPEED >= " + \
                                     search_data[
                                         'speed'] + " AND t.CREATETIME BETWEEN '" + self.statistical_form_page.get_yesterday_begin_time() + "' AND '" + self.statistical_form_page.get_yesterday_end_time() + "' and t.IMEI in " + str(
                    current_user_all_equipment) + ";"

            elif search_data['choose_date'] == 'this_week':
                self.get_total_sql = "SELECT t.IMEI FROM report_track_segment AS t INNER JOIN day_run_summary AS r ON t.IMEI = r.IMEI WHERE r.OVERSPEEDTIMES IS NOT NULL AND t.AVGSPEED >= " + \
                                     search_data[
                                         'speed'] + " AND t.CREATETIME BETWEEN '" + self.statistical_form_page.get_this_week_begin_time() + "' AND '" + self.statistical_form_page.get_this_week_end_time() + "' and t.IMEI in " + str(
                    current_user_all_equipment) + ";"

            elif search_data['choose_date'] == 'last_week':
                self.get_total_sql = "SELECT t.IMEI FROM report_track_segment AS t INNER JOIN day_run_summary AS r ON t.IMEI = r.IMEI WHERE r.OVERSPEEDTIMES IS NOT NULL AND t.AVGSPEED >= " + \
                                     search_data[
                                         'speed'] + " AND t.CREATETIME BETWEEN '" + self.statistical_form_page.get_last_week_begin_time() + "' AND '" + self.statistical_form_page.get_last_week_end_time() + "' and t.IMEI in " + str(
                    current_user_all_equipment) + ";"

            elif search_data['choose_date'] == 'this_month':
                self.get_total_sql = "SELECT t.IMEI FROM report_track_segment AS t INNER JOIN day_run_summary AS r ON t.IMEI = r.IMEI WHERE r.OVERSPEEDTIMES IS NOT NULL AND t.AVGSPEED >= " + \
                                     search_data[
                                         'speed'] + " AND t.CREATETIME BETWEEN '" + self.statistical_form_page.get_this_month_begin_time() + "' AND '" + self.statistical_form_page.get_this_month_end_time() + "' and t.IMEI in " + str(
                    current_user_all_equipment) + ";"

            elif search_data['choose_date'] == 'last_month':
                self.get_total_sql = "SELECT t.IMEI FROM report_track_segment AS t INNER JOIN day_run_summary AS r ON t.IMEI = r.IMEI WHERE r.OVERSPEEDTIMES IS NOT NULL AND t.AVGSPEED >= " + \
                                     search_data[
                                         'speed'] + " AND t.CREATETIME BETWEEN '" + self.statistical_form_page.get_last_month_begin_time() + "' AND '" + self.statistical_form_page.get_last_month_end_time() + "' and t.IMEI in " + str(
                    current_user_all_equipment) + ";"

            elif search_data['choose_date'] == '':
                self.get_total_sql = "SELECT t.IMEI FROM report_track_segment AS t INNER JOIN day_run_summary AS r ON t.IMEI = r.IMEI WHERE r.OVERSPEEDTIMES IS NOT NULL AND t.AVGSPEED >= " + \
                                     search_data[
                                         'speed'] + " AND t.CREATETIME BETWEEN '" + search_data['begin_time'] + "' AND '" + search_data['end_time'] + "' and t.IMEI in " + str(
                    current_user_all_equipment) + ";"

            cursor_02.execute(self.get_total_sql)
            get_total = cursor_02.fetchall()
            total_list = []
            for range1 in get_total:
                for range2 in range1:
                    total_list.append(range2)
            total = len(total_list)
            web_total = self.statistical_form_page.get_total_search_over_speed_number()
            self.assertEqual(total,web_total)

            # 点击导出
            self.statistical_form_page.click_export_over_form()
            self.driver.default_frame()
            cursor_02.close()
            connect_02.close()
        csv_file.close()