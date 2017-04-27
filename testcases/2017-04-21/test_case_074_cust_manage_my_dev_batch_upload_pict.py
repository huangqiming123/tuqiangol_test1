import csv
import unittest


from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.cust_manage.cust_manage_basic_info_and_add_cust_page import CustManageBasicInfoAndAddCustPage
from pages.cust_manage.cust_manage_cust_list_page import CustManageCustListPage
from pages.cust_manage.cust_manage_lower_account_page import CustManageLowerAccountPage
from pages.cust_manage.cust_manage_my_dev_page import CustManageMyDevPage

from pages.login.login_page import LoginPage


# 客户管理-我的设备-批量上传图片

# author:孙燕妮

class TestCase074CustManageMyDevBatchUploadPict(unittest.TestCase):
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
        self.log_in_base  = LogInBase(self.driver,self.base_url)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_cust_manage_my_dev_batch_upload_pict(self):
        '''客户管理-我的设备-批量上传图片'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.log_in_base.log_in()

        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()

        # 我的设备列表全选
        self.cust_manage_my_dev_page.select_all_my_dev()

        '''# 点击批量上传图片
        self.cust_manage_my_dev_page.batch_upload_pict()

        # 选择图片
        self.cust_manage_my_dev_page.select_pict()

        # 获取图片列表长度
        list_size = self.cust_manage_my_dev_page.get_pict_list()

        if list_size > 0 :
            # 清空列表
            self.cust_manage_my_dev_page.upload_clear_list()
            # 获取图片列表长度
            list_size_00 = self.cust_manage_my_dev_page.get_pict_list()
            # 验证清空后列表是否为空
            self.assertEqual(0,list_size_00,"列表清空失败")
        else:
            print("图片未选中")


        # 选择图片
        self.cust_manage_my_dev_page.select_pict()
        # 上传
        self.cust_manage_my_dev_page.click_upload_btn()
        # 获取上传操作状态
        upload_status = self.cust_manage_my_dev_page.get_upload_status()
        # 验证是否操作成功
        self.assertIn("操作成功",upload_status,"操作失败")

        # 关闭上传图片框
        self.cust_manage_my_dev_page.click_upload_dismiss()'''


        # 进入账户中心页面
        self.cust_manage_basic_info_and_add_cust_page.enter_account_center()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()

