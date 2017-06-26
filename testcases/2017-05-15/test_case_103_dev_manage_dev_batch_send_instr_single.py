import csv
import unittest

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_pages import AccountCenterNaviBarPages
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


# 设备管理-设备批量操作-选中单条设备发送指令、删除所选设备

# author:孙燕妮

class TestCase103DevManageDevBatchSendInstrSingle(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePages(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.dev_manage_page_read_csv = DevManagePageReadCsv()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_dev_manage_dev_batch_send_instr_single(self):
        '''测试设备管理-设备批量操作-选中单条设备发送指令'''

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

        # 选中单条设备
        self.dev_manage_page.select_single_check_box()

        csv_file = self.dev_manage_page_read_csv.read_csv('dev_instr_info_edit.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            instr_info = {
                "instr_type": row[0]
            }
            # 点击选中发送指令
            self.dev_manage_page.click_selected_send_instr()
            # 编辑指令信息
            self.dev_manage_page.edit_instr_info(instr_info["instr_type"])
            # 发送指令
            self.dev_manage_page.send_instr_for_single_dev()
            try:
                # 获取指令发送状态
                status = self.dev_manage_page.get_send_instr_status()
                # 验证指令发送是否操作成功
                self.assertIn("操作成功", status, "操作失败")
                self.driver.wait()
                # 删除当前已选设备
                self.dev_manage_page.selected_dev_del()
                # 关闭当前发送指令弹框
                self.dev_manage_page.close_send_instr()
            except:
                print("当前设备不支持发送所选中的指令")

        csv_file.close()
        # 退出登录
        self.account_center_page_navi_bar.dev_manage_usr_logout()
