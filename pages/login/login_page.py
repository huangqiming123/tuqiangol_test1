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
        self.driver.click_element("l,忘记密码？")

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
            self.driver.click_element("x,/html/body/footer/div[1]/ul/li[2]/a/img")
            login_button_text = self.driver.get_element("logins").text
            return login_button_text
        elif language == 'España':
            self.driver.click_element("x,/html/body/footer/div[1]/ul/li[3]/a/img")
            login_button_text = self.driver.get_element("logins").text
            return login_button_text
        elif language == 'Portugal':
            self.driver.click_element("x,/html/body/footer/div[1]/ul/li[4]/a/img")
            login_button_text = self.driver.get_element("logins").text
            return login_button_text
        elif language == 'Polska':
            self.driver.click_element("x,/html/body/footer/div[1]/ul/li[5]/a/img")
            login_button_text = self.driver.get_element("logins").text
            return login_button_text
        elif language == 'Deutschland':
            self.driver.click_element("x,/html/body/footer/div[1]/ul/li[6]/a/img")
            login_button_text = self.driver.get_element("logins").text
            return login_button_text

    # 底部第三方网站链接点击操作
    def enter_third_party_website(self, web_name):
        if web_name == '可信网站':
            self.driver.click_element("s,body > footer > div.certification.ta-c > a:nth-child(1) > img")
        elif web_name == '网络警察':
            self.driver.click_element("s,body > footer > div.certification.ta-c > a:nth-child(1) > img")
        elif web_name == '公共信息网络安全监察':
            self.driver.click_element("s,body > footer > div.certification.ta-c > a:nth-child(2) > img")
        elif web_name == '不良信息举报中心':
            self.driver.click_element("s,body > footer > div.certification.ta-c > a:nth-child(3) > img")

    # 封装登录操作
    def user_login(self, account, password):
        self.account_input(account)
        self.password_input(password)
        self.login_button_click()
        self.driver.wait()

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
