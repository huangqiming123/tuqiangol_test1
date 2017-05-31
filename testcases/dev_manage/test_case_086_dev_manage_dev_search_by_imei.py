import csv
import unittest
from automate_driver.automate_driver import AutomateDriver
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages

class TestCase086DevManageDevSearchByIMEI(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.dev_manage_page_read_csv = DevManagePageReadCsv()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_dev_manage_dev_search_by_imei(self):
        '''测试设备管理-设备搜索-by imei'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.log_in_base.log_in()

        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()

        csv_file = self.dev_manage_page_read_csv.read_csv('single_search_info.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            search_info = {
                "imei": row[0],
                "dev_name": row[1],
                "login_user_dev_type": row[2],
                "user_select": row[3],
                "select_user_dev_type": row[4],
                "vehicle_number": row[5],
                "car_frame": row[6],
                "SIM": row[7],
                "active_start_time": row[8],
                "active_end_time": row[9],
                "plat_expired_start_time": row[10],
                "plat_expired_end_time": row[11],
                "dev_use_range": row[12]
            }

            # 输入imei
            self.dev_manage_page.input_imei(search_info["imei"])

            # 搜索
            self.dev_manage_page.click_search_btn()

            # 获取搜索结果的imei号
            imei = self.dev_manage_page.get_search_result_imei()

            # 验证搜索结果imei与输入的imei是否一致
            self.assertEqual(search_info["imei"], imei, "搜索结果imei与输入的imei不一致")

        csv_file.close()
