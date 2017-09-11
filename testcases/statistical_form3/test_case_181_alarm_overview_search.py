import csv
import unittest
import time

import requests

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from model.send_mail import request_base_url
from pages.alarm_info.alarm_info_page import AlarmInfoPage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.search_sql import SearchSql
from pages.statistical_form.statistic_form_page3 import StatisticFormPage3
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv


class TestCase181AlarmOverviewSearch(unittest.TestCase):
    # 告警总览页面搜索


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
        self.statistical_form_page3 = StatisticFormPage3(self.driver, self.base_url)
        self.seasrch_sql = SearchSql(self.driver, self.base_url)
        self.connect_sql = ConnectSql()
        self.assert_text = AssertText()

        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.driver.clear_cookies()
        self.log_in_base.log_in_jimitest()

        # 登录之后点击控制台，然后点击指令管理
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_alarm_overview_search(self):
        # 断言url
        expect_url = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url, self.alarm_info_page.actual_url_click_alarm())

        # 点击告警总览
        self.alarm_info_page.click_alarm_overview_list()
        # 选择全部告警类型
        self.statistical_form_page3.select_all_alarm_type_in_alarm_overview_search()
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
                'end_time': row[3],
                'is_next': row[4],
                'is_enter_dev': row[5]
            }
            self.statistical_form_page3.add_data_to_search_in_alarm_overview(data)

            # 开始时间和结束时间
            begin_time = self.statistical_form_page3.get_alarm_overview_form_begin_time()
            end_time = self.statistical_form_page3.get_alarm_overview_form_end_time()
            # 全部告警类型
            alarm_type = '1,10,11,12,128,13,14,15,16,17,18,19,192,194,195,2,22,23,3,4,5,6,9,90,ACC_OFF,ACC_ON,in,offline,out,overSpeed,sensitiveAreasFence,stayAlert,stayTimeIn,stayTimeOut'
            all_dev = self.seasrch_sql.search_current_account_equipment(data['user_name'])
            imeis = self.statistical_form_page3.change_dev_imei_format(all_dev)
            # 用户id
            get_current_userid = self.seasrch_sql.search_current_account_user_id(data['user_name'])
            # 全父id
            get_current_full_id = self.seasrch_sql.search_current_account_user_full_id(data['user_name'])
            # 请求url
            request_url = request_base_url()

            if data['is_enter_dev'] == '1':
                request_params = {
                    '_method_': 'getAlarmSummary',
                    'imeis': imeis,
                    'startTime': begin_time,
                    'endTime': end_time,
                    'status': alarm_type,
                    'userIds': get_current_userid
                }
                res = requests.post(request_url, data=request_params)
                time.sleep(10)
                response = res.json()

                # 判断有没有数据
                no_data_display = self.statistical_form_page3.get_no_data_display_in_alarm_overview()
                if no_data_display == 'display: block;':
                    print(response)
                    self.assertEqual(400, response['code'])
                    self.assertEqual('没有找到数据', response['msg'])

                else:
                    # 获取页面上的数据
                    web_total_number = self.statistical_form_page3.get_web_total_number_alarm_overview()
                    web_data = []
                    for n in range(web_total_number):
                        web_data.append({
                            'imei': self.statistical_form_page3.get_imei_in_alarm_overview(n),
                            'sos': self.statistical_form_page3.get_sos_number_in_alarm_overview(n),
                            'blindAreaEnter': self.statistical_form_page3.get_blind_area_enter_in_alarm_overview(
                                n),
                            'blindAreaExit': self.statistical_form_page3.get_blind_area_exit_in_alarm_overview(
                                n),
                            'bootingNotification': self.statistical_form_page3.booting_notification_in_alarm_overview(
                                n),
                            'rearviewMirrorVibrationAlert': self.statistical_form_page3.first_fix_notification_in_alarm_overview(
                                n),
                            'firstFixNotification': self.statistical_form_page3.get_low_external_power_in_alarm_overview(
                                n),
                            'lowExternalPower': self.statistical_form_page3.get_low_power_protection_in_alarm_overview(
                                n),
                            'lowPowerProtection': self.statistical_form_page3.get_sim_card_change_in_alarm_overview(
                                n),
                            'simCardChange': self.statistical_form_page3.get_over_speed_in_alarm_overview(n),
                            'powerOff': self.statistical_form_page3.get_power_off_in_alarm_overview(n),
                            'airplaneModeAfterLowPowerProtection': self.statistical_form_page3.airplane_mode_after_low_power_protection_in_alarm_overview(
                                n),
                            'disassembly': self.statistical_form_page3.disassembly_in_alarm_overview(n),
                            'illegalMobileAlert': self.statistical_form_page3.get_cut_power_in_alarm_overview(
                                n),
                            'insufficientBatteryBackupAlert': self.statistical_form_page3.get_vibration_in_alarm_overview(
                                n),
                            'overStepAlert': self.statistical_form_page3.get_movement_in_alarm_overview(n),
                            'cutPower': self.statistical_form_page3.get_low_power_in_alarm_overview(n),
                            'voice': self.statistical_form_page3.get_exit_geozone_in_alarm_overview(n),
                            'lingerAlert': self.statistical_form_page3.enter_geozone_in_alarm_overview(n),
                            'vibration': self.statistical_form_page3.rearview_mirror_vibration_alert_in_alarm_overview(
                                n),
                            'enterTerminalGeozone': self.statistical_form_page3.get_enter_terminal_geozone_in_alarm_overview(
                                n),
                            'exitTerminalGeozone': self.statistical_form_page3.get_exit_terminal_geozone_in_alarm_overview(
                                n),
                            'overspeed': self.statistical_form_page3.get_off_line_in_alarm_overview(n),
                            'movement': self.statistical_form_page3.get_voice_in_alarm_overview(n),
                            'lowPower': self.statistical_form_page3.get_acc_open_in_alarm_overview(n),
                            'accOpen': self.statistical_form_page3.get_acc_shut_down_in_alarm_overview(n),
                            'accShutdown': self.statistical_form_page3.get_long_time_not_out_fence_in_alarm_overview(
                                n),
                            'enterGeozone': self.statistical_form_page3.get_long_time_not_into_fence_in_alarm_overview(
                                n),
                            'offline': self.statistical_form_page3.get_stay_alert_in_alarm_overview(n),
                            'exitGeozone': self.statistical_form_page3.get_linger_alert_in_alarm_overview(n),
                            'overspeedPlatform': self.statistical_form_page3.get_illegal_mobile_alert_in_alarm_overview(
                                n),
                            'sensitiveAreasFence': self.statistical_form_page3.insufficient_battery_back_up_alert_in_alarm_overview(
                                n),
                            'stayAlert': self.statistical_form_page3.get_over_step_alert_in_alarm_overview(n),
                            'longtimeNotIntoFence': self.statistical_form_page3.get_sensitive_areas_fence_in_alarm_overview(
                                n),
                            'longtimeNotOutFence': self.statistical_form_page3.get_over_speed_platform_in_alarm_overview(
                                n)
                        })
                    print(web_data)
                    res_data = response['data']
                    for data_1 in res_data:
                        del data_1['carCrash'], data_1['dvrVibration'], data_1['overspeedDVR'], data_1[
                            'rapidAcceleration'], data_1['rapidDeceleration'], data_1['sharpTurn'], data_1['status']
                    print(res_data)
                    # self.assertEqual(web_data, res_data)
                    self.assertEqual(len(web_data), len(res_data))
                    for datas in web_data:
                        self.assertIn(datas, res_data)

                    for datas2 in res_data:
                        self.assertIn(datas2, web_data)

            elif data['is_enter_dev'] == '0':
                if data['is_next'] == '0':
                    request_params = {
                        '_method_': 'getAlarmSummary',
                        'userIds': get_current_userid,
                        'startTime': begin_time,
                        'endTime': end_time,
                        'status': alarm_type,
                    }
                    res = requests.post(request_url, data=request_params)
                    time.sleep(10)
                    response = res.json()
                    res_data = response['data']
                    for data_1 in res_data:
                        del data_1['carCrash'], data_1['dvrVibration'], data_1['overspeedDVR'], data_1[
                            'rapidAcceleration'], data_1['rapidDeceleration'], data_1['sharpTurn'], data_1['status']
                    print(res_data)
                    # 获取页面上的数据
                    web_total_number = self.statistical_form_page3.get_web_total_number_alarm_overview()
                    web_data = []
                    for n in range(web_total_number):
                        web_data.append({
                            'imei': self.statistical_form_page3.get_imei_in_alarm_overview(n),
                            'sos': self.statistical_form_page3.get_sos_number_in_alarm_overview(n),
                            'blindAreaEnter': self.statistical_form_page3.get_blind_area_enter_in_alarm_overview(
                                n),
                            'blindAreaExit': self.statistical_form_page3.get_blind_area_exit_in_alarm_overview(
                                n),
                            'bootingNotification': self.statistical_form_page3.booting_notification_in_alarm_overview(
                                n),
                            'rearviewMirrorVibrationAlert': self.statistical_form_page3.first_fix_notification_in_alarm_overview(
                                n),
                            'firstFixNotification': self.statistical_form_page3.get_low_external_power_in_alarm_overview(
                                n),
                            'lowExternalPower': self.statistical_form_page3.get_low_power_protection_in_alarm_overview(
                                n),
                            'lowPowerProtection': self.statistical_form_page3.get_sim_card_change_in_alarm_overview(
                                n),
                            'simCardChange': self.statistical_form_page3.get_over_speed_in_alarm_overview(n),
                            'powerOff': self.statistical_form_page3.get_power_off_in_alarm_overview(n),
                            'airplaneModeAfterLowPowerProtection': self.statistical_form_page3.airplane_mode_after_low_power_protection_in_alarm_overview(
                                n),
                            'disassembly': self.statistical_form_page3.disassembly_in_alarm_overview(n),
                            'illegalMobileAlert': self.statistical_form_page3.get_cut_power_in_alarm_overview(
                                n),
                            'insufficientBatteryBackupAlert': self.statistical_form_page3.get_vibration_in_alarm_overview(
                                n),
                            'overStepAlert': self.statistical_form_page3.get_movement_in_alarm_overview(n),
                            'cutPower': self.statistical_form_page3.get_low_power_in_alarm_overview(n),
                            'voice': self.statistical_form_page3.get_exit_geozone_in_alarm_overview(n),
                            'lingerAlert': self.statistical_form_page3.enter_geozone_in_alarm_overview(n),
                            'vibration': self.statistical_form_page3.rearview_mirror_vibration_alert_in_alarm_overview(
                                n),
                            'enterTerminalGeozone': self.statistical_form_page3.get_enter_terminal_geozone_in_alarm_overview(
                                n),
                            'exitTerminalGeozone': self.statistical_form_page3.get_exit_terminal_geozone_in_alarm_overview(
                                n),
                            'overspeed': self.statistical_form_page3.get_off_line_in_alarm_overview(n),
                            'movement': self.statistical_form_page3.get_voice_in_alarm_overview(n),
                            'lowPower': self.statistical_form_page3.get_acc_open_in_alarm_overview(n),
                            'accOpen': self.statistical_form_page3.get_acc_shut_down_in_alarm_overview(n),
                            'accShutdown': self.statistical_form_page3.get_long_time_not_out_fence_in_alarm_overview(
                                n),
                            'enterGeozone': self.statistical_form_page3.get_long_time_not_into_fence_in_alarm_overview(
                                n),
                            'offline': self.statistical_form_page3.get_stay_alert_in_alarm_overview(n),
                            'exitGeozone': self.statistical_form_page3.get_linger_alert_in_alarm_overview(n),
                            'overspeedPlatform': self.statistical_form_page3.get_illegal_mobile_alert_in_alarm_overview(
                                n),
                            'sensitiveAreasFence': self.statistical_form_page3.insufficient_battery_back_up_alert_in_alarm_overview(
                                n),
                            'stayAlert': self.statistical_form_page3.get_over_step_alert_in_alarm_overview(n),
                            'longtimeNotIntoFence': self.statistical_form_page3.get_sensitive_areas_fence_in_alarm_overview(
                                n),
                            'longtimeNotOutFence': self.statistical_form_page3.get_over_speed_platform_in_alarm_overview(
                                n)
                        })
                    print(web_data)
                    self.assertEqual(len(web_data), len(res_data))
                    for datas in web_data:
                        self.assertIn(datas, res_data)

                    for datas2 in res_data:
                        self.assertIn(datas2, web_data)


                elif data['is_next'] == '1':
                    request_params = {
                        '_method_': 'getAlarmSummary',
                        'currentUser': get_current_full_id,
                        'startTime': begin_time,
                        'endTime': end_time,
                        'status': alarm_type,
                        'childUserFlag': '1'
                    }
                    res = requests.post(request_url, data=request_params)
                    time.sleep(10)
                    response = res.json()
                    res_data = response['data']
                    for data_1 in res_data:
                        del data_1['carCrash'], data_1['dvrVibration'], data_1['overspeedDVR'], data_1[
                            'rapidAcceleration'], data_1['rapidDeceleration'], data_1['sharpTurn'], data_1['status']
                    print(res_data)
                    # 获取页面上的数据
                    web_total_number = self.statistical_form_page3.get_web_total_number_alarm_overview()
                    web_data = []
                    for n in range(web_total_number):
                        web_data.append({
                            'imei': self.statistical_form_page3.get_imei_in_alarm_overview(n),
                            'sos': self.statistical_form_page3.get_sos_number_in_alarm_overview(n),
                            'blindAreaEnter': self.statistical_form_page3.get_blind_area_enter_in_alarm_overview(
                                n),
                            'blindAreaExit': self.statistical_form_page3.get_blind_area_exit_in_alarm_overview(
                                n),
                            'bootingNotification': self.statistical_form_page3.booting_notification_in_alarm_overview(
                                n),
                            'rearviewMirrorVibrationAlert': self.statistical_form_page3.first_fix_notification_in_alarm_overview(
                                n),
                            'firstFixNotification': self.statistical_form_page3.get_low_external_power_in_alarm_overview(
                                n),
                            'lowExternalPower': self.statistical_form_page3.get_low_power_protection_in_alarm_overview(
                                n),
                            'lowPowerProtection': self.statistical_form_page3.get_sim_card_change_in_alarm_overview(
                                n),
                            'simCardChange': self.statistical_form_page3.get_over_speed_in_alarm_overview(n),
                            'powerOff': self.statistical_form_page3.get_power_off_in_alarm_overview(n),
                            'airplaneModeAfterLowPowerProtection': self.statistical_form_page3.airplane_mode_after_low_power_protection_in_alarm_overview(
                                n),
                            'disassembly': self.statistical_form_page3.disassembly_in_alarm_overview(n),
                            'illegalMobileAlert': self.statistical_form_page3.get_cut_power_in_alarm_overview(
                                n),
                            'insufficientBatteryBackupAlert': self.statistical_form_page3.get_vibration_in_alarm_overview(
                                n),
                            'overStepAlert': self.statistical_form_page3.get_movement_in_alarm_overview(n),
                            'cutPower': self.statistical_form_page3.get_low_power_in_alarm_overview(n),
                            'voice': self.statistical_form_page3.get_exit_geozone_in_alarm_overview(n),
                            'lingerAlert': self.statistical_form_page3.enter_geozone_in_alarm_overview(n),
                            'vibration': self.statistical_form_page3.rearview_mirror_vibration_alert_in_alarm_overview(
                                n),
                            'enterTerminalGeozone': self.statistical_form_page3.get_enter_terminal_geozone_in_alarm_overview(
                                n),
                            'exitTerminalGeozone': self.statistical_form_page3.get_exit_terminal_geozone_in_alarm_overview(
                                n),
                            'overspeed': self.statistical_form_page3.get_off_line_in_alarm_overview(n),
                            'movement': self.statistical_form_page3.get_voice_in_alarm_overview(n),
                            'lowPower': self.statistical_form_page3.get_acc_open_in_alarm_overview(n),
                            'accOpen': self.statistical_form_page3.get_acc_shut_down_in_alarm_overview(n),
                            'accShutdown': self.statistical_form_page3.get_long_time_not_out_fence_in_alarm_overview(
                                n),
                            'enterGeozone': self.statistical_form_page3.get_long_time_not_into_fence_in_alarm_overview(
                                n),
                            'offline': self.statistical_form_page3.get_stay_alert_in_alarm_overview(n),
                            'exitGeozone': self.statistical_form_page3.get_linger_alert_in_alarm_overview(n),
                            'overspeedPlatform': self.statistical_form_page3.get_illegal_mobile_alert_in_alarm_overview(
                                n),
                            'sensitiveAreasFence': self.statistical_form_page3.insufficient_battery_back_up_alert_in_alarm_overview(
                                n),
                            'stayAlert': self.statistical_form_page3.get_over_step_alert_in_alarm_overview(n),
                            'longtimeNotIntoFence': self.statistical_form_page3.get_sensitive_areas_fence_in_alarm_overview(
                                n),
                            'longtimeNotOutFence': self.statistical_form_page3.get_over_speed_platform_in_alarm_overview(
                                n)
                        })
                    print(web_data)
                    self.assertEqual(len(web_data), len(res_data))
                    for datas in web_data:
                        self.assertIn(datas, res_data)

                    for datas2 in res_data:
                        self.assertIn(datas2, web_data)

            self.driver.default_frame()
        csv_file.close()
