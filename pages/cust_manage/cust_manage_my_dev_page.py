import os
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page import BasePage

# 客户管理页面-我的设备
# author:孙燕妮
from pages.base.base_page_server import BasePageServer
from pages.base.new_paging import NewPaging


class CustManageMyDevPage(BasePageServer):
    def __init__(self, driver: AutomateDriverServer, base_url):
        super().__init__(driver, base_url)
        self.base_page = BasePage(self.driver, self.base_url)

    # 点击进入“我的设备”
    def enter_my_dev(self):
        self.driver.click_element("markDev")
        self.driver.wait()

    # 获取当前的设备个数
    def count_curr_dev_num(self):
        new_paging = NewPaging(self.driver, self.base_url)
        try:
            total = new_paging.get_total_number("x,//*[@id='paging-dev']", "x,//*[@id='markDevTable']")
            return total
        except:
            return 0
        '''
        # 设置列表底部每页共10条
        self.base_page.select_per_page_number(10)
        # 获取结果共分几页
        total_pages_num = self.base_page.get_total_pages_num("x,//*[@id='paging-dev']")
        # 获取最后一页有几条记录
        last_page_num = self.base_page.last_page_logs_num("x,//*[@id='markDevTable']","x,//*[@id='paging-dev']")
        # 计算当前结果共几条
        count = self.base_page.total_num(total_pages_num,last_page_num)
        return count'''

    # 选择搜索条件-分组
    def select_group(self, group_name):
        # 点击分组下拉框
        self.driver.click_element("markGroup")
        self.driver.wait()
        if group_name == '全部':
            self.driver.click_element("x,//*[@id='markGroup']/div/div/ul/li[1]")
        elif group_name == '默认组':
            self.driver.click_element("x,//*[@id='markGroup']/div/div/ul/li[2]")
        elif group_name == 'test_01':
            self.driver.click_element("x,//*[@id='markGroup']/div/div/ul/li[3]")
        self.driver.wait(1)

    # 选择搜索条件-激活状态
    def select_active_status(self, active_status):
        # 点击激活状态下拉框
        self.driver.click_element("x,//*[@id='allDev']/div[2]/div[1]/div[1]/div[2]/div[3]/span[2]/div[1]/span[2]")
        self.driver.wait()
        if active_status == '激活状态':
            self.driver.click_element(
                "x,//*[@id='allDev']/div[2]/div[1]/div[1]/div[2]/div[3]/span[2]/div[1]/div/ul/li[1]")
        elif active_status == '已激活':
            self.driver.click_element(
                "x,//*[@id='allDev']/div[2]/div[1]/div[1]/div[2]/div[3]/span[2]/div[1]/div/ul/li[2]")
        elif active_status == '未激活':
            self.driver.click_element(
                "x,//*[@id='allDev']/div[2]/div[1]/div[1]/div[2]/div[3]/span[2]/div[1]/div/ul/li[3]")
        self.driver.wait(1)

    # 选择搜索条件-绑定状态
    def select_band_status(self, band_status):
        # 点击绑定状态下拉框
        self.driver.click_element("x,//*[@id='allDev']/div[2]/div[1]/div[1]/div[2]/div[3]/span[2]/div[2]/span[2]")
        self.driver.wait()
        if band_status == '绑定状态':
            self.driver.click_element(
                "x,//*[@id='allDev']/div[2]/div[1]/div[1]/div[2]/div[3]/span[2]/div[2]/div/ul/li[1]")
        elif band_status == '已绑定':
            self.driver.click_element(
                "x,//*[@id='allDev']/div[2]/div[1]/div[1]/div[2]/div[3]/span[2]/div[2]/div/ul/li[2]")
        elif band_status == '未绑定':
            self.driver.click_element(
                "x,//*[@id='allDev']/div[2]/div[1]/div[1]/div[2]/div[3]/span[2]/div[2]/div/ul/li[3]")
        self.driver.wait(1)

    # 选择搜索条件-搜索类型SIM/IMEI，并输入对应号码
    def select_search_type(self, type, number):
        if type == 'IMEI':
            self.driver.click_element("x,//*[@id='allDev']/div[2]/div[1]/div[1]/div[2]/div[2]/label[1]/div/ins")
            self.driver.wait(1)
            # 输入IMEI
            self.driver.operate_input_element("searchSnImeiVal", number)
        elif type == 'SIM':
            self.driver.click_element("x,//*[@id='allDev']/div[2]/div[1]/div[1]/div[2]/div[2]/label[2]/div/ins")
            self.driver.wait(1)
            # 输入SIM
            self.driver.operate_input_element("searchSnImeiVal", number)
        self.driver.wait(1)

    # 输入imei进行搜索
    def search_dev_by_imei(self, imei):
        self.driver.operate_input_element("searchSnImeiVal", imei)
        self.driver.wait(1)

    # 点击搜索
    def click_search_btn(self):
        self.driver.click_element("x,//*[@id='allDev']/div[2]/div[1]/div[1]/div[2]/div[1]/div/span/button")
        self.driver.wait(5)

    # 获取搜索结果的Imei号
    def get_result_imei(self):
        imei = self.driver.get_element("x,//*[@id='markDevTable']/tr/td[3]").text
        return imei

    # 我的设备列表全选
    def select_all_my_dev(self):
        self.driver.click_element("x,//*[@id='deviceTableHeader']/thead/tr/th[1]/span/div/ins")
        self.driver.wait(1)

    # 我的设备列表-选择第一个
    def select_my_first_dev(self):
        self.driver.click_element("x,//*[@id='markDevTable']/tr[1]/td[1]/span/div/ins")
        self.driver.wait(1)

    # 批量编辑
    def click_batch_edit(self):
        self.driver.click_element("x,//*[@id='allDev']/div[2]/div[1]/div[1]/div[1]/button[1]")
        self.driver.wait()

    # 批量编辑-下载导入模板
    def download_import_model(self):
        self.driver.click_element("x,//*[@id='updateTemplate']/div/div/div[2]/div/div/a")
        self.driver.wait()

    # 批量编辑-导入更新文件
    def import_update_file(self):
        self.driver.click_element("x,//*[@id='batchUpdateDevForm']/button")
        self.driver.wait()
        # 调用upfile.exe上传程序
        # os.system("E:\\autoIt_script\\upfile.exe")
        # self.driver.wait()

    # 批量编辑-点击确定
    def click_confirm_btn(self):
        self.driver.click_element("x,//*[@id='updateTemplate']/div/div/div[3]/button[1]")
        self.driver.wait()

    # 批量编辑-点击取消
    def click_dismiss_btn(self):
        self.driver.click_element("x,//*[@id='updateTemplate']/div/div/div[3]/button[2]")
        self.driver.wait()

    # 批量编辑-获取导入操作状态
    def get_import_status(self):
        status = self.driver.get_element("c,layui-layer-content").text
        return status

    # 批量编辑-导入失败-关闭弹框
    def close_alert(self):
        self.driver.click_element("c,layui-layer-close")
        self.driver.wait(1)

    # 批量导出
    def batch_export(self):
        self.driver.click_element("x,//*[@id='allDev']/div[2]/div[1]/div[1]/div[1]/button[3]")
        self.driver.wait()

    # 批量销售
    def batch_sale(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div[1]/div[1]/button[2]')
        self.driver.wait()

    # 批量销售-获取当前已选中设备个数
    def get_curr_selected_dev_num(self):
        selected_num = self.driver.get_element("sale_count_batchSaleid")
        return selected_num

    # 批量销售-输入设备imei
    def input_dev_imei(self, imei):
        self.driver.get_element("sale_imei_batchSaleid").clear()
        self.driver.get_element("sale_imei_batchSaleid").send_keys(imei)
        self.driver.click_element("x,//*[@id='complex_user_sale_batchSaleid']/div[1]/div/div[1]/div/div[3]/button[1]")
        self.driver.wait(1)

    # 选择用户到期时间
    def choose_acc_expired_time(self, account_expired_time):
        self.driver.click_element("x,//*[@id='complex_user_sale_batchSaleid']/div[3]/div[1]/span/div/span[2]")
        self.driver.wait()
        if account_expired_time == '一个月':
            self.driver.click_element(
                "x,//*[@id='complex_user_sale_batchSaleid']/div[3]/div[1]/span/div/div/ul/li[2]")
        elif account_expired_time == '两个月':
            self.driver.click_element(
                "x,//*[@id='complex_user_sale_batchSaleid']/div[3]/div[1]/span/div/div/ul/li[3]")
        elif account_expired_time == '三个月':
            self.driver.click_element(
                "x,//*[@id='complex_user_sale_batchSaleid']/div[3]/div[1]/span/div/div/ul/li[4]")
        elif account_expired_time == '半年':
            self.driver.click_element(
                "x,//*[@id='complex_user_sale_batchSaleid']/div[3]/div[1]/span/div/div/ul/li[5]")
        elif account_expired_time == '一年':
            self.driver.click_element(
                "x,//*[@id='complex_user_sale_batchSaleid']/div[3]/div[1]/span/div/div/ul/li[6]")
        elif account_expired_time == '不限制':
            self.driver.click_element(
                "x,//*[@id='complex_user_sale_batchSaleid']/div[3]/div[1]/span/div/div/ul/li[7]")

    # 右侧搜索框搜索销售用户并选中
    def select_sale_acc(self, user_name):
        self.driver.operate_input_element("batchSaleid_globalSearch_input", user_name)
        # 点击搜索按钮
        self.driver.click_element("batchSaleid_globalSearch_btn")
        self.driver.wait()
        # 选中搜索结果
        self.driver.click_element("c,autocompleter-item")

    # 销售-销售按钮
    def sale_button(self):
        self.driver.click_element("x,//*[@id='complex_user_sale_batchSaleid']/div[3]/div[2]/button[3]")
        self.driver.wait(1)

    # 获取销售成功操作状态弹框的文本内容
    def get_sale_status(self):
        sale_status_text = self.driver.get_element("c,layui-layer-content").text
        return sale_status_text

    # 销售-取消
    def sale_dismiss(self):
        self.driver.click_element("x,//*[@id='complex_user_sale_batchSaleid']/div[3]/div[2]/button[1]")
        self.driver.wait(1)

    # 批量上传图片
    def batch_upload_pict(self):
        self.driver.click_element("x,//*[@id='allDev']/div[2]/div[1]/div[1]/div[1]/button[4]")
        self.driver.wait()

    # 批量上传图片-选择图片
    def select_pict(self):
        self.driver.click_element("file_upload")
        self.driver.wait()
        # 调用upfile.exe上传程序
        # os.system("E:\\autoIt_script\\upfile.exe")
        # self.driver.wait()

    # 批量上传图片-上传
    def click_upload_btn(self):
        self.driver.click_element("x,//*[@id='uploadModal']/div/div/div[3]/button[1]")
        self.driver.wait(3)

    # 批量上传图片-获取上传状态
    def get_upload_status(self):
        upload_status = self.driver.get_element("c,layui-layer-content").text
        return upload_status

    # 批量上传图片-取消上传
    def click_upload_dismiss(self):
        self.driver.click_element("x,//*[@id='uploadModal']/div/div/div[3]/button[2]")
        self.driver.wait(1)

    # 批量上传图片-清空列表
    def upload_clear_list(self):
        self.driver.click_element("x,//*[@id='uploadModal']/div/div/div[2]/div[1]/a")
        self.driver.wait(1)

    # 批量上传图片-获取图片列表
    def get_pict_list(self):
        pict_list = self.driver.get_elements("c,uploadify-queue-item")
        list_size = len(pict_list)
        return list_size

    # 单个设备操作(yanni/第一个)
    # 编辑

    def dev_edit(self):
        # 点击编辑按钮
        self.driver.click_element(
            "x,/html/body/div[2]/div[5]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[10]/a[1]")
        self.driver.wait()

    # 编辑基本信息
    # 基本信息-修改设备名称
    def dev_name_modify(self, dev_name):
        self.driver.operate_input_element('x,//*[@id="device_info_a"]/fieldset/div[2]/div[1]/input', dev_name)

    # 基本信息-移动设备分组
    def dev_group_modify(self, dev_group):
        # 点击分组下拉框
        self.driver.click_element('x,//*[@id="device_info_a"]/fieldset/div[3]/div[1]/span/div/span[2]')
        self.driver.wait(1)
        # 选择分组
        if dev_group == '默认组':
            self.driver.click_element('x,//*[@id="device_info_a"]/fieldset/div[3]/div[1]/span/div/div/ul/li[1]')
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
            self.driver.click_element('x,//*[@id="device_info_a"]/fieldset/div[4]/div[1]/ul/li[7]')
        elif dev_use_range == '无人机':
            self.driver.click_element('x,//*[@id="device_info_a"]/fieldset/div[4]/div[1]/ul/li[8]')
        elif dev_use_range == '其他':
            self.driver.click_element('x,//*[@id="device_info_a"]/fieldset/div[4]/div[1]/ul/li[9]')
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
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset/div[1]/div[1]/input', driver_name)
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
        # 将滚动条滚动至保存按钮处
        save_butt_ele = self.driver.get_element('x,//*[@id="SWFUpload_0"]')
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

    # 客户信息-安装信息-选择安装时间-确定
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
        self.driver.click_element('x,//*[@id="commModal_submit_btn"]')
        self.driver.wait(1)

    # 设备编辑-保存状态
    def dev_info_save_status(self):
        save_status = self.driver.get_element("c,layui-layer-content").text
        return save_status

    # 设备编辑-销售
    def dev_sale(self):
        self.driver.click_element(
            "x,/html/body/div[2]/div[5]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[10]/a[2]")
        self.driver.wait()

    # 列表仅有一个设备时-销售
    def one_dev_sale(self):
        self.driver.click_element("x,//*[@id='markDevTable']/tr/td[10]/a[2]")
        self.driver.wait()

    # 查看位置
    def dev_site(self):
        # 点击查看位置
        self.driver.click_element("x,/html/body/div[2]/div[5]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[3]/"
                                  "table/tbody/tr[1]/td[10]/a[3]")
        self.driver.wait()

    # 更多
    def dev_more(self, more_info):
        if more_info == '轨迹回放':
            # 点击更多
            self.driver.click_element('x,//*[@id="markDevTable"]/tr[1]/td[10]/a[4]')
            self.driver.wait()
            self.driver.click_element("l,轨迹回放")
            self.driver.wait()
        elif more_info == '街景':
            # 点击更多
            self.driver.click_element('x,//*[@id="markDevTable"]/tr[1]/td[10]/a[4]')
            self.driver.wait()
            self.driver.click_element("l,街景")
            self.driver.wait()
        elif more_info == '下发指令':
            # 点击更多
            self.driver.click_element('x,//*[@id="markDevTable"]/tr[1]/td[10]/a[4]')
            self.driver.wait()
            self.driver.click_element("l,下发指令")
            self.driver.wait()
            # 填写sos号码1
            self.driver.operate_input_element("text_0", "111")
            self.driver.wait(1)
            # 点击发送指令
            self.driver.click_element("instruction-send-btn")
            self.driver.wait(1)
            # 关闭窗口
            self.driver.click_element('l,确定')
            sleep(3)
            self.driver.click_element("x,//*[@id='command-modal']/div/div[1]/button")
            self.driver.wait()
        elif more_info == '行车记录':
            # 点击更多
            self.driver.click_element('x,//*[@id="markDevTable"]/tr[1]/td[10]/a[4]')
            self.driver.wait()
            self.driver.click_element("l,行车记录")
            self.driver.wait()
        elif more_info == '二维码':
            # 点击更多
            self.driver.click_element('x,//*[@id="markDevTable"]/tr[1]/td[10]/a[4]')
            self.driver.wait()
            self.driver.click_element("l,二维码")
            self.driver.wait(1)
            # 关闭二维码弹框
            self.driver.click_element("c,layui-layer-close2")
            self.driver.wait(1)
        elif more_info == '查看围栏':
            # 点击更多
            self.driver.click_element('x,//*[@id="markDevTable"]/tr[1]/td[10]/a[4]')
            self.driver.wait()
            self.driver.click_element("l,查看围栏")
            self.driver.wait(1)
            # 关闭围栏弹框
            self.driver.click_element("x,//*[@id='show-fence-table']/div/div/div[1]/button")
            self.driver.wait(1)
        elif more_info == '查看告警':
            # 点击更多
            self.driver.click_element('x,//*[@id="markDevTable"]/tr[1]/td[10]/a[4]')
            self.driver.wait()
            self.driver.click_element("l,查看告警")
            self.driver.wait()

    def acc_easy_search(self, search_keyword):
        # 在设备名称/imei/账号输入框内输入搜索关键词信息
        self.driver.operate_input_element("basicKeyword", search_keyword)
        # 点击搜索用户按钮
        self.driver.click_element("x,//*[@id='complexQuery']/div/button[1]")
        self.driver.wait(3)

    def view_search_cust(self):
        sleep(2)
        self.driver.click_element('x,//*[@id="complex_user_relation_tbody"]/tr[2]/td[7]/a[4]')
        self.driver.wait()
