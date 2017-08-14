import csv
import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.search_sql import SearchSql
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv


class TestCase148SportStatisticalOverview(unittest.TestCase):
    '''
    运动统计，运动总览
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
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.connect_sql = ConnectSql()
        self.search_sql = SearchSql(self.driver, self.base_url)
        self.assert_text = AssertText()
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

    def test_case_sport_statistical_sport_overview(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())
        # 断言
        self.assertEqual(self.assert_text.statistical_form_sport_overview_form(),
                         self.statistical_form_page.actual_text_after_click_sport_overview())
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
            all_dev = self.search_sql.search_current_account_equipment(search_data['search_user'])

            # 连接另一个数据库
            connect_02 = self.connect_sql.connect_tuqiang_form()
            # 创建游标
            cursor_02 = connect_02.cursor()
            # 判断查询的条件
            get_total_sql = self.search_sql.search_sport_overview_sql(all_dev, search_data)
            get_sum_total = self.search_sql.search_sum_sport_overview_sql(all_dev, search_data)
            print(get_sum_total)
            # 计算多少条数据
            cursor_02.execute(get_total_sql)
            get_total = cursor_02.fetchall()
            total_list = []
            for range1 in get_total:
                for range2 in range1:
                    total_list.append(range2)
            total = len(total_list)

            # 计算总里程，超速，停留次数
            cursor_02.execute(get_sum_total)
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
            self.statistical_form_page.switch_to_sport_overview_form_frame()
            web_total = self.statistical_form_page.get_total_search_sport_overview()
            # self.assertEqual(total, web_total)

            # 断言总里程数
            web_mlie_total = self.statistical_form_page.get_total_search_mile_total()
            self.assertAlmostEqual(total_mlie / 1000, float(web_mlie_total))

            # 断言总的超速数
            web_over_speed_total = self.statistical_form_page.get_total_search_over_speed_total()
            # self.assertEqual(str(total_over_speed), web_over_speed_total)

            # 断言总的停留次数
            web_stay_total = self.statistical_form_page.get_total_search_stay_total()
            self.assertEqual(str(total_stay), web_stay_total)
            # 导出
            self.driver.default_frame()
            cursor_02.close()
            connect_02.close()
        csv_file.close()
