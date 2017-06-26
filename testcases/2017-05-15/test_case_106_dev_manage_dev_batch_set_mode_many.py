import unittest
from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_pages import AccountCenterNaviBarPages
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


# 设备管理-设备批量操作-全选设备设置工作模式

# author:孙燕妮

class TestCase106DevManageDevBatchSetModeMany(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePages(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPages(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.dev_manage_page_read_csv = DevManagePageReadCsv()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_dev_manage_dev_batch_set_mode_single(self):
        '''测试设备管理-设备批量操作-全选设备设置工作模式'''

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

        # 获取当前窗口句柄
        account_center_handle = self.driver.get_current_window_handle()

        # 全选设备
        self.dev_manage_page.select_all_check_box()

        # 点击选中设置工作模式
        self.dev_manage_page.click_selected_set_mode()

        # 关闭发送工作模式弹框
        self.dev_manage_page.close_set_mode()

        # 点击本次查询全部设置工作模式
        self.dev_manage_page.click_all_set_mode()
        self.driver.wait()

        # 选择工作模式
        self.dev_manage_page.select_dev_mode()

        # 多条选中设置工作模式
        self.dev_manage_page.set_mode_for_many_dev()

        try:
            # 获取工作模式发送状态
            status = self.dev_manage_page.get_send_instr_status()

            # 验证工作模式发送是否操作成功
            self.assertIn("操作成功", status, "操作失败")

        except:
            print("当前设备列表中没有设备支持发送所选中的工作模式")

        # 点击本次查询全部设置工作模式
        self.dev_manage_page.click_all_set_mode()

        self.driver.wait()

        # 删除已选中设备列表中的第一个设备
        self.dev_manage_page.set_mode_dev_del()

        # 点击工作模式模板管理
        self.dev_manage_page.mode_manage()

        expect_url = self.base_url + '/custom/toTemplate'

        # 获取当前所有窗口句柄
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != account_center_handle:
                self.driver.switch_to_window(handle)
                self.driver.wait(1)
                current_url = self.driver.get_current_url()

                self.assertEqual(expect_url, current_url, "工作模式模板管理页面跳转错误!")
                self.driver.wait()

        # 退出登录
        self.account_center_page_navi_bar.dev_manage_usr_logout()
