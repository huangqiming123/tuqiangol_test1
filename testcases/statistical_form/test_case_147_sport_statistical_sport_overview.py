import csv
import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv


class TestCase147SportStatisticalOverview(unittest.TestCase):
    '''
    用例第147条，运动统计，运动总览
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

    def test_case_147_sport_statistical_sport_overview(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())
        # 断言
        self.driver.switch_to_frame('x,//*[@id="sportOverviewFrame"]')
        self.assertEqual('运动总览', self.statistical_form_page.actual_text_after_click_sport_overview())
        self.driver.default_frame()

        # 读数据
        csv_file = self.statistical_form_page_read_csv.read_csv('sport_statistical_sport_overview_search_data.csv')
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
            self.statistical_form_page.add_data_to_search_sport_overview(search_data)

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
            if search_data['choose_date'] == '':
                # 如果输入时间
                self.get_total_sql = "select b.IMEI from (SELECT s.IMEI FROM day_run_summary AS s WHERE s.IMEI IN " + str(
                    current_user_all_equipment) + " AND s.ATDAY BETWEEN '" + search_data['begin_time'] + "' AND '" + \
                                     search_data['end_time'] + "' GROUP BY s.IMEI) b ;"

                self.get_sum_total = "SELECT s.MILEAGE,s.OVERSPEEDTIMES,s.STOPTIMES FROM day_run_summary AS s WHERE s.IMEI IN " + str(
                    current_user_all_equipment) + " AND s.ATDAY BETWEEN '" + search_data['begin_time'] + "' AND '" + \
                                     search_data['end_time'] + "';"

            elif search_data['choose_date'] == 'yesterday':
                # 时间是昨天
                self.get_total_sql = "select b.IMEI from (SELECT s.IMEI FROM day_run_summary AS s WHERE s.IMEI IN " + str(
                    current_user_all_equipment) + " AND s.ATDAY BETWEEN '" + self.statistical_form_page.get_yesterday_begin_time() + "' AND '" + \
                                     self.statistical_form_page.get_yesterday_end_time() + "' GROUP BY s.IMEI) b ;"

                self.get_sum_total = "SELECT s.MILEAGE,s.OVERSPEEDTIMES,s.STOPTIMES FROM day_run_summary AS s WHERE s.IMEI IN " + str(
                    current_user_all_equipment) + " AND s.ATDAY BETWEEN '" + self.statistical_form_page.get_yesterday_begin_time() + "' AND '" + \
                                     self.statistical_form_page.get_yesterday_end_time() + "';"

            elif search_data['choose_date'] == 'this_week':
                # 选择这周
                self.get_total_sql = "select b.IMEI from (SELECT s.IMEI FROM day_run_summary AS s WHERE s.IMEI IN " + str(
                    current_user_all_equipment) + " AND s.ATDAY BETWEEN '" + self.statistical_form_page.get_this_week_begin_time() + "' AND '" + \
                                     self.statistical_form_page.get_this_week_end_time() + "' GROUP BY s.IMEI) b ;"

                self.get_sum_total = "SELECT s.MILEAGE,s.OVERSPEEDTIMES,s.STOPTIMES FROM day_run_summary AS s WHERE s.IMEI IN " + str(
                    current_user_all_equipment) + " AND s.ATDAY BETWEEN '" + self.statistical_form_page.get_this_week_begin_time() + "' AND '" + \
                                     self.statistical_form_page.get_this_week_end_time() + "';"

            elif search_data['choose_date'] == 'last_week':
                # 上周
                self.get_total_sql = "select b.IMEI from (SELECT s.IMEI FROM day_run_summary AS s WHERE s.IMEI IN " + str(
                    current_user_all_equipment) + " AND s.ATDAY BETWEEN '" + self.statistical_form_page.get_last_week_begin_time() + "' AND '" + \
                                     self.statistical_form_page.get_last_week_end_time() + "' GROUP BY s.IMEI) b ;"

                self.get_sum_total = "SELECT s.MILEAGE,s.OVERSPEEDTIMES,s.STOPTIMES FROM day_run_summary AS s WHERE s.IMEI IN " + str(
                    current_user_all_equipment) + " AND s.ATDAY BETWEEN '" + self.statistical_form_page.get_last_week_begin_time() + "' AND '" + \
                                     self.statistical_form_page.get_last_week_end_time() + "';"

            elif search_data['choose_date'] == 'this_mouth':
                # 本月
                self.get_total_sql = "SELECT b.IMEI from (select s.IMEI FROM day_run_summary AS s WHERE s.IMEI IN " + str(
                    current_user_all_equipment) + " AND s.ATDAY BETWEEN '" + self.statistical_form_page.get_this_month_begin_time() + "' AND '" + \
                                     self.statistical_form_page.get_this_month_end_time() + "' GROUP BY s.IMEI) b ;"

                self.get_sum_total = "select s.MILEAGE,s.OVERSPEEDTIMES,s.STOPTIMES FROM day_run_summary AS s WHERE s.IMEI IN " + str(
                    current_user_all_equipment) + " AND s.ATDAY BETWEEN '" + self.statistical_form_page.get_this_month_begin_time() + "' AND '" + \
                                     self.statistical_form_page.get_this_month_end_time() + "';"

            elif search_data['choose_date'] == 'last_mouth':
                # 上月
                self.get_total_sql = "select b.IMEI from (SELECT s.IMEI FROM day_run_summary AS s WHERE s.IMEI IN " + str(
                    current_user_all_equipment) + " AND s.ATDAY BETWEEN '" + self.statistical_form_page.get_last_month_begin_time() + "' AND '" + \
                                     self.statistical_form_page.get_last_month_end_time() + "' GROUP BY s.IMEI) b ;"

                self.get_sum_total = "SELECT s.MILEAGE,s.OVERSPEEDTIMES,s.STOPTIMES FROM day_run_summary AS s WHERE s.IMEI IN " + str(
                    current_user_all_equipment) + " AND s.ATDAY BETWEEN '" + self.statistical_form_page.get_last_month_begin_time() + "' AND '" + \
                                     self.statistical_form_page.get_last_month_end_time() + "';"
            # 计算多少条数据
            cursor_02.execute(self.get_total_sql)
            get_total = cursor_02.fetchall()
            total_list = []
            for range1 in get_total:
                for range2 in range1:
                    total_list.append(range2)
            total = len(total_list)

            # 计算总里程，超速，停留次数
            cursor_02.execute(self.get_sum_total)
            get_sum_total = cursor_02.fetchall()
            data_list = []
            for range1 in get_sum_total:
                for range2 in range1:
                    data_list.append(range2)
            # 拆分列表
            sum_mlie_list = []
            sum_over_speed_list = []
            sum_stay_list = []
            for n in range(len(data_list)):
                if n % 3 == 0:
                    sum_mlie_list.append(data_list[n])
                elif n % 3 == 1:
                    sum_over_speed_list.append(data_list[n])
                elif n % 3 == 2:
                    sum_stay_list.append(data_list[n])
            # sql的总里程数
            total_mlie = sum(sum_mlie_list)

            new_over_speed_list = []
            for n in range(len(sum_over_speed_list)):
                if sum_over_speed_list[n] == None:
                    pass
                else:
                    new_over_speed_list.append(sum_over_speed_list[n])
            # sql的总超速数
            total_over_speed = sum(new_over_speed_list)
            # sql的总停留次数
            total_stay = sum(sum_stay_list)

            # 断言的部分
            # 断言查询条数
            self.driver.switch_to_frame('x,//*[@id="sportOverviewFrame"]')
            web_total = self.statistical_form_page.get_total_search_sport_overview()
            self.assertEqual(total, web_total)

            # 断言总里程数
            web_mlie_total = self.statistical_form_page.get_total_search_mile_total()
            self.assertAlmostEqual(total_mlie/1000, float(web_mlie_total))

            # 断言总的超速数
            web_over_speed_total = self.statistical_form_page.get_total_search_over_speed_total()
            self.assertEqual(str(total_over_speed), web_over_speed_total)

            # 断言总的停留次数
            web_stay_total = self.statistical_form_page.get_total_search_stay_total()
            self.assertEqual(str(total_stay), web_stay_total)
            # 导出
            self.statistical_form_page.export_sport_overview_data()
            self.driver.default_frame()
            cursor_02.close()
            connect_02.close()
        csv_file.close()