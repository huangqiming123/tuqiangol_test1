import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from pages.alarm_info.alarm_info_page import AlarmInfoPage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase

from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page2 import StatisticalFormPage2
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv


# 告警统计--告警总览--异常搜索验证
# author:戴招利
class TestCase157AlarmOverviewExceptionSearch(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.alarm_info_page = AlarmInfoPage(self.driver, self.base_url)
        self.statistical_form_page_read_csv = StatisticalFormPageReadCsv()
        self.statistical_form_page = StatisticalFormPage(self.driver, self.base_url)
        self.statistical_form_page2 = StatisticalFormPage2(self.driver, self.base_url)
        self.alarm_info_page = AlarmInfoPage(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.assert_text = AssertText()

        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)

    def test_alarm_overview_exception_search(self):
        """
         告警总览页面，异常搜索数据验证
        """
        # 登录
        self.log_in_base.log_in_jimitest()
        # 点击进入统计报表、告警总览
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        self.alarm_info_page.click_alarm_overview_list()

        # 取开始、结束时间
        # data = ["#￥%@#￥！","销售","20002017","abcdyyyyyyy","测试01511abc_@!&","暂无数据"]
        type = ["今天", "本周", "昨天", "上周", "本月", "上月", "自定义"]
        data = ["暂无数据"]

        for time in type:
            time = self.statistical_form_page2.alarm_overview_validation_time(time)
            self.assertEqual(time["page_time"]["page_start_time"], time["sql_time"]["sql_start_time"], "实际与显示的开始时间不相符")
            self.assertEqual(time["page_time"]["page_end_time"], time["sql_time"]["sql_end_time"], "实际与显示的结束时间不相符")

        # 验证提示
        for user in data:
            text = self.statistical_form_page2.alarm_search_user(user)
            print(text)
            self.assertIn(user, text, "搜索后的数据不存在实际搜索出的数据中")

        # 验证搜索下级的imei可以搜索到
        # 填写下级的imei搜索
        sleep(2)
        self.statistical_form_page2.input_imei_to_search_in_alarm_overview_form(self.statistical_form_page2.get_imei())
        # 断言
        # 获取查询设备的imei
        search_imei = self.statistical_form_page2.get_search_imei_in_alarm_overview_form()
        self.assertEqual(search_imei, self.statistical_form_page2.get_imei())

        # 验证停机的设备无法搜索到
        self.statistical_form_page2.input_imei_to_search_in_alarm_overview_form(
            self.statistical_form_page2.get_shut_down_imei())
        # 获取搜索的数量
        get_number_after_search = self.statistical_form_page.get_number_after_search_in_alarm_overview_form()
        self.assertEqual(0, get_number_after_search)

        get_text_after_search = self.statistical_form_page.get_text_after_search_in_alarm_overview_form()
        self.assertIn(self.assert_text.account_center_page_no_data_text(), get_text_after_search)

        # 验证未激活的设备无法搜索到
        self.statistical_form_page2.input_imei_to_search_in_alarm_overview_form(
            self.statistical_form_page2.get_no_active_imei())
        # 获取搜索的数量
        get_number_after_search = self.statistical_form_page.get_number_after_search_in_alarm_overview_form()
        self.assertEqual(0, get_number_after_search)

        get_text_after_search = self.statistical_form_page.get_text_after_search_in_alarm_overview_form()
        self.assertIn(self.assert_text.account_center_page_no_data_text(), get_text_after_search)

        # 点击搜索用户--下拉框
        # self.statistical_form_page2.click_alarm_overview_pull_down()
        self.driver.wait()
        self.driver.default_frame()

        # 点击选择告警类型
        self.statistical_form_page2.click_setting_alarm_type()
        # 点击全选
        self.statistical_form_page2.click_alarm_type_all()

        # 验证勾选全选
        selected = self.statistical_form_page2.setting_alarm_type("保存")
        print(selected)
        for state in selected:
            self.assertEqual(False, state, "勾选全选后，存在未勾选的类型")

        # 保存成功后，验证是否为勾选状态
        self.statistical_form_page2.click_setting_alarm_type()
        selected_true = self.statistical_form_page2.setting_alarm_type("取消")
        print(selected_true)
        for state_true in selected_true:
            self.assertEqual(False, state_true, "全选保存后,再次点击查看勾选状态，状态显示错误")

        # 未勾选全选
        self.statistical_form_page2.click_setting_alarm_type()
        # 点击全选
        self.statistical_form_page2.click_alarm_type_all()

        no_choice = self.statistical_form_page2.setting_alarm_type("保存")
        print(no_choice)
        for state_false in no_choice:
            self.assertEqual(True, state_false, "取消全选保存后,再次点击查看勾选状态，状态显示错误")

        # 取消全选保存成功后，验证是否为勾选状态
        self.statistical_form_page2.click_setting_alarm_type()
        cancel = self.statistical_form_page2.setting_alarm_type("取消")
        print(cancel)
        for select_cancel in cancel:
            self.assertEqual(True, select_cancel, "取消全选保存后,再次点击查看勾选状态，状态显示错误")

    def tearDown(self):
        # 退出浏览器
        self.driver.quit_browser()
