from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.base.base_page import BasePage

# 全局搜索-用户搜索功能的元素及操作
# author:孙燕妮
from pages.base.new_paging import NewPaging


class GlobalAccountSearchPage(BasePage):
    def __init__(self, driver: AutomateDriver, base_url):
        super().__init__(driver, base_url)
        self.base_page = BasePage(self.driver, self.base_url)

    # 全局搜索栏-设备搜索按钮
    def click_easy_search(self):
        self.driver.click_element("x,//*[@id='complexQuery']/div/div/button")
        self.driver.wait(1)

    # 全局搜索栏-用户搜索按钮
    def click_account_search(self):
        self.driver.click_element("x,//*[@id='complexQuery']/div/button[1]")
        self.driver.wait(1)

    # 全局搜索栏-用户搜索
    def acc_easy_search(self, search_keyword):
        # 在设备名称/imei/账号输入框内输入搜索关键词信息
        self.driver.operate_input_element("basicKeyword", search_keyword)
        # 点击搜索用户按钮
        self.driver.click_element("x,//*[@id='complexQuery']/div/button[1]")
        self.driver.wait(3)

    # 全局搜索用户（快捷销售新增的客户）--查看
    def view_search_cust(self):
        sleep(2)
        self.driver.click_element('x,//*[@id="complex_user_relation_tbody"]/tr[2]/td[7]/a[4]')
        self.driver.wait()

    # 用户搜索对话框-切换为用户搜索
    def change_dev_dial_to_account(self):
        # 点击设备/用户下拉框
        self.driver.click_element("x,/html/body/div[13]/div/div/div[2]/div[1]/div[1]/div/div/div/div/span[2]")
        self.driver.wait(1)
        # 选择用户
        self.driver.click_element("x,/html/body/div[13]/div/div/div[2]/div[1]/div[1]/div/div/div/div/div/ul/li[1]")

    # 用户搜索对话框-用户搜索按钮
    def click_account_dial_search(self):
        self.driver.click_element("x,//*[@id='searchUserEquipment']/div/div/div[2]/div[1]/div[1]/div/span/button[1]")
        self.driver.wait(5)

    # 用户搜索对话框-用户搜索
    def account_dial_search(self, search_keyword):
        # 在用户名称/账号输入框内输入搜索关键词信息
        self.driver.operate_input_element("x,//*[@id='searchUserEquipment']/div/div/div[2]/div[1]/div[1]/div/input",
                                          search_keyword)
        # 点击搜索按钮
        self.driver.click_element("x,//*[@id='searchUserEquipment']/div/div/div[2]/div[1]/div[1]/div/span/button[1]")
        self.driver.wait(10)

    # 用户搜索对话框-关闭
    def close_dev_search(self):
        self.driver.click_element("x,//*[@id='searchUserEquipment']/div/div/div[1]/button")
        self.driver.wait(1)

    # 用户精确搜索结果获取
    # 获取其账户
    def get_exact_search_acc(self):
        account_text = self.driver.get_element('x,//*[@id="complex_user_relation_tbody"]/tr[2]/td[2]').text
        return account_text

    # 获取其用户名
    def get_exact_search_name(self):
        name_text = self.driver.get_element("x,//*[@id='complex_user_relation_tbody']/tr[2]/td[2]").text
        return name_text

    # 用户搜索-获取搜索结果共多少条
    def easy_search_result(self):
        # 当搜索结果只有一条时，必可获取到用户信息
        try:
            # 获取用户信息
            self.driver.get_element(
                "x,/html/body/div[13]/div/div/div[2]/div[3]/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[7]/a[1]")
            result_num = 1
            return result_num
        # 当搜索结果大于1条时
        except:
            '''
            # 将滚动条拖动到分页栏
            target = self.driver.get_element("complex_paging_user")
            self.driver.execute_script(target)  # 拖动到可见的元素去

            # 设置每页10条
            self.base_page.select_per_page_number(10)
            # 获取搜索结果共分几页
            total_pages_num =  self.base_page.get_total_pages_num("x,//*[@id='complex_paging_user']")
            # 获取搜索结果最后一页有几条
            last_page_logs_num = self.base_page.last_page_logs_num("x,//*[@id='complex_user_tbody']",
                                                                   "x,//*[@id='complex_paging_user']")
            # 计算当前搜索结果共几条
            total_num = self.base_page.total_num(total_pages_num,last_page_logs_num)
            return total_num'''
            new_paging = NewPaging(self.driver, self.base_url)
            try:
                total = new_paging.get_total_number("x,//*[@id='complex_paging_user']",
                                                    "x,//*[@id='complex_user_tbody']")
                return total
            except:
                return 0

    # 用户详情-用户关系操作
    def click_user_relation_link(self, link_name):

        if link_name == '父根级用户-控制台':
            # 设备详情-用户关系-父用户操作-父根级用户-“控制台”
            self.driver.click_element("x,//*[@id='complex_user_relation_tbody']/tr[1]/td[7]/a[1]")
            self.driver.wait()
        elif link_name == '父根级用户-查看':
            # 设备详情-用户关系-父用户操作-父根级用户-“控制台”
            self.driver.click_element("x,//*[@id='complex_user_relation_tbody']/tr[1]/td[7]/a[2]")
            self.driver.wait()
        elif link_name == '父根级的下级用户-控制台':
            # 设备详情-用户关系-父用户操作-父根级用户-“控制台”
            self.driver.click_element("x,//*[@id='complex_user_relation_tbody']/tr[2]/td[7]/a[1]")
            self.driver.wait()
        elif link_name == '父根级的下级用户-查看':
            # 设备详情-用户关系-父根级的下级用户-“查看”
            self.driver.click_element("x,//*[@id='complex_user_relation_tbody']/tr[2]/td[7]/a[4]")
            self.driver.wait()
        elif link_name == '当前设备用户-控制台':
            # 设备详情-用户关系-当前设备用户-“控制台”
            self.driver.click_element("x,//*[@id='complex_user_relation_tbody']/tr[3]/td[7]/a[1]")
            self.driver.wait()
        elif link_name == '当前设备用户-查看':
            # 设备详情-用户关系-当前设备用户-“查看”
            self.driver.click_element(
                "x,/html/body/div[13]/div/div/div[2]/div[3]/div[2]/div[2]/div[1]/table/tbody/tr[2]/td[7]/a[4]")
            self.driver.wait()

    # 用户详情-用户关系-当前用户-“重置密码”
    def curr_acc_reset_passwd(self):
        self.driver.click_element('x,//*[@id="complex_user_relation_tbody"]/tr[2]/td[7]/a[3]')
        self.driver.wait()

    # 用户详情-用户关系-当前用户-“重置密码”弹框文本内容
    def reset_passwd_content(self):
        reset_passwd_content = self.driver.get_element("c,layui-layer-content").text
        return reset_passwd_content

    # 用户详情-用户关系-当前用户-“重置密码”-确定
    def reset_passwd_ensure(self):
        self.driver.click_element("c,layui-layer-btn0")
        self.driver.wait(1)

    # 用户详情-用户关系-当前用户-“重置密码”-确定-操作状态
    def get_reset_status(self):
        reset_status = self.driver.get_element("c,layui-layer-content").text
        return reset_status

    # 用户详情-用户关系-当前用户-“重置密码”-取消
    def reset_passwd_dismiss(self):
        self.driver.click_element("c,layui-layer-btn1")
        self.driver.wait()

    # 用户详情-用户信息
    def click_acc_info(self):
        self.driver.click_element("x,//*[@id='searchUserEquipment']/div/div/div[2]/div[3]/div[2]/div[1]/ul/li[2]/a")
        self.driver.wait(1)

    # 用户详情-用户信息-选择客户类型
    def acc_type_choose(self, acc_type):
        if acc_type == '销售':
            self.driver.click_element(
                "x,//*[@id='complex_userInfo_Form_complexUpdate']/div[2]/div/div/label[1]/div/ins")

        elif acc_type == '代理商':
            self.driver.click_element(
                "x,//*[@id='complex_userInfo_Form_complexUpdate']/div[2]/div/div/label[2]/div/ins")

        elif acc_type == '用户':
            self.driver.click_element(
                "x,/html/body/div[13]/div/div/div[2]/div[3]/div[2]/div[2]/div[2]/div/form/div[2]/div/div/label[2]/div/ins")

    # 用户详情-用户信息-编辑用户输入框信息
    def acc_input_info_edit(self, acc_name, phone, email, conn, com):
        # 编辑用户名称
        self.driver.operate_input_element("x,//*[@id='complex_userInfo_Form_complexUpdate']/div[3]/div/input", acc_name)
        self.driver.wait(1)
        # 编辑电话
        self.driver.operate_input_element("x,//*[@id='complex_userInfo_Form_complexUpdate']/div[5]/div/input", phone)
        self.driver.wait(1)
        # 编辑邮箱
        self.driver.operate_input_element("x,//*[@id='complex_userInfo_Form_complexUpdate']/div[6]/div/input", email)
        self.driver.wait(1)
        # 编辑联系人
        self.driver.operate_input_element(
            'x,/html/body/div[10]/div/div/div[2]/div[3]/div[2]/div[2]/div[2]/div/form/div[7]/div/input', conn)
        self.driver.wait(1)
        # 编辑公司名
        self.driver.operate_input_element(
            'x,/html/body/div[10]/div/div/div[2]/div[3]/div[2]/div[2]/div[2]/div/form/div[8]/div/input', com)
        self.driver.wait(1)

    # 用户详情-用户信息-修改用户登录权限
    def acc_login_limit_modi(self):
        # 判断App登录权限是否已勾选
        ele = self.driver.get_element("x,//*[@id='complex_userInfo_Form_complexUpdate']/div[10]/div[2]/label/div/ins")
        status = ele.is_selected()
        if status == True:
            # 取消勾选App登录权限
            self.driver.click_element("x,//*[@id='complex_userInfo_Form_complexUpdate']/div[10]/div[2]/label/div/ins")

    # 用户详情-用户信息-修改用户指令权限
    def acc_instr_limit_modi(self):
        # 将滚动条滚动至保存按钮处
        ele = self.driver.get_element("complex_updateUserBtn")
        self.driver.execute_script(ele)
        # 判断批量下发指令是否已勾选
        ele = self.driver.get_element("x,//*[@id='complex_userInfo_Form_complexUpdate']/div[11]/div[1]/label/div/ins")
        status = ele.is_selected()
        if status == False:
            # 勾选批量下发指令
            self.driver.click_element("x,//*[@id='complex_userInfo_Form_complexUpdate']/div[11]/div[1]/label/div/ins")

    # 用户详情-用户信息-修改用户修改权限
    def acc_modi_limit_modi(self):
        # 将滚动条滚动至保存按钮处
        ele = self.driver.get_element("complex_updateUserBtn")
        self.driver.execute_script(ele)
        # 判断修改设备是否已勾选
        ele = self.driver.get_element("x,//*[@id='complex_userInfo_Form_complexUpdate']/div[12]/div/label/div/ins")
        status = ele.is_selected()
        if status == False:
            # 勾选修改设备
            self.driver.click_element("x,//*[@id='complex_userInfo_Form_complexUpdate']/div[12]/div/label/div/ins")

    # 用户详情-用户信息-保存
    def acc_info_save(self):
        # 将滚动条滚动至保存按钮处
        ele = self.driver.get_element("complex_updateUserBtn")
        self.driver.execute_script(ele)
        self.driver.click_element("complex_updateUserBtn")
        self.driver.wait(1)

    # 用户详情-用户信息-保存成功操作状态
    def acc_info_save_status(self):
        save_status = self.driver.get_element("c,layui-layer-content").text
        return save_status

    # 用户详情-用户信息-搜索客户名称/账户
    def acc_search(self, keyword):
        # 将滚动条滚动至搜索输入框处
        ele = self.driver.get_element("complexUpdate_globalSearch_input")
        self.driver.execute_script(ele)
        # 在搜索输入框内输入搜索关键词
        self.driver.operate_input_element("complexUpdate_globalSearch_input", keyword)
        # 点击搜索按钮
        self.driver.click_element("complexUpdate_globalSearch_btn")
        self.driver.wait(1)
        # 选择列表中第一个搜索结果
        self.driver.click_element("x,/html/body/div[13]/div/div/div[2]/div[3]/div[2]/div[2]/div[2]/div/form/div[1]/"
                                  "div[2]/div/div/div/div/ul/li[1]")

    # 用户详情-销售设备
    def click_sale_dev(self):
        self.driver.click_element('x,//*[@id="searchUserEquipment"]/div/div/div[2]/div[3]/div[2]/div[1]/ul/li[3]/a')

    # 用户详情-销售设备-选择用户到期时间
    def choose_account_expired_time(self, account_expired_time):
        self.driver.click_element("x,//*[@id='complex_user_sale_complexSale']/div[2]/div[1]/span/div/span[2]")
        self.driver.wait(1)
        if account_expired_time == '一个月':
            self.driver.click_element("x,//*[@id='complex_user_sale_complexSale']/div[2]/div[1]/span/div/div/ul/li[2]")
        elif account_expired_time == '两个月':
            self.driver.click_element("x,//*[@id='complex_user_sale_complexSale']/div[2]/div[1]/span/div/div/ul/li[3]")
        elif account_expired_time == '三个月':
            self.driver.click_element("x,//*[@id='complex_user_sale_complexSale']/div[2]/div[1]/span/div/div/ul/li[4]")
        elif account_expired_time == '半年':
            self.driver.click_element("x,//*[@id='complex_user_sale_complexSale']/div[2]/div[1]/span/div/div/ul/li[5]")
        elif account_expired_time == '一年':
            self.driver.click_element("x,//*[@id='complex_user_sale_complexSale']/div[2]/div[1]/span/div/div/ul/li[6]")
        elif account_expired_time == '不限制':
            self.driver.click_element("x,//*[@id='complex_user_sale_complexSale']/div[2]/div[1]/span/div/div/ul/li[7]")

    # 用户详情-销售设备-重置
    def reset_dev_sale(self):
        self.driver.click_element("x,//*[@id='complex_user_sale_complexSale']/div[2]/div[1]/button")
        self.driver.wait(1)

    # 用户详情-销售设备-获取当前已选中的设备个数
    def dev_sale_num(self):
        num = self.driver.get_element("sale_count_complexSale").text
        return num

    # 用户详情-销售设备-输入设备imei
    def dev_imei_input(self, imei):
        self.driver.operate_input_element("sale_imei_complexSale", imei)

    # 用户详情-销售设备-添加
    def dev_add(self):
        self.driver.click_element("x,//*[@id='complex_user_sale_complexSale']/div[1]/div/div[1]/div/div[3]/button[1]")
        self.driver.wait(1)

    # 用户详情-销售设备-取消添加
    def dev_add_dismiss(self):
        self.driver.click_element("x,//*[@id='complex_user_sale_complexSale']/div[1]/div/div[1]/div/div[3]/button[2]")
        self.driver.wait(1)

    # 用户详情-销售设备-删除已添加的设备
    def del_add_imei(self):
        self.driver.click_element('x,//*[@id="sale_tbody_complexSale"]/tr/td[4]/a')
        self.driver.wait(1)

    # 用户详情-销售设备-点击销售
    def click_sale_btn(self):
        self.driver.click_element("x,//*[@id='complex_user_sale_complexSale']/div[2]/div[2]/button[3]")

    # 用户详情-销售设备-获取销售状态
    def get_dev_sale_status(self):
        status = self.driver.get_element("c,layui-layer-content").text
        return status

    # 用户详情-销售设备-取消销售
    def click_dis_sale_btn(self):
        self.driver.click_element("x,//*[@id='complex_user_sale_complexSale']/div[2]/div[2]/button[1]")

    # 用户详情-新增下级用户
    def click_add_lower_acc(self):
        self.driver.click_element("x,//*[@id='searchUserEquipment']/div/div/div[2]/div[3]/div[2]/div[1]/ul/li[4]/a")
        self.driver.wait(1)

    # 用户详情-新增下级用户-选择客户类型
    def add_acc_type_choose(self, acc_type):
        if acc_type == '销售':
            self.driver.click_element("x,//*[@id='complex_addUser_form']/div[2]/div[1]/div/label[1]/div/ins")

        elif acc_type == '代理商':
            self.driver.click_element("x,//*[@id='complex_addUser_form']/div[2]/div[1]/div/label[2]/div/ins")

        elif acc_type == '用户':
            self.driver.click_element("x,//*[@id='complex_addUser_form']/div[2]/div[1]/div/label[3]/div/ins")

    # 用户详情-新增下级用户-编辑用户输入框信息
    def add_acc_input_info_edit(self, login_acc, acc_name, phone, email, conn, com, new_pwd):
        # 编辑登录账号
        self.driver.operate_input_element("x,//*[@id='complex_addUser_form']/div[3]/div[1]/input", login_acc)
        self.driver.wait(1)
        # 编辑客户名称
        self.driver.operate_input_element("x,//*[@id='complex_addUser_form']/div[4]/div[1]/input", acc_name)
        self.driver.wait(1)
        # 编辑电话
        self.driver.operate_input_element("x,//*[@id='complex_addUser_form']/div[2]/div[2]/input", phone)
        self.driver.wait(1)
        # 编辑邮箱
        self.driver.operate_input_element("x,//*[@id='complex_addUser_form']/div[3]/div[2]/input", email)
        self.driver.wait(1)
        # 编辑联系人
        self.driver.operate_input_element(
            'x,/html/body/div[10]/div/div/div[2]/div[3]/div[2]/div[2]/div[4]/div/form/div[1]/div[2]/input', conn)
        self.driver.wait(1)
        # 编辑公司名
        self.driver.operate_input_element(
            'x,/html/body/div[10]/div/div/div[2]/div[3]/div[2]/div[2]/div[4]/div/form/div[5]/div[1]/input', com)
        self.driver.wait(1)
        # 清空当前密码，输入新密码
        self.driver.operate_input_element(
            'x,/html/body/div[10]/div/div/div[2]/div[3]/div[2]/div[2]/div[4]/div/form/div[6]/div[1]/input', new_pwd)
        self.driver.wait(1)
        # 确认密码
        self.driver.operate_input_element(
            'x,/html/body/div[10]/div/div/div[2]/div[3]/div[2]/div[2]/div[4]/div/form/div[7]/div/div/input', new_pwd)
        self.driver.wait(1)

    # 用户详情-新增下级用户-修改用户登录权限
    def add_acc_login_limit_modi(self):
        # 判断App登录权限是否已勾选
        ele = self.driver.get_element("x,//*[@id='complex_addUser_form']/div[4]/div[2]/label[1]/div/ins")
        status = ele.is_selected()
        if status == True:
            # 取消勾选App登录权限
            self.driver.click_element("x,//*[@id='complex_addUser_form']/div[4]/div[2]/label[1]/div/ins")

    # 用户详情-新增下级用户-修改用户指令权限
    def add_acc_instr_limit_modi(self):
        # 判断批量下发指令是否已勾选
        ele = self.driver.get_element(
            'x,/html/body/div[13]/div/div/div[2]/div[3]/div[2]/div[2]/div[4]/div/form/div[5]/div[2]/label[1]/div/ins')
        status = ele.is_selected()
        if status == False:
            # 勾选批量下发指令
            self.driver.click_element(
                'x,/html/body/div[13]/div/div/div[2]/div[3]/div[2]/div[2]/div[4]/div/form/div[5]/div[2]/label[1]/div/ins')

    # 用户详情-新增下级用户-修改用户修改权限
    def add_acc_modi_limit_modi(self):
        # 判断修改设备是否已勾选
        ele = self.driver.get_element("x,//*[@id='complex_addUser_form']/div[6]/div[2]/label/div/ins")
        status = ele.is_selected()
        if status == False:
            # 勾选修改设备
            self.driver.click_element("x,//*[@id='complex_addUser_form']/div[6]/div[2]/label/div/ins")

    # 用户详情-新增下级用户-保存
    def add_acc_info_save(self):
        self.driver.click_element("x,//*[@id='complex_addUser_form']/div[8]/div/button")
        self.driver.wait(1)

    # 用户详情-新增下级用户-保存成功操作状态
    def add_acc_info_save_status(self):
        save_status = self.driver.get_element("c,layui-layer-content").text
        return save_status

    # 用户详情-转移客户
    def click_user_trans(self):
        self.driver.click_element("x,//*[@id='searchUserEquipment']/div/div/div[2]/div[3]/div[2]/div[1]/ul/li[5]/a")
        self.driver.wait(1)

    # 用户详情-转移客户-搜索客户
    def user_trans_search(self, trans_user):
        # 搜索框输入账户/客户名称
        self.driver.operate_input_element("complexTrans_globalSearch_input_transCust1", trans_user)
        self.driver.wait(1)
        # 点击搜索
        self.driver.click_element("complexTrans_globalSearch_btn_transCust1")
        self.driver.wait()
        # 选择列表中搜索结果
        self.driver.click_element('c,autocompleter-item')
        self.driver.wait(1)

    # 用户详情-转移客户-转移
    def click_trans(self):
        self.driver.click_element("x,//*[@id='transCustom_form_transCust1']/div[2]/a")
        self.driver.wait(1)

    # 用户详情-转移客户-获取转移状态
    def get_trans_status(self):
        status = self.driver.get_element("c,layui-layer-content").text
        return status

    # 用户列表-链接点击
    def click_acc_list_link(self, link_name):
        if link_name == '控制台':
            self.driver.click_element('x,//*[@id="complex_user_tbody"]/tr[1]/td[7]/a[1]')
            self.driver.wait()
        elif link_name == '查看':
            self.driver.click_element('x,//*[@id="complex_user_tbody"]/tr[1]/td[7]/a[4]')
            self.driver.wait()

    # 用户列表-详情
    def click_acc_details(self):
        self.driver.click_element("x,//*[@id='complex_user_tbody']/tr[1]/td[7]/a[2]")
        self.driver.wait(1)

    # 用户列表-重置密码
    def click_acc_reset_pwd(self):
        self.driver.click_element("x,//*[@id='complex_user_tbody']/tr[1]/td[7]/a[3]")
        self.driver.wait(1)

    # 用户列表-详情-点击返回列表
    def return_list(self):
        self.driver.click_element("x,//*[@id='searchUserEquipment']/div/div/div[2]/div[3]/div[2]/div[1]/button")

    # 用户列表-导出
    def acc_list_export(self):
        # 将滚动条拖动到分页栏
        target = self.driver.get_element("complex_paging_device")
        self.driver.execute_script(target)  # 拖动到可见的元素去

        # 点击导出
        self.driver.click_element("x,//*[@id='searchUserEquipment']/div/div/div[2]/div[3]/div[1]/div/button")
        self.driver.wait()

    def easy_search_results(self):
        # 获取用户搜索的结果
        a = self.driver.get_element('x,//*[@id="complex_paging_user"]').get_attribute('style')
        b = self.driver.get_element('x,//*[@id="complex_user_table_nodata"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_number("x,//*[@id='complex_paging_user']", "x,//*[@id='complex_user_tbody']")
            return total
        else:
            if a == 'display: none;' and b == 'display: none;':
                return 1
            elif a == 'display: none;' and b == 'display: block;':
                return 0

    def click_search_button(self):
        # 搜索单个用户
        self.driver.click_element('x,//*[@id="complexQuery"]/div/button[1]')
        sleep(1)

    def search_only_user(self, exact_search_keyword):
        if exact_search_keyword['account'] == '':
            pass
        else:
            self.driver.operate_input_element('x,//*[@id="searchUserEquipment"]/div/div/div[2]/div[1]/div[1]/div/input',
                                              exact_search_keyword['account'])
            self.driver.click_element(
                'x,//*[@id="searchUserEquipment"]/div/div/div[2]/div[1]/div[1]/div/span/button[1]')
        sleep(4)
        if exact_search_keyword['link_name'] == "父根级用户-控制台":
            self.driver.click_element('x,//*[@id="complex_user_relation_tbody"]/tr[1]/td[7]/a[1]')
            sleep(2)

        elif exact_search_keyword['link_name'] == "父根级用户-查看":
            self.driver.click_element('x,//*[@id="complex_user_relation_tbody"]/tr[1]/td[7]/a[2]')
            sleep(2)

        elif exact_search_keyword['link_name'] == "父根级的下级用户-控制台":
            self.driver.click_element('x,//*[@id="complex_user_relation_tbody"]/tr[2]/td[7]/a[1]')
            sleep(2)

        elif exact_search_keyword['link_name'] == "父根级的下级用户-查看":
            self.driver.click_element('x,//*[@id="complex_user_relation_tbody"]/tr[2]/td[7]/a[4]')
            sleep(2)

    def click_account_search_button(self):
        self.driver.click_element('x,//*[@id="complexQuery"]/div/button[1]')
        sleep(2)

    def search_account(self, account):
        self.driver.operate_input_element('x,//*[@id="searchUserEquipment"]/div/div/div[2]/div[1]/div[1]/div/input',
                                          account)
        self.driver.click_element('x,//*[@id="searchUserEquipment"]/div/div/div[2]/div[1]/div[1]/div/span/button[1]')
        sleep(4)

    def get_first_account(self):
        return self.driver.get_text('x,//*[@id="complex_user_tbody"]/tr[1]/td[4]')
