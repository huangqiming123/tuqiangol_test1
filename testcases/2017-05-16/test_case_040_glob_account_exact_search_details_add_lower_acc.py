import csv
import unittest
from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_pages import AccountCenterNaviBarPages
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.cust_manage.cust_manage_basic_info_and_add_cust_pages import CustManageBasicInfoAndAddCustPages
from pages.cust_manage.cust_manage_lower_account_pages import CustManageLowerAccountPages
from pages.global_search.global_account_search_page import GlobalAccountSearchPage
from pages.global_search.global_search_page_read_csv import GlobleSearchPageReadCsv


# 全局搜索-精确查找设备结果唯一用户详情页面-新增下级用户模块的操作
# 运行前需修改csv中的login_acc登录账号
# author:孙燕妮

class TestCase040GlobAccountExactSearchDetailsAddLowerAcc(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.global_acc_search_page = GlobalAccountSearchPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPages(self.driver, self.base_url)
        self.cust_manage_lower_account_page = CustManageLowerAccountPages(self.driver, self.base_url)
        self.cust_manage_basic_info_and_add_cust_page = CustManageBasicInfoAndAddCustPages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.global_search_page_read_csv = GlobleSearchPageReadCsv()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_glob_account_exact_search_details_add_lower_acc(self):
        '''通过csv测试全局搜索-精确查找设备结果唯一用户详情页面-新增下级用户模块的操作功能'''

        csv_file = self.global_search_page_read_csv.read_csv('add_lower_acc_info.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            acc_info = {
                "account": row[0],
                "acc_type": row[1],
                "login_acc": row[2],
                "acc_name": row[3],
                "phone": row[4],
                "email": row[5],
                "conn": row[6],
                "com": row[7],
                "new_pwd": row[8]
            }

            # 打开途强在线首页-登录页
            self.base_page.open_page()

            # 登录
            self.log_in_base.log_in()

            # 全局搜索栏输入搜索关键词进行用户搜索
            self.global_acc_search_page.acc_easy_search(acc_info["account"])

            # 点击搜索结果-新增下级用户
            self.global_acc_search_page.click_add_lower_acc()

            # 选择用户类型
            self.global_acc_search_page.add_acc_type_choose(acc_info["acc_type"])

            # 编辑用户信息
            self.global_acc_search_page.add_acc_input_info_edit(acc_info["login_acc"],
                                                                acc_info["acc_name"],
                                                                acc_info["phone"],
                                                                acc_info["email"],
                                                                acc_info["conn"],
                                                                acc_info["com"],
                                                                acc_info["new_pwd"])

            # 修改用户登录权限
            self.global_acc_search_page.add_acc_login_limit_modi()

            # 保存
            self.global_acc_search_page.add_acc_info_save()

            # 获取保存操作状态
            status = self.global_acc_search_page.add_acc_info_save_status()

            # 验证操作是否成功
            self.assertIn("操作成功", status, "保存失败")

            # 关闭当前设备搜索对话框
            self.global_acc_search_page.close_dev_search()

            self.driver.wait(1)

            # 进入客户管理
            self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()

            # 进入当前登录账户的下级账户模块
            self.cust_manage_lower_account_page.enter_lower_acc()

            # 搜索新增客户
            self.cust_manage_lower_account_page.input_search_info(acc_info["login_acc"])

            # 搜索
            self.cust_manage_lower_account_page.click_search_btn()

            # 删除该新增客户
            self.cust_manage_lower_account_page.delete_acc()

            # 确定删除
            self.cust_manage_lower_account_page.delete_acc_ensure()

            # 获取删除操作状态
            del_status = self.cust_manage_lower_account_page.get_del_status()

            # 验证是否操作成功
            self.assertIn("操作成功", del_status, "操作失败")

            # 退出登录
            self.account_center_page_navi_bar.dev_manage_usr_logout()

        csv_file.close()
