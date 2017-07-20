import csv
import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.cust_manage.cust_manage_basic_info_and_add_cust_page import CustManageBasicInfoAndAddCustPage
from pages.cust_manage.cust_manage_cust_list_page import CustManageCustListPage
from pages.cust_manage.cust_manage_lower_account_page import CustManageLowerAccountPage
from pages.cust_manage.cust_manage_my_dev_page import CustManageMyDevPage

from pages.login.login_page import LoginPage


# 客户管理-过期设备列表-编辑

# author:孙燕妮

class TestCase067CustManageExpiredDevEdit(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.cust_manage_basic_info_and_add_cust_page = CustManageBasicInfoAndAddCustPage(self.driver, self.base_url)
        self.cust_manage_cust_list_page = CustManageCustListPage(self.driver, self.base_url)
        self.cust_manage_my_dev_page = CustManageMyDevPage(self.driver, self.base_url)
        self.cust_manage_lower_account_page = CustManageLowerAccountPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_cust_manage_expired_dev_edit(self):
        '''客户管理-过期设备列表-编辑'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.login_page.user_login("test_007", "jimi123")

        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()

        # 点击进入到期客户
        self.cust_manage_cust_list_page.click_expired_cust()

        # 选择用户到期
        self.cust_manage_cust_list_page.select_expired_type("用户到期")

        # 选择已过期
        self.cust_manage_cust_list_page.select_expired_status("已过期")

        # 选择过期时间段
        self.cust_manage_cust_list_page.select_expired_time("30天内")

        self.driver.wait()

        # 点击已过期用户
        self.cust_manage_cust_list_page.click_const_acc()

        csv_file = open(r"E:\git\tuqiangol_test\data\cust_manage\expired_dev_edit.csv",
                        'r',
                        encoding='utf8')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            edit_info = {
                "dev_name": row[0],
                "dev_group": row[1],
                "dev_use_range": row[2],
                "SIM": row[3],
                "content": row[4],
                "driver_name": row[5],
                "phone": row[6],
                "id_card": row[7],
                "car_shelf_num": row[8],
                "car_lice_num": row[9],
                "SN": row[10],
                "engine_num": row[11],
                "install_com": row[12],
                "install_pers": row[13],
                "install_addr": row[14],
                "install_posi": row[15]
            }

            # 右侧过期设备列表中的设备-编辑
            self.cust_manage_cust_list_page.expired_dev_edit()

            # 编辑基本信息
            # 修改设备名称
            self.cust_manage_cust_list_page.dev_name_modify(edit_info["dev_name"])
            # 移动设备分组
            self.cust_manage_cust_list_page.dev_group_modify(edit_info["dev_group"])
            # 选择设备使用范围
            self.cust_manage_cust_list_page.dev_use_range_choose(edit_info["dev_use_range"])
            # 填写设备sim卡号
            self.cust_manage_cust_list_page.dev_SIM_edit(edit_info["SIM"])
            # 填写设备备注
            self.cust_manage_cust_list_page.dev_remark_edit(edit_info["content"])
            # 保存
            self.cust_manage_cust_list_page.dev_basic_info_save()
            # 获取保存状态
            save_status = self.cust_manage_cust_list_page.dev_basic_info_save_status()
            # 验证是否保存成功
            self.assertIn("操作成功", save_status, "操作失败")

            sleep(5)
            # 右侧过期设备列表中的设备-编辑
            self.cust_manage_cust_list_page.expired_dev_edit()
            # 编辑客户信息
            self.cust_manage_cust_list_page.dev_cust_info_edit(edit_info["driver_name"],
                                                               edit_info["phone"],
                                                               edit_info["id_card"],
                                                               edit_info["car_shelf_num"],
                                                               edit_info["car_lice_num"],
                                                               edit_info["SN"],
                                                               edit_info["engine_num"])
            # 编辑用户到期时间
            self.cust_manage_cust_list_page.choose_account_expired_date()
            # 编辑安装信息
            self.cust_manage_cust_list_page.dev_install_info_edit(edit_info["install_com"],
                                                                  edit_info["install_pers"],
                                                                  edit_info["install_addr"],
                                                                  edit_info["install_posi"])
            # 选择安装时间
            self.cust_manage_cust_list_page.select_install_time()

            # 保存
            self.cust_manage_cust_list_page.dev_info_save()
            # 获取保存状态
            status = self.cust_manage_cust_list_page.dev_info_save_status()
            # 验证是否保存成功
            self.assertIn("操作成功", status, "操作失败")

            self.driver.wait(1)

        csv_file.close()

        # 进入账户中心页面
        self.cust_manage_basic_info_and_add_cust_page.enter_account_center()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()