import csv
import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.search_sql import SearchSql
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
        self.statistical_form_page = StatisticalFormPage(self.driver, self.base_url)
        self.statistical_form_page_read_csv = StatisticalFormPageReadCsv()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.connect_sql = ConnectSql()
        self.search_sql = SearchSql(self.driver, self.base_url)
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

            all_dev = self.search_sql.search_current_account_equipment(search_data['search_user'])

            # 连接另一个数据库
            connect_02 = self.connect_sql.connect_tuqiang_form()
            # 创建游标
            cursor_02 = connect_02.cursor()
            get_total_sql = self.search_sql.search_acc_sql(all_dev, search_data)
            print(get_total_sql)

            cursor_02.execute(get_total_sql)
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
            total_acc_open = len(acc_open_list)
            total_acc_close = len(acc_close_list)
            total_time = sum(all_time_list)

            # 断言总条数
            web_total = self.statistical_form_page.get_total_search_acc_form_number()
            self.assertEqual(total, web_total)
            # 断言acc打开几次
            web_acc_open_total = self.statistical_form_page.get_total_search_acc_open()
            self.assertEqual(str(total_acc_open), web_acc_open_total)

            # 断言acc关闭几次
            web_acc_close_total = self.statistical_form_page.get_total_search_acc_close()
            self.assertEqual(str(total_acc_close), web_acc_close_total)

            # 断言总时间
            total_times = self.statistical_form_page.change_sec_time(total_time)
            web_all_time_total = self.statistical_form_page.get_total_search_all_time()
            self.assertEqual(total_times, web_all_time_total)

            # 点击导出报表
            self.driver.default_frame()
            cursor_02.close()
            connect_02.close()
        csv_file.close()
