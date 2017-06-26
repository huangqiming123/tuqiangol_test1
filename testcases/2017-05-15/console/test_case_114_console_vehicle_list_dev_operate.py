import unittest
from time import sleep
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.console.console_page import ConsolePage
from pages.console.console_page_read_csv import ConsolePageReadCsv
from pages.dev_manage.dev_manage_page import DevManagePage


# 控制台-车辆列表的单个设备操作（关注、轨迹回放、更多）

# author:孙燕妮

class TestCase114ConsoleVehicleListDevOperate(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.dev_manage_page = DevManagePage(self.driver, self.base_url)
        self.console_page = ConsolePage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.console_page_read_csv = ConsolePageReadCsv()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_console_vehicle_list_dev_operate(self):
        '''测试控制台-车辆列表的单个设备操作（关注、轨迹回放、更多）'''

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

        # 关注/取消关注
        heart_title = self.console_page.attention()

        # 验证获取到的已关注图标title是否正确
        self.assertEqual("已关注", heart_title, "获取到的已关注图标title错误")

        # 轨迹回放
        # 获取当前选中设备的imei
        curr_dev_imei = self.console_page.get_dev_imei()
        # 获取当前选中设备的名称
        curr_dev_name = self.console_page.get_dev_name()

        # 获取当前窗口句柄
        console_handle = self.driver.get_current_window_handle()

        # 点击轨迹回放
        self.console_page.trace_replay()

        # 获取当前所有窗口句柄
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != console_handle:
                self.driver.switch_to_window(handle)
                self.driver.wait(1)
                # 获取轨迹回放页面的dev_imei
                sleep(3)
                dev_imei = self.console_page.get_trace_dev_imei()
                # 验证两者是否一致
                self.assertIn(curr_dev_imei, dev_imei, "当前选中的设备Imei与轨迹回放页面的Imei不一致")
                # 关闭当前窗口
                self.driver.close_current_page()
                # 回到控制台窗口
                self.driver.switch_to_window(console_handle)
                self.driver.wait()

        # 点击更多
        self.console_page.click_more()

        # 街景
        self.console_page.click_street_view()

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

        # 点击更多
        self.console_page.click_more()
        # 点击更多
        self.console_page.click_more()

        # 行车记录
        self.console_page.drive_record()

        # 获取当前所有窗口句柄
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != console_handle:
                self.driver.switch_to_window(handle)
                self.driver.wait(1)
                # 获取行车记录页面的dev_name
                dev_name = self.console_page.get_drive_record_dev_name()

                # 验证两者是否一致
                self.assertEqual(curr_dev_name, dev_name, "当前选中的设备名称与街景页面的设备名称不一致")
                # 关闭当前窗口
                self.driver.close_current_page()
                # 回到控制台窗口
                self.driver.switch_to_window(console_handle)
                self.driver.wait()

        # 点击更多
        self.console_page.click_more()
        # 电子围栏
        self.console_page.elec_rail()

        # 获取当前所有窗口句柄
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != console_handle:
                self.driver.switch_to_window(handle)
                self.driver.wait(1)
                # 获取电子围栏页面的url
                curr_url = self.driver.get_current_url()
                expect_url = self.base_url + '/electricFence/toElectricFence?imei=' + curr_dev_imei
                # 验证两者是否一致
                self.assertEqual(expect_url, curr_url, "当前页面跳转错误")
                # 关闭当前窗口
                self.driver.close_current_page()
                # 回到控制台窗口
                self.driver.switch_to_window(console_handle)
                self.driver.wait()

        '''# 点击更多
        self.console_page.click_more()
        # 移动到组
        self.console_page.move_group()

        csv_file = open(r"E:\git\\tuqiangol_test\data\console\dev_info.csv",
                        'r',
                        encoding='utf8')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            dev_info = {
                "dev_name": row[0],
                "sim": row[1],
                "content": row[2],
                "vehicle_num": row[3],
                "install_pers": row[4]
            }

            # 点击更多
            self.console_page.click_more()
            sleep(2)
            # 设备详情
            self.console_page.dev_info(dev_info["dev_name"],
                                       dev_info["sim"],
                                       dev_info["content"],
                                       dev_info["vehicle_num"],
                                       dev_info["install_pers"])
            # 获取保存状态
            save_status = self.console_page.get_dev_info_save_status()
            # 验证是否操作成功
            self.assertIn("操作成功",save_status,"操作失败")

        csv_file.close()'''

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
