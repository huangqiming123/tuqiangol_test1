import os
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.base.base_page import BasePage

# 全局搜索-设备搜索功能的元素及操作
# author:孙燕妮
from pages.base.new_paging import NewPaging


class GlobalComplexSearchPage(BasePage):
    def __init__(self, driver: AutomateDriver, base_url):
        super().__init__(driver, base_url)
        self.base_page = BasePage(self.driver, self.base_url)

    # 全局搜索栏-高级搜索按钮
    def click_complex_search(self):
        self.driver.click_element("x,//*[@id='complexQuery']/div/div/div/button")
        self.driver.wait(1)

    # 全局搜索栏-设备搜索按钮
    def click_easy_search(self):
        self.driver.click_element("x,//*[@id='complexQuery']/div/div/button")
        self.driver.wait(1)

    # 设备搜索对话框-高级搜索按钮
    def click_dev_dial_complex_search(self):
        self.driver.click_element("x,//*[@id='searchUserEquipment']/div/div/div[2]/div[1]/div[1]/div/span/button[2]")
        self.driver.wait(5)

    # 设备搜索对话框-高级搜索-返回按钮
    def dev_dial_complex_search_back(self):
        self.driver.click_element("x,//*[@id='complex_advanced_search_form']/div[1]/button")
        self.driver.wait(1)

    # 高级搜索-搜索
    def complex_search_click(self):
        self.driver.click_element("x,//*[@id='complex_advanced_search_form']/div[6]/button[1]")
        self.driver.wait(5)

    # 高级搜索-重置
    def complex_search_reset(self):
        self.driver.click_element("x,//*[@id='complex_advanced_search_form']/div[6]/button[2]")
        self.driver.wait()

    # 高级搜索对话框-关闭
    def close_dev_search(self):
        self.driver.click_element("x,//*[@id='searchUserEquipment']/div/div/div[1]/button")
        self.driver.wait(1)

    # 高级搜索对话框-选择用户
    def complex_search_select_acc(self, acc):
        # 点击选择用户
        self.driver.click_element("complex_search_userName")
        self.driver.wait()
        # 输入客户名称/账号
        self.driver.operate_input_element("complex_globalSearch_input", acc)
        # 点击搜索
        self.driver.click_element("complex_globalSearch_btn")
        self.driver.wait(1)
        # 点击搜索结果
        self.driver.click_element("c,autocompleter-item")
        self.driver.wait(1)

    # 高级搜索对话框-选择基本信息
    def complex_search_select_basic_info(self, condi, info):
        # 点击基本信息下拉框
        self.driver.click_element("x,//*[@id='complex_advanced_search_form']/div[3]/div/div/span[2]")
        self.driver.wait()
        # 选择基本信息
        if condi == 'imei':
            # 选择imei
            self.driver.click_element("x,//*[@id='complex_advanced_search_form']/div[3]/div/div/div/ul/li[1]")
            self.driver.wait()
            # 在右侧输入框内输入相应搜索信息
            self.driver.operate_input_element("x,//*[@id='complex_advanced_search_form']/div[3]/input", info)
        elif condi == 'vehicleNumber':
            # 选择车牌号
            self.driver.click_element("x,//*[@id='complex_advanced_search_form']/div[3]/div/div/div/ul/li[2]")
            self.driver.wait()
            # 在右侧输入框内输入相应搜索信息
            self.driver.operate_input_element("x,//*[@id='complex_advanced_search_form']/div[3]/input", info)
        elif condi == 'mcType':
            # 选择设备类型-BD309W
            self.driver.click_element("x,//*[@id='complex_advanced_search_form']/div[3]/div/div/div/ul/li[3]")
            self.driver.wait()
            self.driver.click_element("x,//*[@id='mcType_dev']/div/span[2]")
            self.driver.wait(1)
            self.driver.click_element('x,//*[@id="mcType_dev"]/div/div/ul/li[61]')

            self.driver.wait()
        elif condi == 'sn':
            # 选择SN
            self.driver.click_element("x,//*[@id='complex_advanced_search_form']/div[3]/div/div/div/ul/li[4]")
            self.driver.wait()
            # 在右侧输入框内输入相应搜索信息
            self.driver.operate_input_element("x,//*[@id='complex_advanced_search_form']/div[3]/input", info)
        elif condi == 'carFrame':
            # 选择车架号
            self.driver.click_element("x,//*[@id='complex_advanced_search_form']/div[3]/div/div/div/ul/li[5]")
            self.driver.wait()
            # 在右侧输入框内输入相应搜索信息
            self.driver.operate_input_element("x,//*[@id='complex_advanced_search_form']/div[3]/input", info)
        elif condi == 'sim':
            # 选择设备SIM卡号
            self.driver.click_element("x,//*[@id='complex_advanced_search_form']/div[3]/div/div/div/ul/li[6]")
            self.driver.wait()
            # 在右侧输入框内输入相应搜索信息
            self.driver.operate_input_element("x,//*[@id='complex_advanced_search_form']/div[3]/input", info)
        elif condi == 'deviceName':
            # 选择设备名称
            self.driver.click_element("x,//*[@id='complex_advanced_search_form']/div[3]/div/div/div/ul/li[7]")
            self.driver.wait()
            # 在右侧输入框内输入相应搜索信息
            self.driver.operate_input_element("x,//*[@id='complex_advanced_search_form']/div[3]/input", info)

    # 高级搜索对话框-选择日期类型
    def complex_search_select_date_type(self, date_type, start_time, end_time):
        # 点击日期类型下拉框
        self.driver.click_element("x,//*[@id='complex_advanced_search_form']/div[4]/div/div/span[2]")
        self.driver.wait()
        # 选择日期类型
        if date_type == '激活时间':
            self.driver.click_element("x,//*[@id='complex_advanced_search_form']/div[4]/div/div/div/ul/li[1]")
            self.driver.wait()
            # 输入激活时间段
            # 勾选“时间段”
            self.driver.click_element("x,//*[@id='complex_advanced_search_form']/div[4]/label[2]/div/ins")
            self.driver.wait()
            # 输入开始时间
            self.driver.operate_input_element("advancedSearchSelectStartTime", start_time)
            self.driver.wait(1)
            # 输入结束时间
            self.driver.operate_input_element("advancedSearchSelectEndTime", end_time)
            self.driver.wait(1)
        elif date_type == '用户到期时间':
            self.driver.click_element("x,//*[@id='complex_advanced_search_form']/div[4]/div/div/div/ul/li[2]")
            self.driver.wait()
            # 输入用户到期时间段
            # 勾选“时间段”
            self.driver.click_element("x,//*[@id='complex_advanced_search_form']/div[4]/label[2]/div/ins")
            self.driver.wait()

            # 输入开始时间
            self.driver.operate_input_element("advancedSearchSelectStartTime", start_time)
            self.driver.wait(1)
            # 输入结束时间
            self.driver.operate_input_element("advancedSearchSelectEndTime", end_time)
            self.driver.wait(1)
        elif date_type == '平台到期时间':
            self.driver.click_element("x,//*[@id='complex_advanced_search_form']/div[4]/div/div/div/ul/li[2]")
            self.driver.wait()
            # 输入平台到期时间段
            # 勾选“时间段”
            self.driver.click_element("x,//*[@id='complex_advanced_search_form']/div[4]/label[2]/div/ins")
            self.driver.wait()

            # 输入开始时间
            self.driver.operate_input_element("advancedSearchSelectStartTime", start_time)
            self.driver.wait(1)
            # 输入结束时间
            self.driver.operate_input_element("advancedSearchSelectEndTime", end_time)
            self.driver.wait(1)

    # 高级搜索对话框-选择设备状态
    def complex_search_select_dev_status(self, status):
        if status == '欠费':
            self.driver.click_element("x,//*[@id='complex_advanced_search_form']/div[5]/label[2]/div/ins")
            self.driver.wait(1)
        elif status == '未激活':
            self.driver.click_element("x,//*[@id='complex_advanced_search_form']/div[5]/label[3]/div/ins")
            self.driver.wait(1)

    # 获取暂无数据搜索结果文本内容
    def get_no_result_text(self):
        text = self.driver.get_element("x,/html/body/div[13]/div/div/div[2]/div[4]/div[1]/div/div/div[2]/div/span").text
        return text

    # 高级搜索-获取搜索结果共多少条
    def complex_search_result(self):
        a = self.driver.get_element('x,//*[@id="searchUserEquipment"]/div/div/div[2]/div[4]/div[2]').get_attribute(
            'style')

        if a == 'display: block;':
            return 1
        else:
            b = self.driver.get_element('x,//*[@id="complex_paging_device"]').get_attribute('style')
            if b == 'display: block;':
                new_paging = NewPaging(self.driver, self.base_url)
                # 将滚动条拖动到分页栏
                target = self.driver.get_element("complex_paging_device")
                self.driver.execute_script(target)  # 拖动到可见的元素去
                total = new_paging.get_total_number("x,//*[@id='complex_paging_device']",
                                                    "x,//*[@id='complex_device_tbody']")
                return total
            else:
                return 0
        # 当搜索结果只有一条时，必可获取到用户关系
        '''try:
            # 获取用户关系
            self.driver.get_element('x,//*[@id="searchUserEquipment"]/div/div/div[2]/div[4]/div[2]/div[1]/ul/li[2]/a')
            result_num = 1
            return result_num
        # 当搜索结果大于1条时
        except:
            new_paging = NewPaging(self.driver, self.base_url)
            try:
                # 将滚动条拖动到分页栏
                target = self.driver.get_element("complex_paging_device")
                self.driver.execute_script(target)  # 拖动到可见的元素去
                total = new_paging.get_total_number("x,//*[@id='complex_paging_device']",
                                                    "x,//*[@id='complex_device_tbody']")
                return total
            except:
                return 0

            # 设置每页10条
            self.base_page.select_per_page_number(10)
            # 获取搜索结果共分几页
            total_pages_num =  self.base_page.get_total_pages_num("x,//*[@id='complex_paging_device']")
            # 获取搜索结果最后一页有几条
            last_page_logs_num = self.base_page.last_page_logs_num("x,//*[@id='complex_device_tbody']",
                                                                   "x,//*[@id='complex_paging_device']")
            # 计算当前搜索结果共几条
            total_num = self.base_page.total_num(total_pages_num,last_page_logs_num)
            return total_num'''

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
        elif link_name == '父根级用户-控制台':
            # 设备详情-用户关系-父用户操作-父根级用户-“控制台”
            self.driver.click_element("x,//*[@id='complex_device_user_realtion_tbody']/tr[1]/td[7]/a[1]")
            self.driver.wait()
        elif link_name == '父根级用户-查看':
            # 设备详情-用户关系-父用户操作-父根级用户-“控制台”
            self.driver.click_element("x,//*[@id='complex_device_user_realtion_tbody']/tr[1]/td[7]/a[2]")
            self.driver.wait()
        elif link_name == '父根级的下级用户-控制台':
            # 设备详情-用户关系-父用户操作-父根级用户-“控制台”
            self.driver.click_element("x,//*[@id='complex_device_user_realtion_tbody']/tr[2]/td[7]/a[1]")
            self.driver.wait()
        elif link_name == '父根级的下级用户-查看':
            # 设备详情-用户关系-父根级的下级用户-“查看”
            self.driver.click_element("x,//*[@id='complex_device_user_realtion_tbody']/tr[2]/td[7]/a[4]")
            self.driver.wait()
        elif link_name == '当前设备用户-控制台':
            # 设备详情-用户关系-当前设备用户-“控制台”
            self.driver.click_element("x,//*[@id='complex_device_user_realtion_tbody']/tr[3]/td[7]/a[1]")
            self.driver.wait()
        elif link_name == '当前设备用户-查看':
            # 设备详情-用户关系-当前设备用户-“查看”
            self.driver.click_element("x,//*[@id='complex_device_user_realtion_tbody']/tr[3]/td[7]/a[4]")
            self.driver.wait()

    # 设备详情-用户关系-当前设备用户-“重置密码”
    def curr_dev_reset_passwd(self):
        self.driver.click_element("x,//*[@id='complex_device_user_realtion_tbody']/tr[3]/td[7]/a[3]")
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
        self.driver.operate_input_element("x,//*[@id='device_info_a']/fieldset/div[2]/div[1]/input", dev_name)

    # 设备详情-设备信息-基本信息-移动设备分组
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

    # 设备详情-设备信息-基本信息-选择设备使用范围
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

    # 设备详情-设备信息-基本信息-填写设备SIM卡号
    def dev_SIM_edit(self, SIM):
        self.driver.operate_input_element("x,//*[@id='device_info_a']/fieldset/div[2]/div[2]/input", SIM)

    # 设备详情-设备信息-基本信息-填写设备备注
    def dev_remark_edit(self, content):
        self.driver.operate_input_element("reMark", content)

    # 设备详情-设备信息-基本信息-保存
    def dev_basic_info_save(self):
        self.driver.click_element("x,//*[@id='device_info_form_compelx']/div[3]/div/button")
        self.driver.wait(1)

    # 设备详情-设备信息-基本信息-保存成功操作状态
    def dev_basic_info_save_status(self):
        save_status = self.driver.get_element("c,layui-layer-content").text
        return save_status

    # 设备详情-设备信息-客户信息
    def dev_cust_info_edit(self, driver_name, phone, id_card, car_shelf_num, car_lice_num, SN, engine_num):

        # 点击客户信息
        self.driver.click_element("x,//*[@id='edit_device_info_compelx']/div/ul/li[2]")
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
            "x,/html/body/div[13]/div/div/div[2]/div[4]/div[2]/div[2]/div[2]/div/form/div[3]/div/button")
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

    # 设备详情-设备信息-选择安装时间-今天
    def select_install_time(self):
        # 点击安装时间输入框
        self.driver.click_element("installTime_compelx")
        self.driver.wait(1)
        # 点击确定
        self.driver.click_element("laydate_ok")
        self.driver.wait(1)

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
        self.driver.click_element(
            "x,/html/body/div[13]/div/div/div[2]/div[4]/div[2]/div[2]/div[2]/div/form/div[3]/div/button")
        self.driver.wait(1)

    # 设备详情-设备信息-保存状态
    def dev_info_save_status(self):
        save_status = self.driver.get_element("c,layui-layer-content")
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
        self.driver.click_element("x,//*[@id='autocompleter-1']/ul/li")

    # 设备详情-设备转移-点击转移
    def click_trans_btn(self):
        self.driver.click_element("x,//*[@id='complex_user_sale_complexAllot']/div[3]/div[2]/button[3]")

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
            self.driver.operate_input_element("/html/body/div[13]/div/div/div[2]/div[4]/div[2]/div[2]/div[4]/div/"
                                              "form/div[2]/div[2]/div/div[2]/div/div[3]/div[1]/div[1]/div/input[2]",
                                              "11111")
            self.driver.operate_input_element("text_1", "123457888")
            self.driver.operate_input_element("text_2", "24456768787")
            # 点击删除sos号码
            self.driver.click_element("x,//*[@id='instruction_ul']/li[2]")
            self.driver.wait(1)
            # 选择复选框
            self.driver.click_element("x,//*[@id='params-div']/div/div/label[1]/div/ins")


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
            self.driver.click_element("x,//*[@id='complex_device_tbody']/tr[1]/td[9]/a[2]")
            self.driver.wait()
        elif link_name == '实时跟踪':
            self.driver.click_element("x,//*[@id='complex_device_tbody']/tr[1]/td[9]/a[3]")
            self.driver.wait()
        elif link_name == '查看告警':
            self.driver.click_element("x,//*[@id='complex_device_tbody']/tr[1]/td[9]/a[4]")
            self.driver.wait()

    # 设备列表-详情
    def click_dev_details(self):
        self.driver.click_element("x,//*[@id='complex_device_tbody']/tr[1]/td[9]/a[1]")
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

    def search_dev_arrearage_opeartion(self):
        # 搜索过期设备后详情下发指令
        self.driver.click_element('x,//*[@id="complex_device_tbody"]/tr[1]/td[8]/a[1]')
        sleep(2)
        self.driver.click_element('x,//*[@id="searchUserEquipment"]/div/div/div[2]/div[4]/div[2]/div[1]/ul/li[4]/a')
