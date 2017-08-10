import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


class TestCase087DevManageDevSearchByInputData(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.dev_manage_page_read_csv = DevManagePageReadCsv()
        self.assert_text = AssertText()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_dev_manage_dev_search_by_input_data(self):
        '''测试设备管理-设备搜索-by imei'''
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.base_page.click_chinese_button()
        # 登录
        self.log_in_base.log_in()
        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()
        self.dev_manage_page.click_more_button()

        # 车牌号输入框输入选中用户的设备车牌号包含的字符，点击搜索，点击导出
        dev_vehicle_number = '12'
        self.dev_manage_page.inpui_dev_vehicle_number_to_search(dev_vehicle_number)
        self.dev_manage_page.click_search_btn()
        connect_sql = ConnectSql()
        connect = connect_sql.connect_tuqiang_sql()
        cursor = connect.cursor()
        # 获取查询出来的条数
        number = self.dev_manage_page.get_numbers_after_click_search()
        for n in range(number):
            imei = self.dev_manage_page.get_imei_after_search(n)
            sql = "SELECT d.vehicleNumber FROM equipment_detail d WHERE d.imei = '%s';" % imei
            cursor.execute(sql)
            data = cursor.fetchall()
            vehicle_number = data[0][0]
            self.assertIn(dev_vehicle_number, vehicle_number)

        # 车牌号输入框输入选中用户的设备车牌号不包含的字符，点击搜索，点击导出
        dev_vehicle_number = '不存在的'
        self.dev_manage_page.inpui_dev_vehicle_number_to_search(dev_vehicle_number)
        self.dev_manage_page.click_search_btn()
        text = self.dev_manage_page.get_search_no_dev_name_text()
        self.assertIn(self.assert_text.account_center_page_no_data_text(), text)

        # 车架号输入框输入选中用户的设备车架号包含的字符，点击搜索，点击导出
        self.dev_manage_page.inpui_dev_vehicle_number_to_search('')
        dev_car_frame = '12'
        self.dev_manage_page.input_dev_car_frame_to_search(dev_car_frame)
        self.dev_manage_page.click_search_btn()
        sleep(2)
        # 获取查询出来的条数
        number = self.dev_manage_page.get_numbers_after_click_search()
        for n in range(number):
            imei = self.dev_manage_page.get_imei_after_search(n)
            sql = "SELECT d.carFrame FROM equipment_detail d WHERE d.imei = '%s';" % imei
            cursor.execute(sql)
            data = cursor.fetchall()
            vehicle_number = data[0][0]
            self.assertIn(dev_car_frame, vehicle_number)

        # 车架号输入框输入选中用户的设备车架号不包含的字符，点击搜索，点击导出
        dev_vehicle_number = '不存在的'
        self.dev_manage_page.input_dev_car_frame_to_search(dev_vehicle_number)
        self.dev_manage_page.click_search_btn()
        text = self.dev_manage_page.get_search_no_dev_name_text()
        self.assertIn(self.assert_text.account_center_page_no_data_text(), text)

        # SIM卡号输入框输入选中用户的设备车牌号包含的字符，点击搜索，点击导出
        self.dev_manage_page.input_dev_car_frame_to_search('')
        dev_sim = '12'
        self.dev_manage_page.input_dev_sim_to_search(dev_sim)
        self.dev_manage_page.click_search_btn()
        sleep(2)
        # 获取查询出来的条数
        number = self.dev_manage_page.get_numbers_after_click_search()
        for n in range(number):
            imei = self.dev_manage_page.get_imei_after_search(n)
            sql = "SELECT d.sim FROM equipment_mostly d WHERE d.imei = '%s';" % imei
            cursor.execute(sql)
            data = cursor.fetchall()
            sim_number = data[0][0]
            self.assertIn(dev_sim, sim_number)

        # SIM卡号输入框输入选中用户的设备车牌号不包含的字符，点击搜索，点击导出
        dev_sim_number = '不存在的'
        self.dev_manage_page.input_dev_sim_to_search(dev_sim_number)
        self.dev_manage_page.click_search_btn()
        text = self.dev_manage_page.get_search_no_dev_name_text()
        self.assertIn(self.assert_text.account_center_page_no_data_text(), text)

        # SN码输入框输入选中用户的设备车架号包含的字符，点击搜索，点击导出
        self.dev_manage_page.input_dev_sim_to_search('')
        dev_sn = '12'
        self.dev_manage_page.input_dev_sn_to_search(dev_sn)
        self.dev_manage_page.click_search_btn()
        sleep(2)
        # 获取查询出来的条数
        number = self.dev_manage_page.get_numbers_after_click_search()
        for n in range(number):
            imei = self.dev_manage_page.get_imei_after_search(n)
            sql = "SELECT d.sn FROM equipment_detail d WHERE d.imei = '%s';" % imei
            cursor.execute(sql)
            data = cursor.fetchall()
            sn_number = data[0][0]
            self.assertIn(dev_sn, sn_number)

        # SN码输入框输入选中用户的设备车架号不包含的字符，点击搜索，点击导出
        dev_sn_number = '不存在的'
        self.dev_manage_page.input_dev_sn_to_search(dev_sn_number)
        self.dev_manage_page.click_search_btn()
        text = self.dev_manage_page.get_search_no_dev_name_text()
        self.assertIn(self.assert_text.account_center_page_no_data_text(), text)
