import csv
import unittest
import time
from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.alarm_info.alarm_info_page import AlarmInfoPage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page2 import StatisticalFormPage2
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv


class TestCase170AlarmOverviewSearch(unittest.TestCase):
    '''
    用例第138条，告警总览页面搜索
    author：zhangAo
    '''

    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.alarm_info_page = AlarmInfoPage(self.driver, self.base_url)
        self.statistical_form_page_read_csv = StatisticalFormPageReadCsv()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.statistical_form_page = StatisticalFormPage(self.driver, self.base_url)
        self.statistical_form_page2 = StatisticalFormPage2(self.driver, self.base_url)
        self.connect_sql = ConnectSql()

        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.base_page.click_chinese_button()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.assert_text = AssertText()
        self.log_in_base.log_in_jimitest()
        time.sleep(1)

        # 登录之后点击控制台，然后点击指令管理
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_138_alarm_overview_search(self):
        # 断言url
        expect_url = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url, self.alarm_info_page.actual_url_click_alarm())

        # 点击告警总览
        self.alarm_info_page.click_alarm_overview_list()

        # 输入数据搜索
        csv_file = self.statistical_form_page_read_csv.read_csv('alarm_overview_search_data.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            data = {
                'user_name': row[0],
                'choose_date': row[1],
                'began_time': row[2],
                'end_time': row[3]
            }
            self.alarm_info_page.add_data_to_search_in_alarm_overview(data)

            # 获取搜索出的条数
            web_total = self.alarm_info_page.get_web_total_in_overview_search()
            if web_total == 0:
                self.assertIn(self.assert_text.account_center_page_no_data_text(),
                              self.statistical_form_page.get_no_data_text_in_alarm_overview_page())
            else:
                self.driver.switch_to_frame('x,//*[@id="alarmOverviewFrame"]')
                # sos报警总数
                sos_alarm_total = self.statistical_form_page.get_sos_total_alarm_number()
                list_sos_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page.get_list_sos_alarm_total_number(n)
                    list_sos_alarm_total.append(int(number))
                self.assertEqual(sos_alarm_total, str(sum(list_sos_alarm_total)), "sos报警数显示不一致")

                # 进卫星盲区报警总数
                enter_satellite_dead_zone_alarm_total = self.statistical_form_page.get_enter_satellite_dead_zone_alarm_total()
                list_enter_satellite_dead_zone_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page.get_list_enter_satellite_dead_zone_alarm_total_number(n)
                    list_enter_satellite_dead_zone_alarm_total.append(int(number))
                self.assertEqual(enter_satellite_dead_zone_alarm_total,
                                 str(sum(list_enter_satellite_dead_zone_alarm_total)), "进卫星盲区报警总数数显示不一致")

                # 出卫星盲区报警
                out_satellite_dead_zone_alarm_total = self.statistical_form_page2.get_out_satellite_dead_zone_alarm_total()
                list_out_satellite_dead_zone_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_out_satellite_dead_zone_alarm_total_number(n)
                    list_out_satellite_dead_zone_alarm_total.append(int(number))
                self.assertEqual(out_satellite_dead_zone_alarm_total,
                                 str(sum(list_out_satellite_dead_zone_alarm_total)), "出卫星盲区报警数显示不一致")

                # 开机报警
                starting_up_alarm_total = self.statistical_form_page2.get_starting_up_alarm_total()
                list_starting_up_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_starting_up_alarm_total_number(n)
                    list_starting_up_alarm_total.append(int(number))
                self.assertEqual(starting_up_alarm_total,
                                 str(sum(list_starting_up_alarm_total)), "开机报警数显示不一致")

                # 后视镜震动报警
                rearview_mirror_vibration_alarm_total = self.statistical_form_page2.get_rearview_mirror_vibration_alarm_total()
                list_rearview_mirror_vibration_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_rearview_mirror_vibration_alarm_total_number(n)
                    list_rearview_mirror_vibration_alarm_total.append(int(number))
                self.assertEqual(rearview_mirror_vibration_alarm_total,
                                 str(sum(list_rearview_mirror_vibration_alarm_total)), "后视镜震动报警数显示不一致")

                # 卫星第一次定位报警
                satellite_first_alarm_total = self.statistical_form_page2.get_satellite_first_positioning_alarm_total()
                list_satellite_first_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_satellite_first_positioning_alarm_total_number(n)
                    list_satellite_first_alarm_total.append(int(number))
                self.assertEqual(satellite_first_alarm_total,
                                 str(sum(list_satellite_first_alarm_total)), "卫星第一次定位报警数显示不一致")

                # 外电低电报警
                outer_low_electricity_alarm_total = self.statistical_form_page2.get_outer_low_electricity_alarm_total()
                list_outer_low_electricity_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_outer_low_electricity_alarm_total_number(n)
                    list_outer_low_electricity_alarm_total.append(int(number))
                self.assertEqual(outer_low_electricity_alarm_total,
                                 str(sum(list_outer_low_electricity_alarm_total)), "外电低电报警数显示不一致")

                # 外电低电保护报警
                electricity_protect_alarm_total = self.statistical_form_page2.get_outer_low_electricity_protect_alarm_total()
                list_electricity_protect_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_outer_low_electricity_protect_alarm_total_number(n)
                    list_electricity_protect_alarm_total.append(int(number))
                self.assertEqual(electricity_protect_alarm_total,
                                 str(sum(list_electricity_protect_alarm_total)), "外电低电保护报警数显示不一致")

                # 换卡报警
                change_card_alarm_total = self.statistical_form_page2.get_change_card_alarm_total()
                list_change_card_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_change_card_alarm_total_number(n)
                    list_change_card_alarm_total.append(int(number))
                self.assertEqual(change_card_alarm_total,
                                 str(sum(list_change_card_alarm_total)), "换卡报警数显示不一致")

                # 关机报警
                shutdown_alarm_total = self.statistical_form_page2.get_shutdown_alarm_total()
                list_shutdown_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_shutdown_alarm_total_number(n)
                    list_shutdown_alarm_total.append(int(number))
                self.assertEqual(shutdown_alarm_total,
                                 str(sum(list_shutdown_alarm_total)), "关机报警数显示不一致")

                # 外电低电保护后飞行模式报警
                flight_mode_alarm_total = self.statistical_form_page2.get_flight_mode_alarm_total()
                list_flight_mode_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_flight_mode_alarm_total_number(n)
                    list_flight_mode_alarm_total.append(int(number))
                self.assertEqual(flight_mode_alarm_total,
                                 str(sum(list_flight_mode_alarm_total)), "外电低电保护后飞行模式报警数显示不一致")

                # 拆卸报警
                disassembly_alarm_total = self.statistical_form_page2.get_disassembly_alarm_total()
                list_disassembly_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_disassembly_alarm_total_number(n)
                    list_disassembly_alarm_total.append(int(number))
                self.assertEqual(disassembly_alarm_total,
                                 str(sum(list_disassembly_alarm_total)), "拆卸报警数显示不一致")

                # 非法移动告警
                illegal_move_alarm_total = self.statistical_form_page2.get_illegal_move_alarm_total()
                list_illegal_move_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_illegal_move_alarm_total_number(n)
                    list_illegal_move_alarm_total.append(int(number))
                self.assertEqual(illegal_move_alarm_total,
                                 str(sum(list_illegal_move_alarm_total)), "非法移动告警数显示不一致")

                # 后备电池电量不足告警
                low_battery_alarm_total = self.statistical_form_page2.get_reserve_battery_low_battery_alarm_total()
                list_low_battery_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_reserve_battery_low_battery_alarm_total_number(n)
                    list_low_battery_alarm_total.append(int(number))
                self.assertEqual(low_battery_alarm_total,
                                 str(sum(list_low_battery_alarm_total)), "后备电池电量不足告警数显示不一致")

                # 越界告警
                across_boundaries_alarm_total = self.statistical_form_page2.get_across_boundaries_alarm_total()
                list_across_boundaries_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_across_boundaries_alarm_total_number(n)
                    list_across_boundaries_alarm_total.append(int(number))
                self.assertEqual(across_boundaries_alarm_total,
                                 str(sum(list_across_boundaries_alarm_total)), "越界告警数显示不一致")

                # 断电报警
                power_outages_alarm_total = self.statistical_form_page2.get_power_outages_alarm_total()
                list_power_outages_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_power_outages_alarm_total_number(n)
                    list_power_outages_alarm_total.append(int(number))
                self.assertEqual(power_outages_alarm_total,
                                 str(sum(list_power_outages_alarm_total)), "断电报警数显示不一致")

                # 声控报警
                acoustic_alarm_total = self.statistical_form_page2.get_acoustic_alarm_total()
                list_acoustic_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_acoustic_alarm_total_number(n)
                    list_acoustic_alarm_total.append(int(number))
                self.assertEqual(acoustic_alarm_total,
                                 str(sum(list_acoustic_alarm_total)), "声控报警数显示不一致")

                # 伪基站报警
                pseudo_base_station_alarm_total = self.statistical_form_page2.get_pseudo_base_station_alarm_total()
                list_pseudo_base_station_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_pseudo_base_station_alarm_total_number(n)
                    list_pseudo_base_station_alarm_total.append(int(number))
                self.assertEqual(pseudo_base_station_alarm_total,
                                 str(sum(list_pseudo_base_station_alarm_total)), "伪基站报警数显示不一致")
                # 震动报警
                vibration_alarm_total = self.statistical_form_page2.get_vibration_alarm_total()
                list_vibration_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_vibration_alarm_total_number(n)
                    list_vibration_alarm_total.append(int(number))
                self.assertEqual(vibration_alarm_total,
                                 str(sum(list_vibration_alarm_total)), "震动报警数显示不一致")

                # 进入电子围栏
                enter_electronic_fence_total = self.statistical_form_page2.get_enter_electronic_fence_alarm_total()
                list_enter_electronic_fence_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_enter_electronic_fence_alarm_total_number(n)
                    list_enter_electronic_fence_total.append(int(number))
                self.assertEqual(enter_electronic_fence_total,
                                 str(sum(list_enter_electronic_fence_total)), "进入电子围栏数显示不一致")

                # 离开电子围栏
                leave_electronic_fence_total = self.statistical_form_page2.get_leave_electronic_fence_alarm_total()
                list_leave_electronic_fence_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_leave_electronic_fence_alarm_total_number(n)
                    list_leave_electronic_fence_total.append(int(number))
                self.assertEqual(leave_electronic_fence_total,
                                 str(sum(list_leave_electronic_fence_total)), "离开电子围栏数显示不一致")

                # 超速报警
                super_speed_alarm_total = self.statistical_form_page2.get_super_speed_alarm_total()
                list_super_speed_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_super_speed_alarm_total_number(n)
                    list_super_speed_alarm_total.append(int(number))
                self.assertEqual(super_speed_alarm_total,
                                 str(sum(list_super_speed_alarm_total)), "超速报警数显示不一致")

                # 位移报警
                displacement_alarm_total = self.statistical_form_page2.get_displacement_alarm_total()
                list_displacement_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_displacement_alarm_total_number(n)
                    list_displacement_alarm_total.append(int(number))
                self.assertEqual(displacement_alarm_total,
                                 str(sum(list_displacement_alarm_total)), "位移报警数显示不一致")

                # 低电报警
                low_electricity_alarm_total = self.statistical_form_page2.get_low_electricity_alarm_total()
                list_low_electricity_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_low_electricity_alarm_total_number(n)
                    list_low_electricity_alarm_total.append(int(number))
                self.assertEqual(low_electricity_alarm_total,
                                 str(sum(list_low_electricity_alarm_total)), "低电报警数显示不一致")

                # ACC关闭
                acc_close_alarm_total = self.statistical_form_page2.get_acc_close_alarm_total()
                list_acc_close_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_acc_close_alarm_total_number(n)
                    list_acc_close_alarm_total.append(int(number))
                self.assertEqual(acc_close_alarm_total,
                                 str(sum(list_acc_close_alarm_total)), "ACC关闭数显示不一致")

                # ACC开启
                acc_open_alarm_total = self.statistical_form_page2.get_acc_open_alarm_total()
                list_acc_open_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_acc_open_alarm_total_number(n)
                    list_acc_open_alarm_total.append(int(number))
                self.assertEqual(acc_open_alarm_total,
                                 str(sum(list_acc_open_alarm_total)), "ACC开启数显示不一致")

                # 进入围栏
                enter_fence_alarm_total = self.statistical_form_page2.get_enter_fence_alarm_total()
                list_enter_fence_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_enter_fence_alarm_total_number(n)
                    list_enter_fence_alarm_total.append(int(number))
                self.assertEqual(enter_fence_alarm_total,
                                 str(sum(list_enter_fence_alarm_total)), "进入围栏数显示不一致")

                # 离线告警
                offline_alarm_total = self.statistical_form_page2.get_offline_alarm_total()
                list_offline_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_offline_alarm_total_number(n)
                    list_offline_alarm_total.append(int(number))
                self.assertEqual(offline_alarm_total,
                                 str(sum(list_offline_alarm_total)), "离线告警数显示不一致")

                # 离开围栏
                leave_fence_alarm_total = self.statistical_form_page2.get_leave_fence_alarm_total()
                list_leave_fence_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_leave_fence_alarm_total_number(n)
                    list_leave_fence_alarm_total.append(int(number))
                self.assertEqual(leave_fence_alarm_total,
                                 str(sum(list_leave_fence_alarm_total)), "离开围栏数显示不一致")

                # 黑车围栏告警
                illegal_taxis_fence_alarm_total = self.statistical_form_page2.get_illegal_taxis_fence_alarm_total()
                list_illegal_taxis_fence_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_illegal_taxis_fence_alarm_total_number(n)
                    list_illegal_taxis_fence_alarm_total.append(int(number))
                self.assertEqual(illegal_taxis_fence_alarm_total,
                                 str(sum(list_illegal_taxis_fence_alarm_total)), "黑车围栏告警数显示不一致")

                # 停留告警
                stay_alarm_total = self.statistical_form_page2.get_stay_alarm_total()
                list_stay_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_stay_alarm_total_number(n)
                    list_stay_alarm_total.append(int(number))
                self.assertEqual(stay_alarm_total,
                                 str(sum(list_stay_alarm_total)), "停留告警数显示不一致")

                # 长时间不进
                long_time_not_enter_alarm_total = self.statistical_form_page2.get_long_time_not_enter_alarm_total()
                list_long_time_not_enter_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_long_time_not_enter_alarm_total_number(n)
                    list_long_time_not_enter_alarm_total.append(int(number))
                self.assertEqual(long_time_not_enter_alarm_total,
                                 str(sum(list_long_time_not_enter_alarm_total)), "长时间不进数显示不一致")

                # 长时间不出
                long_time_not_out_alarm_total = self.statistical_form_page2.get_long_time_not_out_alarm_total()
                list_long_time_not_out_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page2.get_list_long_time_not_out_alarm_total_number(n)
                    list_long_time_not_out_alarm_total.append(int(number))
                self.assertEqual(long_time_not_out_alarm_total,
                                 str(sum(list_long_time_not_out_alarm_total)), "长时间不出数显示不一致")

                self.driver.default_frame()
                self.driver.wait()

        csv_file.close()
