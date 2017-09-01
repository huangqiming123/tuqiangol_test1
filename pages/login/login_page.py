from time import sleep

from automate_driver.automate_driver import AutomateDriver
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page import BasePage


# 登录页面的元素及操作
# author:孙燕妮
from pages.base.base_page_server import BasePageServer


class LoginPage(BasePageServer):
    def __init__(self, driver: AutomateDriverServer, base_url):
        super().__init__(driver, base_url)

    # 用户名输入框
    def account_input(self, account):
        self.driver.operate_input_element("account", account)

    # 密码输入框
    def password_input(self, password):
        self.driver.operate_input_element("password", password)

    # 忘记密码点击操作
    def forget_password(self):
        # self.driver.click_element("l,忘记密码？")
        self.driver.click_element("x,/html/body/div[1]/div/div[3]/span[1]/a[1]")

    # 忘记密码-账号输入框
    def forget_passwd_account(self, account):
        self.driver.operate_input_element("x,//*[@id='validmessage-form']/div[1]/div/input",
                                          account)

    # 忘记密码-电话输入框
    def forget_passwd_phone(self, phone):
        self.driver.operate_input_element("x,//*[@id='validmessage-form']/div[2]/div/input",
                                          phone)

    # 取消忘记密码
    def dis_forget_passwd(self):
        self.driver.click_element("x,//*[@id='RetrievePasswordModal']/div/div/div[3]/button[3]")
        self.driver.wait()

    def dis_forget_passwd2(self):
        self.dis_forget_passwd()
        self.forget_password()
        self.driver.wait()
        self.driver.click_element("x,//*[@id='RetrievePasswordModal']/div/div/div[1]/button/span")

    # 体验账号登入
    def taste(self):
        self.user_login("taste", "888888")

    # 登录时记住我勾选框
    def remember_me(self):
        checkbox = self.driver.get_element("checkbox")
        checkbox.click()

    # 检查记住我勾选框状态
    def check_remember_me(self):
        box_status = self.driver.get_element("checkbox").is_selected()
        return box_status

    # 登录按钮点击操作
    def login_button_click(self):
        self.driver.click_element("logins")

    # 获取登录按钮的文本内容
    def login_button_text(self):
        login_button_text = self.driver.get_element("logins").text
        return login_button_text

    # 语言切换操作
    def change_language(self, language):
        if language == 'English':
            self.driver.click_element("x,/html/body/footer/div[1]/ul/li[2]/a")
            sleep(4)
            login_button_text = self.driver.get_element("logins").text
            return login_button_text
        elif language == 'España':
            self.driver.click_element("x,/html/body/footer/div[1]/ul/li[3]/a")
            sleep(4)
            login_button_text = self.driver.get_element("logins").text
            return login_button_text
        elif language == 'Portugal':
            self.driver.click_element("x,/html/body/footer/div[1]/ul/li[4]/a")
            sleep(4)
            login_button_text = self.driver.get_element("logins").text
            return login_button_text
        elif language == 'Polska':
            self.driver.click_element("x,/html/body/footer/div[1]/ul/li[5]/a")
            sleep(4)
            login_button_text = self.driver.get_element("logins").text
            return login_button_text
        elif language == 'Deutschland':
            self.driver.click_element("x,/html/body/footer/div[1]/ul/li[6]/a")
            sleep(4)
            login_button_text = self.driver.get_element("logins").text
            return login_button_text

    # 底部第三方网站链接点击操作
    def enter_third_party_website(self, web_name):
        if web_name == '工商网监':
            self.driver.click_element('x,/html/body/footer/div[3]/a[1]')
        elif web_name == '可信网站':
            self.driver.click_element('x,/html/body/footer/div[3]/a[2]')
        elif web_name == '网络警察':
            self.driver.click_element('x,/html/body/footer/div[3]/a[3]')
        elif web_name == '公共信息网络安全监察':
            self.driver.click_element('x,/html/body/footer/div[3]/a[4]')
        elif web_name == '不良信息举报中心':
            self.driver.click_element('x,/html/body/footer/div[3]/a[5]')

    # 封装登录操作
    def user_login(self, account, password):
        self.account_input(account)
        self.password_input(password)
        self.login_button_click()
        self.driver.wait(3)

    def get_text_after_forget_password(self):
        # 获取点击找回密码后的文本内容
        return self.driver.get_text('x,//*[@id="RetrievePasswordModal"]/div/div/div[1]/h4')

    def get_first_text_after_log_in_tester_account(self):
        return self.driver.get_text('x,//*[@id="index"]/a')

    def get_second_text_after_log_in_tester_account(self):
        return self.driver.get_text('x,//*[@id="reportsManagement"]/a')

    def get_third_text_after_log_in_tester_account(self):
        return self.driver.get_text('x,//*[@id="safetyManagement"]/a')

    def get_four_text_after_log_in_tester_account(self):
        return self.driver.get_text('x,//*[@id="devicesManagement"]/a')

    def get_number_permission_after_click_tester_button(self):
        number = len(list(self.driver.get_elements('x,/html/body/div[1]/nav/div/ul/li')))
        return number

    def get_fifth_text_after_log_in_tester_account(self):
        return self.driver.get_text('x,//*[@id="deviceDistribution"]/a')

    def get_exception_text(self):
        return self.driver.get_text('x,//*[@id="tipsmsg"]')

    # 找回密码--异常验证
    def get_forget_pwd_error_prompt(self, data):
        self.forget_passwd_account(data["account"])
        self.forget_passwd_phone(data["phone"])
        self.driver.operate_input_element("x,//*[@id='validmessage-form']/div[3]/div[1]/input", data["verify_code"])
        if data["type"] == "下一步":
            # 点击下一步
            self.driver.click_element("validSmsCode")
            self.driver.wait()

        elif data["type"] == "获取验证码":
            # 点击验证码
            self.driver.click_element("getValidCodeBtn")
            self.driver.wait()

        # 获取弹框提示语
        try:
            text = self.driver.get_element("c,layui-layer-content").text
        except:
            text = ""

        # 获取账号提示语
        account_prompt = self.get_login_prompt("x,//*[@id='validmessage-form']/div[1]/div/label")
        phone_prompt = self.get_login_prompt("x,//*[@id='validmessage-form']/div[2]/div/label")
        code_prompt = self.get_login_prompt("x,//*[@id='validmessage-form']/div[3]/div/label")

        all_prompt = {
            "account_prompt2": account_prompt,
            "phone_prompt2": phone_prompt,
            "code_prompt2": code_prompt,
            "text_prompt": text
        }

        return all_prompt

    # 登录---取提示语
    def get_login_prompt(self, select):
        try:
            prompt = self.driver.get_text(select)
            return prompt
        except:
            prompt = ""
            return prompt

    # 点击首页
    def click_home_page(self):
        self.driver.click_element("nomalUserCenter")
        sleep(3)

    # 点击体验账号
    def click_experience_account(self):
        self.driver.click_element("x,/html/body/div[1]/div/div[3]/span[1]/a[2]")
        sleep(2)

    # 账号登录后 ，获取账户中心列表
    def get_account_center_list(self):
        list_data = []
        list_len = len(self.driver.get_elements("x,/html/body/div[1]/div[4]/div/div/div[1]/div/div[2]/ul/li"))
        for i in range(list_len):
            text = self.driver.get_text(
                "x,/html/body/div[1]/div[4]/div/div/div[1]/div/div[2]/ul/li[" + str(i + 1) + "]/a")
            list_data.append(text)
        print(list_data)
        return list_data

    # 首页页面跳转
    def login_page_account_overview(self, link_name):
        if link_name == '库存':
            self.driver.click_element("x,//*[@id='creat-0']/div[1]/a")
            self.driver.wait(1)
        if link_name == '总进货数':
            self.driver.click_element("x,//*[@id='creat-0']/div[2]/a")
            self.driver.wait(1)
        elif link_name == '在线':
            self.driver.click_element("x,//*[@id='creat-0']/div[3]/a")
            self.driver.wait(1)
        elif link_name == '离线':
            self.driver.click_element("x,//*[@id='creat-0']/div[4]/a")
            self.driver.wait(1)
        elif link_name == '即将到期':
            self.driver.click_element("x,//*[@id='creat-0']/div[5]/a")
            self.driver.wait(1)
        elif link_name == '已过期':
            self.driver.click_element("x,//*[@id='creat-0']/div[6]/a")
            self.driver.wait(1)
        elif link_name == '已激活':
            self.driver.click_element("x,//*[@id='creat-0']/div[7]/a")
            self.driver.wait(1)
        elif link_name == '未激活':
            self.driver.click_element("x,//*[@id='creat-0']/div[8]/a")
            self.driver.wait(1)
        elif link_name == '告警车辆':
            self.driver.click_element("x,//*[@id='creat-0']/div[9]/a")
            self.driver.wait(1)
        elif link_name == '重点关注车辆':
            self.driver.click_element("x,//*[@id='creat-0']/div[10]/a")
            self.driver.wait(1)

        elif link_name == '控制台':
            self.driver.click_element("x,//*[@id='creat-1']/div[1]/a")
            self.driver.wait(1)
        elif link_name == '统计报表':
            self.driver.click_element("x,//*[@id='creat-1']/div[2]/a")
            self.driver.wait(1)
        elif link_name == '围栏':
            self.driver.click_element("x,//*[@id='creat-1']/div[3]/a")
            self.driver.wait(1)
        elif link_name == '下级客户管理':
            self.driver.click_element("x,//*[@id='creat-1']/div[4]/a")
            self.driver.wait(1)
        elif link_name == '设备管理':
            self.driver.click_element("x,//*[@id='creat-1']/div[5]/a")
            self.driver.wait(1)
        elif link_name == '指令管理':
            self.driver.click_element("x,//*[@id='creat-1']/div[6]/a")
            self.driver.wait(1)
        elif link_name == '地标设置':
            self.driver.click_element("x,//*[@id='creat-1']/div[7]/a")
            self.driver.wait(1)
        elif link_name == '告警':
            self.driver.click_element("x,//*[@id='creat-1']/div[8]/a")
            self.driver.wait(1)
