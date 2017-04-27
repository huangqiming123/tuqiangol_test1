import os
from time import sleep

from selenium.webdriver.support.select import Select

from automate_driver.automate_driver import AutomateDriver
from pages.base.base_page import BasePage

# 客户管理页面-客户列表
# author:孙燕妮
from pages.base.new_paging import NewPaging


class CustManageCustListPage(BasePage):
    def __init__(self, driver: AutomateDriver, base_url):
        super().__init__(driver, base_url)

    # 全部客户

    # 全部客户-编辑客户名称或账号搜索框-精确查找
    def acc_exact_search(self, keyword):
        # 在搜索输入框内输入搜索关键词
        self.driver.operate_input_element("treeDemo_cusTreeKey", keyword)
        # 点击搜索按钮
        self.driver.click_element("treeDemo_cusTreeSearchBtn")
        self.driver.wait(1)
        # 选择列表中第一个搜索结果
        self.driver.click_element("c,autocompleter-item")
        self.driver.wait(1)

    # 全部客户-编辑客户名称或账号搜索框-模糊查找
    def acc_like_search(self, keyword):
        # 在搜索输入框内输入搜索关键词
        self.driver.operate_input_element("treeDemo_cusTreeKey", keyword)
        # 点击搜索按钮
        self.driver.click_element("treeDemo_cusTreeSearchBtn")
        self.driver.wait(1)
        try:
            # 通过classname获取搜索结果列表
            ele_list = self.driver.get_elements("c,autocompleter-item")
            search_result_num = len(ele_list)
            return search_result_num
        except:
            print("当前模糊查找无结果")
            return 0

    # 全部客户-获取当前选中账户的库存
    def get_curr_acc_dev_info(self):
        # 获取当前高亮客户右侧的文本内容
        text = self.driver.get_element("c,curSelectedNode").text
        info = list(str(text).split(sep="("))[1]
        dev_stock = str(info).split(sep="/")[0]
        return dev_stock

    # 全部客户-获取当前登录账户的库存
    def get_curr_login_dev_info(self):
        # 获取当前登录账户右侧的文本内容
        text = self.driver.get_element("treeDemo_1_span").text
        info = list(str(text).split(sep="("))[1]
        dev_info = str(info).split(sep="/")[0]
        dev_stock = str(dev_info).split(sep="存")[1]
        return dev_stock

    # 全部客户-获取当前登录账户的下级客户数
    def get_curr_login_lower_acc(self):
        # 获取到当前登录客户的下级客户树
        self.driver.get_element("treeDemo_1")
        # 将该客户树下ul标签内的所有li标签获取到列表中
        acc_list = list(self.driver.get_elements("x,//*[@id='treeDemo_1']" + "/ul/li"))
        print(acc_list)
        acc_list_num = len(acc_list)
        return acc_list_num

    # 全部客户-获取当前选中账户的下级客户数
    def get_curr_lower_acc(self):
        # 获取当前选中的高亮客户的id属性
        ele_id = self.driver.get_element("c,curSelectedNode").get_attribute("id")
        # 将该id按照末尾字母a来拆分
        ele_id_info = str(ele_id).split("a")[0]
        try:
            # 将拆分后得到的左半部分id信息与switch拼接得到当前选中客户的折叠/展开按钮
            switch_ele_id = ele_id_info + "switch"
            # 点击该折叠/展开按钮，使列表展开
            self.driver.click_element(switch_ele_id)
            self.driver.wait()
            # 将ele_id_info与ul拼接得到该选中客户的下级客户列表
            ul_ele_id = ele_id_info + "ul"
            # 获取其下级客户列表共有几个客户
            lower_acc_list = self.driver.get_elements("x,//*[@id='" + ul_ele_id + "']/li")
            lower_acc_num = len(lower_acc_list)
            return lower_acc_num
        except:
            print("当前选中的客户无下级客户")
            return None

    # 全部客户-点击展开当前客户树的所有下级展开/折叠按钮
    def unfold_acc_list(self):

        # 通过classname获取到当前客户树共几个1级展开/折叠按钮

        '''btn_list = list(self.driver.get_elements("c,noline_docu"))
        btn_num = len(btn_list)
        print(btn_list)
        print(btn_num)
        for i in range(btn_num - 1):
            ele_id = btn_list[i].get_attribute("id")
            self.driver.click_element(ele_id)'''

        self.driver.click_element(self.driver.get_elements("c,noline_docu")[0].get_attribute("id"))
        self.driver.wait()
        self.driver.click_element(self.driver.get_elements("c,noline_docu")[1].get_attribute("id"))
        self.driver.wait()

    # 到期客户
    # 点击进入到期客户
    def click_expired_cust(self):
        self.driver.click_element("expirationUser")
        self.driver.wait()

    # 选择到期客户左侧列表的搜索条件
    # 选择到期类型
    def select_expired_type(self, type):
        # 点击到期类型下拉框
        self.driver.click_element("x,//*[@id='overdueType']/div/span[1]/div/span[2]")
        self.driver.wait()
        if type == '用户到期':
            self.driver.click_element("x,//*[@id='overdueType']/div/span[1]/div/div/ul/li[1]")
        elif type == '平台到期':
            self.driver.click_element("x,//*[@id='overdueType']/div/span[1]/div/div/ul/li[2]")
        self.driver.wait(1)

    # 选择即将到期/已过期
    def select_expired_status(self, status):
        # 点击过期状态下拉框
        self.driver.click_element(
            "x,/html/body/div[2]/div[5]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/span[1]/div/span[2]")
        self.driver.wait()
        if status == '即将到期':
            self.driver.click_element(
                "x,/html/body/div[2]/div[5]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/span[1]/div/div/ul/li[1]")
        elif status == '已过期':
            self.driver.click_element(
                "x,/html/body/div[2]/div[5]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/span[1]/div/div/ul/li[2]")
        self.driver.wait(1)

    # 选择到期时间段
    def select_expired_time(self, time):
        # 点击时间段下拉框
        self.driver.click_element('x,//*[@id="overdueType"]/div/span[2]/div/span[2]')
        self.driver.wait()
        if time == '7天内':
            self.driver.click_element("x,//*[@id='overdueType']/div/span[2]/div/div/ul/li[1]")
        elif time == '30天内':
            self.driver.click_element("x,//*[@id='overdueType']/div/span[2]/div/div/ul/li[2]")
        elif time == '60天内':
            self.driver.click_element("x,//*[@id='overdueType']/div/span[2]/div/div/ul/li[3]")
        elif time == '7-30天内':
            self.driver.click_element("x,//*[@id='overdueType']/div/span[2]/div/div/ul/li[4]")
        elif time == '30-60天内':
            self.driver.click_element("x,//*[@id='overdueType']/div/span[2]/div/div/ul/li[5]")
        elif time == '60天以上':
            self.driver.click_element("x,//*[@id='overdueType']/div/span[2]/div/div/ul/li[6]")
        self.driver.wait(1)

    # 点击yanni/测试01账户
    def click_const_acc(self):
        self.driver.click_element("treeDemo7_2_span")
        self.driver.wait()

    # 操作右侧过期设备列表中的设备-编辑
    def expired_dev_edit(self):
        # 点击编辑按钮
        self.driver.click_element(
            "x,/html/body/div[2]/div[5]/div/div/div[2]/div/div[2]/div[2]/div[4]/table/tbody/tr/td[10]/a[1]")
        self.driver.wait()

    # 编辑基本信息
    # 基本信息-修改设备名称
    def dev_name_modify(self, dev_name):
        self.driver.operate_input_element("x,//*[@id='device_info_a']/fieldset/div[2]/div[1]/input", dev_name)

    # 基本信息-移动设备分组
    def dev_group_modify(self, dev_group):
        # 点击分组下拉框
        self.driver.click_element("x,//*[@id='device_info_a']/fieldset/div[3]/div[1]/span/div/span[2]")
        self.driver.wait(1)
        # 选择分组
        if dev_group == '默认组':
            self.driver.click_element("x,//*[@id='device_info_a']/fieldset/div[3]/div[1]/span/div/div/ul/li[1]")
        elif dev_group == 'test_01':
            self.driver.click_element("x,//*[@id='device_info_a']/fieldset/div[3]/div[1]/span/div/div/ul/li[2]")
        self.driver.wait(1)

    # 基本信息-选择设备使用范围
    def dev_use_range_choose(self, dev_use_range):
        if dev_use_range == '轿车':
            self.driver.click_element("car-ioc-automobile")
        elif dev_use_range == '货车':
            self.driver.click_element("x,//*[@id='device_info_a']/fieldset/div[4]/div[1]/ul/li[2]/i")
        elif dev_use_range == '客车':
            self.driver.click_element("x,//*[@id='device_info_a']/fieldset/div[4]/div[1]/ul/li[2]/i")
        elif dev_use_range == '出租车':
            self.driver.click_element("x,//*[@id='device_info_a']/fieldset/div[4]/div[1]/ul/li[2]/i")
        elif dev_use_range == '摩托车':
            self.driver.click_element("x,//*[@id='device_info_a']/fieldset/div[4]/div[1]/ul/li[2]/i")
        elif dev_use_range == '人':
            self.driver.click_element("x,//*[@id='device_info_a']/fieldset/div[4]/div[1]/ul/li[2]/i")
        elif dev_use_range == '牛':
            self.driver.click_element("x,//*[@id='device_info_a']/fieldset/div[4]/div[1]/ul/li[2]/i")
        elif dev_use_range == '无人机':
            self.driver.click_element("x,//*[@id='device_info_a']/fieldset/div[4]/div[1]/ul/li[2]/i")
        elif dev_use_range == '其他':
            self.driver.click_element("x,//*[@id='device_info_a']/fieldset/div[4]/div[1]/ul/li[2]/i")
        self.driver.wait(1)

    # 基本信息-填写设备SIM卡号
    def dev_SIM_edit(self, SIM):
        self.driver.operate_input_element("x,//*[@id='device_info_a']/fieldset/div[2]/div[2]/input", SIM)

    # 基本信息-填写设备备注
    def dev_remark_edit(self, content):
        self.driver.operate_input_element("reMark", content)

    # 基本信息-保存
    def dev_basic_info_save(self):
        self.driver.click_element("x,/html/body/div[12]/div/div/div[3]/button[1]")
        self.driver.wait(1)

    # 基本信息-保存成功操作状态
    def dev_basic_info_save_status(self):
        save_status = self.driver.get_element("c,layui-layer-content").text
        return save_status

    # 编辑客户信息
    def dev_cust_info_edit(self, driver_name, phone, id_card, car_shelf_num, car_lice_num, SN, engine_num):

        # 点击客户信息
        self.driver.click_element("x,//*[@id='edit_device_info_customer']/div/ul/li[2]")
        self.driver.wait(1)
        # 填写司机名称
        self.driver.operate_input_element("x,//*[@id='device_info_b']/fieldset/div[1]/div[1]/input", driver_name)
        # 填写电话
        self.driver.operate_input_element("x,//*[@id='device_info_b']/fieldset/div[2]/div[1]/input", phone)
        # 填写身份证号码
        self.driver.operate_input_element("x,//*[@id='device_info_b']/fieldset/div[3]/div[1]/input", id_card)
        # 填写车架号
        self.driver.operate_input_element("x,//*[@id='device_info_b']/fieldset/div[4]/div[1]/input", car_shelf_num)
        # 填写车牌号
        self.driver.operate_input_element("x,//*[@id='device_info_b']/fieldset/div[2]/div[2]/input", car_lice_num)
        # 填写SN
        self.driver.operate_input_element("x,//*[@id='device_info_b']/fieldset/div[3]/div[2]/input", SN)
        # 填写电动/发动机号
        self.driver.operate_input_element("engineNumber", engine_num)

    # 客户信息-编辑用户到期时间
    def choose_account_expired_date(self):
        # 确定
        self.driver.click_element("userExpiration_customer")
        self.driver.wait(1)
        self.driver.click_element("laydate_ok")
        self.driver.wait(1)

    # 客户信息-安装信息
    def dev_install_info_edit(self, install_com, install_pers, install_addr, install_posi):
        # 将滚动条滚动至保存按钮处
        save_butt_ele = self.driver.get_element("btn-submit-vehilebund")
        self.driver.execute_script(save_butt_ele)

        # 输入安装公司
        self.driver.operate_input_element("x,//*[@id='device_info_b']/fieldset/fieldset/fieldset/div[2]/div[1]/input",
                                          install_com)
        # 输入安装人员
        self.driver.operate_input_element("x,//*[@id='device_info_b']/fieldset/fieldset/fieldset/div[3]/div/input",
                                          install_pers)
        # 输入安装地址
        self.driver.operate_input_element("x,//*[@id='device_info_b']/fieldset/fieldset/fieldset/div[1]/div[2]/input",
                                          install_addr)
        # 输入安装位置
        self.driver.operate_input_element("x,//*[@id='device_info_b']/fieldset/fieldset/fieldset/div[2]/div[2]/input",
                                          install_posi)

    # 客户信息-安装信息-选择安装时间-今天
    def select_install_time(self):
        # 点击安装时间输入框
        self.driver.click_element("installTime_customer")
        self.driver.wait(1)
        # 点击确定
        self.driver.click_element("laydate_ok")
        self.driver.wait(1)

    # 客户信息-安装信息-上传安装图片
    def dev_install_pict_upload(self):

        # 点击上传图片打开上传窗口
        self.driver.click_element("fileBtn_customer")
        self.driver.wait()
        # 调用upfile.exe上传程序
        os.system("E:\\autoIt_script\\upfile.exe")
        self.driver.wait()

    # 客户信息-安装信息-获取已上传的图片元素
    def get_install_pict_ele(self):
        # 将滚动条滚动至保存按钮处
        save_butt_ele = self.driver.get_element("btn-submit-vehilebund")
        self.driver.execute_script(save_butt_ele)
        self.driver.get_element("c,p-pic")
        self.driver.wait(1)

    # 设备编辑-保存
    def dev_info_save(self):
        self.driver.click_element("x,/html/body/div[12]/div/div/div[3]/button[1]")
        self.driver.wait(1)

    # 设备编辑-保存状态
    def dev_info_save_status(self):
        save_status = self.driver.get_element("c,layui-layer-content").text
        return save_status

    # 操作右侧过期设备列表中的设备-销售
    def expired_dev_sale(self):
        # 点击销售按钮
        self.driver.click_element("x,//*[@id='markExpirationDevTable']/tr/td[10]/a[2]")
        self.driver.wait(5)

    # 获取当前已选设备个数
    def get_curr_selected_dev_num(self):
        num = self.driver.get_element("sale_count_batchSaleid").text
        return num

    # 右侧搜索框搜索销售用户并选中
    def select_sale_acc(self, user_name):
        self.driver.operate_input_element("batchSaleid_globalSearch_input", user_name)
        # 点击搜索按钮
        self.driver.click_element("batchSaleid_globalSearch_btn")
        self.driver.wait()
        # 选中搜索结果
        self.driver.click_element('c,autocompleter-item')

    # 选择用户到期时间
    def choose_acc_expired_time(self, account_expired_time):
        self.driver.click_element("x,//*[@id='complex_user_sale_batchSaleid']/div[3]/div[1]/span/div/span[2]")
        self.driver.wait(1)
        if account_expired_time == '一个月':
            self.driver.click_element("x,//*[@id='complex_user_sale_batchSaleid']/div[3]/div[1]/span/div/div/ul/li[2]")
        elif account_expired_time == '两个月':
            self.driver.click_element("x,//*[@id='complex_user_sale_batchSaleid']/div[3]/div[1]/span/div/div/ul/li[3]")
        elif account_expired_time == '三个月':
            self.driver.click_element("x,//*[@id='complex_user_sale_batchSaleid']/div[3]/div[1]/span/div/div/ul/li[4]")
        elif account_expired_time == '半年':
            self.driver.click_element("x,//*[@id='complex_user_sale_batchSaleid']/div[3]/div[1]/span/div/div/ul/li[5]")
        elif account_expired_time == '一年':
            self.driver.click_element("x,//*[@id='complex_user_sale_batchSaleid']/div[3]/div[1]/span/div/div/ul/li[6]")
        elif account_expired_time == '不限制':
            self.driver.click_element("x,//*[@id='complex_user_sale_batchSaleid']/div[3]/div[1]/span/div/div/ul/li[7]")

    # 销售-销售按钮
    def sale_button(self):
        self.driver.click_element("x,//*[@id='complex_user_sale_batchSaleid']/div[3]/div[2]/button[3]")

    # 获取销售成功操作状态弹框的文本内容
    def get_sale_status(self):
        sale_status_text = self.driver.get_element("c,layui-layer-content").text
        return sale_status_text

    # 销售-销售按钮
    def dis_sale_button(self):
        self.driver.click_element("x,//*[@id='complex_user_sale_batchSaleid']/div[3]/div[2]/button[1]")
        self.driver.wait(1)

    # 操作右侧过期设备列表中的设备-查看位置
    def expired_dev_site(self):
        # 点击查看位置
        self.driver.click_element("x,//*[@id='markExpirationDevTable']/tr/td[10]/a[3]")
        self.driver.wait()

    # 操作右侧过期设备列表中的设备-更多
    def expired_dev_more(self, more_info):

        if more_info == '二维码':
            # 点击更多
            self.driver.click_element(
                'x,/html/body/div[2]/div[5]/div/div/div[2]/div/div[2]/div[2]/div[4]/table/tbody/tr/td[10]/a[4]')
            self.driver.wait()
            self.driver.click_element("x,/html/body/div[31]/ul/li[5]/a")
            self.driver.wait(1)
            # 关闭二维码弹框
            self.driver.click_element("c,layui-layer-close2")
            self.driver.wait(1)
        elif more_info == '查看围栏':
            # 点击更多
            self.driver.click_element(
                "x,/html/body/div[2]/div[5]/div/div/div[2]/div/div[2]/div[2]/div[4]/table/tbody/tr/td[10]/a[4]")
            self.driver.wait()
            self.driver.click_element("x,/html/body/div[31]/ul/li[6]/a")
            self.driver.wait(1)
            # 关闭围栏弹框
            self.driver.click_element("x,//*[@id='show-fence-table']/div/div/div[1]/button")
            self.driver.wait(1)
        elif more_info == '查看告警':
            # 点击更多
            self.driver.click_element(
                "x,/html/body/div[2]/div[5]/div/div/div[2]/div/div[2]/div[2]/div[4]/table/tbody/tr/td[10]/a[4]")
            self.driver.wait()
            self.driver.click_element("x,/html/body/div[31]/ul/li[7]/a")
            self.driver.wait()

    # 过期设备列表-批量延长用户到期时间
    def extend_acc_expired_time(self):
        # 全选设备
        self.driver.click_element("x,//*[@id='expiraTableHeader']/thead/tr/th[1]/span/div/ins")
        self.driver.wait(1)
        # 点击批量延长用户到期
        self.driver.click_element("ProlongUserExpiration")
        self.driver.wait()

    # 批量延长用户到期-选择用户到期时间
    def extend_acc_expired_time_select(self, extendedTime):
        self.driver.click_element("x,//*[@id='expiration_modal_mark']/div/div[2]/div/div[2]/span/div/span[2]")
        self.driver.wait(1)
        if extendedTime == '一个月':
            self.driver.click_element("x,//*[@id='expiration_modal_mark']/div/div[2]/div/div[2]/span/div/div/ul/li[2]")
        elif extendedTime == '两个月':
            self.driver.click_element("x,//*[@id='expiration_modal_mark']/div/div[2]/div/div[2]/span/div/div/ul/li[3]")
        elif extendedTime == '三个月':
            self.driver.click_element("x,//*[@id='expiration_modal_mark']/div/div[2]/div/div[2]/span/div/div/ul/li[4]")
        elif extendedTime == '半年':
            self.driver.click_element("x,//*[@id='expiration_modal_mark']/div/div[2]/div/div[2]/span/div/div/ul/li[5]")
        elif extendedTime == '一年':
            self.driver.click_element("x,//*[@id='expiration_modal_mark']/div/div[2]/div/div[2]/span/div/div/ul/li[6]")

    # 批量延长用户到期-保存
    def save_extend_time(self):
        self.driver.click_element("x,//*[@id='expiration_modal_mark']/div/div[3]/button[1]")
        self.driver.wait(1)

    # 批量延长用户到期-保存状态
    def extend_time_save_status(self):
        save_status = self.driver.get_element("c,layui-layer-content")
        return save_status

    # 批量延长用户到期-取消
    def dis_save_extend_time(self):
        self.driver.click_element("x,//*[@id='expiration_modal_mark']/div/div[3]/button[2]")
        self.driver.wait(1)

    # 过期设备列表-导出
    def export_expired_dev(self):
        # 全选设备
        self.driver.click_element("x,//*[@id='expiraTableHeader']/thead/tr/th[1]/span/div/ins")
        self.driver.wait(1)
        # 点击导出
        self.driver.click_element("x,//*[@id='expireDev']/div[2]/div/button")
        self.driver.wait()

    def get_account_stock_number(self):
        # 获取当前用户库存的数量
        text = self.driver.get_text('x,//*[@id="treeDemo_1_span"]')
        number = text.split('/')[0].split('存')[1]
        return number

    def get_account_total_number(self):
        text = self.driver.get_text('x,//*[@id="treeDemo_1_span"]')
        number = text.split(')')[0].split('数')[1]
        return number

    def get_cus_page_current_account(self):
        text = self.driver.get_text('x,//*[@id="userAccount"]')
        return text

    def usr_info_type(self):
        text = self.driver.get_text('x,//*[@id="userType"]')
        return text

    def get_cus_page_account_phone(self):
        text = self.driver.get_text('x,//*[@id="user_phone"]')
        return text

    def get_cus_page_account_name(self):
        text = self.driver.get_text('x,//*[@id="user_account"]')
        return text

    def get_cus_page_overview_stock_number(self):
        text = self.driver.get_text('x,//*[@id="stock"]')
        return text

    def get_cus_page_overview_total_number(self):
        text = self.driver.get_text('x,//*[@id="receiving"]')
        return text

    def get_equipment_number(self):
        # 获取设备列表中的总数
        a = self.driver.get_element('x,//*[@id="paging-dev"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            number = new_paging.get_total_number('x,//*[@id="paging-dev"]', 'x,//*[@id="markDevTable"]')
            return number
        elif a == 'display: none;':
            return 0

    def add_data_to_search_dev(self, search_data):
        # 搜索设备
        self.driver.operate_input_element('x,//*[@id="treeDemo_cusTreeKey"]', search_data['account'])
        self.driver.click_element('x,//*[@id="treeDemo_cusTreeSearchBtn"]')
        sleep(2)
        self.driver.click_element('c,autocompleter-item')
        sleep(3)

        # 选择组别
        a = self.driver.get_element('x,//*[@id="markGroup"]').get_attribute('style')
        if a == 'display: inline-block;':
            self.driver.click_element('x,//*[@id="markGroup"]/div/span[2]')
            sleep(1)
            if search_data['group'] == '':
                self.driver.click_element('x,//*[@id="markGroup"]/div/div/ul/li[1]')

            elif search_data['group'] == '默认组':
                self.driver.click_element('x,//*[@id="markGroup"]/div/div/ul/li[2]')
            sleep(3)
        # 激活状态
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div[1]/div[2]/div[3]/span[2]/div[1]/span[2]')
        sleep(1)
        if search_data['active'] == '':
            self.driver.click_element(
                'x,//*[@id="allDev"]/div[2]/div[1]/div[1]/div[2]/div[3]/span[2]/div[1]/div/ul/li[1]')

        elif search_data['active'] == '已激活':
            self.driver.click_element(
                'x,//*[@id="allDev"]/div[2]/div[1]/div[1]/div[2]/div[3]/span[2]/div[1]/div/ul/li[2]')

        elif search_data['active'] == '未激活':
            self.driver.click_element(
                'x,//*[@id="allDev"]/div[2]/div[1]/div[1]/div[2]/div[3]/span[2]/div[1]/div/ul/li[3]')
        sleep(3)

        # 绑定状态
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div[1]/div[2]/div[3]/span[2]/div[2]/span[2]')
        sleep(1)
        if search_data['bound'] == '':
            self.driver.click_element(
                'x,//*[@id="allDev"]/div[2]/div[1]/div[1]/div[2]/div[3]/span[2]/div[2]/div/ul/li[1]')

        elif search_data['bound'] == '已绑定':
            self.driver.click_element(
                'x,//*[@id="allDev"]/div[2]/div[1]/div[1]/div[2]/div[3]/span[2]/div[2]/div/ul/li[2]')

        elif search_data['bound'] == '未绑定':
            self.driver.click_element(
                'x,//*[@id="allDev"]/div[2]/div[1]/div[1]/div[2]/div[3]/span[2]/div[2]/div/ul/li[3]')
        sleep(3)

        # sim或者imei
        if search_data['sim_or_imei'] == 'sim':
            self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div[1]/div[2]/div[2]/label[2]/div/ins')

        elif search_data['sim_or_imei'] == 'imei':
            self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div[1]/div[2]/div[2]/label[1]/div/ins')
        sleep(3)

        self.driver.operate_input_element('x,//*[@id="searchSnImeiVal"]', search_data['info'])
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div[1]/div[2]/div[1]/div/span/button')
        sleep(5)

    def click_sale_button(self):
        self.driver.click_element('x,//*[@id="complex_user_sale_batchSaleid"]/div[3]/div[2]/button[3]')
        sleep(2)


