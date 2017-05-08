from time import sleep

from automate_driver.automate_driver import AutomateDriver
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page import BasePage

# 客户管理页面-下级客户
# author:孙燕妮
from pages.base.base_page_server import BasePageServer
from pages.base.new_paging import NewPaging


class CustManageLowerAccountPages(BasePage):
    def __init__(self, driver: AutomateDriver, base_url):
        super().__init__(driver, base_url)
        self.base_page = BasePage(self.driver, self.base_url)

    # 点击进入“下级客户”
    def enter_lower_acc(self):
        self.driver.click_element("markUser")
        self.driver.wait()

    # 获取当前客户的下级客户个数
    def count_curr_lower_acc(self):
        new_paging = NewPaging(self.driver, self.base_url)
        try:
            total = new_paging.get_total_number("x,//*[@id='pagingCustomer']", "x,//*[@id='markUserTable']")
            return total
        except:
            return 0
        '''
        # 设置列表底部每页共10条
        self.base_page.select_per_page_number(10)
        # 获取结果共分几页
        total_pages_num = self.base_page.get_total_pages_num("x,//*[@id='pagingCustomer']")
        # 获取最后一页有几条记录
        last_page_num = self.base_page.last_page_logs_num("x,//*[@id='markUserTable']","x,//*[@id='pagingCustomer']")
        # 计算当前结果共几条
        count = self.base_page.total_num(total_pages_num,last_page_num)
        return count'''

    # 搜索框输入客户名称或账号
    def input_search_info(self, keyword):
        self.driver.operate_input_element("searchAccount", keyword)
        self.driver.wait(1)

    # 点击搜索
    def click_search_btn(self):
        self.driver.click_element("x,//*[@id='allDev']/div[2]/div[2]/div[1]/div[2]/div/div/span/button")
        self.driver.wait()

    # 获取搜索结果账号
    def get_search_result_acc(self):
        result_acc = self.driver.get_element("x,/html/body/div[2]/div[5]/div/div/div[2]/div/div[2]/div[1]/"
                                             "div[2]/div[2]/div[3]/table/tbody/tr/td[2]").text
        return result_acc

    # 点击不同的客户类型
    def click_acc_type(self, type):
        if type == '销售':
            self.driver.click_element("x,//*[@id='allDev']/div[2]/div[2]/div[1]/div[1]/div/button[2]")
            self.driver.wait()
        elif type == '代理商':
            self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[2]/div[1]/div[1]/div/button[2]')
            self.driver.wait()
        elif type == '用户':
            self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[2]/div[1]/div[1]/div/button[3]')
            self.driver.wait()

    # 全选下级客户
    def select_all_acc(self):
        self.driver.click_element("x,//*[@id='clientTableHeader']/thead/tr/th[1]/span/div")
        self.driver.wait(1)

    # 点击新增客户
    def click_add_acc(self):
        self.driver.click_element("x,//*[@id='allDev']/div[2]/div[2]/div[1]/div[1]/button[1]")
        self.driver.wait()

    # 当前账户-新增用户-选择客户类型
    def acc_type_choose(self, acc_type):
        if acc_type == '销售':
            self.driver.click_element("labelSale")

        elif acc_type == '代理商':
            self.driver.click_element('x,//*[@id="labelDistributor"]/div/ins')

        elif acc_type == '用户':
            self.driver.click_element('x,//*[@id="labelUser"]/div/ins')

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

    # 当前账户-新增用户-保存
    def acc_info_save(self):
        # 将滚动条滚动至保存按钮处
        ele = self.driver.get_element("addUserBtn")
        self.driver.execute_script(ele)
        self.driver.click_element("addUserBtn")
        self.driver.wait(1)

    # 当前账户-新增用户-保存成功操作状态
    def acc_info_save_status(self):
        save_status = self.driver.get_element("c,layui-layer-content").text
        return save_status

    # 点击批量转移
    def click_batch_trans(self):
        self.driver.click_element("x,//*[@id='allDev']/div[2]/div[2]/div[1]/div[1]/button[2]")
        self.driver.wait(1)

    # 批量转移-搜素转移客户
    def search_trans_acc(self, acc):
        self.driver.operate_input_element("complexTrans_globalSearch_input_transCust2", acc)
        # 点击搜索
        self.driver.click_element("complexTrans_globalSearch_btn_transCust2")
        self.driver.wait(1)
        # 选择搜索结果  c,autocompleter-item
        self.driver.click_element("c,autocompleter-item")
        self.driver.wait(1)

    # 批量转移-保存
    def trans_info_save(self):
        self.driver.click_element("transCustBtn_id")
        self.driver.wait(1)

    # 批量转移-保存状态
    def trans_info_save_status(self):
        save_status = self.driver.get_element("c,layui-layer-content").text
        return save_status

    # 单个用户操作-编辑
    def click_acc_edit(self):
        self.driver.click_element("x,//*[@id='markUserTable']/tr[1]/td[8]/a[2]")
        self.driver.wait()

    # 单个用户操作-编辑信息
    def edit_acc_input_info_edit(self, acc_name, phone, email, conn, com):
        # 编辑客户名称
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

    # 单个用户操作-编辑信息-保存
    def edit_info_save(self):
        self.driver.click_element("updateUserBtn")
        self.driver.wait(1)

    # 单个用户操作-编辑信息-保存状态
    def edit_info_save_status(self):
        status = self.driver.get_element("c,layui-layer-content").text
        return status

    # 单个用户操作-控制台
    def enter_console(self):
        self.driver.click_element("x,/html/body/div[2]/div[5]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[3]/"
                                  "table/tbody/tr[1]/td[8]/a[1]")
        self.driver.wait()

    # 单个用户操作-重置密码
    def acc_reset_passwd(self):
        self.driver.click_element("x,//*[@id='markUserTable']/tr[1]/td[8]/a[3]")
        self.driver.wait()

    # 单个用户操作-“重置密码”弹框文本内容
    def reset_passwd_content(self):
        reset_passwd_content = self.driver.get_element("c,layui-layer-content").text
        return reset_passwd_content

    # 单个用户操作-“重置密码”-确定
    def reset_passwd_ensure(self):
        self.driver.click_element("c,layui-layer-btn0")
        self.driver.wait(1)

    # 单个用户操作-“重置密码”-确定-操作状态
    def get_reset_status(self):
        reset_status = self.driver.get_element("c,layui-layer-content").text
        return reset_status

    # 单个用户操作-“重置密码”-取消
    def reset_passwd_dismiss(self):
        self.driver.click_element("c,layui-layer-btn1")
        self.driver.wait()

    # 单个用户操作-删除
    def delete_acc(self):
        self.driver.click_element("x,//*[@id='markUserTable']/tr[1]/td[8]/a[4]")
        self.driver.wait(1)

    # 单个用户操作-删除-确定
    def delete_acc_ensure(self):
        self.driver.click_element("c,layui-layer-btn0")
        self.driver.wait(1)

    # 获取删除状态
    def get_del_status(self):
        status = self.driver.get_element("c,layui-layer-content").text
        return status

    # 单个用户操作-删除-取消
    def delete_acc_dismiss(self):
        self.driver.click_element("c,layui-layer-btn1")
        self.driver.wait(1)

    # 单个用户操作-转移客户
    def click_user_trans(self):
        self.driver.click_element("x,//*[@id='markUserTable']/tr[1]/td[8]/a[5]")
        self.driver.wait(1)

    # 单个用户操作-转移客户-搜索客户
    def user_trans_search(self, trans_user):
        # 搜索框输入账户/客户名称
        self.driver.operate_input_element("complexTrans_globalSearch_input_transCust2", trans_user)
        self.driver.wait(1)
        # 点击搜索
        self.driver.click_element("complexTrans_globalSearch_btn_transCust2")
        self.driver.wait()
        # 选择列表中搜索结果
        self.driver.click_element("c,autocompleter-item")
        self.driver.wait(1)

    # 单个用户操作-转移客户-保存
    def click_trans(self):
        self.driver.click_element("transCustBtn_id")
        self.driver.wait(1)

    # 单个用户操作-转移客户-获取转移状态
    def get_trans_status(self):
        status = self.driver.get_element("c,layui-layer-content").text
        return status

    def add_data_to_search_account(self, search_data):
        if search_data['account_type'] == '':
            self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[2]/div[1]/div[1]/div/button[1]')
        elif search_data['account_type'] == '代理商':
            self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[2]/div[1]/div[1]/div/button[2]')
        elif search_data['account_type'] == '用户':
            self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[2]/div[1]/div[1]/div/button[3]')
        sleep(3)

        self.driver.operate_input_element('x,//*[@id="searchAccount"]', search_data['info'])
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[2]/div[1]/div[2]/div/div/span/button')
        sleep(5)

    def get_account_number(self):
        # 获取设备列表中的总数
        a = self.driver.get_element('x,//*[@id="pagingCustomer"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            number = new_paging.get_total_number('x,//*[@id="pagingCustomer"]', 'x,//*[@id="markUserTable"]')
            return number
        elif a == 'display: none;':
            return 0
