import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


class TestCase82DevManageBatchSale(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.dev_manage_page_read_csv = DevManagePageReadCsv()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.assert_text = AssertText()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_dev_manage_batch_sale(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.log_in_base.log_in()
        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()
        # 选择一个设备点击批量销售
        self.dev_manage_page.choose_one_dev_to_search()
        get_first_imei = self.dev_manage_page.get_first_imei_in_list()
        get_dev_type = self.dev_manage_page.get_dev_type_in_list()
        # 点击批量
        self.dev_manage_page.click_batch_sale_button()
        self.dev_manage_page.click_close_batch_sale_button()
        self.dev_manage_page.click_batch_sale_button()

        '''# 搜索右侧客户树
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
        self.assertEqual(str(dev_number), dev_numbers_count)'''

        # 验证界面
        get_sale_title = self.dev_manage_page.get_sale_title_text_in_sale_dev()
        self.assertEqual(self.assert_text.batch_sale_text(), get_sale_title)

        get_imei_in_sale = self.dev_manage_page.get_batch_sale_imei_in_sale_dev()
        self.assertEqual(get_first_imei, get_imei_in_sale)

        get_dev_type_in_sale = self.dev_manage_page.get_dev_type_in_sale()
        self.assertEqual(get_dev_type, get_dev_type_in_sale)

        get_dev_number = self.dev_manage_page.get_dev_number_in_sale_dev()
        self.assertEqual('1', get_dev_number)

        get_dev_account = self.dev_manage_page.get_dev_account_name()
        connect_sql = ConnectSql()
        connect = connect_sql.connect_tuqiang_sql()
        cursor = connect.cursor()
        sql = "select m.account from equipment_mostly m where m.imei = '%s';" % get_first_imei
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        connect.close()

        sql_account = data[0][0]
        self.assertEqual(get_dev_account, sql_account)

        # 输入不存在的IMEI号进行添加
        self.dev_manage_page.add_imei_in_sale_dev_page('bucunzai')

        add_dev_state = self.dev_manage_page.add_dev_after_fail_state()
        self.assertEqual(self.assert_text.dev_page_fail_text(), add_dev_state)
        add_dev_reason = self.dev_manage_page.add_dev_after_fail_reason()
        self.assertEqual(self.assert_text.dev_page_inexistence_text(), add_dev_reason)
        self.dev_manage_page.click_close_fails()
        # 添加不属于当前登陆账号设备总进货数中的设备
        self.dev_manage_page.add_imei_in_sale_dev_page('863666010079196')

        add_dev_state = self.dev_manage_page.add_dev_after_fail_state()
        self.assertEqual(self.assert_text.dev_page_fail_text(), add_dev_state)
        add_dev_reason = self.dev_manage_page.add_dev_after_fail_reason()
        self.assertEqual(self.assert_text.dev_page_inexistence_text(), add_dev_reason)
        self.dev_manage_page.click_close_fails()
        # 添加与设备列表中重复的设备
        self.dev_manage_page.add_imei_in_sale_dev_page(get_first_imei)

        add_dev_state = self.dev_manage_page.add_dev_after_fail_state()
        self.assertEqual(self.assert_text.dev_page_fail_text(), add_dev_state)
        add_dev_reason = self.dev_manage_page.add_dev_after_fail_reason()
        self.assertEqual(self.assert_text.dev_page_repetition_text(), add_dev_reason)
        self.dev_manage_page.click_close_fails()

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
