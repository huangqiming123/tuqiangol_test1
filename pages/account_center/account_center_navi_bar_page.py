from time import sleep

from automate_driver.automate_driver import AutomateDriver
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page import BasePage

# 账户中心页面-招呼栏的元素及操作
# author:孙燕妮
from pages.base.base_page_server import BasePageServer


class AccountCenterNaviBarPage(BasePageServer):
    def __init__(self, driver: AutomateDriverServer, base_url):
        super().__init__(driver, base_url)

    # 招呼栏用户名
    def hello_user_account(self):
        hello_usr = self.driver.get_element("x,/html/body/div[1]/header/div/div[2]/div/div[1]/span/b").text
        return hello_usr

    # 账户总览左下方用户信息
    # --用户名
    def usr_info_name(self):
        usr_name = self.driver.get_element("userName").text
        return usr_name

    # --账号
    def usr_info_account(self):
        usr_account = self.driver.get_element("userAccount").text
        return usr_account

    # --客户类型
    def usr_info_type(self):
        usr_type = self.driver.get_element("userType").text
        return usr_type

    # --电话
    def usr_info_phone(self):
        usr_phone = self.driver.get_element("userPhone").text
        return usr_phone

    # 账户总览下方“我的服务商”信息

    # 销售/代理商账户--服务商
    def sales_usr_service_provider(self):
        service_provider = self.driver.get_element(
            "x,/html/body/div/div/div[2]/div[1]/div/div[3]/div/div[2]/div/div/div/div[2]/ul/li[1]").text
        return service_provider

    # 销售/代理商户账户--联系人
    def sales_usr_service_provider_connect(self):
        service_provider_connect = self.driver.get_element(
            "x,/html/body/div/div/div[2]/div[1]/div/div[3]/div/div[2]/div/div/div/div[2]/ul/li[2]").text
        return service_provider_connect

    # 销售/代理商账户--电话
    def sales_usr_service_provider_phone(self):
        service_provider_phone = self.driver.get_element(
            "x,/html/body/div/div/div[2]/div[1]/div/div[3]/div/div[2]/div/div/div/div[2]/ul/li[3]").text
        return service_provider_phone

    # 普通用户账户--服务商
    def ordinary_usr_service_provider(self):
        service_provider = self.driver.get_element(
            "x,//*[@id='creat-2']/div/div[2]/div/div/div/div[2]/ul/li[1]").text
        return service_provider

    # 普通用户账户--联系人
    def ordinary_usr_service_provider_connect(self):
        service_provider_connect = self.driver.get_element(
            "x,//*[@id='creat-2']/div/div[2]/div/div/div/div[2]/ul/li[2]").text
        return service_provider_connect

    # 普通用户账户--电话
    def ordinary_usr_service_provider_phone(self):
        service_provider_phone = self.driver.get_element(
            "x,//*[@id='creat-2']/div/div[2]/div/div/div/div[2]/ul/li[3]").text
        return service_provider_phone

    # 招呼栏退出系统
    def usr_logout(self):
        # 点击退出系统
        self.driver.float_element(self.driver.get_element('x,/html/body/div[1]/header/div/div[2]/div[2]/div[2]/span/a'))
        sleep(2)
        self.driver.click_element('p,退出系统')
        self.driver.wait()
        # 定位到弹出框内容
        logout_text = self.driver.get_element("c,layui-layer-content").text
        print(logout_text)
        # 点击确定
        self.driver.click_element("c,layui-layer-btn0")
        self.driver.wait()

    # app用户退出
    def app_usr_logout(self):
        # 点击退出系统
        self.driver.float_element(self.driver.get_element('x,/html/body/div[1]/header/div/div[2]/div/div[2]/span/a'))
        sleep(2)
        self.driver.click_element('p,退出系统')
        self.driver.wait()
        # 定位到弹出框内容
        logout_text = self.driver.get_element("c,layui-layer-content").text
        print(logout_text)
        # 点击确定
        self.driver.click_element("c,layui-layer-btn0")
        self.driver.wait()


    # 设备管理-退出系统
    def dev_manage_usr_logout(self):
        self.driver.float_element(self.driver.get_element('x,/html/body/div[2]/header/div/div[2]/div[2]/div[2]/span/a'))
        sleep(2)
        # 点击退出系统
        self.driver.click_element("p,退出系统")
        self.driver.wait()
        # 定位到弹出框内容
        logout_text = self.driver.get_element("c,layui-layer-content").text
        print(logout_text)
        # 点击确定
        self.driver.click_element("c,layui-layer-btn0")
        self.driver.wait()

    # 体验账号—招呼栏退出系统
    def taste_usr_logout(self):
        self.driver.float_element(self.driver.get_element('x,/html/body/div[1]/header/div/div[2]/div/div[2]/span/a'))
        sleep(2)
        # 点击退出系统
        self.driver.click_element('p,退出系统')
        self.driver.wait()
        # 定位到弹出框内容
        logout_text = self.driver.get_element("c,layui-layer-content").text
        print(logout_text)
        # 点击确定
        self.driver.click_element("c,layui-layer-btn0")
        self.driver.wait()

    # 招呼栏退出系统-取消
    def usr_logout_dismiss(self):
        # 点击退出系统
        self.driver.click_element("x,/html/body/div[1]/header/div/div[2]/div[2]/div[2]/span/a")
        sleep(2)
        self.driver.click_element('p,退出系统')
        self.driver.wait()
        # 定位到弹出框内容
        logout_text = self.driver.get_element("c,layui-layer-content").text
        print(logout_text)
        # 点击取消
        self.driver.click_element("c,layui-layer-btn1")
        self.driver.wait()

    # 招呼栏修改资料
    def modify_usr_info(self, user_name, phone, email):
        self.driver.click_element('x,/html/body/div[1]/header/div/div[2]/div[2]/div[2]/span/a')
        sleep(1)
        # 点击招呼栏的修改资料

        self.driver.click_element("p,修改资料")
        sleep(3)
        # 个人资料修改框的客户名称输入
        self.driver.operate_input_element("x,//*[@id='edit-modal-nickName']", user_name)
        # 个人资料修改框的电话输入
        self.driver.operate_input_element("x,//*[@id='edit-modal-phone']", phone)
        # 个人资料修改框的邮箱输入
        self.driver.operate_input_element("x,//*[@id='edit-modal-email']", email)
        # 点击保存按钮
        self.driver.click_element('c,layui-layer-btn0')
        self.driver.wait(1)
        # 获取保存成功状态对话框的文本内容
        self.driver.get_element("c,layui-layer-ico1")
        save_status = self.driver.get_element("c,layui-layer-content").text
        return save_status

    # 招呼栏修改密码
    def modify_user_passwd(self, old_passwd, new_passwd):
        # 点击招呼栏的修改密码
        self.driver.click_element('x,/html/body/div[1]/header/div/div[2]/div[2]/div[2]/span/a')
        sleep(1)
        self.driver.click_element('p,修改密码')
        self.driver.wait(1)
        # 输入旧密码
        self.driver.operate_input_element("oldPwd", old_passwd)
        # 输入新密码
        self.driver.operate_input_element("newPwd", new_passwd)
        # 确认新密码
        self.driver.operate_input_element("renewPwd", new_passwd)
        # 点击保存按钮
        self.driver.click_element('c,layui-layer-btn0')
        self.driver.wait()
        # 获取修改密码成功状态对话框的文本内容
        modify_status = self.driver.get_element("c,layui-layer-content").text
        return modify_status

    # 密码修改成功状态框点击确定
    def modify_passwd_success_comfrim(self):
        self.driver.click_element("x,/html/body/div[7]/div[3]/a")
        self.driver.wait()

    # 招呼栏业务日志
    def business_log(self):
        # 点击招呼栏的业务日志（默认列表为设备管理--分配）
        self.driver.click_element("x,/html/body/div[1]/header/div/div[3]/div/div[1]/a[2]")
        self.driver.wait(5)

    # 点击设备管理-修改
    def log_device_modify(self):
        self.driver.click_element("devDiv_modify_1")
        self.driver.wait(5)

    # 点击客户管理（默认-修改）
    def log_cust_modify(self):
        self.driver.click_element("x,//*[@id='tab_nav_business']/li[2]/a")
        self.driver.wait(5)

    # 点击客户管理-添加
    def log_cust_add(self):
        self.driver.click_element("x,//*[@id='custDiv']/button[2]")
        self.driver.wait(5)

    # 点击客户管理-删除
    def log_cust_delete(self):
        self.driver.click_element("x,//*[@id='custDiv']/button[3]")
        self.driver.wait(5)

    # 点击客户管理-修改密码
    def log_cust_modify_passwd(self):
        self.driver.click_element("x,//*[@id='custDiv']/button[4]")
        self.driver.wait(5)

    # 点击客户管理-重置密码
    def log_cust_reset_passwd(self):
        self.driver.click_element("x,//*[@id='custDiv']/button[5]")
        self.driver.wait(5)

    # 输入搜索条件来查询设备管理日志
    def search_device_log(self, search_info):
        # 点击开始时间
        self.driver.click_element("createTimeStart_fp")
        # 选择日期2017-02-07
        self.driver.click_element("x,//*[@id='laydate_table']/tbody/tr[2]/td[3]")
        # 点击结束时间
        self.driver.click_element("createTimeEnd_fp")
        # 选择时间
        self.driver.click_element("x,//*[@id='laydate_hms']/li[2]/input")
        # 选择20时
        self.driver.click_element("x,//*[@id='laydate_hmsno']/span[21]")
        # 点击确定
        self.driver.click_element("laydate_ok")
        # 输入操作人/目标账号/IMEI号
        self.driver.operate_input_element("selectUserName_xf", search_info)
        # 点击搜索按钮
        self.driver.click_element("search_xf")
        self.driver.wait(5)

    # 输入搜索条件来查询客户管理日志
    def search_cust_log(self, search_info):
        # 点击开始时间
        self.driver.click_element("createTimeStart_fp")
        # 选择日期2017-02-07
        self.driver.click_element("x,//*[@id='laydate_table']/tbody/tr[2]/td[3]")
        # 点击结束时间
        self.driver.click_element("createTimeEnd_fp")
        # 选择时间
        self.driver.click_element("x,//*[@id='laydate_hms']/li[2]/input")
        # 选择20时
        self.driver.click_element("x,//*[@id='laydate_hmsno']/span[21]")
        # 点击确定
        self.driver.click_element("laydate_ok")
        # 输入操作人/目标账号/IMEI号
        self.driver.operate_input_element("selectUserName_fp", search_info)
        # 点击搜索按钮
        self.driver.click_element("search_fp")
        self.driver.wait(5)

    # 招呼栏帮助
    def to_help(self):
        # 点击招呼栏的帮助
        sleep(2)
        self.driver.click_element("x,/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a[2]")
        self.driver.wait(1)

    # 帮助-意见反馈
    def help_feedback(self, suggest_type, suggest_content, contact, phone):
        if suggest_type == '追踪问题':
            # 选中追踪问题
            self.driver.click_element("x,//*[@id='default_Li']/a")
            # 在描述内容框内输入反馈内容
            self.driver.operate_input_element("content", suggest_content)
            # 在联系人框内输入联系人
            self.driver.operate_input_element("linkman", contact)
            # 在联系电话框内输入电话
            self.driver.operate_input_element("phone", phone)
            # 点击保存按钮
            self.driver.click_element("x,//*[@id='userFeedbackForm']/div[4]/div/button")
            self.driver.wait(1)
            # 获取保存成功弹框文本内容
            save_status_01 = self.driver.get_element("c,layui-layer-content").text
            return save_status_01

        elif suggest_type == '轨迹问题':
            # 选中轨迹问题
            self.driver.click_element("x,//*[@id='type']/li[2]/a")
            # 在描述内容框内输入反馈内容
            self.driver.operate_input_element("content", suggest_content)
            # 在联系人框内输入联系人
            self.driver.operate_input_element("linkman", contact)
            # 在联系电话框内输入电话
            self.driver.operate_input_element("phone", phone)
            # 点击保存按钮
            self.driver.click_element("x,//*[@id='userFeedbackForm']/div[4]/div/button")
            self.driver.wait(1)
            # 获取保存成功弹框文本内容
            save_status_02 = self.driver.get_element("c,layui-layer-content").text
            return save_status_02

        elif suggest_type == '指令问题':
            # 选中指令问题
            self.driver.click_element("x,//*[@id='type']/li[3]/a")
            # 在描述内容框内输入反馈内容
            self.driver.operate_input_element("content", suggest_content)
            # 在联系人框内输入联系人
            self.driver.operate_input_element("linkman", contact)
            # 在联系电话框内输入电话
            self.driver.operate_input_element("phone", phone)
            # 点击保存按钮
            self.driver.click_element("x,//*[@id='userFeedbackForm']/div[4]/div/button")
            self.driver.wait(1)
            # 获取保存成功弹框文本内容
            save_status_03 = self.driver.get_element("c,layui-layer-content").text
            return save_status_03

        elif suggest_type == '功能建议':
            # 选中功能建议
            self.driver.click_element("x,//*[@id='type']/li[4]/a")
            # 在描述内容框内输入反馈内容
            self.driver.operate_input_element("content", suggest_content)
            # 在联系人框内输入联系人
            self.driver.operate_input_element("linkman", contact)
            # 在联系电话框内输入电话
            self.driver.operate_input_element("phone", phone)
            # 点击保存按钮
            self.driver.click_element("x,//*[@id='userFeedbackForm']/div[4]/div/button")
            self.driver.wait(1)
            # 获取保存成功弹框文本内容
            save_status_04 = self.driver.get_element("c,layui-layer-content").text
            return save_status_04

        elif suggest_type == '围栏问题':
            # 选中围栏问题
            self.driver.click_element("x,//*[@id='type']/li[5]/a")
            # 在描述内容框内输入反馈内容
            self.driver.operate_input_element("content", suggest_content)
            # 在联系人框内输入联系人
            self.driver.operate_input_element("linkman", contact)
            # 在联系电话框内输入电话
            self.driver.operate_input_element("phone", phone)
            # 点击保存按钮
            self.driver.click_element("x,//*[@id='userFeedbackForm']/div[4]/div/button")
            self.driver.wait(1)
            # 获取保存成功弹框文本内容
            save_status_05 = self.driver.get_element("c,layui-layer-content").text
            return save_status_05

        elif suggest_type == '告警问题':
            # 选中告警问题
            self.driver.click_element("x,//*[@id='type']/li[6]/a")
            # 在描述内容框内输入反馈内容
            self.driver.operate_input_element("content", suggest_content)
            # 在联系人框内输入联系人
            self.driver.operate_input_element("linkman", contact)
            # 在联系电话框内输入电话
            self.driver.operate_input_element("phone", phone)
            # 点击保存按钮
            self.driver.click_element("x,//*[@id='userFeedbackForm']/div[4]/div/button")
            self.driver.wait(1)
            # 获取保存成功弹框文本内容
            save_status_06 = self.driver.get_element("c,layui-layer-content").text
            return save_status_06

        elif suggest_type == '我有疑问':
            # 选中我有疑问
            self.driver.click_element("x,//*[@id='type']/li[7]/a")
            # 在描述内容框内输入反馈内容
            self.driver.operate_input_element("content", suggest_content)
            # 在联系人框内输入联系人
            self.driver.operate_input_element("linkman", contact)
            # 在联系电话框内输入电话
            self.driver.operate_input_element("phone", phone)
            # 点击保存按钮
            self.driver.click_element("x,//*[@id='userFeedbackForm']/div[4]/div/button")
            self.driver.wait(1)
            # 获取保存成功弹框文本内容
            save_status_07 = self.driver.get_element("c,layui-layer-content").text
            return save_status_07

        elif suggest_type == '其他':
            # 选中其他
            self.driver.click_element("x,//*[@id='type']/li[8]/a")
            # 在描述内容框内输入反馈内容
            self.driver.operate_input_element("content", suggest_content)
            # 在联系人框内输入联系人
            self.driver.operate_input_element("linkman", contact)
            # 在联系电话框内输入电话
            self.driver.operate_input_element("phone", phone)
            # 点击保存按钮
            self.driver.click_element("x,//*[@id='userFeedbackForm']/div[4]/div/button")
            self.driver.wait(1)
            # 获取保存成功弹框文本内容
            save_status_08 = self.driver.get_element("c,layui-layer-content").text
            return save_status_08

    def usr_log_out(self):
        # 点击退出系统
        self.driver.float_element(self.driver.get_element('x,/html/body/div[1]/header/div/div[2]/div/div[2]/span/a'))
        sleep(2)
        self.driver.click_element('p,退出系统')
        self.driver.wait()
        # 定位到弹出框内容
        logout_text = self.driver.get_element("c,layui-layer-content").text
        print(logout_text)
        # 点击确定
        self.driver.click_element("c,layui-layer-btn0")
        self.driver.wait()

    def click_modify_usr_info(self):
        self.driver.click_element('x,/html/body/div[1]/header/div/div[2]/div[2]/div[2]/span/a')
        sleep(1)
        # 点击招呼栏的修改资料
        self.driver.click_element("p,修改资料")
        sleep(3)

    def cancel_modify_user_info(self):
        self.driver.click_element('c,layui-layer-btn1')
        sleep(2)

    def close_modify_user_info(self):
        self.driver.click_element('c,layui-layer-ico')
        sleep(2)

    def check_next_user_input_value(self):
        return self.driver.get_element('x,//*[@id="lowerFlag"]/div/input').is_selected()

    def get_all_dev_button_value(self):
        return self.driver.get_element('x,//*[@id="NORMAL"]').get_attribute('class')

    def get_console_class_value(self):
        return self.driver.get_element('x,//*[@id="console"]').get_attribute('class')

    def click_alarm_button_in_console(self):
        self.driver.click_element('x,//*[@id="gaojing"]')
        sleep(2)

    def get_text_after_click_alarm_button(self):
        return self.driver.get_text('x,//*[@id="alarmMessage"]/div[1]/h5')

    def close_alarm_in_console(self):
        self.driver.click_element('x,//*[@id="alarmMessage"]/div[1]/a[1]')
        sleep(2)

    def get_value_sport_statistiacl_value(self):
        return self.driver.get_element('x,//*[@id="ReportTab"]/ul/li[1]').get_attribute('class')

    def get_value_sport_overview_value(self):
        return self.driver.get_element('x,//*[@id="sportOverview"]').get_attribute('class')

    def get_text_after_report(self):
        self.driver.switch_to_frame('x,//*[@id="sportOverviewFrame"]')
        text = self.driver.get_text('x,/html/body/div/div[1]/div/b')
        self.driver.default_frame()
        return text

    # 取提示语
    def get_modify_prompt(self, select):
        try:
            prompt = self.driver.get_text(select)
            return prompt
        except:
            prompt = ""
            return prompt

    # 修改资料---错误提示
    def get_modify_info_exception_prompt(self, data):
        # 客户名称、电话、邮箱,,
        self.driver.operate_input_element("x,//*[@id='edit-modal-nickName']", data["name"])
        self.driver.operate_input_element("x,//*[@id='edit-modal-phone']", data["phone"])
        self.driver.operate_input_element("x,//*[@id='edit-modal-email']", data["email"])
        # 点击保存按钮
        self.driver.click_element('c,layui-layer-btn0')
        self.driver.wait()
        # 获取错误提示
        name_prompt = self.get_modify_prompt("x,//*[@id='edit-modal-userForm']/div[2]/div/label")
        phone_prompt = self.get_modify_prompt("x,//*[@id='edit-modal-userForm']/div[3]/div/label")
        email_prompt = self.get_modify_prompt("x,//*[@id='edit-modal-userForm']/div[4]/div/label")
        all_prompt = {"name": name_prompt,
                      "phone": phone_prompt,
                      "email": email_prompt
                      }
        print(all_prompt)
        return all_prompt

    # 修改资料--取长度
    def get_modifgy_info_element_len(self):
        phone_len = int(self.driver.get_element("x,//*[@id='edit-modal-phone']").get_attribute("maxlength"))
        email_len = int(self.driver.get_element("x,//*[@id='edit-modal-email']").get_attribute("maxlength"))
        len = {"phone_len": phone_len,
               "email_len": email_len
               }
        return len


        # 点击招呼栏的修改密码

    def click_modify_usr_password(self):
        self.driver.click_element('x,/html/body/div[1]/header/div/div[2]/div[2]/div[2]/span/a')
        sleep(2)
        # 点击招呼栏的修改密码
        self.driver.click_element("p,修改密码")
        sleep(3)

    # 修改密码--取消
    def click_password_cancel(self):
        self.driver.click_element('c,layui-layer-btn1')
        self.driver.wait(1)

    # 修改密码---错误提示
    def get_modify_pwd_exception_prompt(self, data):
        # 旧密码、新密码、确认新密码
        self.driver.operate_input_element("oldPwd", data["old_password"])
        self.driver.operate_input_element("newPwd", data["new_password"])
        self.driver.operate_input_element("renewPwd", data["new_password2"])
        # 点击保存按钮
        self.driver.click_element('c,layui-layer-btn0')
        self.driver.wait()

        # 获取弹出框的提示
        try:
            text = self.driver.get_element("c,layui-layer-content").text
        except:
            text = ""
        # 获取错误提示
        old_Pwd = self.get_modify_prompt("x,//*[@id='editpwd-form']/div[1]/div/label")
        new_Pwd = self.get_modify_prompt("x,//*[@id='editpwd-form']/div[2]/div/label")
        new_Pwd2 = self.get_modify_prompt("x,//*[@id='editpwd-form']/div[3]/div/label")

        all_prompt = {"old_Pwd": old_Pwd,
                      "new_Pwd": new_Pwd,
                      "new_Pwd2": new_Pwd2,
                      "text": text
                      }
        print(all_prompt)
        return all_prompt

    #点账户中心
    def click_account_center_button(self):
        sleep(3)
        self.driver.click_element("x,//*[@id='accountCenter']")
        sleep(2)

    #获取头部模块
    def get_page_module(self):
        module = []
        module_len = len(self.driver.get_elements("x,/html/body/div[1]/header/div/div[2]/ul/li"))
        for i in range(module_len):
            text = self.driver.get_text("x,/html/body/div/header/div/div[2]/ul/li[" + str(i + 1) + "]/a")
            module.append(text)
        print(module)
        return module
