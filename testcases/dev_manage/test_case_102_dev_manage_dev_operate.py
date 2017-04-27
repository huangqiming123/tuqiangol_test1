import csv
import unittest
from time import sleep

import pymysql

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page import DevManagePage
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv

from pages.login.login_page import LoginPage


# 设备管理-单个设备操作-编辑、查看位置、查看告警

# author:孙燕妮

class TestCase102DevManageDevOperate(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.dev_manage_page_read_csv = DevManagePageReadCsv()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_dev_manage_dev_operate(self):
        '''测试设备管理-单个设备操作-编辑、查看位置、查看告警'''

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

        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()

        # 设备列表导出
        self.dev_manage_page.dev_list_export()

        csv_file_01 = self.dev_manage_page_read_csv.read_csv('dev_basic_info_edit.csv')
        csv_data_01 = csv.reader(csv_file_01)

        for row in csv_data_01:
            basic_info = {
                "dev_name": row[0],
                "dev_group": row[1],
                "dev_use_range": row[2],
                "SIM": row[3],
                "content": row[4]
            }

            # 点击当前设备列表中单个设备的编辑
            sleep(4)
            self.dev_manage_page.dev_edit()
            self.driver.switch_to_frame('x,//*[@id="commModal_iframe"]')
            # 编辑基本信息
            self.dev_manage_page.dev_name_modify(basic_info["dev_name"])
            self.dev_manage_page.dev_group_modify(basic_info["dev_group"])

            self.dev_manage_page.dev_use_range_choose(basic_info["dev_use_range"])
            self.dev_manage_page.dev_SIM_edit(basic_info["SIM"])
            self.dev_manage_page.dev_remark_edit(basic_info["content"])
            self.driver.default_frame()
            # 保存
            self.dev_manage_page.dev_basic_info_save()

            # 获取保存操作状态
            basic_info_save_status = self.dev_manage_page.dev_basic_info_save_status()

            # 验证
            self.assertIn("操作成功", basic_info_save_status, "操作失败")

        csv_file_01.close()

        csv_file_02 = self.dev_manage_page_read_csv.read_csv('dev_user_info_edit.csv')
        csv_data_02 = csv.reader(csv_file_02)

        for row in csv_data_02:
            user_info = {
                "driver_name": row[0],
                "phone": row[1],
                "id_card": row[2],
                "car_shelf_num": row[3],
                "car_lice_num": row[4],
                "SN": row[5],
                "engine_num": row[6],
                "install_com": row[7],
                "install_pers": row[8],
                "install_addr": row[9],
                "install_posi": row[10]

            }

            # 点击当前设备列表中单个设备的编辑
            sleep(6)
            self.dev_manage_page.dev_edit()
            self.driver.switch_to_frame('x,//*[@id="commModal_iframe"]')
            # 编辑客户信息
            self.dev_manage_page.dev_cust_info_edit(user_info["driver_name"],
                                                    user_info["phone"],
                                                    user_info["id_card"],
                                                    user_info["car_shelf_num"],
                                                    user_info["car_lice_num"],
                                                    user_info["SN"],
                                                    user_info["engine_num"])

            # 编辑安装信息
            self.dev_manage_page.dev_install_info_edit(user_info["install_com"],
                                                       user_info["install_pers"],
                                                       user_info["install_addr"],
                                                       user_info["install_posi"])
            self.driver.default_frame()
            # 保存
            self.dev_manage_page.dev_info_save()

            # 获取保存操作状态
            dev_info_save_status = self.dev_manage_page.dev_info_save_status()

            # 验证
            self.assertIn("操作成功", dev_info_save_status, "操作失败")

        csv_file_02.close()

        # 获取当前窗口句柄
        account_center_handle = self.driver.get_current_window_handle()

        # 点击单个设备的查看位置
        self.dev_manage_page.dev_locate()

        expect_url_locate = self.base_url + '/index'

        # 获取当前所有窗口句柄
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != account_center_handle:
                self.driver.switch_to_window(handle)
                self.driver.wait(1)
                current_url = self.driver.get_current_url()

                self.assertEqual(expect_url_locate, current_url, "查看位置页面跳转错误!")
                # 关闭当前窗口
                self.driver.close_current_page()
                # 回到账户中心窗口
                self.driver.switch_to_window(account_center_handle)
                self.driver.wait()

        # 点击单个设备的查看告警
        self.dev_manage_page.dev_alarm()

        expect_url_alarm = self.base_url + '/deviceReport/statisticalReport'

        # 获取当前所有窗口句柄
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != account_center_handle:
                self.driver.switch_to_window(handle)
                self.driver.wait(1)
                current_url = self.driver.get_current_url()

                self.assertEqual(expect_url_alarm, current_url, "查看告警页面跳转错误!")
                # 关闭当前窗口
                self.driver.close_current_page()
                # 回到账户中心窗口
                self.driver.switch_to_window(account_center_handle)
                self.driver.wait()

        # 退出登录
        self.account_center_page_navi_bar.dev_manage_usr_logout()
