import os
from time import sleep

from selenium.webdriver.common.keys import Keys

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage

# 设备管理页面
# author:孙燕妮
from pages.base.new_paging import NewPaging


class DevManagePages(BasePage):
    def __init__(self, driver: AutomateDriver, base_url):
        super().__init__(driver, base_url)
        self.base_page = BasePage(self.driver, self.base_url)

    # 点击进入控制台页面
    def enter_console(self):
        self.driver.click_element("index")
        self.driver.wait(3)

    # 点击进入设备管理页面
    def enter_dev_manage(self):
        self.driver.click_element('x,//*[@id="device"]/a')
        self.driver.wait(3)

    # 获取当前登录用户的库存数
    def get_login_acc_dev_stock(self):
        # 获取当前登录账户右侧的文本内容
        text = self.driver.get_element("treeDemo_1_span").text
        info = list(str(text).split(sep="("))[1]
        dev_info = str(info).split(sep="/")[0]
        dev_stock = str(dev_info).split(sep="存")[1]
        return dev_stock

    # 左侧客户列表搜索用户并选中
    def search_acc(self, acc):
        self.driver.operate_input_element("cusTreeKey", acc)
        # 搜索
        self.driver.click_element("cusTreeSearchBtn")
        self.driver.wait(1)
        # 选中唯一结果
        self.driver.click_element("c,autocompleter-item")

    # 获取当前选中账户的库存数
    def get_curr_acc_dev_stock(self):
        # 获取当前高亮客户右侧的文本内容
        text = self.driver.get_element("c,curSelectedNode").text
        info = list(str(text).split(sep="("))[1]
        dev_stock = str(info).split(sep="/")[0]
        return dev_stock

    # 获取设备列表的设备总数
    def count_curr_dev_num(self):
        a = self.driver.get_element('x,//*[@id="paging-dev"]').get_attribute("style")
        if a == 'display: none;':
            return 0
        else:
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_number("x,//*[@id='paging-dev']", "x,//*[@id='markDevTable']")
            return total
        '''
        new_paging = NewPaging(self.driver, self.base_url)
        try:
            total = new_paging.get_total_number("x,//*[@id='paging-dev']", "x,//*[@id='markDevTable']")
            return total
        except:
            return 0'''
        ''''
        # 获取结果共分几页
        total_pages_num = self.base_page.get_actual_pages_number("x,//*[@id='paging-dev']")
        # 获取最后一页有几条记录
        last_page_num = self.base_page.last_page_logs_num("x,//*[@id='markDevTable']","x,//*[@id='paging-dev']")
        # 计算当前结果共几条
        count = self.base_page.total_num(total_pages_num,last_page_num)
        return count'''

    # 点击搜索按钮
    def click_search_btn(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[5]/div/button')
        self.driver.wait(3)

    # 搜索条件-输入imei
    def input_imei(self, imei):
        self.driver.operate_input_element("searchIMEI", imei)
        self.driver.wait(1)

    # 获取唯一搜索结果的imei号
    def get_search_result_imei(self):
        imei = self.driver.get_element("x,//*[@id='deviceTableContent']/tbody/tr[1]/td[4]").text
        return imei

    # 获取搜索结果的设备名称
    def get_search_result_dev_name(self):
        dev_name = self.driver.get_element("x,//*[@id='markDevTable']/tr/td[2]").text
        return dev_name

    # 获取搜索结果的设备型号
    def get_search_result_dev_type(self):
        dev_type = self.driver.get_element("x,//*[@id='markDevTable']/tr/td[4]").text
        return dev_type

    # 搜索条件-输入设备名称
    def input_dev_name(self, dev_name):
        self.driver.operate_input_element("deviceName", dev_name)
        self.driver.wait(1)

    # 搜索条件-选择设备型号-jimitest
    def select_dev_type(self, type):
        # 点击设备型号下拉框
        self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/"
                                  "div[3]/div[1]/div/div/span[2]")
        self.driver.wait(1)
        if type == '全部型号':
            self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/"
                                      "div/div[3]/div[1]/div/div/div/ul/li[1]")
        elif type == 'ET210':
            self.driver.click_element("s,body > div.wrapper > div.main > div.container-fluid > div > "
                                      "div.customer-rightsidebar.p-15 > div > div.right-tab-con > "
                                      "div.funcbar > div > div:nth-child(3) > div.d-ib.w120.va-m > "
                                      "div > div > div > ul > li:nth-child(24)")
        elif type == 'GT710':
            self.driver.click_element("s,body > div.wrapper > div.main > div.container-fluid > div > "
                                      "div.customer-rightsidebar.p-15 > div > div.right-tab-con > "
                                      "div.funcbar > div > div:nth-child(3) > div.d-ib.w120.va-m > "
                                      "div > div > div > ul > li:nth-child(20)")
        elif type == 'ET300':
            self.driver.click_element("s,body > div.wrapper > div.main > div.container-fluid > div > "
                                      "div.customer-rightsidebar.p-15 > div > div.right-tab-con > "
                                      "div.funcbar > div > div:nth-child(3) > div.d-ib.w120.va-m > "
                                      "div > div > div > ul > li:nth-child(49)")
        elif type == 'ET200':
            self.driver.click_element(
                'x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div/div/div/ul/li[3]')

        elif type == 'JV200':
            self.driver.click_element(
                'x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div/div/div/ul/li[2]')

        elif type == 'GK308':
            self.driver.click_element(
                'x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div/div/div/ul/li[5]')

        elif type == 'ET110_jimitest':
            self.driver.click_element(
                'x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div/div/div/ul/li[27]')
        self.driver.wait(1)

    # 搜索条件-选择设备型号-web_autotest-ET210
    def choose_dev_type(self):
        self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/"
                                  "div/div/span[2]")
        self.driver.wait(1)
        self.driver.click_element(
            "s,body > div.wrapper > div.main > div.container-fluid > div > div.customer-rightsidebar.p-15 > div > div.right-tab-con > div.funcbar > div > div:nth-child(3) > div.d-ib.w120.va-m > div > div > div > ul > li:nth-child(7)")
        self.driver.wait(1)

    # 选择过期状态
    def select_expired_status(self, expired_status):
        # 点击过期状态下拉框
        self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/"
                                  "div/div[3]/div[2]/div/div/span[2]")
        self.driver.wait(1)
        if expired_status == '即将过期':
            self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/"
                                      "div/div[3]/div[2]/div/div/div/ul/li[2]")
        elif expired_status == '已过期':
            self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/"
                                      "div/div[3]/div[2]/div/div/div/ul/li[3]")
        self.driver.wait(1)

    # 选中包含下级设备
    def contain_lower_dev(self):
        selector = "x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[4]/label/div/ins"
        self.driver.click_element(selector)
        self.driver.wait(1)
        # 判断该复选框是否已选中
        text = self.driver.get_element(selector).is_selected()
        print(text)

    # 点击更多筛选条件
    def more_search_info(self):
        self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[5]/"
                                  "div/div/button")
        self.driver.wait(1)

    # 输入车牌号
    def input_vehicle_number(self, num):
        self.driver.operate_input_element("vehicleNumber", num)
        self.driver.wait(1)

    # 　输入车架号
    def input_car_frame(self, num):
        self.driver.operate_input_element("carFrame", num)
        self.driver.wait(1)

    # 输入SIM卡号
    def input_SIM(self, SIM):
        self.driver.operate_input_element("sim", SIM)
        self.driver.wait(1)

    # 选择激活状态
    def select_active_status(self, status):
        # 点击激活状态下拉框
        self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[6]/"
                                  "div[4]/div/div/span[2]")
        self.driver.wait(1)
        if status == '已激活':
            self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[6]/"
                                      "div[4]/div/div/div/ul/li[2]")
        elif status == '未激活':
            self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[6]/"
                                      "div[4]/div/div/div/ul/li[3]")
        self.driver.wait(1)

    # 选择查询时间段类型
    def select_time_type(self, type):
        # 点击时间类型下拉框
        self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[6]/div[5]/"
                                  "div[1]/div/div/span[2]")
        self.driver.wait(1)
        if type == '激活时间':
            self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[6]/"
                                      "div[5]/div[1]/div/div/div/ul/li[1]")
        elif type == '平台到期时间':
            self.driver.click_element(
                "x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[6]/div[5]/div[1]/div/div/div/ul/li[2]")
        elif type == '用户到期时间':
            self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[6]/"
                                      "div[5]/div[1]/div/div/div/ul/li[3]")
        self.driver.wait(1)

    # 输入查询开始、结束时间
    def input_search_time(self, start, end):
        # 输入开始时间
        self.driver.operate_input_element("startTime_sport", start)
        self.driver.wait(1)
        # 输入结束时间
        self.driver.operate_input_element("endTime_sport", end)
        self.driver.wait(1)

    # 选择使用范围
    def select_dev_use_range(self, dev_use_range):
        if dev_use_range == 'automobile':
            self.driver.click_element("car-ioc-automobile")
        elif dev_use_range == 'truck':
            self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[6]/"
                                      "div[5]/div[4]/ul/li[2]/i")
        elif dev_use_range == 'bus':
            self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[6]/"
                                      "div[5]/div[4]/ul/li[3]/i")
        elif dev_use_range == 'taxi':
            self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[6]/"
                                      "div[5]/div[4]/ul/li[4]/i")
        elif dev_use_range == 'mtc':
            self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[6]/"
                                      "div[5]/div[4]/ul/li[5]/i")
        elif dev_use_range == 'per':
            self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[6]/"
                                      "div[5]/div[4]/ul/li[6]/i")
        elif dev_use_range == 'cow':
            self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[6]/"
                                      "div[5]/div[4]/ul/li[7]/i")
        elif dev_use_range == 'plane':
            self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[6]/"
                                      "div[5]/div[4]/ul/li[8]/i")
        elif dev_use_range == 'other':
            self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[6]/"
                                      "div[5]/div[4]/ul/li[9]/i")
        self.driver.wait(1)

    # 单个设备操作
    # 编辑

    def dev_edit(self):
        # 点击编辑按钮
        self.driver.click_element('x,//*[@id="markDevTable"]/tr[1]/td[11]/a[1]')
        self.driver.wait()

    # 编辑基本信息
    # 基本信息-修改设备名称
    def dev_name_modify(self, dev_name):
        self.driver.operate_input_element('x,//*[@id="device_info_a"]/fieldset/div[2]/div[1]/input', dev_name)

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
            self.driver.click_element('x,//*[@id="device_info_a"]/fieldset/div[4]/div[1]/ul/li[1]')
        elif dev_use_range == '货车':
            self.driver.click_element('x,//*[@id="device_info_a"]/fieldset/div[4]/div[1]/ul/li[2]')
        elif dev_use_range == '客车':
            self.driver.click_element('x,//*[@id="device_info_a"]/fieldset/div[4]/div[1]/ul/li[3]')
        elif dev_use_range == '出租车':
            self.driver.click_element('x,//*[@id="device_info_a"]/fieldset/div[4]/div[1]/ul/li[4]')
        elif dev_use_range == '摩托车':
            self.driver.click_element('x,//*[@id="device_info_a"]/fieldset/div[4]/div[1]/ul/li[5]')
        elif dev_use_range == '人':
            self.driver.click_element('x,//*[@id="device_info_a"]/fieldset/div[4]/div[1]/ul/li[6]')
        elif dev_use_range == '牛':
            self.driver.click_element(
                "x,/html/body/div[10]/div/div/div[2]/div/form/div[1]/fieldset/div[4]/div[1]/ul/li[7]/i")
        elif dev_use_range == '无人机':
            self.driver.click_element(
                "x,/html/body/div[10]/div/div/div[2]/div/form/div[1]/fieldset/div[4]/div[1]/ul/li[8]/i")
        elif dev_use_range == '其他':
            self.driver.click_element(
                "x,/html/body/div[10]/div/div/div[2]/div/form/div[1]/fieldset/div[4]/div[1]/ul/li[9]/i")
        self.driver.wait(1)

    # 基本信息-填写设备SIM卡号
    def dev_SIM_edit(self, SIM):
        self.driver.operate_input_element('x,//*[@id="device_info_a"]/fieldset/div[2]/div[2]/input', SIM)

    # 基本信息-填写设备备注
    def dev_remark_edit(self, content):
        self.driver.operate_input_element("reMark", content)

    # 基本信息-保存
    def dev_basic_info_save(self):
        self.driver.click_element('x,//*[@id="commModal_submit_btn"]')
        self.driver.wait(1)

    # 基本信息-保存成功操作状态
    def dev_basic_info_save_status(self):
        save_status = self.driver.get_element("c,layui-layer-content").text
        return save_status

    # 编辑客户信息
    def dev_cust_info_edit(self, driver_name, phone, id_card, car_shelf_num, car_lice_num, SN, engine_num):
        # 点击客户信息
        self.driver.click_element('x,/html/body/div[1]/ul/li[2]/a')
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

    # 客户信息-安装信息
    def dev_install_info_edit(self, install_com, install_pers, install_addr, install_posi):

        # 输入安装公司
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset[2]/div[2]/div[1]/input',
                                          install_com)
        # 输入安装人员
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset[2]/div[3]/div/input',
                                          install_pers)
        # 输入安装地址
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset[2]/div[1]/div[2]/input',
                                          install_addr)
        # 输入安装位置
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset[2]/div[2]/div[2]/input',
                                          install_posi)

    # 客户信息-安装信息-选择安装时间-今天
    def select_install_time(self):
        # 点击安装时间输入框
        self.driver.click_element("installTime_compelx")
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
        self.driver.click_element('x,//*[@id="commModal_submit_btn"]')
        self.driver.wait(1)

    # 设备编辑-保存状态
    def dev_info_save_status(self):
        save_status = self.driver.get_element("c,layui-layer-content").text
        return save_status

    # 设备编辑-查看位置
    def dev_locate(self):
        self.driver.click_element('x,//*[@id="markDevTable"]/tr[1]/td[11]/a[3]')
        self.driver.wait()

    # 设备编辑-查看告警
    def dev_alarm(self):
        self.driver.click_element("x,//*[@id='markDevTable']/tr[1]/td[9]/a[3]")
        self.driver.wait()

    # 设备列表导出
    def dev_list_export(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[1]/button')
        self.driver.wait(1)

    # 单选设备复选框-下发指令
    def select_single_check_box(self):
        self.driver.click_element("x,//*[@id='markDevTable']/tr[3]/td[1]/label/div/ins")
        self.driver.wait(1)

    # 单选设备复选框-工作模式（GT710）
    def select_single_check_box_mode(self):
        self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[3]/table/tbody/"
                                  "tr[3]/td[1]/label/div/ins")
        self.driver.wait(1)

    # 全选设备复选框
    def select_all_check_box(self):
        self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[2]/"
                                  "table/thead/tr/th[1]/label/div/ins")
        self.driver.wait(1)

    # 选中发送指令
    def click_selected_send_instr(self):
        # 点击"选中发送指令"
        self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[2]/div/button[1]")
        self.driver.wait()

    # 本次查询全部发送指令
    def click_all_send_str(self):
        # 点击"本次查询全部发送指令"
        self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[2]/div/button[2]")
        self.driver.wait()

    # 选中设置工作模式
    def click_selected_set_mode(self):
        # 点击"选中设置工作模式"
        self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[2]/div/button[3]")
        self.driver.wait()

    # 本次查询全部设置工作模式
    def click_all_set_mode(self):
        # 点击"本次查询全部设置工作模式"
        self.driver.click_element("x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[2]/div/button[4]")

    # 单条设备发送指令
    def send_instr_for_single_dev(self):
        # 获取已选设备是否支持发送指令
        is_support = self.driver.get_element("x,//*[@id='check-row-tbody']/tr/td[4]/span").text
        if is_support == '否':
            # 　取消发送
            self.driver.click_element('x,//*[@id="sendCommandModal"]/div/div/div[3]/button[3]')
        elif is_support == '是':
            # 发送指令
            self.driver.click_element("toSendBatchIns")
            self.driver.wait(1)

    # 多条设备发送指令
    def send_instr_for_many_dev(self):
        # 获取当前已选中设备个数
        selected_dev = int(self.driver.get_element("check-total").text)
        is_support = []
        # 获取当前已选设备列表中设备的data属性值
        for i in range(selected_dev):
            j = i + 1
            is_support.append(self.driver.get_element("x,//*[@id='check-row-tbody']/tr[" + str(j) + "]/td[4]").text)

        if '是' in is_support:
            # 发送指令
            self.driver.click_element("toSendBatchIns")
        else:
            # 取消发送
            self.driver.click_element("x,/html/body/div[9]/div/div/div[3]/button[3]")

    # 单条设备下发工作模式
    def set_mode_for_single_dev(self):
        # 获取已选设备是否支持下发工作模式
        is_support = self.driver.get_element("x,//*[@id='checkTbody']/tr/td[4]/span").text
        if is_support == '否':
            # 　取消发送
            self.driver.click_element("x,//*[@id='sendModeCommandModel']/div/div/div[3]/button[2]")
        elif is_support == '是':
            # 发送指令
            self.driver.click_element("x,//*[@id='sendModeCommandModel']/div/div/div[3]/button[1]")
            self.driver.wait(1)

    # 多条设备下发工作模式
    def set_mode_for_many_dev(self):

        # 获取当前已选中设备个数
        selected_dev = int(self.driver.get_element("check-workMode-total").text)
        is_support = []
        # 获取当前已选设备列表中设备是否支持下发工作模式
        for i in range(selected_dev):
            j = i + 1
            is_support.append(self.driver.get_element("x,//*[@id='checkTbody']/tr[" + str(j) + "]/td[4]").text)

        if '是' in is_support:
            # 发送指令
            self.driver.click_element("x,//*[@id='sendModeCommandModel']/div/div/div[3]/button[1]")
        else:
            # 取消发送
            self.driver.click_element("x,//*[@id='sendModeCommandModel']/div/div/div[3]/button[2]")

    # 获取发送指令操作状态
    def get_send_instr_status(self):
        status = self.driver.get_element("c,layui-layer-content").text
        return status

    # 选择指令类型并填写指令内容
    def edit_instr_info(self, instr_type):
        # 点击指令类型选择框
        self.driver.click_element("x,//*[@id='type-div']/div/div/span[2]")
        self.driver.wait(1)

        if instr_type == 'SOS号码01':
            self.driver.click_element("x,//*[@id='type-div']/div/div/div/ul/li[1]")
            self.driver.wait(1)
            # 编辑号码信息
            self.driver.operate_input_element("text_0", "13889958645")
            self.driver.operate_input_element("text_1", "18256987451")
            self.driver.operate_input_element("text_2", "18898754127")

        elif instr_type == '亲情号码01':
            self.driver.click_element("x,//*[@id='type-div']/div/div/div/ul/li[2]")
            self.driver.wait(1)
            # 编辑姓名与号码
            self.driver.operate_input_element("text_0", "小明")
            self.driver.operate_input_element("text_1", "00007")
            self.driver.operate_input_element("text_2", "小红")
            self.driver.operate_input_element("text_3", "00006")
            self.driver.operate_input_element("text_4", "小青")
            self.driver.operate_input_element("text_5", "00009")

        elif instr_type == 'SOS号码02':
            self.driver.click_element("x,//*[@id='type-div']/div/div/div/ul/li[3]")
            self.driver.wait(1)
            # 编辑号码信息
            self.driver.operate_input_element("text_0", "12345")
            self.driver.operate_input_element("text_1", "989786236")
            self.driver.operate_input_element("text_2", "6737263")
            self.driver.wait(1)
            # 点击删除sos号码
            self.driver.click_element("x,//*[@id='instruction_ul']/li[2]")
            self.driver.wait(1)
            # 选择复选框
            self.driver.click_element("x,//*[@id='params-div']/div/div/label[1]/div/ins")

        elif instr_type == '亲情号码02':
            self.driver.click_element("x,//*[@id='type-div']/div/div/div/ul/li[4]")
            self.driver.wait(1)
            # 编辑号码信息
            self.driver.operate_input_element("text_0", "12345")
            self.driver.operate_input_element("text_1", "989786236")
            self.driver.operate_input_element("text_2", "6737263")
            self.driver.wait(1)
            # 点击删除sos号码
            self.driver.click_element("x,//*[@id='instruction_ul']/li[2]")
            self.driver.wait(1)
            # 选择复选框
            self.driver.click_element("x,//*[@id='params-div']/div/div/label[1]/div/ins")

        elif instr_type == '中心号码':
            self.driver.click_element("x,//*[@id='type-div']/div/div/div/ul/li[5]")
            self.driver.wait(1)
            # 编辑号码
            self.driver.operate_input_element("text_0", "999999")
            self.driver.wait(1)

        elif instr_type == '解除摘除报警':
            self.driver.click_element("x,//*[@id='type-div']/div/div/div/ul/li[20]")
            self.driver.wait(1)

        # 选择开始时间为今天
        self.driver.click_element("ins_startTime")
        self.driver.click_element("laydate_today")
        self.driver.wait(1)
        # 选择结束时间为确定
        self.driver.click_element("ins_endTime")
        self.driver.click_element("laydate_ok")
        self.driver.wait(1)

        # 选中发送指令-删除当前所选设备

    def selected_dev_del(self):
        # 点击设备删除
        self.driver.click_element("x,//*[@id='check-row-tbody']/tr/td[6]/a")
        self.driver.wait(1)

    # 关闭当前发送指令框
    def close_send_instr(self):
        self.driver.click_element("x,//*[@id='sendCommandModal']/div/div/div[1]/button")
        self.driver.wait()

    # 关闭当前设置工作模式弹框
    def close_set_mode(self):
        self.driver.click_element("x,//*[@id='sendModeCommandModel']/div/div/div[1]/button")
        self.driver.wait(1)

    # 选择工作模式-第一个
    def select_dev_mode(self):
        self.driver.click_element("x,//*[@id='workModeView']/label[1]")
        self.driver.wait()

    # 新建工作模板
    def add_mode(self, model_name, mode_type, is_cycle, cycle_time):
        self.driver.click_element("create-instructionRules")
        self.driver.wait()
        # 切入iframe
        self.driver.switch_to_iframe('x,//*[@id="customInstructionsModal"]/div/div/div[2]/iframe')
        self.driver.wait()
        # 输入模板名称
        self.driver.operate_input_element("tempName", model_name)
        # 选择工作模式
        if mode_type == '定时模式':
            # 选择上报天数
            self.driver.click_element("x,//*[@id='stageList']/div/div/div/div/div[2]/"
                                      "div[1]/div/div[1]/div/div[1]/span/div/span[2]")
            self.driver.click_element("x,//*[@id='stageList']/div/div/div/div/div[2]/"
                                      "div[1]/div/div[1]/div/div[1]/span/div/div/ul/li[1]")
            # 选择上报次数
            self.driver.click_element("x,//*[@id='stageList']/div/div/div/div/div[2]/"
                                      "div[1]/div/div[1]/div/div[2]/span/div/span[2]")
            self.driver.click_element("x,//*[@id='stageList']/div/div/div/div/div[2]/"
                                      "div[1]/div/div[1]/div/div[2]/span/div/div/ul/li[1]")
            # 选择上报时间
            self.driver.click_element("x,//*[@id='stageList']/div[1]/div/div/div/div[2]/"
                                      "div[1]/div/div[2]/div/ul/li/input")
            # 选择确认
            self.driver.click_element("x,//*[@id='timePicker']/div[2]/button[2]")

            # 选择是否限制周期
            if is_cycle == '限时周期':
                # 输入天数
                self.driver.operate_input_element("x,/html/body/div/div/div/form/div[2]/div[1]/div/div/div/div/div[2]/"
                                                  "div[1]/div/div[3]/div/input", cycle_time)
            elif is_cycle == '不限周期':
                self.driver.click_element("x,/html/body/div/div/div/form/div[2]/div[1]/div/div/div/div/div[2]/div[1]/"
                                          "div/div[3]/div/label[2]/div/ins")


        elif mode_type == '星期模式':
            self.driver.click_element("x,//*[@id='stageList']/div/div/div/div/div[1]/ul/li[2]")
            # 选择上报时间-星期一
            self.driver.click_element("x,//*[@id='stageList']/div/div/div/div/div[2]/div[2]/div/"
                                      "div[1]/div/ul/li[1]/a/label/div/input")
            # 选择上报时间
            self.driver.click_element("x,//*[@id='stageList']/div/div/div/div/div[2]/div[2]/div/div[2]/div/input")
            self.driver.click_element("x,//*[@id='timePicker']/div[2]/button[2]")
            # 选择是否持续上报
            if is_cycle == '限时周期':
                # 输入周数
                self.driver.operate_input_element("x,/html/body/div/div/div/form/div[2]/div[1]/div/div/div/div/div[2]/"
                                                  "div[2]/div/div[3]/div/input", cycle_time)
            elif is_cycle == '不限周期':
                self.driver.click_element(
                    "x,/html/body/div[1]/div/div/form/div[2]/div[1]/div/div/div/div/div[2]/div[2]/"
                    "div/div[3]/div/label[2]/div/ins")



        elif mode_type == '普通模式':
            self.driver.click_element("x,//*[@id='stageList']/div/div/div/div/div[1]/ul/li[3]")
            # 选择唤醒时间
            self.driver.click_element("x,//*[@id='stageList']/div[1]/div/div/div/div[2]/div[3]/div/div[1]/div/input")
            self.driver.click_element("x,//*[@id='timePicker']/div[2]/button[2]")
            # 选择上传间隔-12小时
            self.driver.click_element("x,//*[@id='stageList']/div/div/div/div/div[2]/div[3]/div/"
                                      "div[2]/div/div/div/span[2]")
            self.driver.wait(1)
            self.driver.click_element("x,/html/body/div/div/div/form/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/"
                                      "div[2]/div/div/div/div/ul/li[7]")
            # 选择是否循环上报
            if is_cycle == '限时周期':
                # 输入天数
                self.driver.operate_input_element("x,/html/body/div[1]/div/div/form/div[2]/div[1]/div/div/div/div/"
                                                  "div[2]/div[3]/div/div[3]/div/input", cycle_time)
            elif is_cycle == '不限周期':
                self.driver.click_element("x,/html/body/div/div/div/form/div[2]/div[1]/div/div/div/div/div[2]/div[3]/"
                                          "div/div[3]/div/label[2]/div/ins")
        # 跳出iframe
        self.driver.default_frame()

        # 保存规则
        self.driver.click_element("x,//*[@id='customInstructionsModal']/div/div/div[3]/button[1]")
        self.driver.wait()

    # 新建工作模板-添加自定义
    def add_model_add_define(self):
        self.driver.click_element("create-instructionRules")
        self.driver.wait()
        # 切入iframe
        self.driver.switch_to_iframe('x,//*[@id="customInstructionsModal"]/div/div/div[2]/iframe')
        self.driver.wait()
        # 点击添加自定义
        self.driver.click_element("x,/html/body/div/div/div/form/div[1]/div[2]/button")
        self.driver.wait(1)
        # 删除自定义
        self.driver.click_element("x,//*[@id='stageList']/div[2]/div/div/div/div[1]/a")
        self.driver.wait(1)
        # 跳出iframe
        self.driver.default_frame()
        # 取消
        self.driver.click_element("x,//*[@id='customInstructionsModal']/div/div/div[3]/button[2]")
        self.driver.wait(1)

    # 工作模式模板管理
    def mode_manage(self):
        self.driver.click_element("x,//*[@id='sendModeCommandModel']/div/div/div[2]/form/div[3]/a")
        self.driver.wait()

    # 工作模式模板管理--删除新增模板
    def del_mode(self):
        self.driver.click_element(
            "x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div[4]/table/tbody/tr[1]/td[5]/a[2]")
        self.driver.wait(1)
        # 确定
        self.driver.click_element("c,layui-layer-btn0")
        self.driver.wait()

    # 本次查询全部设置工作模式-删除已选设备
    def set_mode_dev_del(self):
        self.driver.click_element('x,//*[@id="checkTbody"]/tr[1]/td[5]/a')
        self.driver.wait(1)

    def add_data_to_search_dev(self, search_data):
        # 填写数据搜索设备
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[5]/button')
        sleep(2)
        # 设备名称
        self.driver.operate_input_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[2]/input', search_data['dev_name'])

        # 设备型号
        '''self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[3]/div/div/div/span[2]')
        sleep(2)
        if search_data['dev_type'] == 'ET200':
            self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[3]/div/div/div/div/ul/li[2]')

        elif search_data['dev_type'] == '':
            self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[3]/div/div/div/div/ul/li[1]')
        sleep(2)'''

        # 选择过期状态
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[1]/div/div/span[2]')
        sleep(2)
        if search_data['past_due'] == '':
            self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[1]/div/div/div/ul/li[1]')
        elif search_data['past_due'] == '即将过期':
            self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[1]/div/div/div/ul/li[2]')
        elif search_data['past_due'] == '已过期':
            self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[1]/div/div/div/ul/li[3]')
        sleep(2)

        # 填写车牌号
        self.driver.operate_input_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[1]/input',
                                          search_data['plate_numbers'])
        # 填写车架号
        self.driver.operate_input_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[2]/input',
                                          search_data['frame_number'])
        # 填写sim卡号
        self.driver.operate_input_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[3]/input',
                                          search_data['sim'])

        # 选择激活状态
        self.driver.click_element(
            'x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[2]/div/div/span[2]')
        sleep(2)
        if search_data['active'] == '':
            self.driver.click_element(
                'x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[2]/div/div/div/ul/li[1]')
        elif search_data['active'] == '已激活':
            self.driver.click_element(
                'x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[2]/div/div/div/ul/li[2]')
        elif search_data['active'] == '未激活':
            self.driver.click_element(
                'x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[2]/div/div/div/ul/li[3]')
        sleep(2)

        # 选择时间并填写
        self.driver.click_element(
            'x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[5]/div[1]/div/div/span[2]')
        sleep(2)
        if search_data['choose_time'] == '':
            self.driver.click_element(
                'x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[5]/div[1]/div/div/span[2]')
        elif search_data['choose_time'] == '激活时间':
            self.driver.click_element(
                'x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[5]/div[1]/div/div/div/ul/li[1]')
        elif search_data['choose_time'] == '平台到期时间':
            self.driver.click_element(
                'x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[5]/div[1]/div/div/div/ul/li[2]')
        elif search_data['choose_time'] == '用户到期时间':
            self.driver.click_element(
                'x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[5]/div[1]/div/div/div/ul/li[3]')
        sleep(2)
        self.driver.operate_input_element('x,//*[@id="startTime_input"]', search_data['begin_time'])
        self.driver.operate_input_element('x,//*[@id="endTime_input"]', search_data['end_time'])

        # 是否包含下级
        sleep(2)
        a = self.driver.get_element('x,//*[@id="lowerFlag"]/div/input').is_selected()
        if search_data['next'] == '1' and a == False:
            self.driver.click_element('x,//*[@id="lowerFlag"]/div/ins')
        if search_data['next'] == '0' and a == True:
            self.driver.click_element('x,//*[@id="lowerFlag"]/div/ins')

        # 绑定状态
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[3]/div/div/span[2]')
        sleep(2)
        if search_data['band_status'] == '':
            self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[3]/div/div/div/ul/li[1]')

        elif search_data['band_status'] == '已绑定':
            self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[3]/div/div/div/ul/li[2]')

        elif search_data['band_status'] == '未绑定':
            self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[3]/div/div/div/ul/li[3]')

        # 设备类型
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[4]/div/div/span[2]')
        sleep(2)
        if search_data['dev_mold'] == '':
            self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[4]/div/div/div/ul/li[1]')

        elif search_data['dev_mold'] == '有线':
            self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[4]/div/div/div/ul/li[2]')

        elif search_data['dev_mold'] == '电池':
            self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[4]/div/div/div/ul/li[3]')

        # 分组
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[5]/div/div/span[2]')
        sleep(2)
        if search_data['dev_group'] == '所有分组':
            self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[5]/div/div/div/ul/li[1]')

        elif search_data['dev_group'] == '默认组':
            self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[5]/div/div/div/ul/li[2]')

        self.driver.operate_input_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[4]/input',
                                          search_data['sn'])

        # 点击搜索
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[5]/div/button')
        sleep(5)

    def get_dev_number(self):
        a = self.driver.get_element('x,//*[@id="paging-dev"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            number = new_paging.get_total_numbers('x,//*[@id="paging-dev"]', 'x,//*[@id="deviceTableContent"]/tbody')
            return number

        elif a == 'display: none;':
            return 0

    def log_out(self):
        sleep(2)
        self.driver.click_element('x,//*[@id="accountCenter"]/a')
        sleep(2)
        self.driver.float_element(self.driver.get_element('x,/html/body/div[2]/header/div/div[2]/div[2]/div[2]/span/a'))
        sleep(2)
        self.driver.click_element('p,退出系统')
        self.driver.wait()
        # 定位到弹出框内容
        logout_text = self.driver.get_element("c,layui-layer-content").text
        print(logout_text)
        # 点击确定
        self.driver.click_element("c,layui-layer-btn0")
        self.driver.wait()

    def choose_dev_active_and_statr(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[5]/div/div/button')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[2]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[2]/div/div/div/ul/li[2]')

        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[5]/div/button')
        sleep(5)

        self.driver.click_element('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[1]/input')
        sleep(1)

        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[2]/div/div/button[12]')
        sleep(3)

    def click_ensure(self):
        self.driver.click_element('c,layui-layer-btn0')
        sleep(2)

    def click_edit_button(self):
        self.driver.click_element('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[13]/a[1]')
        sleep(2)

    def click_close_edit_button(self):
        self.driver.click_element('c,layui-layer-ico')
        sleep(2)

    def add_data_to_edit_dev_detila(self, data):
        self.switch_to_dev_edit_frame()

        # 填写基本信息
        # 设备名称
        self.driver.operate_input_element('x,//*[@id="device_info_a"]/fieldset/div[2]/div[1]/input', data['dev_name'])
        # sim卡号
        self.driver.operate_input_element('x,//*[@id="device_info_a"]/fieldset[2]/div[1]/div[1]/input', data['sim'])
        # 备注
        self.driver.operate_input_element('x,//*[@id="reMark"]', data['mark'])

        self.driver.click_element('x,/html/body/div[1]/ul/li[2]/a')

        # 司机名称
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset[1]/div[1]/div[1]/input', data['d_name'])
        # 电话
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset[1]/div[1]/div[2]/input', data['d_phone'])
        # 车牌号
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset[1]/div[2]/div[1]/input',
                                          data['plate_numbers'])
        # 身份证好
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset[1]/div[2]/div[2]/input', data['iccid'])
        # sn
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset[1]/div[3]/div[1]/input', data['sn'])
        # 车架号
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset[1]/div[3]/div[2]/input', data['vin'])
        # 发动机
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset[1]/div[4]/div[1]/input',
                                          data['engine_number'])

        el = self.driver.get_element('x,//*[@id="device_info_b"]/fieldset[2]/div[3]/div/input')
        self.driver.execute_script(el)

        # 安装时间
        # self.driver.operate_input_element('x,//*[@id="installTime"]', data['install_time'])
        # 安装地址
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset[2]/div[1]/div[2]/input',
                                          data['install_adress'])
        # 安装公司
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset[2]/div[2]/div[1]/input',
                                          data['install_comp'])
        # 安装人员
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset[2]/div[3]/div/input',
                                          data['install_preson'])

        self.driver.default_frame()
        self.driver.click_element('c,layui-layer-btn0')
        sleep(3)

    def get_dev_name(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[5]/div/button')
        sleep(5)
        return self.driver.get_text('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[3]')

    def click_look_place_button(self):
        self.driver.click_element('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[13]/a[3]')
        sleep(2)

    def get_dev_name_after_click_console(self):
        return self.driver.get_text(
            'x,/html/body/div[1]/div[5]/div/div[1]/div[2]/div[3]/div/div[3]/ul[1]/li/ul/li/div/div[1]/div[3]/div[1]/span[1]')

    def click_track_playback_button(self):
        self.driver.click_element('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[13]/a[4]')
        sleep(2)
        self.driver.click_element('l,轨迹回放')
        sleep(2)

    def get_imei_number(self):
        return self.driver.get_text('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[4]')

    def click_track_playback_get_text(self):
        return self.driver.get_text('x,//*[@id="mapview"]/div[1]/div[1]/div/b')

    def click_driving_recond_button(self):
        self.driver.click_element('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[13]/a[4]')
        sleep(2)
        self.driver.click_element('l,行车记录')
        sleep(2)

    def click_driving_recond_get_text(self):
        return self.driver.get_text('x,//*[@id="mapview"]/div[2]/div/div[1]/b')

    def click_street_scape_button(self):
        self.driver.click_element('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[13]/a[4]')
        sleep(2)
        self.driver.click_element('l,街景')
        sleep(2)

    def click_street_scape_get_text(self):
        return self.driver.get_text('x,//*[@id="mapview"]/div[1]/div/b')

    def choose_dev_active_and_stop(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[5]/div/div/button')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[2]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[2]/div/div/div/ul/li[2]')

        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[5]/div/button')
        sleep(5)

        self.driver.click_element('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[1]/input')
        sleep(1)

        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[2]/div/div/button[10]')
        sleep(3)

    def choose_dev_noactive_and_statr(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[5]/div/div/button')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[2]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[2]/div/div/div/ul/li[3]')

        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[5]/div/button')
        sleep(5)

        self.driver.click_element('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[1]/input')
        sleep(1)

        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[2]/div/div/button[12]')
        sleep(3)

    def choose_dev_noactive_and_stop(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[5]/div/div/button')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[2]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[2]/div/div/div/ul/li[3]')

        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[5]/div/button')
        sleep(5)

        self.driver.click_element('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[1]/input')
        sleep(1)

        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[2]/div/div/button[10]')
        sleep(3)

    def choose_dev_overtime(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[4]/div[6]/div[1]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[4]/div[6]/div[1]/div/div/div/ul/li[3]')

        self.driver.click_element('x,//*[@id="lowerFlag"]/div/ins')
        sleep(5)

        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[4]/div[6]/div[7]/button[1]')
        sleep(2)
        self.driver.click_element('x,//*[@id="markDevTable"]/tr[1]/td[12]/a[1]')
        sleep(2)

    def click_look_alarm_button(self):
        self.driver.click_element('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[13]/a[4]')
        sleep(2)
        self.driver.click_element('l,查看告警')
        sleep(2)

    def click_look_alarm_get_text(self):
        self.driver.switch_to_frame('x,//*[@id="alarmDdetailsFrame"]')
        text = self.driver.get_text('x,/html/body/div[1]/div[1]/div/b')
        self.driver.default_frame()
        return text

    def search_customer(self, param):
        self.driver.operate_input_element('x,//*[@id="deviceManage_cusTreeKey"]', param)
        self.driver.click_element('x,//*[@id="deviceManage_cusTreeSearchBtn"]')
        sleep(4)

    def get_search_customer_no_data_text(self):
        return self.driver.get_text('x,/html/body/div[2]/div[7]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/span')

    def click_batch_sale_button(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[2]/div/div/button[3]')
        sleep(2)

    def click_close_batch_sale_button(self):
        self.driver.click_element('c,layui-layer-ico')
        sleep(3)

    def get_select_account_name(self):
        return self.driver.get_text('x,//*[@id="device_sale_to"]')

    def search_customer_after_click_batch_sale_dev(self, param):
        self.driver.operate_input_element('x,//*[@id="device_sale_globalSearch_input"]', param)
        self.driver.click_element('x,//*[@id="device_sale_globalSearch_btn"]')
        sleep(4)

    def get_search_customer_no_data_text_after_batch_sale_dev(self):
        return self.driver.get_text('x,//*[@id="device_sale_id"]/div[2]/div/div/div/div/span')

    def get_select_dev_number(self):
        return len(list(self.driver.get_elements('x,//*[@id="sale_tbody_device_sale_id"]/tr')))

    def get_dev_numbers(self):
        return self.driver.get_text('x,//*[@id="sale_count_device_sale_id"]')

    def click_batch_issued_command_button(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[2]/div/div/button[7]')
        sleep(2)

    def click_close_batch_batch_issued_command_button(self):
        self.driver.click_element('c,layui-layer-ico')
        sleep(2)

    def get_dev_number_after_click_issued_command(self):
        return len(list(self.driver.get_elements('x,//*[@id="check-row-tbody"]/tr')))

    def get_count_number_after_click_issued_command(self):
        return self.driver.get_text('x,//*[@id="check-total"]')

    def get_imei_input_value(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_a"]/fieldset/div[1]/div[1]/input[2]').get_attribute(
            'disabled')
        self.driver.default_frame()
        return a

    def get_dev_type_input_value(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_a"]/fieldset/div[1]/div[2]/input[2]').get_attribute(
            'disabled')
        self.driver.default_frame()
        return a

    def get_active_time_input_value(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_a"]/fieldset/div[3]/div[2]/input').get_attribute('disabled')
        self.driver.default_frame()
        return a

    def get_expire_time_value(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_a"]/fieldset/div[4]/div[2]/input').get_attribute('disabled')
        self.driver.default_frame()
        return a

    def get_iccid_value(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_a"]/fieldset/div[5]/div[1]/input').get_attribute('disabled')
        self.driver.default_frame()
        return a

    def get_imsi_value(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_a"]/fieldset/div[5]/div[2]/input').get_attribute('disabled')
        self.driver.default_frame()
        return a

    def get_dev_name_max_len(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_a"]/fieldset/div[2]/div[1]/input').get_attribute(
            'maxlength')
        self.driver.default_frame()
        return a

    def get_dev_sim_max_len(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_a"]/fieldset[2]/div[1]/div[1]/input').get_attribute(
            'maxlength')
        self.driver.default_frame()
        return a

    def get_dev_remark_max_len(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="reMark"]').get_attribute('maxlength')
        self.driver.default_frame()
        return a

    def click_cust_info_button(self):
        self.switch_to_dev_edit_frame()
        self.driver.click_element('x,/html/body/div[1]/ul/li[2]/a')
        self.driver.default_frame()

    def get_driver_name_max_len(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_b"]/fieldset[1]/div[1]/div[1]/input').get_attribute(
            'maxlength')
        self.driver.default_frame()
        return a

    def click_driver_phone_max_len(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_b"]/fieldset[1]/div[1]/div[2]/input').get_attribute(
            'maxlength')
        self.driver.default_frame()
        return a

    def driver_vehicle_number_max_len(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_b"]/fieldset[1]/div[2]/div[1]/input').get_attribute(
            'maxlength')
        self.driver.default_frame()
        return a

    def get_driver_iccid_max_len(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_b"]/fieldset[1]/div[2]/div[2]/input').get_attribute(
            'maxlength')
        self.driver.default_frame()
        return a

    def get_driver_sn_max_len(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_b"]/fieldset[1]/div[3]/div[1]/input').get_attribute(
            'maxlength')
        self.driver.default_frame()
        return a

    def driver_car_frame_max_len(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_b"]/fieldset[1]/div[3]/div[2]/input').get_attribute(
            'maxlength')
        self.driver.default_frame()
        return a

    def get_driver_engine_number_max_len(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="engineNumber"]').get_attribute('maxlength')
        self.driver.default_frame()
        return a

    def get_dev_install_address_max_len(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_b"]/fieldset[2]/div[1]/div[2]/input').get_attribute(
            'maxlength')
        self.driver.default_frame()
        return a

    def get_dev_install_company_max_len(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_b"]/fieldset[2]/div[2]/div[1]/input').get_attribute(
            'maxlength')
        self.driver.default_frame()
        return a

    def get_dev_install_position_max_len(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_b"]/fieldset[2]/div[2]/div[2]/input').get_attribute(
            'maxlength')
        self.driver.default_frame()
        return a

    def get_dev_install_personnel_max_len(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_b"]/fieldset[2]/div[3]/div/input').get_attribute(
            'maxlength')
        self.driver.default_frame()
        return a

    def get_imei_in_list(self):
        return self.driver.get_text('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[4]')

    def get_active_time_in_list(self):
        return self.driver.get_text('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[6]')

    def get_expire_time_in_list(self):
        a = self.driver.get_text('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[8]')
        b = a.split(' ')[0]
        return b

    def switch_to_dev_edit_frame(self):
        self.driver.switch_to_frame('x,/html/body/div[36]/div[2]/iframe')

    def get_imei_in_detail(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_a"]/fieldset/div[1]/div[1]/input[2]').get_attribute('value')
        self.driver.default_frame()
        return a

    def get_active_time_in_detail(self):
        # self.driver.switch_to_frame('x,/html/body/div[28]/div[2]/iframe')
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_a"]/fieldset/div[3]/div[2]/input').get_attribute('value')
        self.driver.default_frame()
        return a

    def get_expire_time_in_detail(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_a"]/fieldset/div[4]/div[2]/input').get_attribute('value')
        self.driver.default_frame()
        return a

    def get_dev_type_in_list(self):
        return self.driver.get_text('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[5]')

    def get_dev_name_in_list(self):
        return self.driver.get_text('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[3]')

    def get_dev_sim_in_list(self):
        return self.driver.get_text('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[7]')

    def get_dev_group_in_list(self):
        return self.driver.get_text('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[11]')

    def get_dev_type_in_detail(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_a"]/fieldset/div[1]/div[2]/input[2]').get_attribute('value')
        self.driver.default_frame()
        return a

    def get_dev_name_in_detail(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_a"]/fieldset/div[2]/div[1]/input').get_attribute('value')
        self.driver.default_frame()
        return a

    def get_dev_sim_in_detail(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="device_info_a"]/fieldset[2]/div[1]/div[1]/input').get_attribute('value')
        self.driver.default_frame()
        return a

    def get_dev_group_in_detail(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_text('x,//*[@id="device_info_a"]/fieldset/div[3]/div[1]/span/div/span[2]')
        self.driver.default_frame()
        return a

    def click_sale_in_list_button(self):
        self.driver.click_element('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[13]/a[2]')
        sleep(2)

    def click_close_sale_in_list_button(self):
        self.driver.click_element('c,layui-layer-ico')
        sleep(2)

    def get_imei_in_sale(self):
        return self.driver.get_element('x,//*[@id="sale_tbody_device_sale_id"]/tr/td[1]').text

    def get_dev_type_in_sale(self):
        return self.driver.get_element('x,//*[@id="sale_tbody_device_sale_id"]/tr/td[4]').text

    def get_dev_account_name(self):
        return self.driver.get_text('x,//*[@id="sale_tbody_device_sale_id"]/tr/td[5]')

    def click_sale_button(self):
        self.driver.click_element('x,//*[@id="device_sale_id"]/div[3]/div[2]/button[3]')
        sleep(2)

    def get_fail_text(self):
        return self.driver.get_text('c,layui-layer-content')

    def click_detele_dev(self):
        self.driver.click_element('x,//*[@id="sale_tbody_device_sale_id"]/tr/td[6]/a')
        sleep(2)

    def add_dev_to_sale(self, imei):
        self.driver.click_element('x,//*[@id="sale_imei_device_sale_id"]')
        self.driver.operate_input_element('x,//*[@id="sale_imei_device_sale_id"]', imei)
        self.driver.click_element('x,//*[@id="device_sale_id"]/div[1]/div/div[1]/div/div[3]/button[1]')
        sleep(2)

    def get_imei_after_add_fail(self):
        return self.driver.get_text('x,//*[@id="device_sale_add_result_div"]/div[2]/table/tbody/tr/td[1]')

    def get_status_after_add_fail(self):
        return self.driver.get_text('x,//*[@id="device_sale_add_result_div"]/div[2]/table/tbody/tr/td[2]/span')

    def get_fail_reason(self):
        return self.driver.get_text('x,//*[@id="device_sale_add_result_div"]/div[2]/table/tbody/tr/td[3]')

    def click_close_fail(self):
        self.driver.click_element('c,layui-layer-ico')
        sleep(2)

    def click_batch_upload_pictures_button(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[2]/div/div/button[2]')
        sleep(2)

    def click_close_batch_upload_pictures_button(self):
        self.driver.click_element('c,layui-layer-ico')
        sleep(2)

    def click_cancel_batch_upload_pictures_button(self):
        self.driver.click_element('c,layui-layer-btn1')
        sleep(2)

    def click_ensure_upload(self):
        self.driver.click_element('c,layui-layer-btn0')
        sleep(2)

    def click_all_set_up_work_command(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[2]/div/div/button[9]')
        sleep(2)

    def click_close_all_set_up_work_command(self):
        self.driver.click_element('c,layui-layer-ico')
        sleep(2)

    def click_cancel_all_set_up_work_command(self):
        self.driver.click_element('c,layui-layer-btn1')
        sleep(2)

    def get_list_number(self):
        return len(list(self.driver.get_elements('x,//*[@id="checkTbody"]/tr')))

    def get_count_number(self):
        return self.driver.get_text('x,//*[@id="check-workMode-total"]')

    def delete_dev(self):
        self.driver.click_element('x,//*[@id="checkTbody"]/tr[1]/td[5]/a')
        sleep(2)

    def click_issued_command_button(self):
        self.driver.click_element('c,layui-layer-btn0')
        sleep(2)

    def click_work_command(self):
        self.driver.click_element('x,//*[@id="workModeView"]/label[1]/div/ins')
        sleep(2)

    def click_dev_in_list(self):
        self.driver.click_element('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[1]/input')
        sleep(2)

    def check_input_value(self):
        return self.driver.get_element('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[1]/input').is_selected()

    def click_select_send_command(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[2]/div/div/button[6]')
        sleep(2)

    def click_close_select_send_command(self):
        self.driver.click_element('c,layui-layer-ico')
        sleep(2)

    def click_cancel_select_send_command(self):
        self.driver.click_element('c,layui-layer-btn1')
        sleep(2)

    def get_imei_in_send_command(self):
        return self.driver.get_text('x,//*[@id="check-row-tbody"]/tr/td[1]')

    def get_dev_type_in_send_command(self):
        return self.driver.get_text('x,//*[@id="check-row-tbody"]/tr/td[2]')

    def get_dev_user_in_send_command(self):
        return self.driver.get_text('x,//*[@id="check-row-tbody"]/tr/td[3]')

    def get_dev_number_in_send_command(self):
        return len(list(self.driver.get_elements('x,//*[@id="check-row-tbody"]/tr')))

    def get_dev_count_number_in_send_command(self):
        return self.driver.get_text('x,//*[@id="check-total"]')

    def click_detele_dev_in_send_command(self):
        self.driver.click_element('x,//*[@id="check-row-tbody"]/tr/td[5]')
        sleep(2)

    def click_send_command_in_send_command(self):
        self.driver.click_element('c,layui-layer-btn0')
        sleep(2)

    def click_select_set_up_work_command(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[2]/div/div/button[8]')
        sleep(2)

    def click_close_set_up_work_command(self):
        self.driver.click_element('c,layui-layer-ico')
        sleep(2)

    def click_cancel_set_up_work_command(self):
        self.driver.click_element('c,layui-layer-btn1')
        sleep(2)

    def get_imei_in_set_up_work_command(self):
        return self.driver.get_text('x,//*[@id="checkTbody"]/tr/td[1]')

    def get_dev_number_in_work_command(self):
        return len(list(self.driver.get_elements('x,//*[@id="checkTbody"]/tr')))

    def get_dev_count_number_in_work_command(self):
        return self.driver.get_text('x,//*[@id="check-workMode-total"]')

    def get_dev_type_in_work_command(self):
        return self.driver.get_text('x,//*[@id="checkTbody"]/tr/td[2]')

    def get_dev_user_in_work_command(self):
        return self.driver.get_text('x,//*[@id="checkTbody"]/tr/td[3]')

    def get_dev_status_in_list(self):
        return self.driver.get_text('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[10]')

    def click_select_shut_down(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[2]/div/div/button[10]')
        sleep(2)

    def click_cancel(self):
        self.driver.click_element('c,layui-layer-btn1')
        sleep(2)

    def click_close(self):
        self.driver.click_element('c,layui-layer-ico')
        sleep(2)

    def click_all_shut_down(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[2]/div/div/button[11]')
        sleep(2)

    def get_all_pages(self):
        a = self.driver.get_element('x,//*[@id="paging-dev"]').get_attribute('style')
        if a == "display: block;":
            new_paging = NewPaging(self.driver, self.base_page)
            page = new_paging.get_total_page('x,//*[@id="paging-dev"]')
            return page
        else:
            return 0

    def click_per_page(self, n):
        self.driver.click_element('l,%s' % str(n))

    def get_per_number(self):
        new_paging = NewPaging(self.driver, self.base_page)
        number = new_paging.get_last_page_number('x,//*[@id="markDevTable"]')
        return number

    def get_text_dev_status(self, m):
        text = self.driver.get_text('x,//*[@id="deviceTableContent"]/tbody/tr[%s]/td[10]' % str(m))
        return text

    def click_select_starting_up(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[2]/div/div/button[12]')
        sleep(2)

    def click_all_starting_up(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[2]/div/div/button[13]')
        sleep(2)

    def search_dev(self):
        self.driver.click_element('x,//*[@id="lowerFlag"]/div/ins')
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[5]/div/button')
        sleep(5)

    def search_account(self, param):
        self.driver.operate_input_element('x,//*[@id="deviceManage_cusTreeKey"]', param)
        self.driver.click_element('x,//*[@id="deviceManage_cusTreeSearchBtn"]')
        sleep(3)
        self.driver.click_element('c,autocompleter-item')
        sleep(2)

    def search_bundle_dev(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[5]/div/div/button')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[3]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[3]/div/div/div/ul/li[2]')
        self.driver.click_element('x,//*[@id="lowerFlag"]/div/ins')

        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[5]/div/button')
        sleep(3)

    def click_unbundle_dev(self):
        self.driver.click_element('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[13]/a[4]')
        sleep(2)
        self.driver.click_element('l,解绑')
        sleep(2)

    def click_more_button(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[5]/div/div/button')
        sleep(2)

    def click_close_fails(self):
        self.driver.click_element('x,/html/body/div[31]/span[1]/a')
        sleep(2)

    def click_account_center_button(self):
        self.driver.click_element('x,//*[@id="accountCenter"]/a')
        sleep(3)

    def click_per_account_in_dev_manage_page(self, n):
        self.driver.click_element('x,//*[@id="treeDemo_deviceManage_%s_span"]' % str(n + 1))
        sleep(3)

    def get_per_user_account_in_dev_manage_page(self):
        return self.driver.get_text('x,//*[@id="userAccount"]')

    def get_account_info(self, user_account):
        connect_sql = ConnectSql()
        conncet = connect_sql.connect_tuqiang_sql()
        cursor = conncet.cursor()
        sql = "SELECT o.nickName,o.type,o.phone FROM user_info o WHERE o.account = '%s';" % user_account
        cursor.execute(sql)
        data = cursor.fetchall()
        user_info = {
            'nickname': data[0][0],
            'type': data[0][1],
            'phone': data[0][2]
        }
        cursor.close()
        conncet.close()
        return user_info

    def get_user_nickname_in_page(self):
        return self.driver.get_text('x,//*[@id="user_account"]')

    def get_user_type_in_page(self):
        return self.driver.get_text('x,//*[@id="userType"]')

    def get_user_phone_in_page(self):
        return self.driver.get_text('x,//*[@id="user_phone"]')

    def get_account_nickname_in_cust_tree(self, n):
        return self.driver.get_text('x,//*[@id="treeDemo_deviceManage_%s_span"]' % str(n + 1)).split('(')[0]

    def click_control_account_button(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[1]/div[2]/button')
        sleep(2)

    def get_edit_style_in_dev_page(self):
        return self.driver.get_element('x,//*[@id="editUserFast"]').get_attribute('style')

    def click_edit_account_button(self):
        self.driver.click_element('x,//*[@id="editUserFast"]/button')
        sleep(3)

    def get_up_user_edit_user_in_dev_page(self):
        return self.driver.get_element('x,//*[@id="topUser"]').get_attribute('value')

    def get_user_type_edit_user_in_dev_page(self):
        a = self.driver.get_element('x,//*[@id="labelSale"]/div/input').is_selected()
        b = self.driver.get_element('x,//*[@id="labelDistributor"]/div/input').is_selected()
        c = self.driver.get_element('x,//*[@id="labelUser"]/div/input').is_selected()
        if a == True:
            return '销售'
        elif b == True:
            return '代理商'
        elif c == True:
            return '用户'

    def get_user_name_edit_user_in_dev_page(self):
        return self.driver.get_element('x,//*[@id="nickName"]').get_attribute('value')

    def get_user_account_edit_in_dev_page(self):
        return self.driver.get_element('x,//*[@id="account"]').get_attribute('value')

    def get_user_phone_edit_in_dev_page(self):
        return self.driver.get_element('x,//*[@id="phone"]').get_attribute('value')

    def click_next_user_in_dev_page(self):
        self.driver.click_element('x,//*[@id="treeDemo_deviceManage_2_a"]')
        sleep(3)

    def search_account_in_edit_user(self):
        self.driver.operate_input_element('x,//*[@id="treeDemo2_cusTreeKey"]', 'account')
        self.driver.click_element('x,//*[@id="treeDemo2_cusTreeSearchBtn"]')
        sleep(3)
        self.driver.click_element('c,autocompleter-item')
        sleep(4)

    def get_user_name_after_search_in_edit_user(self):
        return self.driver.get_text('c,curSelectedNode')

    def click_user_to_search_up_user_in_edit_user(self, n):
        self.driver.click_element('x,//*[@id="treeDemo2_%s_a"]' % str(n + 3))
        sleep(3)

    def get_total_page_number_in_dev_manager(self):
        a = self.driver.get_element('x,//*[@id="paging-dev"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_page('x,//*[@id="paging-dev"]')
            return total
        else:
            return 0

    def get_up_page_state(self):
        return self.driver.get_element('x,//*[@id="paging-dev"]/ul/li[1]').get_attribute('class')

    def get_next_page_state(self):
        return self.driver.get_element('x,//*[@id="paging-dev"]/ul/li[3]').get_attribute('class')

    def get_search_no_dev_name_text(self):
        return self.driver.get_text('x,//*[@id="deviceTableContent"]/tbody/tr/td')

    def click_per_number(self):
        self.driver.click_element('c,page-select')
        sleep(2)
        self.driver.get_element('c,page-select').send_keys(Keys.DOWN + Keys.ENTER)
        sleep(2)

        self.driver.click_element('c,page-select')
        sleep(2)
        self.driver.get_element('c,page-select').send_keys(Keys.DOWN + Keys.ENTER)
        sleep(2)

        self.driver.click_element('c,page-select')
        sleep(2)
        self.driver.get_element('c,page-select').send_keys(Keys.DOWN + Keys.ENTER)
        sleep(2)

        self.driver.click_element('c,page-select')
        sleep(2)
        self.driver.get_element('c,page-select').send_keys(Keys.DOWN + Keys.ENTER)
        sleep(2)

    def get_sale_title_text_in_sale_dev(self):
        return self.driver.get_text('c,layui-layer-title')

    def add_imei_in_sale_dev_page(self, param):
        self.driver.click_element('x,//*[@id="sale_imei_device_sale_id"]')
        sleep(2)
        self.driver.operate_input_element('x,//*[@id="sale_imei_device_sale_id"]', param)
        sleep(2)
        self.driver.click_element('x,//*[@id="device_sale_id"]/div[1]/div/div[1]/div/div[3]/button[1]')
        sleep(2)

    def get_dev_in_list_number(self):
        return len(list(self.driver.get_elements('x,//*[@id="sale_tbody_device_sale_id"]/tr')))

    def add_dev_after_fail_state(self):
        return self.driver.get_text('x,//*[@id="device_sale_add_result_div"]/div[2]/table/tbody/tr/td[2]/span')

    def add_dev_after_fail_reason(self):
        return self.driver.get_text('x,//*[@id="device_sale_add_result_div"]/div[2]/table/tbody/tr[1]/td[3]')

    def click_clear_button_in_dev_sale(self):
        self.driver.click_element('x,//*[@id="device_sale_id"]/div[3]/div[1]/button')
        sleep(2)

    def choose_one_dev_to_search(self):
        self.driver.click_element('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[1]/input')
        sleep(2)

    def choose_more_dev_to_search(self):
        self.driver.click_element('x,//*[@id="deviceTableContent"]/tbody/tr[2]/td[1]/input')
        sleep(2)
        self.driver.click_element('x,//*[@id="deviceTableContent"]/tbody/tr[3]/td[1]/input')
        sleep(2)

    def get_dev_number_in_sale_dev(self):
        return self.driver.get_text('x,//*[@id="sale_count_device_sale_id"]')

    def delete_one_dev_in_dev_list(self):
        self.driver.click_element('x,//*[@id="sale_tbody_device_sale_id"]/tr[1]/td[6]/a')
        sleep(2)

    def delete_one_devs_in_dev_list(self):
        self.driver.click_element('x,//*[@id="sale_tbody_device_sale_id"]/tr[3]/td[6]/a')
        sleep(2)

    def get_first_imei_in_list(self):
        return self.driver.get_text('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[4]')

    def get_batch_sale_imei_in_sale_dev(self):
        return self.driver.get_text('x,//*[@id="sale_tbody_device_sale_id"]/tr[1]/td[1]')

    def choose_platform_soon_expire_time(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[1]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[1]/div/div/div/ul/li[2]')
        sleep(2)

    def get_platform_time_after_search(self, n):
        return self.driver.get_text('x,//*[@id="deviceTableContent"]/tbody/tr[%s]/td[8]' % str(n + 1))

    def choose_platform_expire_time(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[1]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[1]/div/div/div/ul/li[3]')
        sleep(3)

    def choose_user_soon_expire_time(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[1]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[1]/div/div/div/ul/li[4]')
        sleep(4)

    def get_user_time_after_search(self, n):
        return self.driver.get_text('x,//*[@id="deviceTableContent"]/tbody/tr[%s]/td[9]' % str(n + 1))

    def choose_user_expire_time(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[1]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[1]/div/div/div/ul/li[5]')
        sleep(5)

    def no_choose_expire_time(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[1]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[1]/div/div/div/ul/li[1]')
        sleep(1)

    def choose_active_dev(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[2]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[2]/div/div/div/ul/li[2]')
        sleep(2)

    def get_active_state_after_search(self, n):
        return self.driver.get_text('x,//*[@id="deviceTableContent"]/tbody/tr[%s]/td[6]' % str(n + 1))

    def choose_noactive_dev(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[2]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[2]/div/div/div/ul/li[3]')
        sleep(2)

    def no_choose_active_state_dev(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[2]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[2]/div/div/div/ul/li[1]')
        sleep(2)

    def choose_band_dev(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[3]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[3]/div/div/div/ul/li[2]')
        sleep(2)

    def get_band_state_after_search(self, n):
        return self.driver.get_text('x,//*[@id="deviceTableContent"]/tbody/tr[%s]/td[12]' % str(n + 1))

    def choose_no_band_dev(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[3]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[3]/div/div/div/ul/li[3]')
        sleep(2)

    def no_choose_band_state_dev(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[3]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[3]/div/div/div/ul/li[1]')
        sleep(2)

    def choose_user_group_to_search(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[5]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[5]/div/div/div/ul/li[2]')
        sleep(2)

    def get_choose_group_name(self):
        return self.driver.get_element(
            'x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[5]/div/div/span[2]').get_attribute('title')

    def get_group_name_in_list(self, n):
        return self.driver.get_text('x,//*[@id="deviceTableContent"]/tbody/tr[%s]/td[11]' % str(n + 1))

    def input_begin_time_to_serach(self, begin_time):
        self.driver.operate_input_element('x,//*[@id="startTime_input"]', begin_time)

    def get_active_time_after_search(self, n):
        return self.driver.get_text('x,//*[@id="deviceTableContent"]/tbody/tr[%s]/td[6]' % str(n + 1))

    def input_end_time_to_search(self, end_time):
        self.driver.operate_input_element('x,//*[@id="endTime_input"]', end_time)

    def choose_platform_time_to_serach(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[5]/div[1]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[5]/div[1]/div/div/div/ul/li[2]')
        sleep(2)

    def choose_user_time_to_serach(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[5]/div[1]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[5]/div[1]/div/div/div/ul/li[3]')
        sleep(2)

    def inpui_dev_vehicle_number_to_search(self, dev_vehicle_number):
        self.driver.operate_input_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[1]/input',
                                          dev_vehicle_number)

    def get_imei_after_search(self, n):
        return self.driver.get_text('x,//*[@id="deviceTableContent"]/tbody/tr[%s]/td[4]' % str(n + 1))

    def input_dev_car_frame_to_search(self, dev_car_frame):
        self.driver.operate_input_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[2]/input', dev_car_frame)

    def input_dev_sim_to_search(self, dev_sim):
        self.driver.operate_input_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[3]/input', dev_sim)

    def input_dev_sn_to_search(self, dev_sn):
        self.driver.operate_input_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[4]/input', dev_sn)

    def search_platform_expire_and_contain_next_in_dev_page(self):
        # 点击包含下级
        self.driver.click_element('x,//*[@id="lowerFlag"]/div/ins')
        # 点击更多
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[5]/div/div/button')
        sleep(2)
        # 选择平台即将过期
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[1]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[1]/div/div/div/ul/li[2]')
        sleep(2)

        # 点击搜索
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[5]/div/button')
        sleep(5)

    def get_no_data_text_after_search_in_dev_page(self):
        return self.driver.get_text('x,//*[@id="dev-noData"]/div/span')

    def get_total_number_in_issued_command_page(self):
        return self.driver.get_text('x,//*[@id="check-total"]')

    def get_total_number_list_in_issued_command_page(self):
        return len(list(self.driver.get_elements('x,//*[@id="check-row-tbody"]/tr')))

    def get_total_number_per_page_in_dev_manager(self):
        return len(list(self.driver.get_elements('x,//*[@id="markDevTable"]/tr')))

    def get_per_imei_in_dev_page(self, n):
        return self.driver.get_text('x,//*[@id="markDevTable"]/tr[%s]/td[3]' % str(n + 1))

    def get_per_imei_in_issued_command(self, m):
        return self.driver.get_text('x,//*[@id="check-row-tbody"]/tr[%s]/td[1]' % str(m + 1))

    def click_batch_issued_work_type_button(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[2]/div/div/button[9]')
        sleep(3)

    def get_total_number_in_issued_work_type_page(self):
        return self.driver.get_text('x,//*[@id="check-workMode-total"]')

    def get_total_number_list_in_issued_work_type_page(self):
        return len(list(self.driver.get_elements('x,//*[@id="checkTbody"]/tr')))

    def get_per_imei_in_issued_work_type_page(self, m):
        return self.driver.get_text('x,//*[@id="checkTbody"]/tr[%s]/td[1]' % str(m + 1))

    def click(self):
        self.driver.click_element('x,//*[@id="deviceTableHeader"]/thead/tr/th[5]')

    def click_batch_set_user_overdue_time_button(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[2]/div/div/button[4]')
        sleep(3)

    def click_close_set_user_overdue_time_button(self):
        self.driver.click_element('c,layui-layer-ico')
        sleep(2)

    def click_clance_set_user_overdue_time_button(self):
        self.driver.click_element('x,//*[@id="user_device_expires_id"]/div[2]/div[2]/button[1]')
        sleep(2)

    def get_text_after_click_set_user_overdue_time_button(self):
        return self.driver.get_text('c,layui-layer-title')

    def click_add_imei_to_set_user_overdue_time(self, param):
        self.driver.click_element('x,//*[@id="sale_imei_user_device_expires_id"]')
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="sale_imei_user_device_expires_id"]', param)
        self.driver.click_element('x,//*[@id="user_device_expires_id"]/div[1]/div/div[1]/div/div[3]/button[1]')
        sleep(2)

    def get_fail_status_after_clcik_ensure(self):
        return self.driver.get_text('x,//*[@id="device_sale_add_result_div"]/div[2]/table/tbody/tr/td[2]/span')

    def get_fail_reason_after_click_ensure(self):
        return self.driver.get_text('x,//*[@id="device_sale_add_result_div"]/div[2]/table/tbody/tr/td[3]')

    def click_close_fail_text(self):
        self.driver.click_element('x,/html/body/div[30]/span[1]/a')
        sleep(2)

    def get_dev_total_mileage_max_len(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="totalKm"]').get_attribute('maxlength')
        self.driver.default_frame()
        return a

    def input_dev_total_mileage_in_dev_detail(self, param):
        self.switch_to_dev_edit_frame()
        self.driver.operate_input_element('x,//*[@id="totalKm"]', param)
        sleep(2)
        self.driver.default_frame()

    def get_text_after_input_dev_total_mileage(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_text('x,//*[@id="device_info_b"]/fieldset[1]/div[5]/div[1]/label')
        self.driver.default_frame()
        return a

    def search_dev_in_dev_manage_page(self, param):
        self.driver.click_element('x,//*[@id="searchIMEI"]')
        sleep(2)
        self.driver.operate_input_element('x,//*[@id="searchIMEI"]', param)
        sleep(1)
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[5]/div/button')
        sleep(4)

    def click_look_dev_fence_in_dev_page(self):
        self.driver.click_element('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[13]/a[4]')
        sleep(2)
        self.driver.click_element('l,查看围栏')
        sleep(2)

    def get_in_fence_select_in_look_fence_page(self):
        a = self.driver.get_element('x,//*[@id="option0"]/td[2]/label[1]/div/input').is_selected()
        return a

    def get_out_fence_select_in_look_fence_page(self):
        a = self.driver.get_element('x,//*[@id="option0"]/td[2]/label[2]/div/input').is_selected()
        return a

    def click_in_fence_input_checkbox(self):
        self.driver.click_element('x,//*[@id="option0"]/td[2]/label[1]/div/ins')
        sleep(1)

    def click_out_fence_input_checkbox(self):
        self.driver.click_element('x,//*[@id="option0"]/td[2]/label[2]/div/ins')
        sleep(1)

    def get_text_after_click_ensure(self):
        return self.driver.get_text('c,layui-layer-content')

    def get_text_after_click_all_issued_command(self):
        return self.driver.get_text('c,layui-layer-content')

    def get_text_after_click_issued_work_template(self):
        return self.driver.get_text('c,layui-layer-content')

    def get_color_max_len(self):
        self.switch_to_dev_edit_frame()
        a = self.driver.get_element('x,//*[@id="vehicleColor"]').get_attribute('maxlength')
        self.driver.default_frame()
        return a

    def click_cancels(self):
        self.driver.click_element('c,layui-layer-btn0')
        sleep(2)
