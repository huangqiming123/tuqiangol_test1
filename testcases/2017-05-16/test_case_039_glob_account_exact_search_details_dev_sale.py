import csv
import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_pages import AccountCenterNaviBarPages
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.global_search.global_account_search_page import GlobalAccountSearchPage
from pages.global_search.global_search_page_read_csv import GlobleSearchPageReadCsv


# 全局搜索-精确查找设备结果唯一用户详情页面-销售设备模块的操作
# 运行需提前修改csv中imei账号
# author:孙燕妮

class TestCase039GlobAccountExactSearchDetailsDevSale(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.global_acc_search_page = GlobalAccountSearchPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.global_search_page_read_csv = GlobleSearchPageReadCsv()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_glob_account_exact_search_details_dev_sale(self):
        '''通过csv测试全局搜索-精确查找设备结果唯一用户详情页面-销售设备模块的操作功能'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.log_in_base.log_in()
        self.global_acc_search_page.click_account_search_button()
        csv_file = self.global_search_page_read_csv.read_csv('acc_sale_dev.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            sale_info = {
                'account': row[0],
                "imei": row[1]
            }
            self.global_acc_search_page.search_account(sale_info['account'])
            # 点击搜索结果-销售设备
            self.global_acc_search_page.click_sale_dev()
            # 输入设备imei
            self.global_acc_search_page.dev_imei_input(sale_info["imei"])
            self.driver.wait(1)
            # 取消添加
            self.global_acc_search_page.dev_add_dismiss()
            self.driver.wait(1)
            # 输入设备imei
            self.global_acc_search_page.dev_imei_input(sale_info["imei"])
            self.driver.wait(1)
            # 添加
            self.global_acc_search_page.dev_add()
            self.driver.wait(1)
            # 获取当前已选设备个数
            add_num = self.global_acc_search_page.dev_sale_num()

            # 验证设备是否添加成功
            self.assertEqual("1", add_num, "设备添加失败")

            # 删除
            sleep(2)
            self.global_acc_search_page.del_add_imei()
            self.driver.wait()
            # 获取当前已选设备个数
            del_num = self.global_acc_search_page.dev_sale_num()

            # 验证设备是否删除成功
            self.assertEqual("0", del_num, "设备删除失败")

            # 输入设备imei
            self.global_acc_search_page.dev_imei_input(sale_info["imei"])

            # 添加
            self.global_acc_search_page.dev_add()
            self.driver.wait()
            # 重置
            self.global_acc_search_page.reset_dev_sale()
            self.driver.wait()
            # 获取当前已选设备个数
            reset_num = self.global_acc_search_page.dev_sale_num()

            # 验证是否重置成功
            self.assertEqual("0", reset_num, "重置失败")

            # 输入设备imei
            self.global_acc_search_page.dev_imei_input(sale_info["imei"])

            # 添加
            self.global_acc_search_page.dev_add()

            # 取消销售
            self.global_acc_search_page.click_dis_sale_btn()
            self.driver.wait()

            # 全局搜索栏输入搜索关键词进行用户搜索
            self.global_acc_search_page.acc_easy_search(sale_info["account"])

            # 点击搜索结果-销售设备
            self.global_acc_search_page.click_sale_dev()

            # 输入设备imei
            self.global_acc_search_page.dev_imei_input(sale_info["imei"])

            # 添加
            self.global_acc_search_page.dev_add()
            self.driver.wait()
            # 销售
            self.global_acc_search_page.click_sale_btn()

            # 获取销售操作状态
            status = self.global_acc_search_page.get_dev_sale_status()

            # 验证是否操作成功
            self.assertIn("操作成功", status, "销售成功")

            # 关闭当前设备搜索对话框
            self.global_acc_search_page.close_dev_search()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()

        csv_file.close()
