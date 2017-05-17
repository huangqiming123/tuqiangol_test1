import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.console.console_page import ConsolePage
from pages.dev_manage.dev_manage_page import DevManagePage

from pages.login.login_page import LoginPage


# 控制台-当前登录账户设备的各类数据统计验证

# author:孙燕妮

class TestCase108ConsoleDevInfoCountWithLoginUser(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePage(self.driver, self.base_url)
        self.console_page = ConsolePage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_console_dev_info_count_with_login_user(self):
        '''测试控制台-当前登录账户设备的各类数据统计验证'''

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

        # 获取当前登录账户的库存及总数
        dev_info_01 = self.console_page.get_curr_login_dev_info()
        dev_stock_01 = dev_info_01["库存"]
        dev_total_01 = dev_info_01["总数"]

        # 获取当前客户列表中登录账户的库存及总数
        dev_info_02 = self.console_page.get_cust_list_login_dev_info()
        dev_stock_02 = dev_info_02["库存"]
        dev_total_02 = dev_info_02["总数"]

        # 验证以上两者信息是否显示一致
        self.assertEqual(dev_stock_01, dev_stock_02, "当前登录账户的库存数显示不一致")
        self.assertEqual(dev_total_01, dev_total_02, "当前登录账户的总数显示不一致")

        # 点击“全部”
        self.console_page.click_all()

        # 获取当前登录账户的“全部”设备数
        all_num = self.console_page.get_all_dev_num()

        # 统计当前“全部”列表设备总数
        sleep(5)
        count_all = self.console_page.count_all_group_dev()

        # 验证全部设备数是否与库存数一致
        self.assertEqual(int(dev_stock_01), all_num, "全部设备数与库存数不一致")
        # 验证全部设备数与实际设备数是否一致
        self.assertEqual(all_num, count_all, "全部设备数与实际设备数不一致")

        # 点击“已关注”
        self.console_page.click_focus()

        # 获取当前登录账户的“已关注”设备数
        focus_num = self.console_page.get_focus_dev_num()

        # 统计当前“已关注”列表设备总数
        count_focus = self.console_page.count_all_group_dev()

        # 验证已关注设备数与实际已关注设备数是否一致
        self.assertEqual(focus_num, count_focus, "已关注设备数与实际已关注设备数不一致")

        # 点击“在线”
        self.console_page.click_online()

        # 获取当前登录账户的“在线”设备数
        online_num = self.console_page.get_online_dev_num()

        # 统计当前“在线”列表设备总数
        count_online = self.console_page.count_all_group_dev()

        # 验证在线设备数与实际在线设备数是否一致
        self.assertEqual(online_num, count_online, "在线设备数与实际在线设备数不一致")

        # 点击“离线”
        self.console_page.click_offline()

        # 获取当前登录账户的“离线”设备数
        offline_num = self.console_page.get_offline_dev_num()

        # 统计当前“离线”列表设备总数
        count_offline = self.console_page.count_all_group_dev()

        # 验证离线设备数与实际离线设备数是否一致
        self.assertEqual(offline_num, count_offline, "离线设备数与实际离线设备数不一致")

        # 点击“未激活”
        self.console_page.click_noactive()

        # 获取当前登录账户的“未激活”设备数
        noactive_num = self.console_page.get_noactive_dev_num()

        # 统计当前“未激活”列表设备总数
        count_noactive = self.console_page.count_all_group_dev()

        # 验证未激活设备数与实际未激活设备数是否一致
        self.assertEqual(noactive_num, count_noactive, "未激活设备数与实际未激活设备数不一致")

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
