import os
from time import sleep

from selenium.webdriver.common.keys import Keys

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage

# 全局搜索-设备搜索功能的元素及操作
# author:孙燕妮
from pages.base.new_paging import NewPaging


class GlobalDevSearchPage(BasePage):
    def __init__(self, driver: AutomateDriver, base_url):
        super().__init__(driver, base_url)
        self.base_page = BasePage(self.driver, self.base_url)

    # 全局搜索栏-设备搜索按钮
    def click_easy_search(self):
        self.driver.click_element('x,//*[@id="globalSearch"]/a')
        self.driver.wait(1)

    # 全局搜索栏-设备搜索
    def device_easy_search(self, search_keyword):
        # self.swith_to_search_frame()

        # 在设备名称/imei输入框内输入搜索关键词信息
        self.driver.operate_input_element('x,/html/body/div[1]/div[1]/div[1]/div/input', search_keyword)
        # 点击搜索设备按钮
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/div/button')
        sleep(5)
        # self.driver.default_frame()

    # 设备搜索对话框-设备搜索按钮
    def click_dev_dial_search(self):
        self.driver.click_element("x,//*[@id='searchUserEquipment']/div/div/div[2]/div[1]/div[1]/div/span/button[1]")
        self.driver.wait(5)

    # 设备搜索对话框-设备搜索
    def dev_dial_search(self, search_keyword):
        # 在设备名称/imei/司机/车牌输入框内输入搜索关键词信息
        self.driver.operate_input_element("x,//*[@id='searchUserEquipment']/div/div/div[2]/div[1]/div[1]/div/input",
                                          search_keyword)
        # 点击搜索按钮
        self.driver.click_element("x,//*[@id='searchUserEquipment']/div/div/div[2]/div[1]/div[1]/div/span/button[1]")
        self.driver.wait(15)

    # 设备搜索对话框-关闭
    def close_dev_search(self):
        self.driver.click_element("x,//*[@id='searchUserEquipment']/div/div/div[1]/button")
        self.driver.wait(1)

    # 设备搜索-获取搜索结果共多少条
    def easy_search_result(self):
        # 当搜索结果只有一条时，必可获取到用户关系--一级用户--查看
        # self.swith_to_search_frame()
        a = self.driver.get_element('x,//*[@id="complex_paging_device"]').get_attribute('style')
        b = self.driver.get_element('x,//*[@id="complex_device_table_nodata"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_number('x,//*[@id="complex_paging_device"]',
                                                'x,//*[@id="complex_device_tbody"]')
            # self.driver.default_frame()
            return total
        else:
            if a == 'display: none;' and b == 'display: none;':
                # self.driver.default_frame()
                return 1
            elif a == 'display: none;' and b == 'display: block;':
                # self.driver.default_frame()
                return 0

    # 设备详情-用户关系操作
    def click_user_relation_link(self, link_name):
        if link_name == '轨迹回放':
            self.driver.click_element("l,轨迹回放")
            self.driver.wait()
        elif link_name == '实时跟踪':
            self.driver.click_element("l,实时跟踪")
            self.driver.wait()
        elif link_name == '查看告警':
            self.driver.click_element("l,查看告警")
            self.driver.wait()
        elif link_name == '查看位置':
            self.driver.click_element("l,查看位置")
            self.driver.wait()
        elif link_name == '控制台1':
            self.driver.click_element('x,//*[@id="complex_device_user_realtion_tbody"]/tr[1]/td[7]/a[1]')
            sleep(2)
        elif link_name == '查看1':
            self.driver.click_element('x,//*[@id="complex_device_user_realtion_tbody"]/tr[1]/td[7]/a[2]')
            sleep(2)
        elif link_name == '控制台2':
            self.driver.click_element('x,//*[@id="complex_device_user_realtion_tbody"]/tr[2]/td[7]/a[1]')
            sleep(2)
        elif link_name == "查看2":
            self.driver.click_element('x,//*[@id="complex_device_user_realtion_tbody"]/tr[2]/td[7]/a[4]')
            sleep(2)
        '''
        elif link_name == '父根级用户-控制台':
            # 设备详情-用户关系-父用户操作-父根级用户-“控制台”
            self.driver.click_element(
                "x,/html/body/div[13]/div/div/div[2]/div[4]/div[2]/div[2]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[7]/a[1]")
            self.driver.wait()
        elif link_name == '父根级用户-查看':
            # 设备详情-用户关系-父用户操作-父根级用户-“控制台”
            self.driver.click_element(
                "x,/html/body/div[13]/div/div/div[2]/div[4]/div[2]/div[2]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[7]/a[2]")
            self.driver.wait()
        elif link_name == '父根级的下级用户-控制台':
            # 设备详情-用户关系-父用户操作-父根级用户-“控制台”
            self.driver.click_element(
                "x,/html/body/div[13]/div/div/div[2]/div[4]/div[2]/div[2]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[7]/a[1]")
            self.driver.wait()
        elif link_name == '父根级的下级用户-查看':
            # 设备详情-用户关系-父根级的下级用户-“查看”
            self.driver.click_element(
                "x,/html/body/div[13]/div/div/div[2]/div[4]/div[2]/div[2]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[7]/a[4]")
            self.driver.wait()
        elif link_name == '当前设备用户-控制台':
            # 设备详情-用户关系-当前设备用户-“控制台”
            self.driver.click_element(
                "x,/html/body/div[13]/div/div/div[2]/div[4]/div[2]/div[2]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[7]/a[1]")
            self.driver.wait()
        elif link_name == '当前设备用户-查看':
            # 设备详情-用户关系-当前设备用户-“查看”
            self.driver.click_element(
                "x,/html/body/div[13]/div/div/div[2]/div[4]/div[2]/div[2]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[7]/a[4]")
            self.driver.wait()'''

    # 设备详情-用户关系-当前设备用户-“重置密码”
    def curr_dev_reset_passwd(self):
        self.driver.click_element('x,//*[@id="complex_device_user_realtion_tbody"]/tr[2]/td[7]/a[3]')
        self.driver.wait()

    # 设备详情-用户关系-当前设备用户-“重置密码”弹框文本内容
    def reset_passwd_content(self):
        reset_passwd_content = self.driver.get_element("c,layui-layer-content").text
        return reset_passwd_content

    # 设备详情-用户关系-当前设备用户-“重置密码”-确定
    def reset_passwd_ensure(self):
        self.driver.click_element("c,layui-layer-btn0")
        self.driver.wait(1)

    # 设备详情-用户关系-当前设备用户-“重置密码”-确定-操作状态
    def get_reset_status(self):
        reset_status = self.driver.get_element("c,layui-layer-content").text
        return reset_status

    # 设备详情-用户关系-当前设备用户-“重置密码”-取消
    def reset_passwd_dismiss(self):
        self.driver.click_element("c,layui-layer-btn1")
        self.driver.wait()

    # 设备详情-设备信息-基本信息编辑
    def click_dev_info(self):
        self.driver.click_element("x,//*[@id='searchUserEquipment']/div/div/div[2]/div[4]/div[2]/div[1]/ul/li[2]/a")
        self.driver.wait(1)

    # 设备详情-设备信息-基本信息-修改设备名称
    def dev_name_modify(self, dev_name):
        self.driver.operate_input_element('x,//*[@id="device_info_a"]/fieldset/div[2]/div[1]/input', dev_name)

    # 设备详情-设备信息-基本信息-移动设备分组
    def dev_group_modify(self, dev_group):
        # 点击分组下拉框
        self.driver.click_element('x,//*[@id="device_info_a"]/fieldset/div[3]/div[1]/span/div/span[2]')
        self.driver.wait(1)
        # 选择分组
        if dev_group == '默认组':
            self.driver.click_element("x,//*[@id='device_info_a']/fieldset/div[3]/div[1]/span/div/div/ul/li[1]")
        elif dev_group == 'test_01':
            self.driver.click_element("x,//*[@id='device_info_a']/fieldset/div[3]/div[1]/span/div/div/ul/li[2]")
        self.driver.wait(1)

    # 设备详情-设备信息-基本信息-选择设备使用范围
    def dev_use_range_choose(self, dev_use_range):
        if dev_use_range == '轿车':
            self.driver.click_element('x,//*[@id="car-ioc-automobile"]')
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
            self.driver.click_element('x,//*[@id="device_info_a"]/fieldset/div[4]/div[1]/ul/li[7]')
        elif dev_use_range == '无人机':
            self.driver.click_element('x,//*[@id="device_info_a"]/fieldset/div[4]/div[1]/ul/li[8]')
        elif dev_use_range == '其他':
            self.driver.click_element('x,//*[@id="device_info_a"]/fieldset/div[4]/div[1]/ul/li[9]')
        self.driver.wait(1)

    # 设备详情-设备信息-基本信息-填写设备SIM卡号
    def dev_SIM_edit(self, SIM):
        self.driver.operate_input_element('x,//*[@id="device_info_a"]/fieldset/div[2]/div[2]/input', SIM)

    # 设备详情-设备信息-基本信息-填写设备备注
    def dev_remark_edit(self, content):
        self.driver.operate_input_element("reMark", content)

    # 设备详情-设备信息-基本信息-保存
    def dev_basic_info_save(self):
        self.driver.click_element('x,//*[@id="device_info_form"]/div[3]/div/button')
        self.driver.wait(1)

    # 设备详情-设备信息-基本信息-保存成功操作状态
    def dev_basic_info_save_status(self):
        save_status = self.driver.get_element("c,layui-layer-content").text
        return save_status

    # 设备详情-设备信息-客户信息
    def dev_cust_info_edit(self, driver_name, phone, id_card, car_shelf_num, car_lice_num, SN, engine_num):

        # 点击客户信息
        self.driver.click_element('x,/html/body/div[1]/ul/li[2]/a')
        self.driver.wait(1)
        # 填写司机名称
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset/div[1]/div[1]/input', driver_name)
        # 填写电话
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset/div[1]/div[2]/input', phone)
        # 填写身份证号码
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset/div[2]/div[2]/input', id_card)
        # 填写车架号
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset/div[3]/div[2]/input', car_shelf_num)
        # 填写车牌号
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset/div[2]/div[1]/input', car_lice_num)
        # 填写SN
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset/div[3]/div[1]/input', SN)
        # 填写电动/发动机号
        self.driver.operate_input_element('x,//*[@id="engineNumber"]', engine_num)

    # 设备详情-设备信息-客户信息-选择用户到期时间
    def choose_account_expired_time(self, account_expired_time):
        self.driver.click_element("x,/html/body/div[13]/div/div/div[2]/div[4]/div[2]/div[2]/div[2]/div/form/"
                                  "div[2]/fieldset/div[1]/div[2]/span/div/span[2]")
        self.driver.wait(1)
        if account_expired_time == '一个月':
            self.driver.click_element("x,/html/body/div[13]/div/div/div[2]/div[4]/div[2]/div[2]/div[2]/div/form/"
                                      "div[2]/fieldset/div[1]/div[2]/span/div/div/ul/li[2]")
        elif account_expired_time == '两个月':
            self.driver.click_element("x,/html/body/div[13]/div/div/div[2]/div[4]/div[2]/div[2]/div[2]/div/form/"
                                      "div[2]/fieldset/div[1]/div[2]/span/div/div/ul/li[3]")
        elif account_expired_time == '三个月':
            self.driver.click_element("x,/html/body/div[13]/div/div/div[2]/div[4]/div[2]/div[2]/div[2]/div/form/"
                                      "div[2]/fieldset/div[1]/div[2]/span/div/div/ul/li[4]")
        elif account_expired_time == '半年':
            self.driver.click_element("x,/html/body/div[13]/div/div/div[2]/div[4]/div[2]/div[2]/div[2]/div/form/"
                                      "div[2]/fieldset/div[1]/div[2]/span/div/div/ul/li[5]")
        elif account_expired_time == '一年':
            self.driver.click_element("x,/html/body/div[13]/div/div/div[2]/div[4]/div[2]/div[2]/div[2]/div/form/"
                                      "div[2]/fieldset/div[1]/div[2]/span/div/div/ul/li[6]")
        elif account_expired_time == '不限制':
            self.driver.click_element("x,/html/body/div[13]/div/div/div[2]/div[4]/div[2]/div[2]/div[2]/div/form/"
                                      "div[2]/fieldset/div[1]/div[2]/span/div/div/ul/li[7]")

    # 设备详情-设备信息-安装信息
    def dev_install_info_edit(self, install_com, install_pers, install_addr, install_posi):
        # 将滚动条滚动至保存按钮处
        save_butt_ele = self.driver.get_element(
            'x,//*[@id="device_info_form"]/div[3]/div/button')
        self.driver.execute_script(save_butt_ele)

        # 输入安装公司
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset/fieldset/fieldset/div[2]/div[1]/input',
                                          install_com)
        # 输入安装人员
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset/fieldset/fieldset/div[3]/div/input',
                                          install_pers)
        # 输入安装地址
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset/fieldset/fieldset/div[1]/div[2]/input',
                                          install_addr)
        # 输入安装位置
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset/fieldset/fieldset/div[2]/div[2]/input',
                                          install_posi)

    # 设备详情-设备信息-选择安装时间-今天
    def select_install_time(self):
        # 点击安装时间输入框
        self.driver.operate_input_element('x,//*[@id="installTime"]', '2017-04-05 02:52')

    # 设备详情-设备信息-安装信息-上传安装图片
    def dev_install_pict_upload(self):

        # 点击上传图片打开上传窗口
        self.driver.click_element("fileBtn_compelx")
        self.driver.wait()
        # 调用upfile.exe上传程序
        os.system("E:\\autoIt_script\\upfile.exe")
        self.driver.wait()

    # 设备详情-设备信息-安装信息-获取已上传的图片元素
    def get_install_pict_ele(self):
        # 将滚动条滚动至保存按钮处
        save_butt_ele = self.driver.get_element(
            "x,/html/body/div[13]/div/div/div[2]/div[4]/div[2]/div[2]/div[2]/div/form/div[3]/div/button")
        self.driver.execute_script(save_butt_ele)
        self.driver.get_element("c,p-pic")
        self.driver.wait(1)

    # 设备详情-设备信息-保存
    def dev_info_save(self):
        self.driver.click_element('x,//*[@id="device_info_form"]/div[3]/div/button')
        self.driver.wait(1)

    # 设备详情-设备信息-保存状态
    def dev_info_save_status(self):
        save_status = self.driver.get_element("c,layui-layer-content").text
        return save_status

    # 设备详情-设备转移
    def click_dev_trans(self):
        self.driver.click_element("x,//*[@id='searchUserEquipment']/div/div/div[2]/div[4]/div[2]/div[1]/ul/li[3]/a")
        self.driver.wait(1)

    # 设备详情-设备转移-删除默认已选设备
    def del_curr_dev(self):
        self.driver.click_element("x,//*[@id='sale_tbody_complexAllot']/tr/td[4]/a")
        self.driver.wait(1)

    # 设备详情-设备转移-重置
    def reset_dev_trans(self):
        self.driver.click_element("x,//*[@id='complex_user_sale_complexAllot']/div[3]/div[1]/button")
        self.driver.wait(1)

    # 设备详情-设备转移-获取当前已选中的设备个数
    def dev_sele_num(self):
        num = self.driver.get_element("sale_count_complexAllot").text
        return num

    # 设备详情-设备转移-输入设备imei
    def dev_imei_input(self, imei):
        self.driver.operate_input_element("sale_imei_complexAllot", imei)

    # 设备详情-设备转移-添加
    def dev_add(self):
        self.driver.click_element("x,//*[@id='complex_user_sale_complexAllot']/div[1]/div/div[1]/div/div[3]/button[1]")
        self.driver.wait(1)

    # 设备详情-设备转移-取消添加
    def dev_add_dismiss(self):
        self.driver.click_element("x,//*[@id='complex_user_sale_complexAllot']/div[1]/div/div[1]/div/div[3]/button[2]")
        self.driver.wait(1)

    # 设备详情-设备转移-查找转移客户
    def dev_trans_cust(self, user_name):
        self.driver.operate_input_element("complexAllot_globalSearch_input", user_name)
        # 点击搜索按钮
        self.driver.click_element("complexAllot_globalSearch_btn")
        self.driver.wait(1)
        # 选中搜索结果
        self.driver.click_element("c,autocompleter-item")

    # 设备详情-设备转移-点击转移
    def click_trans_btn(self):
        self.driver.click_element("x,//*[@id='complex_user_sale_complexAllot']/div[3]/div[2]/button[3]")
        self.driver.wait(1)

    # 设备详情-设备转移-获取转移状态
    def get_dev_trans_status(self):
        status = self.driver.get_element("c,layui-layer-content").text
        return status

    # 设备详情-设备转移-取消转移
    def click_dis_trans_btn(self):
        self.driver.click_element("x,//*[@id='complex_user_sale_complexAllot']/div[3]/div[2]/button[1]")

    # 设备详情-设备指令
    def click_dev_instr(self):
        self.driver.click_element("x,//*[@id='searchUserEquipment']/div/div/div[2]/div[4]/div[2]/div[1]/ul/li[4]/a")
        self.driver.wait(1)

    # 设备详情-设备指令-未激活设备
    def get_no_act_dev_hint(self):
        hint = self.driver.get_element("c,layui-layer-content").text
        return hint

    # 设备详情-设备指令-选择指令类型，编辑
    def dev_instr_type_edit(self, instr_type):
        # 点击指令类型选择框
        self.driver.click_element("x,//*[@id='type-div']/div/div/span[2]")
        self.driver.wait(1)

        if instr_type == "SOS号码":
            self.driver.click_element("x,//*[@id='type-div']/div/div/div/ul/li[1]")
            self.driver.wait(1)
            # 输入号码
            self.driver.operate_input_element('text_0', '1234567898')
            self.driver.operate_input_element("text_1", "123457888")
            self.driver.operate_input_element("text_2", "24456768787")
            # 点击删除sos号码
            # self.driver.click_element("x,//*[@id='instruction_ul']/li[2]")
            self.driver.wait(1)
            # 选择复选框
            # self.driver.click_element("x,//*[@id='params-div']/div/div/label[1]/div/ins")


        elif instr_type == "中心号码":
            self.driver.click_element("x,//*[@id='type-div']/div/div/div/ul/li[2]")
            self.driver.wait(1)
            # 输入中心号码
            self.driver.operate_input_element("text_0", "09911111")
            # 点击删除中心号码
            self.driver.click_element("x,//*[@id='instruction_ul']/li[2]")


        elif instr_type == "震动报警":
            self.driver.click_element("x,//*[@id='type-div']/div/div/div/ul/li[3]")
            self.driver.wait(1)
            # 选择上报方式-平台
            self.driver.click_element("x,//*[@id='params-div']/div/div[1]/div/div/span[2]")
            self.driver.wait(1)
            self.driver.click_element("x,//*[@id='params-div']/div/div[1]/div/div/div/ul/li[1]")


        elif instr_type == "位移报警":
            self.driver.click_element("x,//*[@id='type-div']/div/div/div/ul/li[4]")
            self.driver.wait(1)
            # 输入信息
            self.driver.operate_input_element("text_0", "200")
            # 点击关闭位移
            self.driver.click_element("x,//*[@id='instruction_ul']/li[2]")


        elif instr_type == "断电报警":
            self.driver.click_element("x,//*[@id='type-div']/div/div/div/ul/li[5]")
            self.driver.wait(1)
            # 选择上报方式-平台
            self.driver.click_element("x,//*[@id='params-div']/div/div[1]/div/div/span[2]")
            self.driver.wait(1)
            self.driver.click_element("x,//*[@id='params-div']/div/div[1]/div/div/div/ul/li[1]")


        elif instr_type == "低电报警":
            self.driver.click_element("x,//*[@id='type-div']/div/div/div/ul/li[6]")
            self.driver.wait(1)
            # 选择上报方式-平台
            self.driver.click_element("x,//*[@id='params-div']/div/div[1]/div/div/span[2]")
            self.driver.wait(1)
            self.driver.click_element("x,//*[@id='params-div']/div/div[1]/div/div/div/ul/li[1]")


        elif instr_type == "震动灵敏度":
            # 将滚动条拖动到"自定义"
            target = self.driver.get_element("x,//*[@id='type-div']/div/div/div/ul/li[11]")
            self.driver.execute_script(target)  # 拖动到可见的元素去

            self.driver.click_element("x,//*[@id='type-div']/div/div/div/ul/li[7]")
            self.driver.wait(1)
            # 选择灵敏度-等级一
            self.driver.click_element("x,//*[@id='params-div']/div/div[1]/div/div/span[2]")
            self.driver.wait(1)
            self.driver.click_element("x,//*[@id='params-div']/div/div[1]/div/div/div/ul/li[1]")

        elif instr_type == "设防/撤防":
            # 将滚动条拖动到"自定义"
            target = self.driver.get_element("x,//*[@id='type-div']/div/div/div/ul/li[11]")
            self.driver.execute_script(target)  # 拖动到可见的元素去

            self.driver.click_element("x,//*[@id='type-div']/div/div/div/ul/li[8]")
            self.driver.wait(1)

        elif instr_type == "设防模式":
            # 将滚动条拖动到"自定义"
            target = self.driver.get_element("x,//*[@id='type-div']/div/div/div/ul/li[11]")
            self.driver.execute_script(target)  # 拖动到可见的元素去

            self.driver.click_element("x,//*[@id='type-div']/div/div/div/ul/li[9]")
            self.driver.wait(1)
            # 选择自动
            self.driver.click_element("x,/html/body/div[13]/div/div/div[2]/div[4]/div[2]/div[2]/div[4]/div/"
                                      "form/div[2]/div[2]/div/div[2]/div/div[3]/div[1]/div/div/label[2]/div/ins")

        elif instr_type == "远程控制":
            # 将滚动条拖动到"自定义"
            target = self.driver.get_element("x,//*[@id='type-div']/div/div/div/ul/li[11]")
            self.driver.execute_script(target)  # 拖动到可见的元素去

            self.driver.click_element("x,//*[@id='type-div']/div/div/div/ul/li[10]")
            self.driver.wait(1)
            # 点击恢复油电
            self.driver.click_element("x,/html/body/div[13]/div/div/div[2]/div[4]/div[2]/div[2]/div[4]/div/form/"
                                      "div[2]/div[2]/div/div[2]/div/div[2]/div/ul/li[2]")


        elif instr_type == "自定义":
            # 将滚动条拖动到"自定义"
            target = self.driver.get_element("x,//*[@id='type-div']/div/div/div/ul/li[11]")
            self.driver.execute_script(target)  # 拖动到可见的元素去

            self.driver.click_element("x,//*[@id='type-div']/div/div/div/ul/li[11]")
            self.driver.wait(1)
            # 输入自定义指令
            self.driver.operate_input_element("text_0", "sos#")

    # 设备详情-设备指令-发送指令
    def dev_instr_send(self):
        self.driver.click_element("instruction-send-btn")
        self.driver.wait(1)

    # 设备列表-链接点击
    def click_dev_list_link(self, link_name):
        if link_name == '轨迹回放':
            self.driver.click_element('x,//*[@id="complex_device_tbody"]/tr[1]/td[8]/a[2]')
            self.driver.wait()
        elif link_name == '实时跟踪':
            self.driver.click_element('x,//*[@id="complex_device_tbody"]/tr[1]/td[8]/a[3]')
            self.driver.wait()
        elif link_name == '查看告警':
            self.driver.click_element('x,//*[@id="complex_device_tbody"]/tr[1]/td[8]/a[4]')
            self.driver.wait()

    # 设备列表-详情
    def click_dev_details(self):
        self.driver.click_element('x,//*[@id="complex_device_tbody"]/tr[1]/td[8]/a[1]')
        self.driver.wait(1)

    # 设备列表-详情-点击返回列表
    def return_list(self):
        self.driver.click_element("x,//*[@id='searchUserEquipment']/div/div/div[2]/div[4]/div[2]/div[1]/button")

    # 设备列表-导出
    def dev_list_export(self):
        # 将滚动条拖动到分页栏
        target = self.driver.get_element("complex_paging_device")
        self.driver.execute_script(target)  # 拖动到可见的元素去

        # 点击分页
        self.driver.click_element("x,//*[@id='searchUserEquipment']/div/div/div[2]/div[4]/div[1]/div/div/button")
        self.driver.wait()

    def select_account_search(self):
        # 选择用户搜索
        self.driver.click_element(
            'x,//*[@id="searchUserEquipment"]/div/div/div[2]/div[1]/div[1]/div/div/div/div/span[2]')
        sleep(1)
        self.driver.click_element(
            'x,//*[@id="searchUserEquipment"]/div/div/div[2]/div[1]/div[1]/div/div/div/div/div/ul/li[1]')
        sleep(1)

    def account_easy_search(self, search_data):
        # 填写用户搜索的条件，进行搜索
        # self.swith_to_search_frame()
        self.driver.operate_input_element('x,/html/body/div[1]/div[1]/div[1]/div/input', search_data['account_info'])
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/button[1]')
        sleep(5)
        # self.driver.default_frame()

    def get_account_before_reset_password(self):
        # 获取重置密码的用户名
        return self.driver.get_text('x,//*[@id="complex_device_user_realtion_tbody"]/tr[2]/td[4]')

    def click_equipment_button(self):
        self.driver.click_element('x,//*[@id="complexQuery"]/div/div/button')

    def add_data_to_search_complex(self, search_data):
        # 增加数据去搜索高级
        # self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        # 点击选择用户
        self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[2]/div/div[1]/span/button')
        sleep(1)
        # 输入客户名称/账号
        self.driver.operate_input_element('x,//*[@id="complex_globalSearch_input"]', search_data['account'])
        sleep(2)
        self.driver.click_element('x,//*[@id="complex_globalSearch_btn"]')
        sleep(3)
        # 点击搜索结果
        self.driver.click_element('c,autocompleter-item')
        sleep(2)

        # 选择基本信息
        self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[3]/div/div/span[2]')
        sleep(1)
        if search_data['base_info'] == 'imei':
            self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[3]/div/div/div/ul/li[1]')
            sleep(1)
            self.driver.operate_input_element('x,//*[@id="complex_advanced_search_form"]/div[3]/input',
                                              search_data['info'])

        elif search_data['base_info'] == '车牌号':
            self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[3]/div/div/div/ul/li[2]')
            sleep(1)
            self.driver.operate_input_element('x,//*[@id="complex_advanced_search_form"]/div[3]/input',
                                              search_data['info'])

        elif search_data['base_info'] == '设备类型':
            self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[3]/div/div/div/ul/li[3]')
            sleep(1)
            self.driver.click_element('x,//*[@id="mcType_dev"]/div/span[2]')
            sleep(1)
            if search_data['info'] == 'ET100':
                self.driver.click_element('x,//*[@id="mcType_dev"]/div/div/ul/li[7]')

        elif search_data['base_info'] == 'SN':
            self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[3]/div/div/div/ul/li[4]')
            sleep(1)
            self.driver.operate_input_element('x,//*[@id="complex_advanced_search_form"]/div[3]/input',
                                              search_data['info'])

        elif search_data['base_info'] == '车架号':
            self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[3]/div/div/div/ul/li[5]')
            sleep(1)
            self.driver.operate_input_element('x,//*[@id="complex_advanced_search_form"]/div[3]/input',
                                              search_data['info'])

        elif search_data['base_info'] == '设备SIM卡号':
            self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[3]/div/div/div/ul/li[6]')
            sleep(1)
            self.driver.operate_input_element('x,//*[@id="complex_advanced_search_form"]/div[3]/input',
                                              search_data['info'])

        elif search_data['base_info'] == '设备名称':
            self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[3]/div/div/div/ul/li[7]')
            sleep(1)
            self.driver.operate_input_element('x,//*[@id="complex_advanced_search_form"]/div[3]/input',
                                              search_data['info'])

        elif search_data['base_info'] == '':
            self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[3]/div/div/span[2]')

        # 选择日期类型
        sleep(3)
        self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[4]/div/div/span[2]')
        sleep(1)
        if search_data['date_type'] == '':
            self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[4]/div/div/span[2]')

        elif search_data['date_type'] == '激活时间':
            self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[4]/div/div/div/ul/li[1]')

        elif search_data['date_type'] == '平台到期时间':
            self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[4]/div/div/div/ul/li[2]')

        # 填写日期
        begin_time = search_data['date'].split('/')[0]
        end_time = search_data['date'].split('/')[1]

        if search_data['is_date'] == '':
            # 不选择时间段
            self.driver.operate_input_element('x,//*[@id="advancedSearchSelectStartTime"]', begin_time)

        elif search_data['is_date'] == '1':
            # 选择时间段
            self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[4]/label[2]/div/ins')
            sleep(2)
            self.driver.operate_input_element('x,//*[@id="advancedSearchSelectStartTime"]', begin_time)
            sleep(2)
            self.driver.operate_input_element('x,//*[@id="advancedSearchSelectEndTime"]', end_time)

        # 选择欠费
        if search_data['arrearage'] == '1':
            self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[5]/label[2]/div/ins')

        # 选择未激活
        if search_data['no_active'] == '1':
            self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[5]/label[3]/div/ins')

        # 点击搜索
        self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[6]/button[1]')
        sleep(10)
        self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[6]/button[2]')

        # self.driver.default_frame()

    def device_easy_searchs(self, param):
        self.driver.operate_input_element('x,//*[@id="searchUserEquipment"]/div/div/div[2]/div[1]/div[1]/div/input',
                                          param)
        self.driver.click_element('x,//*[@id="searchUserEquipment"]/div/div/div[2]/div[1]/div[1]/div/span/button[1]')
        sleep(4)

    def close_search(self):
        self.driver.click_element('c,layui-layer-ico')

    def swith_to_search_frame(self):
        self.driver.switch_to_frame('x,/html/body/div[16]/div[2]/iframe')

    def click_dev_search(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/div/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/div/div/div/div/ul/li[3]')
        sleep(5)
        self.driver.default_frame()

    def click_dev_searchs(self):
        self.swith_to_search_frame()
        # self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/div/div/div/span[2]')
        # sleep(2)
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/div/button')
        sleep(5)
        self.driver.default_frame()

    def click_account_search(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/button[1]')
        sleep(2)
        # self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/div/div/div/div/ul/li[3]')
        # sleep(5)
        self.driver.default_frame()

    def click_app_accounts_search(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/div/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/div/div/div/div/ul/li[1]')
        sleep(5)
        self.driver.default_frame()

    def click_senior_search_button(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/div/div/button')
        sleep(2)
        self.driver.default_frame()

    def click_app_account_search(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/button[2]')
        sleep(2)
        self.driver.default_frame()

    def app_account_easy_search(self, search_data):
        # self.swith_to_search_frame()
        self.driver.operate_input_element('x,/html/body/div[1]/div[1]/div[1]/div/input', search_data['account_info'])
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/button[2]')
        sleep(5)
        # self.driver.default_frame()

    def get_dev_search_marked_words(self):
        # self.swith_to_search_frame()
        text = self.driver.get_element('x,/html/body/div[1]/div[1]/div[1]/div/input').get_attribute('placeholder')
        # self.driver.default_frame()
        return text

    def select_search_user(self):
        # self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/div/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/div/div/div/div/ul/li[3]')
        sleep(2)
        # self.driver.default_frame()

    def select_search_app_user(self):
        # self.swith_to_search_frame()
        # self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/div/div/div/span[2]')
        # sleep(2)
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/button[2]')
        sleep(2)
        # self.driver.default_frame()

    def click_search_button(self):
        # self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/span/span/button')
        sleep(5)
        # self.driver.default_frame()

    def click_console_button(self):
        # self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_mobileUser_tbody"]/tr[1]/td[7]/a[1]')
        sleep(3)
        # self.driver.default_frame()

    def click_detail_in_app_user_search(self):
        # self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[4]/div/div[1]/table/tbody/tr[1]/td[7]/a[2]')
        sleep(3)
        # self.driver.default_frame()

    def get_app_user_name_in_app_search(self):
        # self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_mobileUser_tbody"]/tr[1]/td[2]')
        # self.driver.default_frame()
        return text

    def get_app_user_type_in_app_search(self):
        # self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_mobileUser_tbody"]/tr[1]/td[3]/div')
        # self.driver.default_frame()
        return text

    def get_app_user_account_in_app_search(self):
        # self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_mobileUser_tbody"]/tr[1]/td[4]')
        # self.driver.default_frame()
        return text

    def get_app_user_phone_in_app_search(self):
        # self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_mobileUser_tbody"]/tr[1]/td[5]')
        # self.driver.default_frame()
        return text

    def get_app_user_dev_number_in_app_search(self):
        # self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_mobileUser_tbody"]/tr[1]/td[6]')
        # self.driver.default_frame()
        return text

    def get_app_name_in_detail(self):
        # self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_mobileUser_detail_tbody"]/tr/td[2]')
        # self.driver.default_frame()
        return text

    def get_app_type_in_detail(self):
        # self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_mobileUser_detail_tbody"]/tr/td[3]/div')
        # self.driver.default_frame()
        return text

    def get_app_account_in_detail(self):
        # self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_mobileUser_detail_tbody"]/tr/td[4]')
        # self.driver.default_frame()
        return text

    def get_app_phone_in_detail(self):
        # self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_mobileUser_detail_tbody"]/tr/td[5]')
        # self.driver.default_frame()
        return text

    def get_app_dev_number_in_detail(self):
        # self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_mobileUser_detail_tbody"]/tr/td[6]')
        # self.driver.default_frame()
        return text

    def get_app_dev_number_in_detail_by_list(self):
        # self.swith_to_search_frame()
        t = self.driver.get_element('x,//*[@id="complex_mobileDevice_table_nodata"]').get_attribute('style')
        if t == 'display: block;':
            # self.driver.default_frame()
            return 0
        else:
            n = NewPaging(self.driver, self.base_url).get_last_page_number(
                'x,//*[@id="complex_mobileUser_device_tbody"]')
            # self.driver.default_frame()
            return n

    def click_reset_password_button(self):
        # self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_mobileUser_tbody"]/tr[1]/td[7]/a[3]')
        sleep(2)
        # self.driver.default_frame()

    def close_button(self):
        # self.swith_to_search_frame()
        self.driver.click_element('c,layui-layer-ico')
        sleep(2)
        # self.driver.default_frame()

    def cancel_button(self):
        # self.swith_to_search_frame()
        self.driver.click_element('c,layui-layer-btn1')
        sleep(2)
        # self.driver.default_frame()

    def ensure_button(self):
        # self.swith_to_search_frame()
        self.driver.click_element('c,layui-layer-btn0')
        sleep(2)
        # self.driver.default_frame()

    def get_text_after_succeed(self):
        # self.swith_to_search_frame()
        text = self.driver.get_text('c,layui-layer-content')
        # self.driver.default_frame()
        return text

    def return_app_user_list(self):
        # self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[4]/div/div[2]/div[1]/button')
        sleep(5)
        # self.driver.default_frame()

    def click_console_button_in_app_detail(self):
        # self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_mobileUser_detail_tbody"]/tr/td[7]/a[1]')
        sleep(2)
        # self.driver.default_frame()

    def click_reset_password_button_in_app_detail(self):
        # self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_mobileUser_detail_tbody"]/tr/td[7]/a[3]')
        sleep(2)
        # self.driver.default_frame()

    def get_dev_name_in_app_detail(self):
        # self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_mobileUser_device_tbody"]/tr[1]/td[2]/span')
        # self.driver.default_frame()
        return text

    def get_dev_imei_in_app_detail(self):
        # self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_mobileUser_device_tbody"]/tr[1]/td[3]')
        # self.driver.default_frame()
        return text

    def get_dev_type_in_app_detail(self):
        # self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_mobileUser_device_tbody"]/tr[1]/td[4]')
        # self.driver.default_frame()
        return text

    def get_dev_active_time_in_app_detail(self):
        # self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_mobileUser_device_tbody"]/tr[1]/td[5]')
        # self.driver.default_frame()
        return text

    def get_dev_expire_time_in_app_detail(self):
        # self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_mobileUser_device_tbody"]/tr[1]/td[6]')
        # self.driver.default_frame()
        return text

    def get_dev_bound_user_in_app_detail(self):
        # self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_mobileUser_device_tbody"]/tr/td[8]')
        # self.driver.default_frame()
        return text

    def click_dev_operation_detail_in_app_detail(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_mobileUser_device_tbody"]/tr/td[10]/a[1]')
        sleep(2)
        self.driver.default_frame()

    def get_dev_name_in_dev_detail(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_device_detail_tbody"]/tr/td[2]/span')
        self.driver.default_frame()
        return text

    def get_dev_imei_in_dev_detail(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_device_detail_tbody"]/tr/td[3]')
        self.driver.default_frame()
        return text

    def get_dev_type_in_dev_detail(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_device_detail_tbody"]/tr/td[4]')
        self.driver.default_frame()
        return text

    def get_dev_active_time_in_dev_detail(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_device_detail_tbody"]/tr/td[5]')
        self.driver.default_frame()
        return text

    def get_dev_expire_time_in_dev_detail(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_device_detail_tbody"]/tr/td[6]')
        self.driver.default_frame()
        return text

    def get_dev_bound_user_in_dev_detail(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_device_detail_tbody"]/tr/td[8]')
        self.driver.default_frame()
        return text

    def click_track_replay_button_in_app_detail(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_mobileUser_device_tbody"]/tr[1]/td[10]/a[2]')
        sleep(2)
        self.driver.default_frame()

    def get_imei_in_replay(self):
        text = self.driver.get_text('x,//*[@id="driverName"]/span')
        imei = text.split('：')[1].split(')')[0]
        return imei

    def get_dev_name_in_replay(self):
        text = self.driver.get_text('x,//*[@id="driverName"]')
        dev_name = text.split('  ')[0]
        return dev_name

    def return_app_user_detail_list(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[3]/div[2]/div[1]/button')
        sleep(4)
        self.driver.default_frame()

    def click_track_preset_button_in_app_detail(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_mobileUser_device_tbody"]/tr[1]/td[10]/a[3]')
        sleep(2)
        self.driver.default_frame()

    def get_imei_in_track_preset(self):
        text = self.driver.get_text('x,//*[@id="imeiHead"]')
        return text

    def get_dev_name_in_track_preset(self):
        text = self.driver.get_text('x,//*[@id="driverName"]')
        return text

    def click_alarm_detail_button_in_app_detail(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_mobileUser_device_tbody"]/tr[1]/td[10]/a[4]')
        sleep(2)
        self.driver.default_frame()

    def get_text_after_click_alarm_detail(self):
        self.driver.switch_to_frame('x,//*[@id="alarmDdetailsFrame"]')
        text = self.driver.get_text('x,/html/body/div[1]/div[1]/div/b')
        self.driver.default_frame()
        return text

    def get_user_name_in_user_search(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_user_tbody"]/tr[1]/td[2]')
        self.driver.default_frame()
        return text

    def get_user_type_in_user_search(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_user_tbody"]/tr[1]/td[3]/div')
        self.driver.default_frame()
        return text

    def get_user_account_in_user_search(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_user_tbody"]/tr[1]/td[4]')
        self.driver.default_frame()
        return text

    def get_user_dev_number_in_user_search(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_user_tbody"]/tr[1]/td[6]')
        self.driver.default_frame()
        return text

    def click_console_button_in_user_search(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_user_tbody"]/tr[1]/td[7]/a[1]')
        sleep(2)
        self.driver.default_frame()

    def click_detail_in_user_search(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_user_tbody"]/tr[1]/td[7]/a[2]')
        sleep(2)
        self.driver.default_frame()

    def click_return_search_list(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[2]/div[2]/div[1]/button')
        sleep(2)
        self.driver.default_frame()

    def click_look_button_in_user_search(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_user_tbody"]/tr[1]/td[7]/a[4]')
        sleep(2)
        self.driver.default_frame()

    def get_dev_numebr_in_dev_manage(self):
        a = self.driver.get_element('x,//*[@id="paging-dev"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_numbers('x,//*[@id="paging-dev"]', 'x,//*[@id="deviceTableContent"]/tbody')
            return total
        else:
            return 0

    def click_reset_password_button_in_user_search(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_user_tbody"]/tr[1]/td[7]/a[3]')
        sleep(2)
        self.driver.default_frame()

    def click_search_buttons(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/span/div/button[1]')
        sleep(3)
        self.driver.default_frame()

    def click_user_info_in_user_detail(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[2]/div[2]/div[1]/ul/li[2]/a')
        sleep(3)
        self.driver.default_frame()

    def get_user_name_in_detail(self):
        self.swith_to_search_frame()
        text = self.driver.get_element(
            'x,//*[@id="complex_userInfo_Form_complexUpdate"]/div[3]/div/input').get_attribute('value')
        self.driver.default_frame()
        return text

    def get_user_type_in_detail(self):
        self.swith_to_search_frame()
        a = self.driver.get_element(
            'x,//*[@id="complex_userInfo_Form_complexUpdate"]/div[2]/div/div/label[1]/div/input').is_selected()
        b = self.driver.get_element(
            'x,//*[@id="complex_userInfo_Form_complexUpdate"]/div[2]/div/div/label[2]/div/input').is_selected()
        c = self.driver.get_element(
            'x,//*[@id="complex_userInfo_Form_complexUpdate"]/div[2]/div/div/label[3]/div/input').is_selected()
        if a == True:
            self.driver.default_frame()
            return ' 销售'
        elif b == True:
            self.driver.default_frame()
            return ' 代理商'
        elif c == True:
            self.driver.default_frame()
            return ' 用户'

    def get_user_account_in_detail(self):
        self.swith_to_search_frame()
        text = self.driver.get_element(
            'x,//*[@id="complex_userInfo_Form_complexUpdate"]/div[4]/div/input').get_attribute('value')
        self.driver.default_frame()
        return text

    def get_user_account_input_value_in_detail(self):
        self.swith_to_search_frame()
        text = self.driver.get_element(
            'x,//*[@id="complex_userInfo_Form_complexUpdate"]/div[4]/div/input').get_attribute('readonly')
        self.driver.default_frame()
        return text

    def get_up_user_name_in_detail(self):
        self.swith_to_search_frame()
        text = self.driver.get_element('x,//*[@id="editorSelectRole"]/div/input').get_attribute('value')
        self.driver.default_frame()
        return text

    def get_up_user_input_value_in_detail(self):
        self.swith_to_search_frame()
        text = self.driver.get_element('x,//*[@id="editorSelectRole"]/div/input').get_attribute('readonly')
        self.driver.default_frame()
        return text

    def search_user_in_user_info(self, search_data):
        self.swith_to_search_frame()
        self.driver.operate_input_element('x,//*[@id="complexUpdate_globalSearch_input"]', search_data)
        self.driver.click_element('x,//*[@id="complexUpdate_globalSearch_btn"]')
        sleep(4)
        text = self.driver.get_text('x,//*[@id="editorTreeRoleBox"]/div/div/div/span')
        self.driver.default_frame()
        return text

    def get_up_user_name_in_details(self):
        text = self.driver.get_element('x,//*[@id="editorSelectRole"]/div/input').get_attribute('value')
        return text

    def click_sale_dev_in_user_info(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[2]/div[2]/div[1]/ul/li[3]/a')
        sleep(2)
        self.driver.default_frame()

    def get_sale_user_name(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="sale_to_complexSale"]')
        self.driver.default_frame()
        return text

    def click_add_user_in_user_info(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[2]/div[2]/div[1]/ul/li[4]/a')
        sleep(2)
        self.driver.default_frame()

    def get_up_user_in_add_user(self):
        self.swith_to_search_frame()
        text = self.driver.get_element('x,//*[@id="complex_addUser_form"]/div[1]/div[1]/input').get_attribute('value')
        self.driver.default_frame()
        return text

    def check_add_user_account_input_in_user_info(self, param):
        self.swith_to_search_frame()
        self.driver.operate_input_element('x,//*[@id="complex_addUser_form"]/div[3]/div[1]/input', param)
        self.driver.default_frame()

    def get_text_account_input_expertion(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_addUser_form"]/div[3]/div[1]/label')
        self.driver.default_frame()
        return text

    def click_save_add_user(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_addUser_form"]/div[8]/div/button')
        sleep(2)
        self.driver.default_frame()

    def get_user_account_input_max_len(self):
        self.swith_to_search_frame()
        text = self.driver.get_element('x,//*[@id="complex_addUser_form"]/div[3]/div[1]/input').get_attribute(
            'maxlength')
        self.driver.default_frame()
        return text

    def check_add_user_name_input_in_user_info(self, param):
        self.swith_to_search_frame()
        self.driver.operate_input_element('x,//*[@id="complex_addUser_form"]/div[4]/div[1]/input', param)
        self.driver.default_frame()

    def get_text_name_input_expertion(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_addUser_form"]/div[4]/div[1]/label')
        self.driver.default_frame()
        return text

    def click_add_user_password_first_input_in_user_info(self, param):
        self.swith_to_search_frame()
        self.driver.operate_input_element('x,//*[@id="password"]', param)
        self.driver.default_frame()

    def click_add_user_password_second_input_in_user_info(self, param):
        self.swith_to_search_frame()
        self.driver.operate_input_element('x,//*[@id="markPswAgain_complex_addUser_form"]/div/input', param)
        self.driver.default_frame()

    def get_first_password_text(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_addUser_form"]/div[6]/div[1]/label')
        self.driver.default_frame()
        return text

    def get_second_password_text(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="markPswAgain_complex_addUser_form"]/div/label')
        self.driver.default_frame()
        return text

    def get_dev_name_in_dev_search(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_device_tbody"]/tr[1]/td[2]')
        self.driver.default_frame()
        return text

    def get_dev_imei_in_dev_search(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_device_tbody"]/tr[1]/td[3]')
        self.driver.default_frame()
        return text

    def get_dev_type_in_dev_search(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_device_tbody"]/tr[1]/td[4]')
        self.driver.default_frame()
        return text

    def get_dev_active_time_in_dev_search(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_device_tbody"]/tr[1]/td[5]')
        self.driver.default_frame()
        return text

    def get_dev_expire_time_in_dev_search(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_device_tbody"]/tr[1]/td[6]')
        self.driver.default_frame()
        return text

    def click_track_play_button_in_dev_search(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_device_tbody"]/tr[1]/td[9]/a[2]')
        sleep(2)
        self.driver.default_frame()

    def get_text_after_click_track_play(self):
        return self.driver.get_text('x,//*[@id="mapview"]/div[1]/div[1]/div/b')

    def get_dev_name_and_imei_after_click_track_play(self):
        return self.driver.get_text('x,//*[@id="driverName"]')

    def click_track_preset_button_in_dev_search(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_device_tbody"]/tr[1]/td[9]/a[3]')
        sleep(2)
        self.driver.default_frame()

    def get_text_after_click_track_preset(self):
        return self.driver.get_text('x,//*[@id="mapview"]/div[1]/div/b')

    def click_look_alarm_button_in_dev_search(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_device_tbody"]/tr[1]/td[9]/a[4]')
        sleep(2)
        self.driver.default_frame()

    def click_detail_in_dev_search(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_device_tbody"]/tr[1]/td[9]/a[1]')
        sleep(2)
        self.driver.default_frame()

    def get_dev_name_in_detail(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_device_detail_tbody"]/tr/td[2]')
        self.driver.default_frame()
        return text

    def get_dev_imei_in_detail(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_device_detail_tbody"]/tr/td[3]')
        self.driver.default_frame()
        return text

    def get_dev_type_in_detail(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_device_detail_tbody"]/tr/td[4]')
        self.driver.default_frame()
        return text

    def get_dev_active_time_in_detail(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_device_detail_tbody"]/tr/td[5]')
        self.driver.default_frame()
        return text

    def get_dev_expire_time_in_detail(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_device_detail_tbody"]/tr/td[6]')
        self.driver.default_frame()
        return text

    def click_track_play_button_in_dev_detail(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_device_detail_tbody"]/tr/td[10]/a[2]')
        sleep(2)
        self.driver.default_frame()

    def click_track_preset_button_in_dev_detail(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_device_detail_tbody"]/tr/td[10]/a[3]')
        sleep(2)
        self.driver.default_frame()

    def click_look_alarm_button_in_dev_detail(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_device_detail_tbody"]/tr/td[10]/a[4]')
        sleep(2)
        self.driver.default_frame()

    def click_look_place_button_in_dev_detail(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_device_detail_tbody"]/tr/td[10]/a[5]')
        sleep(2)
        self.driver.default_frame()

    def get_text_after_click_look_place(self):
        return self.driver.get_element('x,//*[@id="key2"]').get_attribute('value')

    def get_type_after_click_look_place(self):
        return self.driver.get_text(
            'x,/html/body/div[1]/div[5]/div/div[1]/div[2]/div[3]/div/div[4]/ul[1]/li/ul/li/div/div[1]/div[3]/div[1]/span[1]')

    def click_dev_search_button(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/span/div/button[1]')
        sleep(2)
        self.driver.default_frame()

    def click_dev_info_button_in_dev_detail(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[3]/div[2]/div[1]/ul/li[2]/a')
        sleep(2)
        self.driver.default_frame()

    def get_dev_imei_in_dev_info(self):
        self.swith_to_search_frame()
        self.driver.switch_to_frame('x,//*[@id="complex_editDevice_iframe"]')
        text = self.driver.get_element('x,//*[@id="device_info_a"]/fieldset/div[1]/div[1]/input[2]').get_attribute(
            'value')
        self.driver.default_frame()
        self.driver.default_frame()
        return text

    def get_dev_type_in_dev_info(self):
        self.swith_to_search_frame()
        self.driver.switch_to_frame('x,//*[@id="complex_editDevice_iframe"]')
        text = self.driver.get_element('x,//*[@id="device_info_a"]/fieldset/div[1]/div[2]/input[2]').get_attribute(
            'value')
        self.driver.default_frame()
        self.driver.default_frame()
        return text

    def get_dev_name_in_dev_info(self):
        self.swith_to_search_frame()
        self.driver.switch_to_frame('x,//*[@id="complex_editDevice_iframe"]')
        text = self.driver.get_element('x,//*[@id="device_info_a"]/fieldset/div[2]/div[1]/input').get_attribute('value')
        self.driver.default_frame()
        self.driver.default_frame()
        return text

    def click_dev_tran_button_in_dev_detail(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[3]/div[2]/div[1]/ul/li[3]/a')
        sleep(2)
        self.driver.default_frame()

    def click_customer(self, n):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_allotDev_tree_complexAllot_%s_span"]' % str(n + 2))
        sleep(2)
        self.driver.default_frame()

    def get_customer_name_in_header(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="allot_to_complexAllot"]')
        self.driver.default_frame()
        return text

    def get_click_customer_name(self, n):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_allotDev_tree_complexAllot_%s_span"]' % (n + 2))
        self.driver.default_frame()
        return text

    def search_user_in_dev_detail(self, param):
        self.swith_to_search_frame()
        self.driver.operate_input_element('x,//*[@id="complexAllot_globalSearch_input"]', param)
        self.driver.click_element('x,//*[@id="complexAllot_globalSearch_btn"]')
        sleep(3)
        self.driver.default_frame()

    def get_text_after_search_user_in_dev_detail(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_user_sale_complexAllot"]/div[2]/div/div/div/div')
        self.driver.default_frame()
        return text

    def add_dev_to_trans(self, dev_imei_in_detail):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="sale_imei_complexAllot"]')
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="sale_imei_complexAllot"]', dev_imei_in_detail)
        self.driver.click_element('x,//*[@id="complex_user_sale_complexAllot"]/div[1]/div/div[1]/div/div[3]/button[1]')
        sleep(2)
        self.driver.default_frame()

    def get_file_imei_after_add_imei(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="device_add_result_div"]/div[2]/table/tbody/tr/td[1]')
        self.driver.default_frame()
        return text

    def get_file_reason_add_imei(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="device_add_result_div"]/div[2]/table/tbody/tr/td[3]')
        self.driver.default_frame()
        return text

    def get_file_status(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="device_add_result_div"]/div[2]/table/tbody/tr/td[2]')
        self.driver.default_frame()
        return text

    def close_file_info(self):
        self.swith_to_search_frame()
        self.driver.click_element('c,layui-layer-ico')
        self.driver.default_frame()

    def click_detele_dev_in_dev_tran(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="sale_tbody_complexAllot"]/tr/td[6]/a')
        sleep(2)
        self.driver.default_frame()

    def click_trans_dev_button(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_user_sale_complexAllot"]/div[3]/div[2]/button[2]')
        sleep(2)
        self.driver.default_frame()

    def get_text_after_click_trans_dev(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('c,layui-layer-content')
        self.driver.default_frame()
        return text

    def click_reset_button(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_user_sale_complexAllot"]/div[3]/div[1]/button')
        sleep(2)
        self.driver.default_frame()

    def click_dev_command_button(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[3]/div[2]/div[1]/ul/li[4]/a')
        sleep(2)
        self.driver.default_frame()

    def get_dev_imei_in_command(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="instruction_IMEI"]')
        self.driver.default_frame()
        return text

    def get_dev_name_in_command(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="instruction_deviceName"]')
        self.driver.default_frame()
        return text

    def click_higher_search(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/div/div/button')
        sleep(2)
        self.driver.default_frame()

    def click_pull_down_customer(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[2]/div/div[1]/span/button')
        sleep(2)
        self.driver.default_frame()

    def click_customer_in_higher_search(self, n):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_search_tree_%s_span"]' % str(n + 1))
        sleep(2)
        self.driver.default_frame()

    def get_customer_name(self, n):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="complex_search_tree_%s_span"]' % str(n + 1))
        self.driver.default_frame()
        return text

    def get_customer_text(self):
        self.swith_to_search_frame()
        text = self.driver.get_element('x,//*[@id="complex_search_userName"]').get_attribute('value')
        self.driver.default_frame()
        return text

    def check_start_date_type(self, date):
        self.swith_to_search_frame()
        self.driver.operate_input_element('x,//*[@id="advancedSearchSelectStartTime"]', date)
        self.driver.click_element('x,/html/body/div[3]/div[1]/div/table/thead/tr/th[8]')
        self.driver.default_frame()

    def get_text_after_input_date(self):
        self.swith_to_search_frame()
        text = self.driver.get_text('x,//*[@id="laydate_time"]/p')
        self.driver.default_frame()
        return text

    def click_time_quantum_button(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[4]/label[2]/div/ins')
        sleep(2)
        self.driver.default_frame()

    def check_end_date_type(self, param):
        self.swith_to_search_frame()
        self.driver.operate_input_element('x,//*[@id="advancedSearchSelectEndTime"]', param)
        self.driver.click_element('x,/html/body/div[2]/div[1]/table/thead/tr/th[6]')
        self.driver.default_frame()

    def get_time_quantum_input_value(self):
        self.swith_to_search_frame()
        value = self.driver.get_element(
            'x,//*[@id="complex_advanced_search_form"]/div[4]/label[2]/div/input').is_selected()
        self.driver.default_frame()
        return value

    def click_arrearage_button(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[5]/label[2]/div/ins')
        sleep(2)
        self.driver.default_frame()

    def get_arrearage_input_value(self):
        self.swith_to_search_frame()
        value = self.driver.get_element(
            'x,//*[@id="complex_advanced_search_form"]/div[5]/label[2]/div/input').is_selected()
        self.driver.default_frame()
        return value

    def click_not_active_button(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[5]/label[3]/div/ins')
        sleep(2)
        self.driver.default_frame()

    def get_not_active_input_value(self):
        self.swith_to_search_frame()
        value = self.driver.get_element(
            'x,//*[@id="complex_advanced_search_form"]/div[5]/label[3]/div/input').is_selected()
        self.driver.default_frame()
        return value

    def get_text_dev_info(self):
        self.swith_to_search_frame()
        text = self.driver.get_element('x,//*[@id="complex_advanced_search_form"]/div[3]/input').get_attribute(
            'placeholder')
        self.driver.default_frame()
        return text

    def click_car_plate_number_dev_info(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[3]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[3]/div/div/div/ul/li[2]')
        sleep(1)
        self.driver.default_frame()

    def click_sn_dev_info(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[3]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[3]/div/div/div/ul/li[4]')
        sleep(1)
        self.driver.default_frame()

    def click_vin_dev_info(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[3]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[3]/div/div/div/ul/li[5]')
        sleep(1)
        self.driver.default_frame()

    def click_sim_dev_info(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[3]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[3]/div/div/div/ul/li[6]')
        sleep(1)
        self.driver.default_frame()

    def click_dev_name_dev_info(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[3]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[3]/div/div/div/ul/li[7]')
        sleep(1)
        self.driver.default_frame()

    def get_total_page_number_after_search_dev(self):
        a = self.driver.get_element('x,//*[@id="complex_paging_device"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_page_and_total_number('x,//*[@id="complex_paging_device"]',
                                                               'x,//*[@id="complex_device_tbody"]')
            return total
        else:
            return [0, 0]

    def get_no_data_text_in_search_dev(self):
        return self.driver.get_text('x,//*[@id="complex_device_table_nodata"]/div/span')

    def get_up_page_class_active_in_dev_search(self):
        return self.driver.get_element('x,//*[@id="complex_paging_device"]/ul/li[1]').get_attribute('class')

    def get_next_page_class_active_in_dev_search(self):
        return self.driver.get_element('x,//*[@id="complex_paging_device"]/ul/li[3]').get_attribute('class')

    def click_per_page(self, n):
        self.driver.click_element('l,%s' % str(n + 1))
        sleep(3)

    def get_per_frist_number_in_dev_search(self):
        return self.driver.get_text('x,//*[@id="complex_device_tbody"]/tr[1]/td[1]')

    def click_per_page_number(self):
        self.driver.click_element('c,page-select')
        sleep(2)
        self.driver.get_element('c,page-select').send_keys(Keys.DOWN + Keys.ENTER)
        sleep(5)

    def get_page_number_in_dev_search(self):
        new_paging = NewPaging(self.driver, self.base_url)
        total = new_paging.get_total_page('x,//*[@id="complex_paging_device"]')
        return total

    def click_dev_detail_after_search_dev(self):
        self.driver.click_element('x,//*[@id="complex_device_tbody"]/tr[1]/td[9]/a[1]')
        sleep(2)

    def click_dev_info_in_dev_detail(self):
        self.driver.click_element('x,/html/body/div[3]/div[2]/div[1]/ul/li[2]/a')
        sleep(2)

    def switch_to_dev_info_frame(self):
        self.driver.switch_to_frame('x,//*[@id="complex_editDevice_iframe"]')

    def click_cubic_oil_edit_in_dev_info(self):
        self.driver.click_element('x,//*[@id="device_info_a"]/fieldset[2]/div[1]/div/label[1]/div/ins')
        sleep(2)

    def click_ensure_button(self):
        self.driver.click_element('x,//*[@id="device_info_form"]/div[3]/div/button')
        sleep(2)

    def get_text_cubic1_after_click_ensure_button(self):
        return self.driver.get_text('x,//*[@id="device_info_a"]/fieldset[2]/div[2]/div[1]/div[1]/div[4]/label')

    def get_text_cubic2_after_click_ensure_button(self):
        return self.driver.get_text('x,//*[@id="device_info_a"]/fieldset[2]/div[2]/div[1]/div[2]/div[4]/label')

    def get_text_cubic3_after_click_ensure_button(self):
        return self.driver.get_text('x,//*[@id="device_info_a"]/fieldset[2]/div[2]/div[1]/div[3]/div[4]/label')

    def add_cubic_oil_parm_in_dev_info(self, param, param1, param2):
        self.driver.operate_input_element(
            'x,//*[@id="device_info_a"]/fieldset[2]/div[2]/div[1]/div[1]/div[2]/div/input', param)
        self.driver.operate_input_element(
            'x,//*[@id="device_info_a"]/fieldset[2]/div[2]/div[1]/div[2]/div[2]/div/input', param1)
        self.driver.operate_input_element(
            'x,//*[@id="device_info_a"]/fieldset[2]/div[2]/div[1]/div[3]/div[2]/div/input', param2)

    def get_succeed_text_after_click_ensure_button(self):
        return self.driver.get_text('c,layui-layer-content')

    def get_imei_in_dev_detail(self):
        return self.driver.get_text('x,//*[@id="complex_device_detail_tbody"]/tr/td[3]')

    def click_transfer_dev_button_in_dev_detail(self):
        self.driver.click_element('x,/html/body/div[3]/div[2]/div[1]/ul/li[3]/a')
        sleep(2)

    def get_imei_after_transfer_dev_button(self):
        return self.driver.get_text('x,//*[@id="sale_tbody_complexAllot"]/tr/td[1]')

    def click_sale_button_in_dev_detail(self):
        self.driver.click_element('x,//*[@id="complex_user_sale_complexAllot"]/div[3]/div[2]/button[2]')
        sleep(2)

    def get_text_after_click_transfer_button(self):
        return self.driver.get_text('c,layui-layer-content')

    def click_detele_dev_in_dev_transfer(self):
        self.driver.click_element('x,//*[@id="sale_tbody_complexAllot"]/tr/td[6]/a')
        sleep(2)

    def get_dev_number_in_dev_transfer_page(self):
        return len(list(self.driver.get_elements('x,//*[@id="sale_tbody_complexAllot"]/tr')))

    def get_dev_count_number_in_dev_transfer_page(self):
        return self.driver.get_text('x,//*[@id="sale_count_complexAllot"]')

    def click_frist_user_in_dev_transfer_page(self):
        self.driver.click_element('x,//*[@id="complex_allotDev_tree_complexAllot_1_span"]')

    def get_frist_user_name_in_dev_transfer_page(self):
        return self.driver.get_text('x,//*[@id="complex_allotDev_tree_complexAllot_1_span"]')

    def get_select_user_name_in_dev_transfer_page(self):
        return self.driver.get_text('x,//*[@id="allot_to_complexAllot"]')

    def click_reset_button_in_transfer_page(self):
        self.driver.click_element('x,//*[@id="complex_user_sale_complexAllot"]/div[3]/div[1]/button')
        sleep(2)

    def get_second_imei_in_dev_detail(self):
        return self.driver.get_text('x,//*[@id="complex_device_tbody"]/tr[2]/td[3]')

    def get_third_imei_in_dev_detail(self):
        return self.driver.get_text('x,//*[@id="complex_device_tbody"]/tr[3]/td[3]')

    def get_fourth_imei_in_dev_detail(self):
        return self.driver.get_text('x,//*[@id="complex_device_tbody"]/tr[4]/td[3]')

    def add_dev_to_trans_in_transfer_page(self, param):
        self.driver.click_element('x,//*[@id="sale_imei_complexAllot"]')
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="sale_imei_complexAllot"]', param)
        self.driver.click_element('x,//*[@id="complex_user_sale_complexAllot"]/div[1]/div/div[1]/div/div[3]/button[1]')
        sleep(3)

    def get_add_failure_status_after_click_add_button(self):
        return self.driver.get_text('x,//*[@id="device_add_result_div"]/div[2]/table/tbody/tr/td[2]/span')

    def get_add_failure_reason_after_click_add_button(self):
        return self.driver.get_text('x,//*[@id="device_add_result_div"]/div[2]/table/tbody/tr/td[3]')

    def click_close_failure_windows(self):
        self.driver.click_element('x,/html/body/div[5]/span[1]/a')
        sleep(2)

    def get_list_dev_number_in_dev_transfer_page(self):
        return len(list(self.driver.get_elements('x,//*[@id="sale_tbody_complexAllot"]/tr')))

    def get_dev_types_in_dev_detail(self):
        return self.driver.get_text('x,//*[@id="complex_device_detail_tbody"]/tr/td[2]')

    def clcik_dev_command_button(self):
        self.driver.click_element('x,/html/body/div[3]/div[2]/div[1]/ul/li[4]/a')
        sleep(2)

    def get_dev_imei_in_command_page(self):
        return self.driver.get_text('x,//*[@id="instruction_IMEI"]')

    def get_dev_name_in_command_page(self):
        return self.driver.get_text('x,//*[@id="instruction_deviceName"]')

    def click_advanced_search_button(self):
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/div/div/button')
        sleep(2)

    def click_search_button_in_dev_advanced_search_page(self):
        self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[2]/div/div[1]/span/button/i')
        sleep(2)

    def add_user_name_to_search_in_dev_advanced_search_page(self, user):
        self.driver.operate_input_element('x,//*[@id="complex_globalSearch_input"]', user)
        self.driver.click_element('x,//*[@id="complex_globalSearch_btn"]')
        sleep(5)

    def get_text_after_click_search_button_in_dev_advanced_search_page(self):
        return self.driver.get_text('x,//*[@id="complex_advanced_search_form"]/div[2]/div/div[2]/div/div/div')

    def get_first_page_total_number_in_dev_search(self):
        return len(list(self.driver.get_elements('x,//*[@id="complex_device_tbody"]/tr')))

    def get_imei_in_dev_search(self, n):
        return self.driver.get_text('x,//*[@id="complex_device_tbody"]/tr[%s]/td[3]' % str(n + 1))

    def get_first_total_number_in_advanced_search(self):
        return len(list(self.driver.get_elements('x,//*[@id="complex_device_tbody"]/tr')))

    def get_imei_in_dev_advanced_search(self, x):
        return self.driver.get_text('x,//*[@id="complex_device_tbody"]/tr[%s]/td[3]' % str(x + 1))

    def click_get_back_button_in_advanced_search(self):
        self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[1]/button')
        sleep(3)

    def click_detail_button_in_dev_advanced_search_page(self):
        self.driver.click_element('x,//*[@id="complex_device_tbody"]/tr[1]/td[9]/a[1]')
        sleep(2)

    def get_imei_after_click_detail_button_in_dev_advanced(self):
        return self.driver.get_text('x,//*[@id="complex_device_detail_tbody"]/tr/td[3]')

    def click_tracker_play_button_in_dev_advanced_page(self):
        self.driver.click_element('x,//*[@id="complex_device_detail_tbody"]/tr/td[10]/a[2]')
        sleep(3)

    def get_imei_after_click_tracker_play_in_tracker_play(self):
        return self.driver.get_text('x,//*[@id="driverName"]/span')

    def click_track_preset_button_in_dev_advanced_page(self):
        self.driver.click_element('x,//*[@id="complex_device_detail_tbody"]/tr/td[10]/a[3]')
        sleep(3)

    def click_alarm_detail_button_in_dev_advanced_page(self):
        self.driver.click_element('x,//*[@id="complex_device_detail_tbody"]/tr/td[10]/a[4]')
        sleep(3)

    def click_look_loacltion_button_in_dev_advanced_page(self):
        self.driver.click_element('x,//*[@id="complex_device_detail_tbody"]/tr/td[10]/a[5]')
        sleep(3)

    def click_search_buttons_in_dev_advanced_search_page(self):
        self.driver.click_element('x,//*[@id="complex_advanced_search_form"]/div[6]/button[1]')
        sleep(3)

    def click_console_button_in_dev_advanced(self):
        self.driver.click_element('x,//*[@id="complex_device_user_realtion_tbody"]/tr[2]/td[7]/a[1]')
        sleep(2)

    def click_look_button_in_dev_advanced(self):
        self.driver.click_element('x,//*[@id="complex_device_user_realtion_tbody"]/tr[2]/td[7]/a[4]')
        sleep(3)

    def get_user_dev_number_in_dev_advanced(self):
        return self.driver.get_text('x,//*[@id="complex_device_user_realtion_tbody"]/tr[2]/td[6]')

    def get_user_dev_total_number_in_dev_page(self):
        a = self.driver.get_element('x,//*[@id="paging-dev"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_numbers('x,//*[@id="paging-dev"]', 'x,//*[@id="deviceTableContent"]/tbody')
            return total
        else:
            return 0

    def click_dev_info_in_dev_advancde_search_page(self):
        self.driver.click_element('x,/html/body/div[3]/div[2]/div[1]/ul/li[2]/a')
        sleep(3)

    def get_imei_in_dev_info_after_click_dev_info_button(self):
        return self.driver.get_element('x,//*[@id="device_info_a"]/fieldset[1]/div[1]/div[1]/input[2]').get_attribute(
            'value')

    def get_imei_input_attribute_in_dev_info_page(self):
        return self.driver.get_element('x,//*[@id="device_info_a"]/fieldset[1]/div[1]/div[1]/input[2]').get_attribute(
            'disabled')

    def input_dev_name_modify_dev_info_in_dev_info_page(self, param):
        self.driver.operate_input_element('x,//*[@id="device_info_a"]/fieldset[1]/div[2]/div[1]/input', param)

    def click_ensure_button_in_dev_info_page(self):
        self.driver.click_element('x,//*[@id="device_info_form"]/div[3]/div/button')
        sleep(2)

    def get_text_after_click_ensure_in_dev_info_page(self):
        self.driver.default_frame()
        return self.driver.get_text('c,layui-layer-content')

    def select_dev_group_in_dev_info_page(self):
        self.driver.click_element('x,//*[@id="device_info_a"]/fieldset[1]/div[3]/div[1]/span/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//*[@id="device_info_a"]/fieldset[1]/div[3]/div[1]/span/div/div/ul/li[1]')
        sleep(2)

    def click_dev_range_of_use_in_dev_info_page(self, number):
        self.driver.click_element('x,//*[@id="device_info_a"]/fieldset[1]/div[4]/div[1]/ul/li[%s]' % number)
        sleep(2)

    def get_iccid_input_attribute_in_dev_info_page(self):
        return self.driver.get_element('x,//*[@id="device_info_a"]/fieldset[1]/div[5]/div[1]/input').get_attribute(
            'disabled')

    def get_sale_time_input_attribute_in_dev_info_page(self):
        return self.driver.get_element('x,//*[@id="device_info_a"]/fieldset[1]/div[5]/div[1]/input').get_attribute(
            'disabled')

    def add_over_speed_and_over_speed_time_to_modify_dev_info(self, param, param1):
        self.driver.operate_input_element('x,//*[@id="device_info_a"]/fieldset[1]/div[6]/div[1]/input', param)
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="device_info_a"]/fieldset[1]/div[6]/div[3]/input', param1)

    def add_remark_to_modify_dev_info(self, param):
        self.driver.operate_input_element('x,//*[@id="reMark"]', param)

    def get_dev_type_input_attribute_in_dev_info_page(self):
        return self.driver.get_element('x,//*[@id="device_info_a"]/fieldset[1]/div[1]/div[2]/input[2]').get_attribute(
            'disabled')

    def add_sim_number_to_modify_dev_info_page(self, sim):
        self.driver.operate_input_element('x,//*[@id="device_info_a"]/fieldset[2]/div[1]/div[1]/input', sim)

    def get_active_time_input_attribute_in_dev_info_page(self):
        return self.driver.get_element('x,//*[@id="device_info_a"]/fieldset[1]/div[3]/div[2]/input').get_attribute(
            'disabled')

    def get_platform_time_input_attribute_in_dev_info_page(self):
        return self.driver.get_element('x,//*[@id="device_info_a"]/fieldset[1]/div[4]/div[2]/input').get_attribute(
            'disabled')

    def get_imsi_input_attribute_in_dev_info_page(self):
        return self.driver.get_element('x,//*[@id="device_info_a"]/fieldset[1]/div[5]/div[2]/input').get_attribute(
            'disabled')

    def get_export_time_attribute_in_dev_info_page(self):
        return self.driver.get_element('x,//*[@id="device_info_a"]/fieldset[1]/div[5]/div[2]/input').get_attribute(
            'disabled')

    def get_dev_imei_in_transfer_dev_page(self):
        return self.driver.get_text('x,//*[@id="sale_tbody_complexAllot"]/tr/td[1]')

    def click_transfer_button_in_transfer_page(self):
        self.driver.click_element('x,//*[@id="complex_user_sale_complexAllot"]/div[3]/div[2]/button[2]')
        sleep(2)

    def clcik_dev_imei_in_transfer_page(self):
        self.driver.click_element('x,//*[@id="sale_tbody_complexAllot"]/tr/td[6]/a')
        sleep(2)

    def click_user_to_transfer_dev_in_transfer_dev_page(self):
        self.driver.click_element('x,//*[@id="complex_allotDev_tree_complexAllot_1_span"]')
        sleep(2)

    def get_dev_user_account_by_sql(self, param):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_tuqiang_sql()
        cursor = connect.cursor()
        sql = "SELECT m.account FROM equipment_mostly m where m.imei = '%s';" % param
        cursor.execute(sql)
        data = cursor.fetchall()
        user_account = data[0][0]
        cursor.close()
        connect.close()
        return user_account

    def get_dev_user_account_in_transfer_page(self):
        return self.driver.get_text('x,//*[@id="sale_tbody_complexAllot"]/tr/td[5]')

    def get_second_imei_in_dev_advanced_page(self):
        return self.driver.get_text('x,//*[@id="complex_device_tbody"]/tr[2]/td[3]')

    def get_third_imei_in_dev_advanced_page(self):
        return self.driver.get_text('x,//*[@id="complex_device_tbody"]/tr[3]/td[3]')

    def get_fourth_imei_in_dev_advanced_page(self):
        return self.driver.get_text('x,//*[@id="complex_device_tbody"]/tr[4]/td[3]')

    def get_total_dev_number_in_transfer_page(self):
        return self.driver.get_text('x,//*[@id="sale_count_complexAllot"]')

    def get_second_dev_user_account_in_transfer_page(self):
        return self.driver.get_text('x,//*[@id="sale_tbody_complexAllot"]/tr[2]/td[5]')

    def get_total_page_after_click_app_search(self):
        a = self.driver.get_element('x,//*[@id="complex_paging_mobileUser"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_page_and_total_number('x,//*[@id="complex_paging_mobileUser"]',
                                                               'x,//*[@id="complex_mobileUser_tbody"]')
            print(total)
            return total
        else:
            return 0

    def get_no_data_text_in_app_user_search(self):
        return self.driver.get_text('x,//*[@id="complex_mobileUser_table_nodata"]/div/span')

    def get_previous_page_class_in_app_user_search(self):
        return self.driver.get_element('x,//*[@id="complex_paging_mobileUser"]/ul/li[1]').get_attribute('class')

    def get_next_page_class_in_app_user_search(self):
        return self.driver.get_element('x,//*[@id="complex_paging_mobileUser"]/ul/li[3]').get_attribute('class')

    def click_search_button_in_user_search_page(self):
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/button[1]')
        sleep(3)

    def get_total_page_after_click_user_search_search(self):
        a = self.driver.get_element('x,//*[@id="complex_paging_user"]').get_attribute('style')
        if a == 'display: block;':
            new_page = NewPaging(self.driver, self.base_url)
            total = new_page.get_total_page_and_total_number('x,//*[@id="complex_paging_user"]',
                                                             'x,//*[@id="complex_user_tbody"]')
            return total
        else:
            return 0

    def get_no_data_text_in_user_search(self):
        return self.driver.get_text('x,//*[@id="complex_user_table_nodata"]/div/span')

    def get_previous_page_class_in_user_search(self):
        return self.driver.get_element('x,//*[@id="complex_paging_user"]/ul/li[1]').get_attribute('class')

    def get_next_page_class_in_user_search(self):
        return self.driver.get_element('x,//*[@id="complex_paging_user"]/ul/li[3]').get_attribute('class')

    def get_per_frist_number_in_user_search(self):
        return self.driver.get_text('x,//*[@id="complex_user_tbody"]/tr[1]/td[1]')

    def get_page_number_in_user_search(self):
        new_paging = NewPaging(self.driver, self.base_url)
        total = new_paging.get_total_page('x,//*[@id="complex_paging_user"]')
        return total

    def get_per_frist_number_in_dev_searchs(self):
        return self.driver.get_text('x,//*[@id="complex_mobileUser_tbody"]/tr[1]/td[1]')

    def get_dev_imei_in_details(self):
        return self.driver.get_text('x,//*[@id="complex_device_detail_tbody"]/tr/td[3]')

    def get_dev_status_in_dev_detail(self):
        return self.driver.get_text('x,//*[@id="complex_device_detail_tbody"]/tr/td[9]')

    def click_close_button(self):
        self.driver.click_element('c,layui-layer-ico')
        sleep(2)

    def click_cancel_page_button(self):
        self.driver.click_element('x,//*[@id="console"]/a')
        sleep(2)

    def add_dev_imei_to_search_in_console(self, get_dev_imei):
        self.driver.operate_input_element('x,//*[@id="key2"]', get_dev_imei)
        self.driver.click_element('x,//*[@id="console_equipment_searchBtn"]')
        sleep(3)

    def get_dev_status_in_console_page(self):
        return self.driver.get_text('x,//*[@id="normal_search_ul"]/li/div/div[1]/div[3]/div[1]/span[2]')

    def get_total_page_after_search_user(self):
        a = self.driver.get_element('x,//*[@id="complex_paging_user"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            return new_paging.get_total_page('x,//*[@id="complex_paging_user"]')
        else:
            return 0

    def get_per_page_total_number_in_search_user(self):
        return len(list(self.driver.get_elements('x,//*[@id="complex_user_tbody"]/tr')))

    def get_user_type_in_search_user(self, i):
        return self.driver.get_element('x,//*[@id="complex_user_tbody"]/tr[%s]/td[3]/div' % str(i + 1)).get_attribute(
            'title')

    def get_user_account_in_search_user(self, i):
        return self.driver.get_text('x,//*[@id="complex_user_tbody"]/tr[%s]/td[4]' % str(i + 1))

    def search_user(self, user_account):
        self.driver.operate_input_element('x,/html/body/div[1]/div[1]/div[1]/div/input', user_account)
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/button[1]')
        sleep(5)

    def click_add_next_user_in_search_user(self):
        self.driver.click_element('x,/html/body/div[2]/div[2]/div[1]/ul/li[4]/a')
        sleep(3)

    def get_user_type_number_in_search_user(self):
        return len(list(self.driver.get_elements('x,//*[@id="complex_addUser_form"]/div[2]/div[1]/div/label')))

    def get_new_next_display_in_search_user(self):
        return self.driver.get_element('x,/html/body/div[2]/div[2]/div[1]/ul/li[4]').get_attribute('style')

    def close_buttons(self):
        self.swith_to_search_frame()
        self.driver.click_element('c,layui-layer-ico')
        sleep(2)
        self.driver.default_frame()

    def cancel_buttons(self):
        self.swith_to_search_frame()
        self.driver.click_element('c,layui-layer-btn1')
        sleep(2)
        self.driver.default_frame()

    def ensure_buttons(self):
        self.swith_to_search_frame()
        self.driver.click_element('c,layui-layer-btn0')
        sleep(2)
        self.driver.default_frame()

    def get_text_after_succeeds(self):
        self.swith_to_search_frame()
        self.driver.click_element('c,layui-layer-content')
        sleep(2)
        self.driver.default_frame()

    def select_search_app_users(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/div/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/div/div/div/div/ul/li[3]')
        sleep(2)
        self.driver.default_frame()

    def click_search_buttonss(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/span/span/button')
        sleep(5)
        self.driver.default_frame()

    def select_search_dev(self):
        # self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/div/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/div/div/div/div/ul/li[2]')
        sleep(2)
        # self.driver.default_frame()

    def click_search_dev_button(self):
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/div/button')
        sleep(2)

    def swith_to_search_frames(self):
        self.driver.switch_to_iframe('x,/html/body/div[4]/div[2]/iframe')

    def click_user_search_buttons(self):
        self.swith_to_search_frame()
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[1]/div/button[1]')
        sleep(2)
        self.driver.default_frame()
