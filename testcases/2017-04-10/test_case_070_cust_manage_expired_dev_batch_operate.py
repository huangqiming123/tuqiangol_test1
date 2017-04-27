import csv
import unittest


from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.cust_manage.cust_manage_basic_info_and_add_cust_page import CustManageBasicInfoAndAddCustPage
from pages.cust_manage.cust_manage_cust_list_page import CustManageCustListPage
from pages.cust_manage.cust_manage_lower_account_page import CustManageLowerAccountPage
from pages.cust_manage.cust_manage_my_dev_page import CustManageMyDevPage

from pages.login.login_page import LoginPage


# 客户管理-过期设备列表-批量操作

# author:孙燕妮

class TestCase070CustManageExpiredDevBatchOperate(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.cust_manage_basic_info_and_add_cust_page = CustManageBasicInfoAndAddCustPage(self.driver, self.base_url)
        self.cust_manage_cust_list_page  = CustManageCustListPage(self.driver, self.base_url)
        self.cust_manage_my_dev_page  = CustManageMyDevPage(self.driver, self.base_url)
        self.cust_manage_lower_account_page = CustManageLowerAccountPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_cust_manage_expired_dev_batch_operate(self):
        '''客户管理-过期设备列表-批量操作'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.login_page.user_login("test_007", "jimi123")

        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()

        # 点击进入到期客户
        self.cust_manage_cust_list_page.click_expired_cust()

        # 选择用户到期
        #self.cust_manage_cust_list_page.select_expired_type("用户到期")

        # 选择已过期
        self.cust_manage_cust_list_page.select_expired_status("已过期")

        # 选择过期时间段
        self.cust_manage_cust_list_page.select_expired_time("30天内")

        self.driver.wait()

        # 点击已过期用户
        self.cust_manage_cust_list_page.click_const_acc()

        self.driver.wait()




        # 批量延长用户到期
        #self.cust_manage_cust_list_page.extend_acc_expired_time()

        extend_time_list = ["一个月","两个月","三个月","半年","一年"]

        # 选择延长时间
        self.cust_manage_cust_list_page.extend_acc_expired_time_select(extend_time_list[0])

        '''# 保存
        self.cust_manage_cust_list_page.save_extend_time()

        # 获取保存操作状态
        save_status = self.cust_manage_cust_list_page.extend_time_save_status()

        # 验证是否操作成功
        self.assertIn("操作成功",save_status,"操作失败")'''

        # 取消
        self.cust_manage_cust_list_page.dis_save_extend_time()

        # 批量导出
        self.cust_manage_cust_list_page.export_expired_dev()




        # 退出登录
        self.account_center_page_navi_bar.dev_manage_usr_logout()

