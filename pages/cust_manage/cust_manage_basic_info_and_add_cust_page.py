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
        self.driver.click_element("customerManagement")
        self.driver.wait(3)

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
    def acc_type_choose(self, acc_type):
        if acc_type == '销售':
            self.driver.click_element("labelSale")

        elif acc_type == '代理商':
            self.driver.click_element("labelDistributor")

        elif acc_type == '用户':
            self.driver.click_element("labelUser")

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
        ele = self.driver.get_element("addUserBtn")
        self.driver.execute_script(ele)
        self.driver.click_element("addUserBtn")
        self.driver.wait(1)

    # 当前账户-编辑用户-保存成功操作状态
    def acc_info_save_status(self):
        save_status = self.driver.get_element("c,layui-layer-content").text
        return save_status

    # 当前账户-编辑用户-搜索客户名称/账户
    def acc_search(self, keyword):
        # 将滚动条滚动至搜索输入框处
        ele = self.driver.get_element("treeDemo2_cusTreeKey")
        self.driver.execute_script(ele)
        # 在搜索输入框内输入搜索关键词
        self.driver.operate_input_element("treeDemo2_cusTreeKey", keyword)
        # 点击搜索按钮
        self.driver.click_element("treeDemo2_cusTreeSearchBtn")
        self.driver.wait(1)
        # 选择列表中第一个搜索结果
        self.driver.click_element('c,autocompleter-item')

    # 新增客户
    def add_acc(self):
        # 点击新增客户
        self.driver.click_element("x,/html/body/div[2]/div[5]/div/div/div[1]/div/div[1]/a/i")
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
