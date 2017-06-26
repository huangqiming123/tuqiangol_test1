import unittest

from automate_driver.automate_driver import AutomateDriver
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


class TestCase1108DevManageEditDev(unittest.TestCase):
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
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_1108_dev_manage_edit_dev(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()
        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()

        imei_in_list = self.dev_manage_page.get_imei_in_list()
        active_time_in_list = self.dev_manage_page.get_active_time_in_list()
        expire_time_in_list = self.dev_manage_page.get_expire_time_in_list()
        dev_type_in_list = self.dev_manage_page.get_dev_type_in_list()
        dev_name_in_list = self.dev_manage_page.get_dev_name_in_list()
        dev_sim_in_list = self.dev_manage_page.get_dev_sim_in_list()
        dev_group_in_list = self.dev_manage_page.get_dev_group_in_list()
        # 点击批量
        self.dev_manage_page.click_edit_button()
        self.dev_manage_page.click_close_edit_button()
        self.dev_manage_page.click_edit_button()

        # 判断打开的编辑信息是否正确
        imei_in_detail = self.dev_manage_page.get_imei_in_detail()
        self.assertEqual(imei_in_list, imei_in_detail)

        active_time_in_detail = self.dev_manage_page.get_active_time_in_detail()
        self.assertEqual(active_time_in_list, active_time_in_detail)

        expire_time_in_detail = self.dev_manage_page.get_expire_time_in_detail()
        self.assertEqual(expire_time_in_list, expire_time_in_detail)

        dev_type_in_detail = self.dev_manage_page.get_dev_type_in_detail()
        self.assertEqual(dev_type_in_list, dev_type_in_detail)

        dev_name_in_detail = self.dev_manage_page.get_dev_name_in_detail()
        self.assertEqual(dev_name_in_list, dev_name_in_detail)

        dev_sim_in_detail = self.dev_manage_page.get_dev_sim_in_detail()
        self.assertEqual(dev_sim_in_list, dev_sim_in_detail)

        dev_group_in_detail = self.dev_manage_page.get_dev_group_in_detail()
        self.assertEqual(dev_group_in_list, dev_group_in_detail)

        # 判断 设备imei、设备类型、激活时间、平台到期时间、iccid、imsi是不可以编辑的
        imei_input = self.dev_manage_page.get_imei_input_value()
        self.assertEqual('true', imei_input)

        dev_type_input = self.dev_manage_page.get_dev_type_input_value()
        self.assertEqual('true', dev_type_input)

        active_time_input = self.dev_manage_page.get_active_time_input_value()
        self.assertEqual('true', active_time_input)

        expire_time_value = self.dev_manage_page.get_expire_time_value()
        self.assertEqual('true', expire_time_value)

        iccid_value = self.dev_manage_page.get_iccid_value()
        self.assertEqual('true', iccid_value)

        imsi_value = self.dev_manage_page.get_imsi_value()
        self.assertEqual('true', imsi_value)

        # 验证输入框的最大长度
        dev_name_max_len = self.dev_manage_page.get_dev_name_max_len()
        self.assertEqual('50', dev_name_max_len)

        dev_sim_max_len = self.dev_manage_page.get_dev_sim_max_len()
        self.assertEqual('20', dev_sim_max_len)

        dev_remark_max_len = self.dev_manage_page.get_dev_remark_max_len()
        self.assertEqual('500', dev_remark_max_len)

        # 点击客户信息
        self.dev_manage_page.click_cust_info_button()

        # 验证输入框的最大长度
        driver_name_max_len = self.dev_manage_page.get_driver_name_max_len()
        self.assertEqual('20', driver_name_max_len)

        driver_phone_max_len = self.dev_manage_page.click_driver_phone_max_len()
        self.assertEqual('20', driver_phone_max_len)

        driver_vehicle_number_max_len = self.dev_manage_page.driver_vehicle_number_max_len()
        self.assertEqual('50', driver_vehicle_number_max_len)

        driver_iccid_max_len = self.dev_manage_page.get_driver_iccid_max_len()
        self.assertEqual('18', driver_iccid_max_len)

        driver_sn_max_len = self.dev_manage_page.get_driver_sn_max_len()
        self.assertEqual('50', driver_sn_max_len)

        driver_car_frame_max_len = self.dev_manage_page.driver_car_frame_max_len()
        self.assertEqual('50', driver_car_frame_max_len)

        driver_engine_number_max_len = self.dev_manage_page.get_driver_engine_number_max_len()
        self.assertEqual('100', driver_engine_number_max_len)

        dev_install_address_max_len = self.dev_manage_page.get_dev_install_address_max_len()
        self.assertEqual('200', dev_install_address_max_len)

        dev_install_company_max_len = self.dev_manage_page.get_dev_install_company_max_len()
        self.assertEqual('100', dev_install_company_max_len)

        dev_install_position_max_len = self.dev_manage_page.get_dev_install_position_max_len()
        self.assertEqual('200', dev_install_position_max_len)

        dev_install_personnel_max_len = self.dev_manage_page.get_dev_install_personnel_max_len()
        self.assertEqual('50', dev_install_personnel_max_len)
