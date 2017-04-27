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


class TestCase152SportStatisticalAccForm(unittest.TestCase):
    '''
    用例第152条，运动报表，acc报表
    author ：zhangAo
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

    def test_case_152_sport_statistical_acc_form(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())

        # 点击停留报表
        self.statistical_form_page.click_acc_form_button()
        # 断言
        self.driver.switch_to_frame('x,//*[@id="AccReportFrame"]')
        self.assertEqual('ACC报表', self.statistical_form_page.actual_text_after_click_acc_button())
        self.driver.default_frame()

        # 读数据
        # 读取查询数据
        csv_file = self.statistical_form_page_read_csv.read_csv('sport_statistical_acc_search_data.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'search_user': row[0],
                'status': row[1],
                'choose_date': row[2],
                'begin_time': row[3],
                'end_time': row[4]
            }

            self.statistical_form_page.add_data_to_search_acc_form(search_data)
            self.driver.switch_to_frame('x,//*[@id="AccReportFrame"]')

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
            if search_data['choose_date'] == 'today' and search_data['status'] == '':
                # 条件1、时间选择今天，状态选择全部
                self.get_total_sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment AS a WHERE a.IMEI in " + str(
                    current_user_all_equipment) + " and (a.START BETWEEN '" + self.statistical_form_page.get_today_begin_date() + "' and '" + self.statistical_form_page.get_today_end_time() + "' or a.END BETWEEN '" + self.statistical_form_page.get_today_begin_date() + "' and '" + self.statistical_form_page.get_today_end_time() + "' or (a.START <= '" + self.statistical_form_page.get_today_begin_date() + "' and a.END >= '" + self.statistical_form_page.get_today_end_time() + "'));"

            elif search_data['choose_date'] == 'yesterday' and search_data['status'] == '':
                # 条件2、时间选择昨天，状态选择全部
                self.get_total_sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment AS a WHERE a.IMEI in " + str(
                    current_user_all_equipment) + " and (a.START BETWEEN '" + self.statistical_form_page.get_yesterday_begin_time() + "' and '" + self.statistical_form_page.get_yesterday_end_time() + "' or a.END BETWEEN '" + self.statistical_form_page.get_yesterday_begin_time() + "' and '" + self.statistical_form_page.get_yesterday_end_time() + "' or (a.START <= '" + self.statistical_form_page.get_yesterday_begin_time() + "' and a.END >= '" + self.statistical_form_page.get_yesterday_end_time() + "'));"

            elif search_data['choose_date'] == 'this_week' and search_data['status'] == '':
                # 条件3、时间选择这周，状态选择全部
                self.get_total_sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment AS a WHERE a.IMEI in " + str(
                    current_user_all_equipment) + " and (a.START BETWEEN '" + self.statistical_form_page.get_this_week_begin_time() + "' and '" + self.statistical_form_page.get_this_week_end_time() + "' or a.END BETWEEN '" + self.statistical_form_page.get_this_week_begin_time() + "' and '" + self.statistical_form_page.get_this_week_end_time() + "' or (a.START <= '" + self.statistical_form_page.get_this_week_begin_time() + "' and a.END >= '" + self.statistical_form_page.get_this_week_end_time() + "'));"

            elif search_data['choose_date'] == 'last_week' and search_data['status'] == '':
                # 　条件4 时间选择上周，状态选择全部
                self.get_total_sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment AS a WHERE a.IMEI in " + str(
                    current_user_all_equipment) + " and (a.START BETWEEN '" + self.statistical_form_page.get_last_week_begin_time() + "' and '" + self.statistical_form_page.get_last_week_end_time() + "' or a.END BETWEEN '" + self.statistical_form_page.get_last_week_begin_time() + "' and '" + self.statistical_form_page.get_last_week_end_time() + "' or (a.START <= '" + self.statistical_form_page.get_last_week_begin_time() + "' and a.END >= '" + self.statistical_form_page.get_last_week_end_time() + "'));"

            elif search_data['choose_date'] == 'this_month' and search_data['status'] == '':
                # 条件5 时间选择本月，状态选择全部
                self.get_total_sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment AS a WHERE a.IMEI in " + str(
                    current_user_all_equipment) + " and (a.START BETWEEN '" + self.statistical_form_page.get_this_month_begin_time() + "' and '" + self.statistical_form_page.get_this_month_end_time() + "' or a.END BETWEEN '" + self.statistical_form_page.get_this_month_begin_time() + "' and '" + self.statistical_form_page.get_this_month_end_time() + "' or (a.START <= '" + self.statistical_form_page.get_this_month_begin_time() + "' and a.END >= '" + self.statistical_form_page.get_this_month_end_time() + "'));"

            elif search_data['choose_date'] == 'last_month' and search_data['status'] == '':
                # 条件6 时间选择上月，状态选择全部
                self.get_total_sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment AS a WHERE a.IMEI in " + str(
                    current_user_all_equipment) + " and (a.START BETWEEN '" + self.statistical_form_page.get_last_month_begin_time() + "' and '" + self.statistical_form_page.get_last_month_end_time() + "' or a.END BETWEEN '" + self.statistical_form_page.get_last_month_begin_time() + "' and '" + self.statistical_form_page.get_last_month_end_time() + "' or (a.START <= '" + self.statistical_form_page.get_last_month_begin_time() + "' and a.END >= '" + self.statistical_form_page.get_last_month_end_time() + "'));"

            elif search_data['choose_date'] == '' and search_data['status'] == '':
                # 条件7、时间填写，状态选择全部
                self.get_total_sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment AS a WHERE a.IMEI in " + str(
                    current_user_all_equipment) + " and (a.START BETWEEN '" + search_data['begin_time'] + "' and '" + \
                                     search_data['end_time'] + "' or a.END BETWEEN '" + search_data[
                                         'begin_time'] + "' and '" + search_data['end_time'] + "' or (a.START <= '" + \
                                     search_data['begin_time'] + "' and a.END >= '" + search_data['end_time'] + "'));"

            elif search_data['choose_date'] == 'today' and search_data['status'] != '':
                # 条件8、时间选择今天，状态选择不是全部
                self.get_total_sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment AS a WHERE a.IMEI in " + str(
                    current_user_all_equipment) + " and (a.START BETWEEN '" + self.statistical_form_page.get_today_begin_date() + "' and '" + self.statistical_form_page.get_today_end_time() + "' or a.END BETWEEN '" + self.statistical_form_page.get_today_begin_date() + "' and '" + self.statistical_form_page.get_today_end_time() + "' or (a.START <= '" + self.statistical_form_page.get_today_begin_date() + "' and a.END >= '" + self.statistical_form_page.get_today_end_time() + "')) and a.acc= " + \
                                     search_data['status'] + ";"

            elif search_data['choose_date'] == 'yesterday' and search_data['status'] != '':
                # 条件9、时间选择昨天，状态不是选择全部
                self.get_total_sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment AS a WHERE a.IMEI in " + str(
                    current_user_all_equipment) + " and (a.START BETWEEN '" + self.statistical_form_page.get_yesterday_begin_time() + "' and '" + self.statistical_form_page.get_yesterday_end_time() + "' or a.END BETWEEN '" + self.statistical_form_page.get_yesterday_begin_time() + "' and '" + self.statistical_form_page.get_yesterday_end_time() + "' or (a.START <= '" + self.statistical_form_page.get_yesterday_begin_time() + "' and a.END >= '" + self.statistical_form_page.get_yesterday_end_time() + "')) and a.acc= " + \
                                     search_data['status'] + ";"

            elif search_data['choose_date'] == 'this_week' and search_data['status'] != '':
                # 条件10、时间选择这周，状态不是选择全部
                self.get_total_sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment AS a WHERE a.IMEI in " + str(
                    current_user_all_equipment) + " and (a.START BETWEEN '" + self.statistical_form_page.get_this_week_begin_time() + "' and '" + self.statistical_form_page.get_this_week_end_time() + "' or a.END BETWEEN '" + self.statistical_form_page.get_this_week_begin_time() + "' and '" + self.statistical_form_page.get_this_week_end_time() + "' or (a.START <= '" + self.statistical_form_page.get_this_week_begin_time() + "' and a.END >= '" + self.statistical_form_page.get_this_week_end_time() + "')) and a.acc= " + \
                                     search_data['status'] + ";"

            elif search_data['choose_date'] == 'last_week' and search_data['status'] != '':
                # 条件11 时间选择上周，状态不是选择全部
                self.get_total_sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment AS a WHERE a.IMEI in " + str(
                    current_user_all_equipment) + " and (a.START BETWEEN '" + self.statistical_form_page.get_last_week_begin_time() + "' and '" + self.statistical_form_page.get_last_week_end_time() + "' or a.END BETWEEN '" + self.statistical_form_page.get_last_week_begin_time() + "' and '" + self.statistical_form_page.get_last_week_end_time() + "' or (a.START <= '" + self.statistical_form_page.get_last_week_begin_time() + "' and a.END >= '" + self.statistical_form_page.get_last_week_end_time() + "')) and a.acc= " + \
                                     search_data['status'] + ";"

            elif search_data['choose_date'] == 'this_month' and search_data['status'] != '':
                # 条件12 时间选择本月，状态不是选择全部
                self.get_total_sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment AS a WHERE a.IMEI in " + str(
                    current_user_all_equipment) + " and (a.START BETWEEN '" + self.statistical_form_page.get_this_month_begin_time() + "' and '" + self.statistical_form_page.get_this_month_end_time() + "' or a.END BETWEEN '" + self.statistical_form_page.get_this_month_begin_time() + "' and '" + self.statistical_form_page.get_this_month_end_time() + "' or (a.START <= '" + self.statistical_form_page.get_this_month_begin_time() + "' and a.END >= '" + self.statistical_form_page.get_this_month_end_time() + "')) and a.acc= " + \
                                     search_data['status'] + ";"

            elif search_data['choose_date'] == 'last_month' and search_data['status'] != '':
                # 条件13 时间选择上月，状态不是选择全部
                self.get_total_sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment AS a WHERE a.IMEI in " + str(
                    current_user_all_equipment) + " and (a.START BETWEEN '" + self.statistical_form_page.get_last_month_begin_time() + "' and '" + self.statistical_form_page.get_last_month_end_time() + "' or a.END BETWEEN '" + self.statistical_form_page.get_last_month_begin_time() + "' and '" + self.statistical_form_page.get_last_month_end_time() + "' or (a.START <= '" + self.statistical_form_page.get_last_month_begin_time() + "' and a.END >= '" + self.statistical_form_page.get_last_month_end_time() + "')) and a.acc= " + \
                                     search_data['status'] + ";"

            elif search_data['choose_date'] == '' and search_data['status'] != '':
                # 条件14、时间填写，状态不是选择全部
                self.get_total_sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment AS a WHERE a.IMEI in " + str(
                    current_user_all_equipment) + " and (a.START BETWEEN '" + search_data['begin_time'] + "' and '" + \
                                     search_data['end_time'] + "' or a.END BETWEEN '" + search_data[
                                         'begin_time'] + "' and '" + search_data['end_time'] + "' or (a.START <= '" + \
                                     search_data['begin_time'] + "' and a.END >= '" + search_data[
                                         'end_time'] + "')) and a.acc= " + search_data['status'] + ";"
            cursor_02.execute(self.get_total_sql)
            get_total = cursor_02.fetchall()

            total_list = []
            for range1 in get_total:
                for range2 in range1:
                    total_list.append(range2)
            get_total_list = []
            acc_open_list = []
            acc_close_list = []
            all_time_list = []
            for n in range(len(total_list)):
                if n % 3 == 0:
                    get_total_list.append(total_list[n])

                elif n % 3 == 1:
                    if total_list[n] == 1:
                        acc_open_list.append(total_list[n])
                    elif total_list[n] == 0:
                        acc_close_list.append(total_list[n])
                elif n % 3 == 2:
                    all_time_list.append(total_list[n])

            total = len(get_total_list)
            total_acc_open=len(acc_open_list)
            total_acc_close =len(acc_close_list)
            total_time = sum(all_time_list)

            # 断言总条数
            web_total = self.statistical_form_page.get_total_search_acc_form_number()
            self.assertEqual(total, web_total)
            # 断言acc打开几次
            web_acc_open_total = self.statistical_form_page.get_total_search_acc_open()
            self.assertEqual(str(total_acc_open),web_acc_open_total)

            # 断言acc关闭几次
            web_acc_close_total = self.statistical_form_page.get_total_search_acc_close()
            self.assertEqual(str(total_acc_close),web_acc_close_total)

            # 断言总时间
            total_times = self.statistical_form_page.change_sec_time(total_time)
            web_all_time_total = self.statistical_form_page.get_total_search_all_time()
            self.assertEqual(total_times,web_all_time_total)

            # 点击导出报表
            self.statistical_form_page.click_export_acc_form()
            self.driver.default_frame()
            cursor_02.close()
            connect_02.close()
        csv_file.close()
