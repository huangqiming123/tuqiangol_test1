from time import sleep

from selenium.webdriver.common.keys import Keys

from automate_driver.automate_driver import AutomateDriver
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page import BasePage

# 客户管理页面-客户基本信息及新增客户
# author:孙燕妮
from pages.base.base_page_server import BasePageServer


class CustManageBasicInfoAndAddCustPage(BasePageServer):
    def __init__(self, driver: AutomateDriverServer, base_url):
        super().__init__(driver, base_url)

    # 点击进入客户管理页面
    def enter_cust_manage(self):
        self.driver.wait(3)
        self.driver.click_element("customer")
        self.driver.wait(3)

    def click_left_tree_current_user(self):
        self.driver.click_element("treeDemo_1_span")
        # self.driver.execute_script(current_user)
        sleep(1)

    # 点击进入账户中心页面
    def enter_account_center(self):
        self.driver.click_element("accountCenter")
        self.driver.wait(3)

    # 当前账户信息
    # 当前账户-用户名
    def get_curr_acc_username(self):
        username = self.driver.get_element("user_account").text
        return username

    # 当前账户-账号
    def get_curr_account(self):
        account = self.driver.get_element("userAccount").text
        return account

    # 当前账户-客户类型
    def get_curr_acc_type(self):
        acc_type = self.driver.get_element("userType").text
        return acc_type

    # 当前账户-客户电话
    def get_curr_acc_phone(self):
        acc_phone = self.driver.get_element("user_phone").text
        return acc_phone

    # 当前账户-库存
    def get_curr_acc_stock(self):
        acc_stock = self.driver.get_element("stock").text
        return acc_stock

    # 当前账户-总数
    def get_curr_acc_total_dev(self):
        acc_total_dev = self.driver.get_element("receiving").text
        return acc_total_dev

    # 当前账户-未激活
    def get_curr_acc_diss_active(self):
        acc_diss_active = self.driver.get_element("noActive").text
        return acc_diss_active

    # 当前账户-已激活
    def get_curr_acc_active(self):
        acc_active = self.driver.get_element("active").text
        return acc_active

    # 当前账户-已过期
    def get_curr_acc_expired(self):
        acc_expired = self.driver.get_element("devExpired").text
        return acc_expired

    # 当前账户-即将到期
    def get_curr_acc_expiring(self):
        acc_expiring = self.driver.get_element("devExpiring").text
        return acc_expiring

    # 当前账户-在线
    def get_curr_acc_online(self):
        acc_online = self.driver.get_element("onLine").text
        return acc_online

    # 当前账户-离线
    def get_curr_acc_offline(self):
        acc_offline = self.driver.get_element("noOnLine").text
        return acc_offline

    # 当前账户-监控用户
    def monitor_acc(self):
        # 点击监控用户
        self.driver.click_element(
            "x,/html/body/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div/button")
        self.driver.wait()

    # 当前账户-编辑用户
    def edit_acc(self):
        # 点击编辑用户
        self.driver.click_element("x,//*[@id='editUserFast']/button")
        self.driver.wait()

    # 当前账户-编辑用户-选择客户类型
    def acc_type_choose(self, acc_type, type_id=""):
        if acc_type == '销售':
            # self.driver.click_element("x,/html/body/div/div/form/div[2]/div/div[2]/label[1]")
            self.driver.click_element("x,//*[@id='typeRoleRadio1']/label[1]")

        elif acc_type == '代理商':
            try:
                #self.driver.click_element("x,/html/body/div/div/form/div[2]/div/div[2]/label[2]")
                self.driver.click_element("x,//*[@id='typeRoleRadio1']/label[2]")
            except:
                self.driver.click_element("x,//*[@id='typeRoleRadio2']/label[1]")
                #self.driver.click_element("x,/html/body/div/div/form/div[2]/div/div[3]/label[1]")

        elif acc_type == '用户':
            if type_id == "typeRoleRadio1":
                self.driver.click_element("x,//*[@id='typeRoleRadio1']/label[3]")

            if type_id == "typeRoleRadio2":
                self.driver.click_element("x,//*[@id='typeRoleRadio2']/label[2]")

            if type_id == "typeRoleRadio3":
                self.driver.click_element("x,//*[@id='typeRoleRadio3']/label")


    # 当前账户-编辑用户-编辑用户输入框信息
    def acc_input_info_edit(self, acc_name, phone, email, conn, com):
        # 编辑用户名称
        self.driver.operate_input_element("nickName", acc_name)
        self.driver.wait(1)
        # 编辑电话
        self.driver.operate_input_element("phone", phone)
        self.driver.wait(1)
        # 编辑邮箱
        self.driver.operate_input_element("email", email)
        self.driver.wait(1)
        # 编辑联系人
        self.driver.operate_input_element("contact", conn)
        self.driver.wait(1)
        # 编辑公司名
        self.driver.operate_input_element("companyName", com)
        self.driver.wait(1)

    # 当前账户-编辑用户-修改用户登录权限
    def acc_login_limit_modi(self):
        # 将滚动条滚动至修改权限处
        # ele = self.driver.get_element("x,/html/body/div[9]/div/div/div[2]/div/form/div[13]/label")
        # self.driver.execute_script(ele)
        # 判断App登录权限是否已勾选
        ele = self.driver.get_element('x,//*[@id="appLogin"]')
        status = ele.is_selected()
        if status == True:
            # 取消勾选App登录权限
            self.driver.click_element('x,//*[@id="userForm"]/div[11]/div[2]/label/div/ins')

    # 当前账户-编辑用户-修改用户指令权限
    def acc_instr_limit_modi(self):
        # 将滚动条滚动至修改权限处
        # ele = self.driver.get_element("x,/html/body/div[9]/div/div/div[2]/div/form/div[13]/label")
        # self.driver.execute_script(ele)
        # 判断批量下发指令是否已勾选
        ele = self.driver.get_element('x,//*[@id="isBatchSendIns"]')
        status = ele.is_selected()
        if status == False:
            # 勾选批量下发指令
            self.driver.click_element("x,//*[@id='userForm']/div[12]/div[1]/label/div/ins")

    # 当前账户-编辑用户-修改用户修改权限
    def acc_modi_limit_modi(self):
        # 将滚动条滚动至修改权限处
        # ele = self.driver.get_element("x,/html/body/div[9]/div/div/div[2]/div/form/div[13]/label")
        # self.driver.execute_script(ele)
        # 判断修改设备是否已勾选
        ele = self.driver.get_element('x,//*[@id="updateDevFlag"]')
        status = ele.is_selected()
        if status == False:
            # 勾选修改设备
            self.driver.click_element("x,//*[@id='userForm']/div[13]/div/label/div/ins")

    # 当前账户-编辑用户-保存
    def acc_info_save(self):
        # 将滚动条滚动至保存按钮处
        ele = self.driver.get_element("updateUserBtn")
        self.driver.execute_script(ele)
        self.driver.click_element("updateUserBtn")
        self.driver.wait(1)

    # 新增用户-保存
    def acc_add_save(self):
        # 将滚动条滚动至保存按钮处

        self.driver.click_element('c,layui-layer-btn0')
        self.driver.wait(1)

    # 当前账户-编辑用户-保存成功操作状态
    def acc_info_save_status(self):
        save_status = self.driver.get_element("c,layui-layer-content").text
        return save_status

    # 当前账户-编辑用户-搜索客户名称/账户
    def acc_search(self, keyword):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        # 将滚动条滚动至搜索输入框处
        ele = self.driver.get_element("treeDemo2_cusTreeKey")
        self.driver.execute_script(ele)
        # 在搜索输入框内输入搜索关键词
        self.driver.operate_input_element("treeDemo2_cusTreeKey", keyword)
        # 点击搜索按钮
        self.driver.click_element("treeDemo2_cusTreeSearchBtn")
        self.driver.wait(4)
        # 选择列表中第一个搜索结果
        self.driver.click_element('c,autocompleter-item')
        self.driver.default_frame()

    # 新增客户
    def add_acc(self):
        # 点击新增客户
        self.driver.click_element("x,/html/body/div[1]/div[5]/div/div/div[2]/div/div[2]/div[2]/div/button[1]")
        self.driver.wait()

    # 当前账户-新增用户-编辑用户输入框信息
    def add_acc_input_info_edit(self, acc_name, account, pwd, phone, email, conn, com):
        # 编辑客户名称
        self.driver.operate_input_element("nickName", acc_name)
        self.driver.wait(1)
        # 编辑登录账号
        self.driver.operate_input_element("account", account)
        self.driver.wait(1)
        # 编辑密码
        self.driver.operate_input_element("password", pwd)
        self.driver.wait(1)
        # 确认密码
        self.driver.operate_input_element("pswAgain", pwd)
        self.driver.wait(1)
        # 编辑电话
        self.driver.operate_input_element("phone", phone)
        self.driver.wait(1)
        # 编辑邮箱
        self.driver.operate_input_element("email", email)
        self.driver.wait(1)
        # 编辑联系人
        self.driver.operate_input_element("contact", conn)
        self.driver.wait(1)
        # 编辑公司名
        self.driver.operate_input_element("companyName", com)
        self.driver.wait(1)

    def click_tran_account(self):
        self.driver.click_element('x,//*[@id="customerlist"]/tr[1]/td[8]/a[5]')
        sleep(2)

    def choose_up_account(self, account):
        self.driver.switch_to_frame('x,//*[@id="layui-layer-iframe13"]')
        self.driver.operate_input_element('x,//*[@id="treeDemo2_cusTreeKey"]', account)
        self.driver.click_element('x,//*[@id="treeDemo2_cusTreeSearchBtn"]')
        sleep(2)
        self.driver.click_element('c,autocompleter-item')
        sleep(2)

    def click_ensure_tran(self):
        self.driver.click_element('c,layui-layer-btn0')
        sleep(2)

    def get_account_text(self):
        return self.driver.get_text('x,//*[@id="customerlist"]/tr[1]/td[4]')

    def close_add_account(self):
        self.driver.click_element('c,layui-layer-ico')
        sleep(2)

    def add_data_to_search_account(self, data):
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="treeDemo_cusTreeKey"]', data['account'])

        self.driver.click_element('x,//*[@id="treeDemo_cusTreeSearchBtn"]')
        sleep(3)
        self.driver.click_element('c,autocompleter-item')
        sleep(2)

    def get_account_type(self):
        return self.driver.get_text('x,//*[@id="userType"]')

    def get_account(self):
        return self.driver.get_text('x,//*[@id="userAccount"]')

    def get_account_phone(self):
        return self.driver.get_text('x,//*[@id="user_phone"]')

    def get_account_name(self):
        return self.driver.get_text('x,//*[@id="user_account"]')

    def click_monitoring_account_button(self):
        #self.driver.click_element('x,/html/body/div[1]/div[4]/div/div/div[2]/div/div[1]/div/button')
        self.driver.click_element('x,/html/body/div[1]/div[5]/div/div/div[2]/div/div[1]/div/button')
        sleep(2)

    def get_text_after_click(self):
        text = self.driver.get_text('x,//*[@id="account"]')
        return text.split('(')[0]

    def edit_button_style_value(self):
        a = self.driver.get_element('x,//*[@id="editUserFast"]').get_attribute('style')
        return a

    def click_edit_account_button(self):
        self.driver.click_element('x,//*[@id="editUserFast"]/button')
        sleep(2)

    def click_close_edit_accunt_button(self):
        self.driver.click_element('c,layui-layer-ico')
        sleep(2)

    def get_account_name_after_click_edit(self):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        text = self.driver.get_element('x,//*[@id="topUser"]').get_attribute('value')
        self.driver.default_frame()
        return text

    def cancel_add_account(self):
        self.driver.click_element('c,layui-layer-btn1')

    def get_up_account_value(self):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        value = self.driver.get_element('x,//*[@id="topUser"]').get_attribute('readonly')
        self.driver.default_frame()
        return value

    def get_account_name_input(self):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        a = self.driver.get_element('x,//*[@id="nickName"]').get_attribute('readonly')
        self.driver.default_frame()
        return a

    def add_account_name(self, param):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        self.driver.operate_input_element('x,//*[@id="nickName"]', param)
        self.driver.default_frame()

    def get_add_account_name_exception_text(self):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        text = self.driver.get_text('x,//*[@id="userForm"]/div[3]/div/label')
        self.driver.default_frame()
        return text

    def add_account(self, param):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        self.driver.operate_input_element('x,//*[@id="account"]', param)
        self.driver.default_frame()

    def get_add_account_exception_text(self):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        text = self.driver.get_text('x,//*[@id="userForm"]/div[4]/div/label')
        self.driver.default_frame()
        return text

    def get_account_name_max_len(self):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        a = self.driver.get_element('x,//*[@id="nickName"]').get_attribute('maxlength')
        self.driver.default_frame()
        return a

    def click_ensure(self):
        self.driver.click_element('c,layui-layer-btn0')

    def get_account_max_len(self):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        a = self.driver.get_element('x,//*[@id="account"]').get_attribute('maxlength')
        self.driver.default_frame()
        return a

    def add_password_first(self, param):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        self.driver.operate_input_element('x,//*[@id="password"]', param)
        self.driver.default_frame()

    def add_password_second(self, param):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        self.driver.operate_input_element('x,//*[@id="pswAgain"]', param)
        self.driver.default_frame()

    def get_text_first_password(self):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        text = self.driver.get_text('x,//*[@id="markPassword"]/div[1]/div/label')
        self.driver.default_frame()
        return text

    def get_text_second_password(self):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        text = self.driver.get_text('x,//*[@id="markPswAgain"]/div/label')
        self.driver.default_frame()
        return text

    def get_phone_max_len(self):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        a = self.driver.get_element('x,//*[@id="phone"]').get_attribute('maxlength')
        self.driver.default_frame()
        return a

    def get_email_max_len(self):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        a = self.driver.get_element('x,//*[@id="email"]').get_attribute('maxlength')
        self.driver.default_frame()
        return a

    def get_connect_max_len(self):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        a = self.driver.get_element('x,//*[@id="contact"]').get_attribute('maxlength')
        self.driver.default_frame()
        return a

    def get_comp_max_len(self):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        a = self.driver.get_element('x,//*[@id="companyName"]').get_attribute('maxlength')
        self.driver.default_frame()
        return a

    def add_email_format(self, param):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        self.driver.operate_input_element('x,//*[@id="email"]', param)
        self.driver.default_frame()

    def get_text_email_text(self):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        text = self.driver.get_text('x,//*[@id="userForm"]/div[7]/div/label')
        self.driver.default_frame()
        return text

    def search_cust(self, param):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        self.driver.operate_input_element('x,//*[@id="treeDemo2_cusTreeKey"]', param)
        self.driver.click_element('x,//*[@id="treeDemo2_cusTreeSearchBtn"]')
        sleep(4)
        self.driver.default_frame()

    #编辑-搜索--点击查询结果
    def click_search_user(self):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        self.driver.click_element("c,autocompleter")
        self.driver.default_frame()

    def get_search_no_data_text(self):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        text = self.driver.get_text('x,//*[@id="treeRoleBox"]/div[1]/div[1]/span')
        self.driver.default_frame()
        return text

    def search_customer(self, param):
        self.driver.operate_input_element('x,//*[@id="treeDemo_cusTreeKey"]', param)
        self.driver.click_element('x,//*[@id="treeDemo_cusTreeSearchBtn"]')
        sleep(2)

    def get_search_customer_no_data_text(self):
        return self.driver.get_text(
            's,body > div.wrapper > div.main.oh > div > div > div.customer-leftsidebar > div > div > div.p-tb10.js-side-tree-box.show-userlist > div.tree-search > div.autocompleter-nodata > span')

    def click_edit_customer(self):
        self.driver.click_element('s,#customerlist > tr:nth-child(1) > td:nth-child(8) > a:nth-child(2)')
        sleep(2)

    def get_cust_type(self):
        text = self.driver.get_text('s,#customerlist > tr:nth-child(1) > td:nth-child(3)')
        return text

    def get_cust_account(self):
        text = self.driver.get_text('s,#customerlist > tr:nth-child(1) > td:nth-child(2)')
        return text

    def get_account_after_edit(self):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        text = self.driver.get_element('s,#account').get_attribute('value')
        self.driver.default_frame()
        return text

    def click_cancel_edit(self):
        self.driver.click_element('c,layui-layer-btn1')
        sleep(2)

    def get_up_account_after_edit(self):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        text = self.driver.get_element('s,#topUser').get_attribute('value')
        self.driver.default_frame()
        return text

    def get_account_type_after_edit(self):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        a = self.driver.get_element('s,#labelSale > div > input[type="radio"]').is_selected()
        b = self.driver.get_element('s,#labelDistributor > div > input[type="radio"]').is_selected()
        c = self.driver.get_element('s,#labelUser > div > input[type="radio"]').is_selected()

        if a == True:
            self.driver.default_frame()
            return " 销售"

        elif b == True:
            self.driver.default_frame()
            return " 代理商"

        elif c == True:
            self.driver.default_frame()
            return " 用户"

    def get_up_input_value(self):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        text = self.driver.get_element('s,#topUser').get_attribute('readonly')
        self.driver.default_frame()
        return text

    def get_account_value(self):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        text = self.driver.get_element('s,#account').get_attribute('disabled')
        self.driver.default_frame()
        return text

    def click_transfer_customer(self):
        self.driver.click_element('x,//*[@id="customerlist"]/tr[1]/td[8]/a[5]')
        sleep(2)

    def click_first_account(self):
        self.driver.click_element('x,//*[@id="customerlist"]/tr[1]/td[1]/span/div/ins')
        sleep(2)

    def click_batch_transfer_customer(self):
        self.driver.click_element('x,//*[@id="customerlist"]/tr[1]/td[8]/a[5]')
        sleep(2)

    def click_all_select_button(self):
        self.driver.click_element('x,//*[@id="customertableheader"]/thead/tr/th[1]/span/div/ins')
        sleep(2)

    def get_all_select_value(self):
        return self.driver.get_element('x,//*[@id="userAllCheck"]').is_selected()

    def get_per_account_number(self):
        number = len(list(self.driver.get_elements('x,//*[@id="customerlist"]')))
        return number

    def click_cancel_select_list(self):
        self.driver.click_element('x,//*[@id="customerlist"]/tr[1]/td[1]/span/div/ins')
        sleep(2)

    def select_per_page_numbers(self):
        self.driver.click_element('c,page-select')
        sleep(2)
        self.driver.get_element('c,page-select').send_keys(Keys.DOWN + Keys.ENTER)
        sleep(2)

    def get_texts_email_text(self):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        text = self.driver.get_text('x,//*[@id="userForm"]/div[6]/div/label')
        self.driver.default_frame()
        return text

    # 当前账户-新增用户（密码默认888888）
    def add_default_password_acc(self, acc_name, account, phone, email, conn, com):
        # 编辑客户名称
        self.driver.operate_input_element("nickName", acc_name)
        self.driver.wait(1)
        # 编辑登录账号
        self.driver.operate_input_element("account", account)
        self.driver.wait(1)
        # 编辑电话
        self.driver.operate_input_element("phone", phone)
        self.driver.wait(1)
        # 编辑邮箱
        self.driver.operate_input_element("email", email)
        self.driver.wait(1)
        # 编辑联系人
        self.driver.operate_input_element("contact", conn)
        self.driver.wait(1)
        # 编辑公司名
        self.driver.operate_input_element("companyName", com)
        self.driver.wait(1)

    # 修改默认密码
    def user_default_password_edit(self, password):
        self.driver.operate_input_element("x,//*[@id='newPwd_advise']", password)
        self.driver.operate_input_element("x,//*[@id='renewPwd_advise']", password)
        self.driver.wait(1)
        self.driver.click_element("x,//*[@id='layui-layer1']/div[3]/a")

    # 修改密码后的提示
    def user_default_password_edit_prompt(self, user_type=""):
        if user_type == "用户":
            prompt = self.driver.get_text("x,/html/body/div[4]/div[2]")
            print(prompt)
            self.driver.wait()
            self.driver.click_element("x,/html/body/div[4]/div[3]/a")
            return prompt
        else:
            prompt = self.driver.get_text("x,/html/body/div[7]/div[2]")
            print(prompt)
            self.driver.wait()
            self.driver.click_element("x,/html/body/div[7]/div[3]/a")
            return prompt


    # 点击设备管理页面的监控用户
    def click_dev_page_monitoring_account_button(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[1]/div[2]/button')
        sleep(2)

    # 获取控制台--左侧客户名称
    def get_console_page_username(self):
        text = self.driver.get_text("x,//*[@id='account']")
        name = text.split("(")[0]
        print(name)
        return name

    # 获取默认密码提示
    def get_update_default_password_prompt(self, newPwd, renewPwd):
        self.driver.operate_input_element("x,//*[@id='newPwd_advise']", newPwd)
        self.driver.operate_input_element("x,//*[@id='renewPwd_advise']", renewPwd)
        self.driver.wait(1)
        self.driver.click_element("x,//*[@id='layui-layer1']/div[3]/a")
        self.driver.wait(1)

        #获取提示
        pwd1_prompt = self.driver.get_text("x,//*[@id='editpwd-form_advise']/div[1]/div/label")
        pwd2_prompt = self.driver.get_text("x,//*[@id='editpwd-form_advise']/div[2]/div/label")
        data = {
            "newPwd": pwd1_prompt,
            "renewPwd": pwd2_prompt
        }
        return data

    # 新增账号--web登录权限
    def setting_web_login_permissions(self, state):
        print(state)
        if state == "True":
            sleep(2)
            web_status = self.driver.get_element("webLogin").is_selected()
            return web_status

        elif state == "False":
            self.driver.click_element("x,//*[@id='userForm']/div[11]/div[1]/label")
            web_status = self.driver.get_element("webLogin").is_selected()
            return web_status

    # 新增账号--app登录权限
    def setting_app_login_permissions(self, state):
        if state == "True":
            sleep(2)
            app_status = self.driver.get_element("appLogin").is_selected()
            return app_status

        elif state == "False":
            self.driver.click_element("x,//*[@id='userForm']/div[11]/div[2]/label")
            app_status = self.driver.get_element("appLogin").is_selected()
            return app_status

    # 指令权限--批量下发指令
    def setting_command_permissions(self, state):
        command_status = str(self.driver.get_element("isBatchSendIns").is_selected())

        if command_status == state:
            print(command_status)
            return command_status

        elif command_status != state:
            self.driver.click_element("x,//*[@id='customer_isBatchSendIns']/label")
            command_status = self.driver.get_element("isBatchSendIns").is_selected()
            print(command_status)
            return command_status

    # 指令权限--批量下发工作模式
    def setting_working_mode_permissions(self, state):
        working_mode_status = str(self.driver.get_element("isBatchSendFM").is_selected())
        if working_mode_status == state:
            print(working_mode_status)
            return working_mode_status

        elif working_mode_status != state:
            self.driver.click_element("x,//*[@id='customer_isBatchSendFM']/label")
            working_mode_status = self.driver.get_element("isBatchSendFM").is_selected()
            print(working_mode_status)
            return working_mode_status


    #点设备管理
    def get_facility_manage_page_function_button(self):
        self.driver.click_element("device")
        sleep(2)
        #获取全部功能按钮
        button_list = []
        all_data = len(self.driver.get_elements("x,//*[@id='allDev']/div[2]/div[2]/div/div/button"))
        for a in range(all_data):
            text = self.driver.get_text("x,//*[@id='allDev']/div[2]/div[2]/div/div/button[" + str(a + 1) +"]")
            button_list.append(text)

        print("设备管理页面", button_list)
        return button_list

    #获取指令管理页面模块
    def get_command_page_module(self):
        self.driver.click_element("x,/html/body/div[2]/header/div/div[2]/div[2]/div[2]/a[1]")
        sleep(2)
        #获取指令模块
        command_module = []
        all_module = len(self.driver.get_elements("x,//*[@id='insManage_ul']/li"))
        for a in range(all_module):
            text = self.driver.get_text("x,/html/body/div[1]/div[5]/div/div/div[1]/div/div[2]/ul/li[" + str(a + 1) +"]")
            command_module.append(text)

        print("指令管理页面", command_module)
        return command_module

    #转移客户-账户查找
    def transfer_import_account_search(self, search_account):
        # 点击下拉箭头图标
        self.search_cust(search_account)
        self.driver.wait(3)
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        #获取查询结果
        list_data = len(self.driver.get_elements("x,/html/body/div/div/form/div/div/div[1]/div/ul/li"))

        if list_data >=1:
            list = []
            for i in range(list_data):
                text = self.driver.get_text("x,/html/body/div/div/form/div/div/div[1]/div/ul/li[" + str(i + 1) +"]")
                list.append(text)
            self.driver.default_frame()
            print(list)
            return list
        else:
            no_data = self.driver.get_text('x,//*[@id="treeRoleBox"]/div[1]/div[1]/span')
            self.driver.default_frame()
            print(no_data)
            return no_data


    #获取客户类型列表
    def get_acc_user_type_list(self):
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        type_list_len = len(self.driver.get_elements("x,/html/body/div/div/form/div[2]/div/div"))
        print(type_list_len)
        for i in range(type_list_len):
            # 获取style状态
            state = self.driver.get_element("x,//*[@id='typeRoleRadio" + str(i + 1) + "']").get_attribute('style')
            if state == "display: none;":
                continue
            else:
                print("else", ("x,//*[@id='typeRoleRadio" + str(i + 1) + "']"))
                list_len = len(
                    self.driver.get_elements("x,/html/body/div/div/form/div[2]/div/div[" + str(i + 2) + "]/label"))
                if list_len == 3:
                    sale = self.driver.get_text("x,//*[@id='typeRoleRadio1']/label[1]")
                    distributor = self.driver.get_text("x,//*[@id='typeRoleRadio1']/label[2]")
                    user = self.driver.get_text("x,//*[@id='typeRoleRadio1']/label[3]")

                    type_data = {"sale": sale,
                                 "distributor": distributor,
                                 "user": user,
                                 "length": list_len,
                                 "type_id": "typeRoleRadio1"
                                 }
                    print("333", type_data)
                    self.driver.default_frame()
                    return type_data
                elif list_len == 2:
                    distributor = self.driver.get_text("x,//*[@id='typeRoleRadio2']/label[1]")
                    user = self.driver.get_text("x,//*[@id='typeRoleRadio2']/label[2]")
                    type_data = {
                        "distributor": distributor,
                        "user": user,
                        "length": list_len,
                        "type_id": "typeRoleRadio2"
                    }
                    print("222", type_data)
                    self.driver.default_frame()
                    return type_data
                else:
                    user = self.driver.get_text("x,//*[@id='typeRoleRadio3']/label")
                    type_data = {"user": user,
                                 "length": list_len,
                                 "type_id": "typeRoleRadio3"
                                 }
                    print("1111", type_data)
                    self.driver.default_frame()
                    return type_data

    #点击编辑-取消--编辑
    def click_edit_customer_process(self):
        self.click_edit_customer()
        self.click_cancel_edit()
        self.click_edit_customer()
