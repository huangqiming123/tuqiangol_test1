import os
from time import sleep

from selenium.webdriver.support.select import Select

from automate_driver.automate_driver import AutomateDriver
from pages.base.base_page import BasePage


# 控制台页面
# author:孙燕妮

class ConsolePage(BasePage):
    def __init__(self, driver: AutomateDriver, base_url):
        super().__init__(driver, base_url)

    # 当前登录账户库存及总数
    def get_curr_login_dev_info(self):
        # 获取当前登录账户右侧的文本内容
        text = self.driver.get_element("account").text
        info = str(text).split(sep="(")[1]
        dev_info_01 = str(info).split(sep="/")[0]
        dev_stock = str(dev_info_01).split(sep="存")[1]
        dev_info_02 = str(info).split(sep="/")[1]
        dev_total = str(dev_info_02).split(sep="数")[1]
        info = {"库存": dev_stock, "总数": dev_total}
        return info

    # 获取客户列表登录账户库存及总数
    def get_cust_list_login_dev_info(self):
        # 获取当前登录账户右侧的文本内容
        text = self.driver.get_element("treeDemo_1_span").text
        info = list(str(text).split(sep="("))[1]
        dev_info_01 = str(info).split(sep="/")[0]
        dev_stock = str(dev_info_01).split(sep="存")[1]
        dev_info_02 = str(info).split(sep="/")[1]
        dev_total = str(dev_info_02).split(sep="数")[1]
        info = {"库存": dev_stock, "总数": dev_total}
        return info

    # 客户列表收起/展开
    def cust_list_fold_or_unfold(self):
        self.driver.click_element("x,//*[@id='sidesubtitleid']/button")
        self.driver.wait(1)

    # 设备列表收起/展开
    def dev_list_fold_or_unfold(self):
        self.driver.click_element("x,//*[@id='mapBox']/div[1]/div/div[3]/div[1]/button")
        self.driver.wait(1)

    # 客户列表-查找客户
    def search_user(self, keyword):
        # 搜索框内输入客户名称或账号
        self.driver.operate_input_element("cusTreeKey", keyword)
        # 点击搜索按钮
        self.driver.click_element("cusTreeSearchBtn")
        self.driver.wait(1)
        # 选中搜索结果
        self.driver.click_element("c,autocompleter-item")
        self.driver.wait(1)

    # 客户列表-获取当前选中账户的库存
    def get_curr_acc_dev_info(self):
        # 获取当前高亮客户右侧的文本内容
        text = self.driver.get_element("c,curSelectedNode").text
        info_01 = list(str(text).split(sep="("))[1]
        dev_stock = str(info_01).split(sep="/")[0]
        info_02 = list(str(text).split(sep=")"))[0]
        dev_total = str(info_02).split(sep="/")[1]
        info = {"库存": dev_stock, "总数": dev_total}
        return info

    # 点击“全部”
    def click_all(self):
        self.driver.click_element("x,//*[@id='mapBox']/div[1]/div/div[3]/div[2]/div/div[2]/a[1]")
        self.driver.wait()

    # 点击“已关注”
    def click_focus(self):
        self.driver.click_element("x,//*[@id='mapBox']/div[1]/div/div[3]/div[2]/div/div[2]/a[2]")
        self.driver.wait()

    # 点击“在线”
    def click_online(self):
        self.driver.click_element("x,//*[@id='mapBox']/div[1]/div/div[3]/div[2]/div/div[2]/a[3]")
        self.driver.wait()

    # 点击“离线”
    def click_offline(self):
        self.driver.click_element("x,//*[@id='mapBox']/div[1]/div/div[3]/div[2]/div/div[2]/a[4]")
        self.driver.wait()

    # 点击“未激活”
    def click_noactive(self):
        self.driver.click_element("x,//*[@id='mapBox']/div[1]/div/div[3]/div[2]/div/div[2]/a[5]")
        self.driver.wait()

    # 设备列表-统计当前设备总和
    def count_all_group_dev(self):
        # 折叠默认组
        self.driver.click_element(
            "x,/html/body/div[1]/div[4]/div/div[1]/div/div[3]/div[2]/div/div[4]/ul/li[1]/div/div/span/i")
        self.driver.wait(1)
        # 获取共多少个分组
        group_list = self.driver.get_elements("x,//*[@id='accordion']/li")
        group_num = len(group_list)
        print(group_num)
        # 获取默认组的设备个数
        default_dev = self.driver.get_element("x,/html/body/div[1]/div[4]/div/div[1]/div/div[3]/div[2]/div/div[4]/ul/"
                                              "li[1]/div/div/span/span[2]/span").text
        dev_num_list = [default_dev]
        print(dev_num_list)
        # 获取每个分组(除默认组外)有多少个设备
        for i in range(group_num - 1):
            j = i + 2
            dev_num_list.append(self.driver.get_element(
                "x,/html/body/div[1]/div[4]/div/div[1]/div/div[3]/div[2]/div/div[4]/ul/li[" + str(
                    j) + "]/div/div/span[2]/span[2]/span").text)
            self.driver.wait(1)
        print(dev_num_list)
        dev_num_list_size = len(dev_num_list)
        dev_num_list_int = []
        for a in range(dev_num_list_size):
            dev_num_list_int.append(int(dev_num_list[a]))
        print(dev_num_list_int)
        # 统计设备总和
        dev_num_total = 0
        for i in range(dev_num_list_size):
            dev_num_total = dev_num_total + dev_num_list_int[i]

        print("当前结果共" + str(group_num) + "个分组，设备总和为" + str(dev_num_total))
        return dev_num_total

    # 设备列表-获取“全部”设备个数
    def get_all_dev_num(self):
        all_dev_num = int(self.driver.get_element("indexAll").text)
        return all_dev_num

    # 设备列表-获取“已关注”设备个数
    def get_focus_dev_num(self):
        focus_dev_num = int(self.driver.get_element("attentions").text)
        return focus_dev_num

    # 设备列表-获取“在线”设备个数
    def get_online_dev_num(self):
        online_dev_num = int(self.driver.get_element("onlineCount").text)
        return online_dev_num

    # 设备列表-获取“离线”设备个数
    def get_offline_dev_num(self):
        offline_dev_num = int(self.driver.get_element("offlineCount").text)
        return offline_dev_num

    # 设备列表-获取“未激活”设备个数
    def get_noactive_dev_num(self):
        noactive_dev_num = int(self.driver.get_element("nonactivated").text)
        return noactive_dev_num

    # 折叠默认组
    def fold_default_group(self):
        self.driver.click_element(
            "x,/html/body/div[1]/div[4]/div/div[1]/div/div[3]/div[2]/div/div[4]/ul/li[1]/div/div/span/i")
        self.driver.wait(1)

    # 设备列表-设备搜索
    def search_dev(self, keyword):
        # 搜索框内输入imei/司机/车牌/设备名称
        self.driver.operate_input_element("nope", keyword)
        # 点击搜索按钮
        self.driver.click_element("index-search")
        self.driver.wait(1)

    # 设备列表-imei精确搜索-获取搜索结果设备id
    def get_dev_imei_search_result(self):
        group_open_list = self.driver.get_elements("c,open")
        group_open_list_size = len(group_open_list)
        if group_open_list_size == 1:
            # 当只有一个组呈展开状态时，精确搜索设备必然在默认组，获取当前展开组的搜索结果设备id
            dev_id = self.driver.get_element("s,li.open ul.submenu li:nth-child(1)").get_attribute("id")
            return dev_id
        elif group_open_list_size > 1:
            # 当有两个组呈展开状态时，精确搜索设备必然在非默认组，折叠默认组，则当前打开的组即为设备所在组，获取搜索结果所在组的设备id
            # 折叠默认组
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div[1]/div/div[3]/div[2]/div/div[4]/"
                                      "ul/li[1]/div/div/span/i")
            self.driver.wait()
            # 获取当前展开组的设备id
            dev_id = self.driver.get_element("s,li.open ul.submenu li:nth-child(1)").get_attribute("id")
            return dev_id

    # 设备列表-模糊查找-获取搜索结果总设备数
    def get_dev_like_search_result(self):
        dev_total_num = self.count_all_group_dev()
        return dev_total_num

    # 新建分组
    def add_group(self, group_name):
        self.driver.click_element("x,//*[@id='mapBox']/div[1]/div/div[3]/div[2]/div/div[3]/div/a[1]")
        self.driver.wait(1)
        # 输入组名
        self.driver.operate_input_element("orgName", group_name)
        # 点击添加
        self.driver.click_element("x,//*[@id='mapBox']/div[1]/div/div[3]/div[2]/div/div[3]/form/button[1]")
        self.driver.wait(1)

    # 新建分组-取消
    def dis_add_group(self, group_name):
        self.driver.click_element("x,//*[@id='mapBox']/div[1]/div/div[3]/div[2]/div/div[3]/div/a[1]")
        self.driver.wait(1)
        # 输入组名
        self.driver.operate_input_element("orgName", group_name)
        # 点击取消
        self.driver.click_element("x,//*[@id='mapBox']/div[1]/div/div[3]/div[2]/div/div[3]/form/button[2]")
        self.driver.wait(1)

    # 修改分组
    def edit_group(self, group_name):
        # 获取当前共几个分组
        group_list = self.driver.get_elements("x,//*[@id='accordion']/li")
        self.driver.wait(1)
        # 鼠标悬浮在已存在的非默认分组上(最后一个)
        self.driver.float_element(group_list[-1])
        self.driver.wait()
        sleep(2)
        # 点击编辑按钮
        self.driver.click_element(
            'x,/html/body/div[1]/div[4]/div/div[1]/div/div[3]/div[2]/div/div[4]/ul/li[9]/div/div/span[1]/a[1]')
        self.driver.wait()
        # 输入组名
        self.driver.operate_input_element("newOrganizeName", group_name)
        self.driver.wait()
        # 点击确定
        sleep(2)
        self.driver.click_element(
            "x,/html/body/div[1]/div[4]/div/div[1]/div/div[3]/div[2]/div/div[4]/ul/li[9]/div/div/form/button[1]")
        self.driver.wait(1)

    # 获取操作状态
    def get_edit_group_status(self):
        status = self.driver.get_element("c,layui-layer-content").text
        return status

    # 删除分组
    def del_group(self):
        # 获取当前共几个分组
        group_list = self.driver.get_elements("x,//*[@id='accordion']/li")
        self.driver.wait(1)
        # 鼠标悬浮在已存在的非默认分组上(最后一个)
        self.driver.float_element(group_list[-1])
        self.driver.wait()
        # 点击删除按钮
        sleep(3)
        self.driver.click_element(
            "x,/html/body/div[1]/div[4]/div/div[1]/div/div[3]/div[2]/div/div[4]/ul/li[9]/div/div/span[1]/a[2]")
        self.driver.wait()
        # 确认删除
        self.driver.click_element("x,/html/body/div[18]/div[3]/a[1]")
        self.driver.wait(1)

    # 获取当前分组总数
    def count_group_num(self):
        group_list = self.driver.get_elements("x,//*[@id='accordion']/li")
        group_num = len(group_list)
        return group_num

    # 选择排序方式
    def select_order_type(self, order):
        # 鼠标悬浮在排序方式元素处
        ele = self.driver.get_element("x,/html/body/div[1]/div[4]/div/div[1]/div/div[3]/div[2]/div/div[3]/div/a[2]")
        self.driver.float_element(ele)
        self.driver.wait()
        if order == '按在线':
            self.driver.click_element(
                "x,/html/body/div[1]/div[4]/div/div[1]/div/div[3]/div[2]/div/div[3]/div/a[2]/ul/li[1]")
            self.driver.wait(1)
        elif order == '按名称':
            self.driver.click_element(
                "x,/html/body/div[1]/div[4]/div/div[1]/div/div[3]/div[2]/div/div[3]/div/a[2]/ul/li[2]")
            self.driver.wait(1)

    # 单个设备操作
    # 点击车辆列表中的单个设备-默认组-第一个设备
    def click_dev(self):
        self.driver.click_element("x,/html/body/div[1]/div[4]/div/div[1]/div/div[3]/div[2]/div/div[4]/ul/li[1]/"
                                  "ul/li[1]/div[1]")
        self.driver.wait(1)

    # 获取当前选中设备的设备imei
    def get_dev_imei(self):
        dev_info = self.driver.get_element("x,/html/body/div[1]/div[4]/div/div[1]/div/div[3]/div[2]/div/div[4]/ul/"
                                           "li[1]/ul/li[1]/div[1]/a").get_attribute("id")
        dev_imei = str(dev_info).split(sep='_')[1]
        return dev_imei

    # 获取当前选中设备的设备名称
    def get_dev_name(self):
        dev_name = self.driver.get_element("x,/html/body/div[1]/div[4]/div/div[1]/div/div[3]/div[2]/div/div[4]/ul/"
                                           "li[1]/ul/li[1]/div[1]/a").get_attribute("title")
        return dev_name

    # 关注/取消关注
    def attention(self):
        # 获取关注/取消关注按钮的文本内容
        text = self.driver.get_element("x,/html/body/div[1]/div[4]/div/div[1]/div/div[3]/div[2]/div/div[4]/ul/li[1]/"
                                       "ul/li[1]/div[2]/a[1]").text
        if text == '关注':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div[1]/div/div[3]/div[2]/div/div[4]/ul/li[1]/"
                                      "ul/li[1]/div[2]/a[1]")
            self.driver.wait(1)
            # 获取已关注图标的文本title
            heart_title = self.driver.get_element("c,fa-heart").get_attribute("title")
            return heart_title
        elif text == '取消关注':
            # 获取已关注图标的文本title
            heart_title = self.driver.get_element("c,fa-heart").get_attribute("title")
            # 点击取消关注
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div[1]/div/div[3]/div[2]/div/div[4]/ul/li[1]/"
                                      "ul/li[1]/div[2]/a[1]")
            self.driver.wait(1)
            return heart_title

    # 轨迹回放
    def trace_replay(self):
        self.driver.click_element("x,/html/body/div[1]/div[4]/div/div[1]/div/div[3]/div[2]/div/div[4]/ul/li[1]/ul/li[1]"
                                  "/div[2]/a[2]")
        self.driver.wait()

    # 获取轨迹回放页面的设备imei
    def get_trace_dev_imei(self):
        dev_info = self.driver.get_element(
            "x,/html/body/div[1]/div/div/div/div[3]/div/div[3]/div[1]/form/div[1]/div/span").text
        dev_imei = str(dev_info).split(sep='：')[1]
        return dev_imei

    # 更多
    def click_more(self):
        self.driver.click_element("x,/html/body/div[1]/div[4]/div/div[1]/div/div[3]/div[2]/div/div[4]/ul/li[1]/ul/"
                                  "li[1]/div[2]/a[3]")
        self.driver.wait()

    # 街景
    def click_street_view(self):
        self.driver.click_element("s,ul.func-list.fs-12.lh-2 li a[title=街景]")
        self.driver.wait()

    # 获取街景页面的设备Imei
    def get_street_view_imei(self):
        dev_imei = self.driver.get_element("imeiHead").text
        return dev_imei

    # 下发指令
    def send_instr(self):
        self.driver.click_element("s,ul.func-list.fs-12.lh-2 li a[title=下发指令]")
        self.driver.wait()
        # 选择指令类型-sos号码
        self.driver.click_element("x,/html/body/div[9]/div/div[2]/form/div[2]/div[2]/div/div[1]/div/div/span[2]")
        self.driver.click_element("x,/html/body/div[9]/div/div[2]/form/div[2]/div[2]/div/div[1]/div/div/div/ul/li[1]")
        self.driver.wait(1)
        # 输入指令信息
        self.driver.operate_input_element("text_0", '0000')
        self.driver.operate_input_element("text_1", '11111')
        self.driver.operate_input_element("text_2", '11111')
        # 发送指令
        self.driver.click_element("instruction-send-btn")
        self.driver.wait(1)
        # 关闭发送指令窗口
        self.driver.click_element("x,/html/body/div[9]/div/div[1]/button")

    # 行车记录
    def drive_record(self):
        self.driver.click_element("s,ul.func-list.fs-12.lh-2 li a[title=行车记录]")
        self.driver.wait()

    # 获取行车记录页面的设备名称
    def get_drive_record_dev_name(self):
        dev_name = self.driver.get_element(
            "x,/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/form/div[1]/div").text
        return dev_name

    # 电子围栏
    def elec_rail(self):
        self.driver.click_element("s,ul.func-list.fs-12.lh-2 li a[title=电子围栏]")
        self.driver.wait()

    # 移动到组
    def move_group(self):
        ele = self.driver.get_element("s,ul.func-list.fs-12.lh-2 li a[title=移动到组]")
        self.driver.float_element(ele)
        # 选择目的组别
        self.driver.click_element("s,ul.func-list.fs-12.lh-2 li ul.list-sub-func.fs-12.lh-2 li a[title=默认组]")
        self.driver.wait()

    # 设备详情
    def dev_info(self, dev_name, sim, content, vehicle_num, install_pers):
        self.driver.click_element("s,ul.func-list.fs-12.lh-2 li a[title=设备详情]")
        self.driver.wait()
        # 编辑基本信息
        # 修改设备名称
        self.driver.operate_input_element(
            "x,/html/body/div[10]/div/div/div[2]/div/form/div[1]/fieldset/div[2]/div[1]/input", dev_name)
        # 编辑sim
        self.driver.operate_input_element(
            "x,/html/body/div[10]/div/div/div[2]/div/form/div[1]/fieldset/div[2]/div[2]/input", sim)
        # 编辑备注
        self.driver.operate_input_element("reMark", content)
        # 点击客户信息
        self.driver.click_element("x,/html/body/div[10]/div/div/div[2]/div/div/ul/li[2]")
        self.driver.wait(1)
        # 编辑客户信息
        # 编辑车牌号
        self.driver.operate_input_element(
            "x,/html/body/div[10]/div/div/div[2]/div/form/div[2]/fieldset/div[2]/div[2]/input", vehicle_num)
        # 编辑安装人员
        self.driver.operate_input_element(
            "x,/html/body/div[10]/div/div/div[2]/div/form/div[2]/fieldset/fieldset/fieldset/div[3]/div/input",
            install_pers)
        # 保存
        self.driver.click_element("x,/html/body/div[10]/div/div/div[3]/button[1]")
        self.driver.wait(1)

    # 获取设备信息保存状态
    def get_dev_info_save_status(self):
        status = self.driver.get_element("c,layui-layer-content").text
        return status

    # 获取地图中设备imei
    def get_map_dev_imei(self):
        dev_imei = self.driver.get_element(
            "s,#allmap > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div > div > div.popover-body > table > tbody > tr:nth-child(1) > td").text
        return dev_imei

    # 获取地图中设备名称
    def get_map_dev_name(self):
        dev_name = self.driver.get_element(
            "s,#allmap > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div > div > div.popover-body > table > tbody > tr:nth-child(2) > td").text
        return dev_name

    # 地图中的单个设备操作
    # 街景
    def map_dev_street_view(self):
        self.driver.click_element("x,//*[@id='allmap']/div[1]/div[2]/div[1]/div/div/div[3]/a[1]")
        self.driver.wait()

    # 轨迹回放
    def map_dev_trace_replay(self):
        self.driver.click_element("x,//*[@id='allmap']/div[1]/div[2]/div[1]/div/div/div[3]/a[2]")
        self.driver.wait()

    # 下发指令
    def map_dev_send_instr(self):
        self.driver.click_element("x,//*[@id='allmap']/div[1]/div[2]/div[1]/div/div/div[3]/a[3]")
        self.driver.wait()
        # 选择指令类型-sos号码
        self.driver.click_element("x,/html/body/div[9]/div/div[2]/form/div[2]/div[2]/div/div[1]/div/div/span[2]")
        self.driver.click_element("x,/html/body/div[9]/div/div[2]/form/div[2]/div[2]/div/div[1]/div/div/div/ul/li[1]")
        self.driver.wait(1)
        # 输入指令信息
        sleep(3)
        self.driver.operate_input_element("text_0", '0000')
        self.driver.operate_input_element("text_1", '11111')
        self.driver.operate_input_element("text_2", '11111')
        # 发送指令
        self.driver.click_element("instruction-send-btn")
        self.driver.wait(1)
        # 关闭发送指令窗口
        self.driver.click_element("x,/html/body/div[9]/div/div[1]/button")

    # 设备详情
    def map_dev_info(self, dev_name, sim, content, vehicle_num, install_pers):
        self.driver.click_element(
            'x,/html/body/div[1]/div[4]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div/div[3]/a[4]')
        self.driver.wait()
        # 编辑基本信息
        self.driver.switch_to_frame('x,//*[@id="commModal_iframe"]')
        # 修改设备名称
        self.driver.operate_input_element('x,//*[@id="device_info_a"]/fieldset/div[2]/div[1]/input', dev_name)
        # 编辑sim
        self.driver.operate_input_element('x,//*[@id="device_info_a"]/fieldset/div[2]/div[2]/input', sim)
        # 编辑备注
        self.driver.operate_input_element("reMark", content)
        # 点击客户信息
        self.driver.click_element('x,/html/body/div[1]/ul/li[2]/a')
        self.driver.wait(1)
        # 编辑客户信息
        # 编辑车牌号
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset/div[2]/div[1]/input', vehicle_num)
        # 编辑安装人员
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset/fieldset/fieldset/div[3]/div/input',
                                          install_pers)
        self.driver.default_frame()
        # 保存
        self.driver.click_element('x,//*[@id="commModal_submit_btn"]')
        self.driver.wait(1)

    # 电子围栏
    def map_dev_elec_rail(self):
        self.driver.click_element(
            "x,/html/body/div[1]/div[4]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div/div[3]/a[5]")
        self.driver.wait()

    # 查看告警
    def map_dev_alarm(self):
        self.driver.click_element("x,//*[@id='allmap']/div[1]/div[2]/div[1]/div/div/div[3]/a[6]")
        self.driver.wait()

    # 单个设备信息框的关闭
    def close_map_dev_info(self):
        self.driver.click_element("c,popover-close")
        self.driver.wait(1)
