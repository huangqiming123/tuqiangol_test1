import csv
import unittest
from time import sleep
from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.assert_text2 import AssertText2
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.cust_manage.cust_manage_basic_info_and_add_cust_page import CustManageBasicInfoAndAddCustPage
from pages.cust_manage.cust_manage_lower_account_page import CustManageLowerAccountPage
from pages.cust_manage.cust_manage_page_read_csv import CustManagePageReadCsv
from pages.login.login_page import LoginPage


# 客户管理-编辑用户-验证指令权限
# author:戴招利
class TestCase730816CustManageEditUserCommandLimit(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.cust_manage_basic_info_and_add_cust_page = CustManageBasicInfoAndAddCustPage(self.driver, self.base_url)
        self.cust_manage_lower_account_page = CustManageLowerAccountPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.cust_manage_page_read_csv = CustManagePageReadCsv()
        self.assert_text = AssertText()
        self.assert_text2 = AssertText2()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_edit_account_command_limit_verify(self):
        '''测试客户管理-编辑指令权限后验证'''

        self.base_page.open_page()

        csv_file = self.cust_manage_page_read_csv.read_csv('add_user_command_limit_data.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            info = {
                "passwd": row[4],
                "command": row[9],
                "working_mode": row[10],
                "wdit_account": row[11]
            }

            # 登录
            self.log_in_base.log_in()

            # 进入客户管理页面
            self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()
            # 搜索账号
            self.cust_manage_lower_account_page.input_search_info(info["wdit_account"])
            # 搜索
            self.cust_manage_lower_account_page.click_search_btn()

            # 点击编辑用户
            self.cust_manage_basic_info_and_add_cust_page.click_edit_customer()
            self.cust_manage_basic_info_and_add_cust_page.click_cancel_edit()
            self.cust_manage_basic_info_and_add_cust_page.click_edit_customer()
            self.cust_manage_basic_info_and_add_cust_page.locate_to_iframe()

            # 是或否批量下发指令 和批量下发工作模式
            command_status = self.cust_manage_basic_info_and_add_cust_page.setting_command_permissions(info["command"])
            working_mode_status = self.cust_manage_basic_info_and_add_cust_page.setting_working_mode_permissions(
                info["working_mode"])
            self.assertEqual(info["command"], str(command_status), "勾选状态与期望不一致")
            self.assertEqual(info["working_mode"], str(working_mode_status), "勾选状态与期望不一致")
            self.driver.default_frame()
            sleep(2)
            self.cust_manage_basic_info_and_add_cust_page.acc_add_save()
            sleep(1)
            # 退出登录
            self.account_center_page_navi_bar.usr_logout()

            self.log_in_base.log_in_with_csv(info["wdit_account"], info["passwd"])
            sleep(1)
            hello_usr = self.account_center_page_navi_bar.hello_user_account()
            self.assertIn(info["wdit_account"], hello_usr, "登录成功后招呼栏账户名显示错误")
            sleep(1)

            # 进入设备管理/指令管理页面，获取功能按钮
            facility_manage_data = self.cust_manage_basic_info_and_add_cust_page.get_facility_manage_page_function_button()
            sleep(2)
            command_manage_data = self.cust_manage_basic_info_and_add_cust_page.get_command_page_module()

            # 获取中文，依次是：选中发送指令、本次查询全部发送指令、选中设置工作模式、本次查询全部设置工作模式
            #工作模式模板管理, 下发工作模式任务管理, 下发工作模式管理, 下发指令任务管理, 下发指令管理
            send_command = self.assert_text2.dev_manage_select_send_command()
            all_send_command = self.assert_text2.dev_manage_select_all_send_command()
            working_mode = self.assert_text2.dev_manage_setting_working_mode()
            all_working_mode = self.assert_text2.dev_manage_setting_all_working_mode()
            template_manage = self.assert_text.command_manager_page_work_type_template_management()
            working_mode_task_manage = self.assert_text2.comm_manage_send_working_mode_task_manage()
            working_mode_manage = self.assert_text2.comm_manage_send_working_mode_manage()
            task_manage = self.assert_text2.comm_manage_command_task_manage()
            comm_manager = self.assert_text.command_manager_page_issued_command_manager()

            command_list =[]
            working_mode_list = []
            #循环设备管理页面的数据
            for b in facility_manage_data:
                #选中发送指令 和 本次查询全部发送指令
                if send_command in b or all_send_command in b:
                    command_list.append(b)
                #选中设置工作模式 和 本次查询全部设置工作模式
                elif working_mode in b or all_working_mode in b:
                    working_mode_list.append(b)


            #循环指令管理页面的数据
            for c in command_manage_data:
                #下发指令任务管理 和 下发指令管理
                if task_manage in c or comm_manager in c:
                    command_list.append(c)
                #工作模式模板管理, 下发工作模式任务管理, 下发工作模式管理
                elif template_manage in c or working_mode_task_manage in c or working_mode_manage in c:
                    working_mode_list.append(c)

            print("指令", command_list)
            print("工作模式", working_mode_list)

            #验证设备、指令管理页面功能按钮显示情况
            if command_status == True and working_mode_status == True:
                # 指令（设备页+指令管理页）
                self.assertEqual(send_command, command_list[0])
                self.assertEqual(all_send_command, command_list[1])
                self.assertEqual(task_manage, command_list[2])
                self.assertEqual(comm_manager, command_list[3])

                # 工作模式（设备页+指令管理页）
                self.assertEqual(working_mode, working_mode_list[0])
                self.assertEqual(all_working_mode, working_mode_list[1])
                self.assertEqual(template_manage, working_mode_list[2])
                self.assertEqual(working_mode_task_manage, working_mode_list[3])
                self.assertEqual(working_mode_manage, working_mode_list[4])

            elif command_status == False and working_mode_status == False:
                self.assertEqual(comm_manager, command_list[0])
                self.assertEqual(0, len(working_mode_list))

            elif command_status == True and working_mode_status == False:
                self.assertEqual(send_command, command_list[0])
                self.assertEqual(all_send_command, command_list[1])
                self.assertEqual(task_manage, command_list[2])
                self.assertEqual(comm_manager, command_list[3])
                self.assertEqual(0, len(working_mode_list))

            elif command_status == False and working_mode_status == True:
                self.assertEqual(comm_manager, command_list[0])
                self.assertEqual(working_mode, working_mode_list[0])
                self.assertEqual(all_working_mode, working_mode_list[1])
                self.assertEqual(template_manage, working_mode_list[2])
                self.assertEqual(working_mode_task_manage, working_mode_list[3])
                self.assertEqual(working_mode_manage, working_mode_list[4])

            # 退出登录
            sleep(1)
            self.account_center_page_navi_bar.usr_logout()
        csv_file.close()