import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


class TestCase1109DevManageSaleInList(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.dev_manage_page_read_csv = DevManagePageReadCsv()
        self.connect_sql = ConnectSql()
        self.assert_text = AssertText()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_1109_dev_manage_sale_in_list(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()
        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()
        imei_in_list = self.dev_manage_page.get_imei_in_list()
        dev_type_in_list = self.dev_manage_page.get_dev_type_in_list()

        # 点击批量
        self.dev_manage_page.click_sale_in_list_button()

        self.dev_manage_page.click_close_sale_in_list_button()

        self.dev_manage_page.click_sale_in_list_button()

        # 点击销售
        self.dev_manage_page.click_sale_button()

        # 获取打开销售之后的imei和设备类型
        imei_in_sale = self.dev_manage_page.get_imei_in_sale()
        self.assertEqual(imei_in_list, imei_in_sale)
        dev_type_in_sale = self.dev_manage_page.get_dev_type_in_sale()
        self.assertEqual(dev_type_in_list, dev_type_in_sale)
        dev_account_name = self.dev_manage_page.get_dev_account_name()

        connect = self.connect_sql.connect_tuqiang_sql()
        cursor = connect.cursor()
        get_account_sql = "select o.account from equipment_mostly e inner join user_info o on e.userId = o.userId where e.imei = '%s';" % imei_in_list
        cursor.execute(get_account_sql)
        account_data = cursor.fetchall()
        account = account_data[0][0]
        cursor.close()
        connect.close()

        self.assertEqual(dev_account_name, account)

        # 搜索右侧客户树
        # 循环点击5次
        for n in range(5):
            self.driver.click_element('x,//*[@id="treeDemo_device_sale_id_%s_span"]' % str(n + 1))
            sleep(2)
            # 判断数量
            get_account_dev_number = self.driver.get_text('x,//*[@id="treeDemo_device_sale_id_%s_span"]' % str(n + 1))

            name = self.dev_manage_page.get_select_account_name()
            self.assertEqual(get_account_dev_number, name)

        # 搜索无数据
        self.dev_manage_page.search_customer_after_click_batch_sale_dev('无数据')
        get_text = self.dev_manage_page.get_search_customer_no_data_text_after_batch_sale_dev()
        self.assertIn(self.assert_text.account_center_page_no_data_text(), get_text)

        # 获取选中设备的数量
        dev_number = self.dev_manage_page.get_select_dev_number()

        # 获取抬头设备统计的数量
        dev_numbers_count = self.dev_manage_page.get_dev_numbers()
        self.assertEqual(str(dev_number), dev_numbers_count)

        # 删除设备后 点击销售
        self.dev_manage_page.click_detele_dev()
        self.dev_manage_page.click_sale_button()

        ### 添加设备
        # 成功添加的
        self.dev_manage_page.add_dev_to_sale(imei_in_list)

        # 添加重复的
        self.dev_manage_page.add_dev_to_sale(imei_in_list)

        # 获取失败后的imei
        imei_after_add_fail = self.dev_manage_page.get_imei_after_add_fail()
        self.assertEqual(imei_in_list, imei_after_add_fail)

        status = self.dev_manage_page.get_status_after_add_fail()
        self.assertEqual(self.assert_text.dev_page_fail_text(), status)

        fail_reason = self.dev_manage_page.get_fail_reason()
        self.assertEqual(self.assert_text.dev_page_repetition_text(), fail_reason)
        self.dev_manage_page.click_close_fail()

        # 添加不存在的imei
        self.dev_manage_page.add_dev_to_sale('我就是要添加不存在的')
        # 获取失败后的imei
        imei_after_add_fail = self.dev_manage_page.get_imei_after_add_fail()
        self.assertEqual('我就是要添加不存在的', imei_after_add_fail)

        status = self.dev_manage_page.get_status_after_add_fail()
        self.assertEqual(self.assert_text.dev_page_fail_text(), status)

        fail_reason = self.dev_manage_page.get_fail_reason()
        self.assertEqual(self.assert_text.dev_page_inexistence_text(), fail_reason)
        self.dev_manage_page.click_close_fail()
