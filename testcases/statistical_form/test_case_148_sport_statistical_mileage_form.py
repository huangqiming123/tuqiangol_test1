import csv
import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv


class TestCase148SportStatisticalMileageForm(unittest.TestCase):
    '''
    用例第148条，运动统计 里程报表
    author:zhangAo
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

    def test_case_148_sport_statistical_mileage_form(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())
        # 点击里程报表
        self.statistical_form_page.click_mileage_form_button()
        # 断言
        self.driver.switch_to_frame('x,//*[@id="mileageReportFrame"]')
        self.assertEqual('里程报表', self.statistical_form_page.actual_text_after_click_mileage_form_button())
        self.driver.default_frame()

        # 读取查询数据
        csv_file = self.statistical_form_page_read_csv.read_csv('sport_statistical_milage_form_search_data.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'search_user': row[0],
                'type': row[1],
                'choose_date': row[2],
                'begin_time': row[3],
                'end_time': row[4]
            }
            self.statistical_form_page.add_data_to_search_mileage_form(search_data)
            self.driver.switch_to_frame('x,//*[@id="mileageReportFrame"]')

            # 连接数据库
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

            # 判断查询条件
            if search_data['type'] == "mile":
                if search_data['choose_date'] == 'today':
                    self.get_total_sql = "SELECT m.IMEI FROM report_track_segment AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND (m.STARTTIME BETWEEN '" + self.statistical_form_page.get_today_begin_date() + "' and '" + self.statistical_form_page.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + self.statistical_form_page.get_today_begin_date() + "' and '" + self.statistical_form_page.get_today_end_time() + "' or (m.STARTTIME <= '" + self.statistical_form_page.get_today_begin_date() + "' and m.ENDTIME >= '" + self.statistical_form_page.get_today_end_time() + "'));"

                    self.get_all_mile_and_time_sql = "SELECT m.DISTANCE,m.RUNTIMESECOND FROM report_track_segment AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND (m.STARTTIME BETWEEN '" + self.statistical_form_page.get_today_begin_date() + "' and '" + self.statistical_form_page.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + self.statistical_form_page.get_today_begin_date() + "' and '" + self.statistical_form_page.get_today_end_time() + "' or (m.STARTTIME <= '" + self.statistical_form_page.get_today_begin_date() + "' and m.ENDTIME >= '" + self.statistical_form_page.get_today_end_time() + "'));"

                elif search_data['choose_date'] == 'yesterday':
                    self.get_total_sql = "SELECT m.IMEI FROM report_track_segment AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND (m.STARTTIME BETWEEN '" + self.statistical_form_page.get_yesterday_begin_time() + "' and '" + self.statistical_form_page.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + self.statistical_form_page.get_yesterday_begin_time() + "' and '" + self.statistical_form_page.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.statistical_form_page.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + self.statistical_form_page.get_yesterday_end_time() + "'));"

                    self.get_all_mile_and_time_sql = "SELECT m.DISTANCE,m.RUNTIMESECOND FROM report_track_segment AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND (m.STARTTIME BETWEEN '" + self.statistical_form_page.get_yesterday_begin_time() + "' and '" + self.statistical_form_page.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + self.statistical_form_page.get_yesterday_begin_time() + "' and '" + self.statistical_form_page.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.statistical_form_page.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + self.statistical_form_page.get_yesterday_end_time() + "'));"

                elif search_data['choose_date'] == 'this_week':
                    self.get_total_sql = "SELECT m.IMEI FROM report_track_segment AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND (m.STARTTIME BETWEEN '" + self.statistical_form_page.get_this_week_begin_time() + "' and '" + self.statistical_form_page.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + self.statistical_form_page.get_this_week_begin_time() + "' and '" + self.statistical_form_page.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.statistical_form_page.get_this_week_begin_time() + "' and m.ENDTIME >= '" + self.statistical_form_page.get_this_week_end_time() + "'));"

                    self.get_all_mile_and_time_sql = "SELECT m.DISTANCE,m.RUNTIMESECOND FROM report_track_segment AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND (m.STARTTIME BETWEEN '" + self.statistical_form_page.get_this_week_begin_time() + "' and '" + self.statistical_form_page.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + self.statistical_form_page.get_this_week_begin_time() + "' and '" + self.statistical_form_page.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.statistical_form_page.get_this_week_begin_time() + "' and m.ENDTIME >= '" + self.statistical_form_page.get_this_week_end_time() + "'));"

                elif search_data['choose_date'] == 'last_week':
                    self.get_total_sql = "SELECT m.IMEI FROM report_track_segment AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND (m.STARTTIME BETWEEN '" + self.statistical_form_page.get_last_week_begin_time() + "' and '" + self.statistical_form_page.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + self.statistical_form_page.get_last_week_begin_time() + "' and '" + self.statistical_form_page.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.statistical_form_page.get_last_week_begin_time() + "' and m.ENDTIME >= '" + self.statistical_form_page.get_last_week_end_time() + "'));"

                    self.get_all_mile_and_time_sql = "SELECT m.DISTANCE,m.RUNTIMESECOND FROM report_track_segment AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND (m.STARTTIME BETWEEN '" + self.statistical_form_page.get_last_week_begin_time() + "' and '" + self.statistical_form_page.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + self.statistical_form_page.get_last_week_begin_time() + "' and '" + self.statistical_form_page.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.statistical_form_page.get_last_week_begin_time() + "' and m.ENDTIME >= '" + self.statistical_form_page.get_last_week_end_time() + "'));"

                elif search_data['choose_date'] == 'this_month':
                    self.get_total_sql = "SELECT m.IMEI FROM report_track_segment AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND (m.STARTTIME BETWEEN '" + self.statistical_form_page.get_this_month_begin_time() + "' and '" + self.statistical_form_page.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + self.statistical_form_page.get_this_month_begin_time() + "' and '" + self.statistical_form_page.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.statistical_form_page.get_this_month_begin_time() + "' and m.ENDTIME >= '" + self.statistical_form_page.get_this_month_end_time() + "'));"

                    self.get_all_mile_and_time_sql = "SELECT m.DISTANCE,m.RUNTIMESECOND FROM report_track_segment AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND (m.STARTTIME BETWEEN '" + self.statistical_form_page.get_this_month_begin_time() + "' and '" + self.statistical_form_page.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + self.statistical_form_page.get_this_month_begin_time() + "' and '" + self.statistical_form_page.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.statistical_form_page.get_this_month_begin_time() + "' and m.ENDTIME >= '" + self.statistical_form_page.get_this_month_end_time() + "'));"

                elif search_data['choose_date'] == 'last_month':
                    self.get_total_sql = "SELECT m.IMEI FROM report_track_segment AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND (m.STARTTIME BETWEEN '" + self.statistical_form_page.get_last_month_begin_time() + "' and '" + self.statistical_form_page.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + self.statistical_form_page.get_last_month_begin_time() + "' and '" + self.statistical_form_page.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.statistical_form_page.get_last_month_begin_time() + "' and m.ENDTIME >= '" + self.statistical_form_page.get_last_month_end_time() + "'));"

                    self.get_all_mile_and_time_sql = "SELECT m.DISTANCE,m.RUNTIMESECOND FROM report_track_segment AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND (m.STARTTIME BETWEEN '" + self.statistical_form_page.get_last_month_begin_time() + "' and '" + self.statistical_form_page.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + self.statistical_form_page.get_last_month_begin_time() + "' and '" + self.statistical_form_page.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.statistical_form_page.get_last_month_begin_time() + "' and m.ENDTIME >= '" + self.statistical_form_page.get_last_month_end_time() + "'));"

                elif search_data['choose_date'] == '':
                    self.get_total_sql = "SELECT m.IMEI FROM report_track_segment AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND (m.STARTTIME BETWEEN '" + search_data[
                                             'begin_time'] + "' and '" + search_data[
                                             'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data[
                                             'begin_time'] + "' and '" + search_data[
                                             'end_time'] + "' or (m.STARTTIME <= '" + search_data[
                                             'begin_time'] + "' and m.ENDTIME >= '" + search_data['end_time'] + "'));"

                    self.get_all_mile_and_time_sql = "SELECT m.DISTANCE,m.RUNTIMESECOND FROM report_track_segment AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND (m.STARTTIME BETWEEN '" + search_data[
                                                         'begin_time'] + "' and '" + search_data[
                                                         'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data[
                                                         'begin_time'] + "' and '" + search_data[
                                                         'end_time'] + "' or (m.STARTTIME <= '" + search_data[
                                                         'begin_time'] + "' and m.ENDTIME >= '" + search_data[
                                                         'end_time'] + "'));"

                self.web_total = self.statistical_form_page.get_total_search_mileage_form()

            elif search_data['type'] == 'day':
                if search_data['choose_date'] == 'yesterday':
                    self.get_total_sql = "SELECT m.IMEI FROM day_mileage_summary AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND m.STARTTIME BETWEEN '" + self.statistical_form_page.get_yesterday_begin_time() + "' AND '" + self.statistical_form_page.get_yesterday_end_time() + "'  AND m.ENDTIME BETWEEN  '" + self.statistical_form_page.get_yesterday_begin_time() + "' AND '" + self.statistical_form_page.get_yesterday_end_time() + "';"

                    self.get_all_mile_sql = "SELECT m.DISTANCE FROM day_mileage_summary AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND m.STARTTIME BETWEEN '" + self.statistical_form_page.get_yesterday_begin_time() + "' AND '" + self.statistical_form_page.get_yesterday_end_time() + "'  AND m.ENDTIME BETWEEN  '" + self.statistical_form_page.get_yesterday_begin_time() + "' AND '" + self.statistical_form_page.get_yesterday_end_time() + "';"

                elif search_data['choose_date'] == 'this_week':
                    self.get_total_sql = "SELECT m.IMEI FROM day_mileage_summary AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND m.STARTTIME BETWEEN '" + self.statistical_form_page.get_this_week_begin_time() + "' AND '" + self.statistical_form_page.get_this_week_end_time() + "'  AND m.ENDTIME BETWEEN  '" + self.statistical_form_page.get_this_week_begin_time() + "' AND '" + self.statistical_form_page.get_this_week_end_time() + "';"

                    self.get_all_mile_sql = "SELECT m.DISTANCE FROM day_mileage_summary AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND m.STARTTIME BETWEEN '" + self.statistical_form_page.get_this_week_begin_time() + "' AND '" + self.statistical_form_page.get_this_week_end_time() + "'  AND m.ENDTIME BETWEEN  '" + self.statistical_form_page.get_this_week_begin_time() + "' AND '" + self.statistical_form_page.get_this_week_end_time() + "';"

                elif search_data['choose_date'] == 'last_week':
                    self.get_total_sql = "SELECT m.IMEI FROM day_mileage_summary AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND m.STARTTIME BETWEEN '" + self.statistical_form_page.get_last_week_begin_time() + "' AND '" + self.statistical_form_page.get_last_week_end_time() + "'  AND m.ENDTIME BETWEEN  '" + self.statistical_form_page.get_last_week_begin_time() + "' AND '" + self.statistical_form_page.get_last_week_end_time() + "';"

                    self.get_all_mile_sql = "SELECT m.DISTANCE FROM day_mileage_summary AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND m.STARTTIME BETWEEN '" + self.statistical_form_page.get_last_week_begin_time() + "' AND '" + self.statistical_form_page.get_last_week_end_time() + "'  AND m.ENDTIME BETWEEN  '" + self.statistical_form_page.get_last_week_begin_time() + "' AND '" + self.statistical_form_page.get_last_week_end_time() + "';"

                elif search_data['choose_date'] == 'this_month':
                    self.get_total_sql = "SELECT m.IMEI FROM day_mileage_summary AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND m.STARTTIME BETWEEN '" + self.statistical_form_page.get_this_month_begin_time() + "' AND '" + self.statistical_form_page.get_this_month_end_time() + "'  AND m.ENDTIME BETWEEN  '" + self.statistical_form_page.get_this_month_begin_time() + "' AND '" + self.statistical_form_page.get_this_month_end_time() + "';"

                    self.get_all_mile_sql = "SELECT m.DISTANCE FROM day_mileage_summary AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND m.STARTTIME BETWEEN '" + self.statistical_form_page.get_this_month_begin_time() + "' AND '" + self.statistical_form_page.get_this_month_end_time() + "'  AND m.ENDTIME BETWEEN  '" + self.statistical_form_page.get_this_month_begin_time() + "' AND '" + self.statistical_form_page.get_this_month_end_time() + "';"

                elif search_data['choose_date'] == 'last_month':
                    self.get_total_sql = "SELECT m.IMEI FROM day_mileage_summary AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND m.STARTTIME BETWEEN '" + self.statistical_form_page.get_last_month_begin_time() + "' AND '" + self.statistical_form_page.get_last_month_end_time() + "'  AND m.ENDTIME BETWEEN  '" + self.statistical_form_page.get_last_month_begin_time() + "' AND '" + self.statistical_form_page.get_last_month_end_time() + "';"

                    self.get_all_mile_sql = "SELECT m.DISTANCE FROM day_mileage_summary AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND m.STARTTIME BETWEEN '" + self.statistical_form_page.get_last_month_begin_time() + "' AND '" + self.statistical_form_page.get_last_month_end_time() + "'  AND m.ENDTIME BETWEEN  '" + self.statistical_form_page.get_last_month_begin_time() + "' AND '" + self.statistical_form_page.get_last_month_end_time() + "';"

                elif search_data['choose_date'] == '':
                    self.get_total_sql = "SELECT m.IMEI FROM day_mileage_summary AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND m.STARTTIME BETWEEN '" + search_data[
                                             'begin_time'] + "' AND '" + search_data[
                                             'end_time'] + "'  AND m.ENDTIME BETWEEN  '" + search_data[
                                             'begin_time'] + "' AND '" + search_data['end_time'] + "';"
                    self.get_all_mile_sql = "SELECT m.DISTANCE FROM day_mileage_summary AS m WHERE m.IMEI IN " + str(
                        current_user_all_equipment) + " AND m.STARTTIME BETWEEN '" + search_data[
                                                'begin_time'] + "' AND '" + search_data[
                                                'end_time'] + "'  AND m.ENDTIME BETWEEN  '" + search_data[
                                                'begin_time'] + "' AND '" + search_data['end_time'] + "';"
                self.web_total = self.statistical_form_page.get_total_search_mileage_form_with_day()

            cursor_02.execute(self.get_total_sql)
            get_total = cursor_02.fetchall()
            total_list = []
            for range1 in get_total:
                for range2 in range1:
                    total_list.append(range2)
            total = len(total_list)
            self.assertEqual(total, self.web_total)

            # 判断查询的条件
            if search_data['type'] == 'mile':
                # 查询的选择里程
                cursor_02.execute(self.get_all_mile_and_time_sql)
                get_all_mlie_and_time = cursor_02.fetchall()
                get_all_mlie_and_time_list = []
                for range1 in get_all_mlie_and_time:
                    for range2 in range1:
                        get_all_mlie_and_time_list.append(range2)

                # 拆分列表
                all_mile_list = []
                all_time_list = []
                for n in range(len(get_all_mlie_and_time_list)):
                    if n % 2 == 0:
                        all_mile_list.append(get_all_mlie_and_time_list[n])

                    elif n % 2 == 1:
                        all_time_list.append(get_all_mlie_and_time_list[n])

                # 计算总里程 和 总时间
                total_mile = sum(all_mile_list)
                total_time = sum(all_time_list)
                # 断言总时间和总里程，总油耗
                web_total_mile = self.statistical_form_page.get_mileage_all_mile()
                self.assertAlmostEqual(total_mile / 1000, float(web_total_mile))

                web_total_time = self.statistical_form_page.get_mileage_all_time()
                chang_total_time_type = self.statistical_form_page.change_sec_time(total_time)
                self.assertEqual(chang_total_time_type, web_total_time)

                # 计算总油耗
                get_total_oil = total_mile / 1000 / 100 * 8
                total_oil = '%.2f' % get_total_oil
                self.assertEqual(str(total_oil), self.statistical_form_page.get_mileage_total_oil())

            elif search_data['type'] == 'day':
                # 如果选择天
                cursor_02.execute(self.get_all_mile_sql)
                get_all_mile_data = cursor_02.fetchall()
                get_all_mile_list = []
                for range1 in get_all_mile_data:
                    for range2 in range1:
                        get_all_mile_list.append(range2)

                total_mile_with_day = sum(get_all_mile_list)
                # 断言
                self.assertAlmostEqual(total_mile_with_day / 1000,
                                       float(self.statistical_form_page.get_mileage_with_day_total_mile()))

            # 点击导出
            self.statistical_form_page.click_export_mileage_form()
            self.driver.default_frame()
            cursor_02.close()
            connect_02.close()
        csv_file.close()
