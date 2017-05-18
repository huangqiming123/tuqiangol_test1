import os
from time import sleep

from automate_driver.automate_driver import AutomateDriver
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
        self.driver.click_element("x,/html/body/div[1]/header/div/div[2]/div[1]/a")
        self.driver.wait(1)

    # 全局搜索栏-设备搜索
    def device_easy_search(self, search_keyword):
        self.driver.switch_to_frame('x,/html/body/div[13]/div[2]/iframe')

        # 在设备名称/imei输入框内输入搜索关键词信息
        self.driver.operate_input_element('x,/html/body/div[1]/div[1]/div/input', search_keyword)
        # 点击搜索设备按钮
        self.driver.click_element('x,/html/body/div[1]/div[1]/div/span/div/button[1]')
        sleep(5)
        self.driver.default_frame()

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
        self.driver.switch_to_frame('x,/html/body/div[13]/div[2]/iframe')
        a = self.driver.get_element('x,//*[@id="complex_paging_device"]').get_attribute('style')
        b = self.driver.get_element('x,//*[@id="complex_device_table_nodata"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_number('x,//*[@id="complex_paging_device"]',
                                                'x,//*[@id="complex_device_tbody"]')
            self.driver.default_frame()
            return total
        else:
            if a == 'display: none;' and b == 'display: none;':
                self.driver.default_frame()
                return 1
            elif a == 'display: none;' and b == 'display: block;':
                self.driver.default_frame()
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
        self.driver.switch_to_frame('x,/html/body/div[13]/div[2]/iframe')
        self.driver.operate_input_element('x,/html/body/div[1]/div[1]/div/input', search_data['account_info'])
        self.driver.click_element('x,/html/body/div[1]/div[1]/div/span/div/button[1]')
        sleep(5)
        self.driver.default_frame()

    def get_account_before_reset_password(self):
        # 获取重置密码的用户名
        return self.driver.get_text('x,//*[@id="complex_device_user_realtion_tbody"]/tr[2]/td[4]')

    def click_equipment_button(self):
        self.driver.click_element('x,//*[@id="complexQuery"]/div/div/button')

    def add_data_to_search_complex(self, search_data):
        # 增加数据去搜索高级
        self.driver.switch_to_frame('x,/html/body/div[13]/div[2]/iframe')
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

        self.driver.default_frame()

    def device_easy_searchs(self, param):
        self.driver.operate_input_element('x,//*[@id="searchUserEquipment"]/div/div/div[2]/div[1]/div[1]/div/input',
                                          param)
        self.driver.click_element('x,//*[@id="searchUserEquipment"]/div/div/div[2]/div[1]/div[1]/div/span/button[1]')
        sleep(4)

    def close_search(self):
        self.driver.click_element('c,layui-layer-ico')

    def click_dev_search(self):
        self.driver.switch_to_frame('x,/html/body/div[13]/div[2]/iframe')
        self.driver.click_element('x,/html/body/div[1]/div[1]/div/div/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,/html/body/div[1]/div[1]/div/div/div/div/div/ul/li[2]')
        sleep(2)
        self.driver.default_frame()

    def click_senior_search_button(self):
        self.driver.switch_to_frame('x,/html/body/div[13]/div[2]/iframe')
        self.driver.click_element('x,/html/body/div[1]/div[1]/div/span/div/button[2]')
        sleep(2)
        self.driver.default_frame()

    def click_app_account_search(self):
        self.driver.switch_to_frame('x,/html/body/div[13]/div[2]/iframe')
        self.driver.click_element('x,/html/body/div[1]/div[1]/div/div/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,/html/body/div[1]/div[1]/div/div/div/div/div/ul/li[3]')
        sleep(2)
        self.driver.default_frame()

    def app_account_easy_search(self, search_data):
        self.driver.switch_to_frame('x,/html/body/div[13]/div[2]/iframe')
        self.driver.operate_input_element('x,/html/body/div[1]/div[1]/div/input', search_data['account_info'])
        self.driver.click_element('x,/html/body/div[1]/div[1]/div/span/span/button')
        sleep(5)
        self.driver.default_frame()
