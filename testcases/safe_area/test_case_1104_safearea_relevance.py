import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.safe_area.safe_area_page import SafeAreaPage


class TestCase1104SafeAreaRelevance(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.safe_area_page = SafeAreaPage(self.driver, self.base_url)

        self.base_page.open_page()
        self.driver.set_window_max()
        self.log_in_base.log_in_jimitest()
        self.safe_area_page.click_control_after_click_safe_area()

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_1104_safe_area_relevance(self):
        # 断言url
        expect_url = self.base_url + "/safearea/geozonemap?flag=0"
        self.assertEqual(expect_url, self.driver.get_current_url())

        # 选择围栏
        self.safe_area_page.click_select_fence_button()
        # 点击关联
        self.safe_area_page.click_relevance_button()
        # 关闭
        self.safe_area_page.click_close()

        # 点击关联
        self.safe_area_page.click_relevance_button()
        # 关闭
        self.safe_area_page.click_cancel_edit()

        # 点击关联
        self.safe_area_page.click_relevance_button()
        # 循环点击左侧的客户树
        for n in range(5):
            self.safe_area_page.click_customer(n)
            # 获取右侧暂无数据的属性
            attribute = self.safe_area_page.get_no_data_attribute()
            if 'display: none;' in attribute:
                text = self.safe_area_page.get_text_no_data()
                self.assertEqual('  暂无数据 ', text)
            else:
                # 点击收起默认组
                self.safe_area_page.click_close_default_group()
                group_number = self.safe_area_page.get_total_group()
                for m in range(group_number):
                    # 点击每一个分组
                    group_total_dev = self.safe_area_page.get_total_dev_in_per_group(m)
                    self.safe_area_page.click_open_per_group(m)
                    list_total_dev = self.safe_area_page.get_list_dev_in_per_group(m)
                    self.assertEqual(group_total_dev, str(list_total_dev))

        # 验证已选中的设备数量和统计的是否一致
        count_dev_number = self.safe_area_page.get_count_dev_number()
        get_list_total_number = self.safe_area_page.get_list_total_number()
        self.assertEqual(str(get_list_total_number), count_dev_number)

        # 验证邮箱发送的按钮是否选中
        send_email = self.safe_area_page.get_send_email_button_value()
        if send_email == False:
            self.safe_area_page.click_send_email_button()
            send_emails = self.safe_area_page.get_send_email_button_value()
            self.assertEqual(True, send_emails)
            email_style = self.safe_area_page.get_email_style()
            self.assertEqual('block', email_style)

            '''# 验证邮箱的格式
            self.safe_area_page.add_email_to_check_email_type('sdfasf')
            self.safe_area_page.click_ensure()
            text = self.safe_area_page.get_text_after_ensure()
            self.assertEqual('邮箱格式错误.', text)

            self.safe_area_page.add_email_to_check_email_type('')
            self.safe_area_page.add_email_to_check_second_email_type('sdfasf')
            self.safe_area_page.click_ensure()
            text = self.safe_area_page.get_text_after_ensure()
            self.assertEqual('邮箱格式错误.', text)

            self.safe_area_page.add_email_to_check_email_type('')
            self.safe_area_page.add_email_to_check_second_email_type('')
            self.safe_area_page.add_email_to_check_third_email_type('sfdsaf')
            self.safe_area_page.click_ensure()
            text = self.safe_area_page.get_text_after_ensure()
            self.assertEqual('邮箱格式错误.', text)'''
        else:
            email_style = self.safe_area_page.get_email_style()
            self.assertEqual('block', email_style)

            '''# 验证邮箱的格式
            self.safe_area_page.add_email_to_check_email_type('sdfasf')
            self.safe_area_page.click_ensure()
            text = self.safe_area_page.get_text_after_ensures()
            self.assertEqual('邮箱格式错误.', text)

            self.safe_area_page.add_email_to_check_email_type('')
            self.safe_area_page.add_email_to_check_second_email_type('sdfasf')
            self.safe_area_page.click_ensure()
            text = self.safe_area_page.get_text_after_ensure()
            self.assertEqual('邮箱格式错误.', text)

            self.safe_area_page.add_email_to_check_email_type('')
            self.safe_area_page.add_email_to_check_second_email_type('')
            self.safe_area_page.add_email_to_check_third_email_type('sfdsaf')
            self.safe_area_page.click_ensure()
            text = self.safe_area_page.get_text_after_ensure()
            self.assertEqual('邮箱格式错误.', text)'''
