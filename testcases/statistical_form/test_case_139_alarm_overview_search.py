import csv
import unittest
import time
from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.alarm_info.alarm_info_page import AlarmInfoPage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv


class TestCase138AlarmOverviewSearch(unittest.TestCase):
    '''
    用例第138条，告警总览页面搜索
    author：zhangAo
    '''

    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.alarm_info_page = AlarmInfoPage(self.driver, self.base_url)
        self.statistical_form_page_read_csv = StatisticalFormPageReadCsv()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.statistical_form_page = StatisticalFormPage(self.driver, self.base_url)
        self.connect_sql = ConnectSql()
        self.assert_text = AssertText()

        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.driver.clear_cookies()
        self.log_in_base.log_in_jimitest()

        # 登录之后点击控制台，然后点击指令管理
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_138_alarm_overview_search(self):
        # 断言url
        expect_url = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url, self.alarm_info_page.actual_url_click_alarm())

        # 点击告警总览
        self.alarm_info_page.click_alarm_overview_list()
        # 断言文本
        expect_text_after_click_alarm = self.assert_text.statistical_form_page_alarm_overview()
        self.driver.switch_to_frame('x,//*[@id="alarmOverviewFrame"]')
        self.assertEqual(expect_text_after_click_alarm, self.alarm_info_page.actual_text_click_alarm_info())
        self.driver.default_frame()
        # 输入数据搜索
        csv_file = self.statistical_form_page_read_csv.read_csv('alarm_overview_search_data.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            data = {
                'user_name': row[0],
                'choose_date': row[1],
                'began_time': row[2],
                'end_time': row[3]
            }
            self.alarm_info_page.add_data_to_search_in_alarm_overview(data)
            self.driver.switch_to_frame('x,//*[@id="alarmOverviewFrame"]')
            # 连接数据库
            connect = self.connect_sql.connect_tuqiang_sql()
            # 创建游标
            cursor = connect.cursor()
            # 查询搜索用户的uesrID
            get_user_id_sql = "SELECT userId FROM user_info WHERE account ='" + data['user_name'] + "';"
            # 执行sql
            cursor.execute(get_user_id_sql)
            get_user_id = cursor.fetchall()
            user_id = get_user_id[0][0]

            # 当前用户下设置
            get_current_user_all_equipment = "SELECT a.imei FROM equipment_mostly AS a WHERE a.status = 'NORMAL' and a.userId = " + user_id + " and a.expiration > CURDATE();"
            cursor.execute(get_current_user_all_equipment)
            all_equipment = cursor.fetchall()

            all_equipment_list = []
            for range1 in all_equipment:
                for range2 in range1:
                    all_equipment_list.append(range2)

            current_user_all_equipment = tuple(all_equipment_list)

            cursor.close()
            connect.close()
            time.sleep(5)
            # 连接另一个数据库
            connect_02 = self.connect_sql.connect_tuqiang_sql()
            # 创建游标
            cursor_02 = connect_02.cursor()

            get_total_sql = "SELECT a.IMEI,a.USER_ID FROM alarm_info AS a WHERE a.CREATETIME BETWEEN  '" + self.alarm_info_page.get_first_time() + "' AND  '" + self.alarm_info_page.get_second_time() + "' and a.imei in " + str(
                current_user_all_equipment) + " and a.USER_ID = " + user_id + " GROUP BY a.IMEI ;"
            # 执行sql
            print(get_total_sql)
            cursor_02.execute(get_total_sql)
            get_total = cursor_02.fetchall()
            total_list = []
            for range1 in get_total:
                for range2 in range1:
                    total_list.append(range2)
            total = len(total_list) / 2

            # 查询web端的总条数
            web_total = self.alarm_info_page.get_web_total_in_overview_search()
            # 断言
            self.assertEqual(total, web_total)
            self.driver.default_frame()
            cursor_02.close()
            connect_02.close()
        csv_file.close()
