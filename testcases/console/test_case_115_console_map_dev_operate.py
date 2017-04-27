import csv
import unittest
from time import sleep

import pymysql

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.console.console_page import ConsolePage
from pages.console.console_page_read_csv import ConsolePageReadCsv
from pages.dev_manage.dev_manage_page import DevManagePage

from pages.login.login_page import LoginPage


# 控制台-地图中的单个设备操作（街景、轨迹回放、下发指令、设备详情、电子围栏、查看告警）

# author:孙燕妮

class TestCase115ConsoleVehicleListDevOperate(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePage(self.driver, self.base_url)
        self.console_page = ConsolePage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.console_page_read_csv = ConsolePageReadCsv()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_console_map_dev_operate(self):
        '''测试控制台-地图中的单个设备操作（街景、轨迹回放、下发指令、设备详情、电子围栏、查看告警）'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.log_in_base.log_in()

        # 获取当前窗口句柄
        account_center_handle = self.driver.get_current_window_handle()

        # 点击进入控制台
        self.dev_manage_page.enter_console()

        # 获取当前所有窗口句柄
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != account_center_handle:
                # 切换到账户中心窗口
                self.driver.switch_to_window(account_center_handle)
                self.driver.wait(1)
                # 关闭账户中心窗口
                self.driver.close_current_page()
                # 回到控制台窗口
                self.driver.switch_to_window(handle)
                self.driver.wait()

        # 点击车辆列表中的单个设备
        self.console_page.click_dev()

        # 获取当前选中设备的imei
        curr_dev_imei = self.console_page.get_dev_imei()

        # 获取当前选中设备名称
        curr_dev_name = self.console_page.get_dev_name()

        # 获取地图中显示对应设备详情信息
        dev_imei = self.console_page.get_map_dev_imei()
        dev_name = self.console_page.get_map_dev_name()

        # 验证两者是否一致
        self.assertEqual(curr_dev_imei, dev_imei, "当前选中的设备imei与地图中显示的imei不一致")
        self.assertEqual(curr_dev_name, dev_name, "当前选中的设备名称与地图中显示的名称不一致")

        # 获取当前窗口句柄
        console_handle = self.driver.get_current_window_handle()

        # 地图中单个设备的街景
        self.console_page.map_dev_street_view()

        # 获取当前所有窗口句柄
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != console_handle:
                self.driver.switch_to_window(handle)
                self.driver.wait(1)
                # 获取街景页面的dev_imei
                dev_imei = self.console_page.get_street_view_imei()
                # 验证两者是否一致
                self.assertEqual(curr_dev_imei, dev_imei, "当前选中的设备Imei与街景页面的Imei不一致")
                # 关闭当前窗口
                self.driver.close_current_page()
                # 回到控制台窗口
                self.driver.switch_to_window(console_handle)
                self.driver.wait()

        # 地图中单个设备的轨迹回放
        self.console_page.map_dev_trace_replay()

        # 获取当前所有窗口句柄
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != console_handle:
                self.driver.switch_to_window(handle)
                self.driver.wait(1)
                # 获取轨迹回放页面的dev_imei
                dev_imei = self.console_page.get_trace_dev_imei()
                # 验证两者是否一致
                self.assertIn(curr_dev_imei, dev_imei, "当前选中的设备Imei与轨迹回放页面的Imei不一致")
                # 关闭当前窗口
                self.driver.close_current_page()
                # 回到控制台窗口
                self.driver.switch_to_window(console_handle)
                self.driver.wait()

        # 地图中单个设备的下发指令
        try:
            self.console_page.map_dev_send_instr()
        except:
            print('不支持下发指令')
        sleep(3)

        self.driver.click_element('x,//*[@id="command-modal"]/div/div[1]/button')

        csv_file = self.console_page_read_csv.read_csv('dev_info.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            dev_info = {
                "dev_name": row[0],
                "sim": row[1],
                "content": row[2],
                "vehicle_num": row[3],
                "install_pers": row[4]
            }

            # 地图中单个设备的设备详情
            sleep(5)
            self.console_page.map_dev_info(dev_info["dev_name"],
                                           dev_info["sim"],
                                           dev_info["content"],
                                           dev_info["vehicle_num"],
                                           dev_info["install_pers"])

        csv_file.close()

        # 地图中单个设备的电子围栏
        sleep(3)
        self.console_page.map_dev_elec_rail()

        # 获取当前所有窗口句柄
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != console_handle:
                self.driver.switch_to_window(handle)
                self.driver.wait(1)
                # 获取电子围栏页面的url
                curr_url = self.driver.get_current_url()
                expect_url = self.base_url +  '/electricFence/toElectricFence?imei=874544562356578'
                # 验证两者是否一致
                self.assertEqual(expect_url, curr_url, "当前页面跳转错误")
                # 关闭当前窗口
                self.driver.close_current_page()
                # 回到控制台窗口
                self.driver.switch_to_window(console_handle)
                self.driver.wait()

        # 地图中单个设备的查看告警
        self.console_page.map_dev_alarm()

        # 获取当前所有窗口句柄
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != console_handle:
                self.driver.switch_to_window(handle)
                self.driver.wait(1)
                # 获取告警页面的url
                curr_url = self.driver.get_current_url()
                expect_url = self.base_url + '/alarmInfo/toAlarmInfo'
                # 验证两者是否一致
                self.assertEqual(expect_url, curr_url, "当前页面跳转错误")
                # 关闭当前窗口
                self.driver.close_current_page()
                # 回到控制台窗口
                self.driver.switch_to_window(console_handle)
                self.driver.wait()

        # 关闭地图中单个设备信息框
        self.console_page.close_map_dev_info()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
