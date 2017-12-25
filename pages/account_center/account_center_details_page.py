from time import sleep

from selenium.webdriver.common.keys import Keys

from automate_driver.automate_driver import AutomateDriver
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page import BasePage

# 账户中心页面-账户详情的元素及操作
# author:孙燕妮
from pages.base.base_page_server import BasePageServer
from pages.base.new_paging import NewPaging


class AccountCenterDetailsPage(BasePageServer):
    def __init__(self, driver: AutomateDriverServer, base_url):
        super().__init__(driver, base_url)

    # 点击账户总览
    def click_account_pandect(self):
        self.driver.click_element("zSales")
        sleep(2)

    # 账户总览页面跳转
    def account_overview(self, link_name):

        if link_name == '库存':
            self.driver.click_element('x,//*[@id="creat-0"]/div[1]/a')
            self.driver.wait(1)
        elif link_name == '总进货数':
            self.driver.click_element('x,//*[@id="creat-0"]/div[2]/a')
            self.driver.wait(1)
        elif link_name == '在线':
            self.driver.click_element('x,//*[@id="creat-0"]/div[3]/a')
            self.driver.wait(1)
        elif link_name == '离线':
            self.driver.click_element('x,//*[@id="creat-0"]/div[4]/a')
            self.driver.wait(1)
        elif link_name == '即将到期':
            self.driver.click_element('x,//*[@id="creat-0"]/div[5]/a')
            self.driver.wait(1)
        elif link_name == '已过期':
            self.driver.click_element('x,//*[@id="creat-0"]/div[6]/a')
            self.driver.wait(1)
        elif link_name == '已激活':
            self.driver.click_element('x,//*[@id="creat-0"]/div[7]/a')
            self.driver.wait(1)
        elif link_name == '未激活':
            self.driver.click_element('x,//*[@id="creat-0"]/div[8]/a')
            self.driver.wait(1)
        elif link_name == '告警车辆':
            self.driver.click_element('x,//*[@id="creat-0"]/div[9]/a')
            self.driver.wait(1)
        elif link_name == '重点关注车辆':
            self.driver.click_element('x,//*[@id="creat-0"]/div[10]/a')
            self.driver.wait(1)
        elif link_name == '控制台':
            self.driver.click_element('x,//*[@id="creat-1"]/div[1]/a')
            self.driver.wait(1)
        elif link_name == '统计报表':
            self.driver.click_element('x,//*[@id="creat-1"]/div[2]/a')
            self.driver.wait(1)
        elif link_name == '围栏':
            self.driver.click_element('x,//*[@id="creat-1"]/div[3]/a')
            self.driver.wait(1)
        elif link_name == '下级客户管理':
            self.driver.click_element('x,//*[@id="creat-1"]/div[4]/a')
            self.driver.wait(1)
        elif link_name == '设备管理':
            self.driver.click_element('x,//*[@id="creat-1"]/div[5]/a')
            self.driver.wait(1)
        elif link_name == '指令管理':
            self.driver.click_element('x,//*[@id="creat-1"]/div[6]/a')
            self.driver.wait(1)
        elif link_name == '地标设置':
            self.driver.click_element('x,//*[@id="creat-1"]/div[7]/a')
            self.driver.wait(1)
        elif link_name == '告警':
            self.driver.click_element('x,//*[@id="creat-1"]/div[8]/a')
            self.driver.wait(1)

    # 快捷销售
    def fast_sales(self):
        self.driver.click_element("x,//*[@id='eSales']/a")
        self.driver.wait()

    # 快捷销售-账户查找
    def fast_sales_find_account(self, search_account):
        # 点击“销售给”下拉箭头图标
        self.driver.click_element('showTree-btn')
        # 下拉搜索框内输入精确的用户名/账号
        self.driver.operate_input_element("ac_putDevice_globalSearch_SalesName", search_account)
        # 点击搜索按钮
        self.driver.click_element("ac_putDevice_globalSearch_btn")
        self.driver.wait(3)
        # 点击搜索结果列表中唯一的账户
        self.driver.click_element("c,autocompleter-item")
        self.driver.wait(1)

    ## 快捷销售-账户查找2
    def import_account_search(self, search_account):
        # 点击下拉箭头图标
        self.driver.click_element("showTree-btn")
        self.driver.wait(1)
        self.driver.operate_input_element("ac_putDevice_globalSearch_SalesName", search_account)
        self.driver.wait(1)
        self.driver.click_element("ac_putDevice_globalSearch_btn")
        self.driver.wait(5)
        # 获取查询结果
        list_data = len(self.driver.get_elements("x,/html/body/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/"
                                                 "div[1]/div[1]/div[2]/div/div[1]/div/ul/li"))
        if list_data >= 1:
            list = []
            for i in range(list_data):
                text = self.driver.get_text("x,/html/body/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/"
                                            "div[1]/div[1]/div[2]/div/div[1]/div/ul/li[" + str(i + 1) + "]")
                list.append(text)
            print(list)
            return list
        else:
            no_data = self.driver.get_text("x,/html/body/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[1]"
                                           "/div[1]/div[2]/div/div[1]/div/span")
            print(no_data)
            return no_data

    # 快速销售--销售给--点击用户
    def click_sell_user(self, numeral):
        # 点击下拉箭头图标
        self.driver.click_element("showTree-btn")
        sleep(2)
        self.driver.click_element("x,/html/body/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[1]"
                                  "/div[1]/div[2]/div/div[2]/ul/li/ul/li[" + str(numeral) + "]/a/span[2]")
        sleep(2)

    # ENTER建搜索账号
    def search_user_click_enter(self, search_account):
        # 点击下拉箭头图标
        self.driver.click_element("showTree-btn")
        self.driver.wait(1)
        # 定位输入框
        search = self.driver.get_element("ac_putDevice_globalSearch_SalesName")
        self.driver.operate_input_element("ac_putDevice_globalSearch_SalesName", search_account)
        self.driver.wait(1)
        search.send_keys(Keys.ENTER)
        self.driver.wait(3)
        # 清空
        search.send_keys(Keys.BACKSPACE)
        self.driver.operate_input_element("ac_putDevice_globalSearch_SalesName", search_account)
        self.driver.wait(1)
        search.send_keys(Keys.ENTER)

    # 下级客户、库存搜索
    def subordinate_account_search(self, user):
        self.driver.operate_input_element("treeSubUser_search_input", user)
        self.driver.click_element("treeSubUser_search_btn")
        sleep(5)
        user_len = len(
            self.driver.get_elements("x,/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/ul/li"))
        if user_len >= 1:
            list_data = []
            for i in range(user_len):
                text = self.driver.get_text(
                    "x,/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/ul/li[" + str(i + 1) + "]")
                list_data.append(text)
            print(list_data)
            return list_data
        else:
            no_data = self.driver.get_text("x,/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[1]/span")
            return no_data

    # 下级客户--直接点击列表
    def click_list_subordinate_client(self, number):
        self.driver.click_element("x,/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/ul/"
                                  "li/ul/li[" + str(number) + "]/a/span[2]")
        sleep(1)

        # ENTER建搜索账号

    def search_subordinate_client_click_enter(self, search_account):
        # 定位输入框
        search = self.driver.get_element("treeSubUser_search_input")
        self.driver.operate_input_element("treeSubUser_search_input", search_account)
        self.driver.wait(1)
        search.send_keys(Keys.ENTER)
        self.driver.wait(3)
        # 清空
        search.send_keys(Keys.BACKSPACE)
        self.driver.operate_input_element("treeSubUser_search_input", search_account)
        self.driver.wait(1)
        search.send_keys(Keys.ENTER)

    '''# 已选中账户后获取账户框内显示的账户名文本内容
    def get_selected_account(self):
        selected_account_text = self.driver.get_element("x,//*[@id='autocompleter-1']/div").text
        return selected_account_text'''

    # 快捷销售-设备查找、添加
    def fast_sales_find_and_add_device(self, device_imei):
        # 在“追加设备”框内输入账号下存在的设备imei号（一个/多个）
        if "/" in device_imei:
            self.driver.get_element('searchIMEI').click()
            self.driver.clear("searchIMEI")
            self.driver.wait(1)
            value = device_imei.split("/")
            print(value)
            for i in value:
                add_sim = self.driver.get_element("searchIMEI")
                self.driver.input_sim('searchIMEI', i)
                add_sim.send_keys(Keys.ENTER)

            # 获取imei计数
            imei_count = self.get_device_imei_count()
            data = {"import_count": len(value),
                    "add_count": imei_count
                    }

            # 点击“添加”按钮
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[3]/button[1]')
            self.driver.wait()
            return data
        else:
            self.driver.operate_input_element("searchIMEI", device_imei)
            self.driver.wait(1)
            imei_count = self.get_device_imei_count()
            self.driver.click_element("x,/html/body/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]"
                                      "/div[2]/div/div/div/div[3]/button[1]")
            self.driver.wait()
            return imei_count

    '''# 已添加设备imei后获取设备框内显示的设备imei文本内容
    def get_selected_device(self):
        selected_device_text = self.driver.get_element("searchIMEI").text
        return selected_device_text'''

    # 快捷销售-设备查找-取消添加
    def fast_sales_find_and_dis_add_device(self, device_imei):
        # 在“追加设备”框内输入存在的设备imei号
        self.driver.operate_input_element("searchIMEI", device_imei)
        # 点击“取消”按钮
        self.driver.click_element('x,/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[3]/button[2]')

    # 快捷销售-设备列表-删除
    def delete_list_device(self):
        count = len(self.driver.get_elements("x,//*[@id='succList']/tr"))
        print("长度", count)
        if count > 1:
            for i in range(count):
                self.driver.click_element("x,/html/body/div/div/div/div/div[2]/div/div[2]/table/tr/td[6]/a")
                self.driver.wait(1)
        else:
            self.driver.click_element("x,/html/body/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/"
                                      "div[2]/table/tr[1]/td[6]/a")

    # 快捷销售-设备查找-获取输入imei计数
    def get_device_imei_count(self):
        dev_num = self.driver.get_element("ac_dev_num").text
        sleep(1)
        return dev_num

    # 快捷销售-设备查找-获取已选设备个数
    def get_selected_device_num(self):
        dev_num = int(self.driver.get_element("selectedCount").text)
        return dev_num

    # 快速销售-设备查找-提示成功个数
    def get_device_prompt_succeed_count(self):
        succeed_count = self.driver.get_text("succCount")
        return int(succeed_count)

    # 快速销售-设备查找-提示失败个数
    def get_device_prompt_failure_count(self):
        failure_count = self.driver.get_text("failCount")
        print("失败数", failure_count)
        return int(failure_count)

    # 快速销售-设备查找-提示列表失败个数
    def get_device_list_failure_count(self):
        list_count = len(self.driver.get_elements("x,//*[@id='failedList']/tr"))
        return list_count

    # 快速销售-添加成功个数
    def get_list_succeed_count(self):
        count = len(self.driver.get_elements("x,//*[@id='succList']/tr"))
        print("列表", count)
        return count

    # 获取消息中的数据
    def get_prompt_list_data(self):
        all_imei = []
        all_state = []
        all_cause = []
        count = len(self.driver.get_elements("x,//*[@id='failedList']/tr"))
        print("333", count)
        for i in range(count):
            imei = self.driver.get_text("x,//*[@id='failedList']/tr[" + str(i + 1) + "]/td[1]")
            state = self.driver.get_text("x,//*[@id='failedList']/tr[" + str(i + 1) + "]/td[2]/span")
            cause = self.driver.get_text("x,//*[@id='failedList']/tr[" + str(i + 1) + "]/td[3]")
            all_imei.append(imei)
            all_state.append(state)
            all_cause.append(cause)
        data = {
            "imei": all_imei,
            "state": all_state,
            "cause": all_cause,
        }
        return data

    # 点击消息提示的X
    def click_prompt_close(self):
        self.driver.click_element("c,layui-layer-ico")

    # 快捷销售-选择用户到期时间
    def choose_account_expired_time(self, account_expired_time):
        self.driver.click_element("x,/html/body/div[1]/div/div/div/div[3]/span/div/span[2]")
        self.driver.wait(1)
        if account_expired_time == '一个月':
            self.driver.click_element("x,/html/body/div[1]/div/div/div/div[3]/span/div/div/ul/li[2]")
        elif account_expired_time == '两个月':
            self.driver.click_element("x,/html/body/div[1]/div/div/div/div[3]/span/div/div/ul/li[3]")
        elif account_expired_time == '三个月':
            self.driver.click_element("x,/html/body/div[1]/div/div/div/div[3]/span/div/div/ul/li[4]")
        elif account_expired_time == '半年':
            self.driver.click_element("x,/html/body/div[1]/div/div/div/div[3]/span/div/div/ul/li[5]")
        elif account_expired_time == '一年':
            self.driver.click_element("x,/html/body/div[1]/div/div/div/div[3]/span/div/div/ul/li[6]")
        elif account_expired_time == '不限制':
            self.driver.click_element("x,/html/body/div[1]/div/div/div/div[3]/span/div/div/ul/li[7]")

    # 快捷销售-销售按钮
    def sale_button(self):
        self.driver.click_element("x,/html/body/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/button[3]")

    # 获取销售成功操作状态弹框的文本内容
    def get_sale_status(self):
        sale_status_text = self.driver.get_element("c,layui-layer-content").text
        return sale_status_text

    # 快捷销售-重置
    def reset_device(self):
        self.driver.click_element("resetDevice")

    # 快捷销售-新增客户
    def add_cust(self, acc_type, acc_name, account, pwd, phone, email, conn, com):
        # self.driver.switch_to_frame('x,//*[@id="usercenterFrame"]')
        # 点击新增客户
        # self.driver.click_element("x,/html/body/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/button")
        # self.driver.default_frame()
        sleep(2)
        self.switch_to_add_account_in_new_center()
        # 选择客户类型
        if acc_type == '销售':
            self.driver.click_element("x,//*[@id='addRole_userForm']/div[2]/div/div/label[1]")
        elif acc_type == '代理商':
            self.driver.click_element("x,//*[@id='addRole_userForm']/div[2]/div/div/label[2]")
        elif acc_type == '用户':
            self.driver.click_element('x,//*[@id="addRole_userForm"]/div[2]/div/div/label[3]')
        # 编辑客户名称
        self.driver.operate_input_element("nickName", acc_name)
        self.driver.wait(1)
        # 编辑登录账号
        self.driver.operate_input_element("account", account)
        self.driver.wait(1)
        # 编辑密码
        self.driver.operate_input_element("passWord", pwd)
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
        # 保存
        self.driver.click_element("c,layui-layer-btn0")
        self.driver.wait(1)

    # 快捷销售-新增客户--取消
    def add_cust_cancel(self):
        # 添加
        self.click_add()
        sleep(2)
        # 取消
        self.driver.click_element("c,layui-layer-ico")
        sleep(2)
        self.click_add()
        sleep(2)
        self.driver.click_element("c,layui-layer-ico")
        sleep(2)

    # 点击添加按钮
    def click_add(self):
        self.driver.switch_to_frame('x,//*[@id="fastSellFrame"]')
        self.driver.click_element("x,/html/body/div[1]/div/div/div/div[1]/div[1]/div[2]/button")
        self.driver.default_frame()

    # 添加账号--搜索用户
    def add_account_search_user(self, user):
        # 将滚动条滚动至搜索输入框处
        self.switch_to_add_account_in_new_center()
        # 输入账号搜索
        self.driver.operate_input_element('x,//*[@id="treeDemo2_cusTreeKey"]', user)
        self.driver.click_element('x,//*[@id="treeDemo2_cusTreeSearchBtn"]')
        sleep(3)
        self.driver.click_element("c,autocompleter")
        sleep(2)
        self.driver.default_frame()

    def switch_to_add_account_in_new_center(self):
        self.driver.switch_to_frame('x,/html/body/div[9]/div[2]/iframe')

    # 获取新增客户保存状态
    def get_add_save_status(self):
        status = self.driver.get_element("c,layui-layer-content").text
        return status

    # 右侧客户树查找客户
    def search_cust(self, keyword):
        # 客户名称/账号输入框内输入搜索关键词
        self.driver.operate_input_element("treeSubUser_search_input", keyword)
        # 搜索
        self.driver.click_element("treeSubUser_search_btn")
        self.driver.wait()
        # 选中查询结果
        self.driver.click_element("c,autocompleter-item")
        self.driver.wait(1)





        # 下级客户库存

    def get_current_account_all_equipment(self):
        # 获取当前用户下库存的设备
        return self.driver.get_text('stock')

    def get_actual_current_account_all_equipment(self):
        # 获取当前的用户库存总数
        a = self.driver.get_element('x,//*[@id="paging-dev"]').get_attribute("style")
        if a == 'display: none;':
            return 0
        else:
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_numbers("x,//*[@id='paging-dev']", "x,//*[@id='markDevTable']")
            return total

    def get_current_account_online_all_equipment(self):
        # 获取当前用户在线的设备总数
        return self.driver.get_text('x,//*[@id="onLine2"]')

    def get_actual_current_account_online_all_equipment(self):
        return self.driver.get_text('x,//*[@id="onlineCount"]')

    def get_current_account_total_equipment(self):
        return self.driver.get_text('x,//*[@id="repertory"]')

    def get_actual_text_after_click_alarm(self):
        return self.driver.get_text('x,//*[@id="safemenu"]/li[1]/a')

    def get_current_account_next(self):
        # 获取左侧列表的下级用户总数
        a = list(self.driver.get_elements('x,//*[@id="treeDemo_1_ul"]/li'))
        return len(a)

    def get_actual_current_account_next(self):
        a = self.driver.get_element('x,//*[@id="pagingCustomer"]').get_attribute("style")
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_number('x,//*[@id="pagingCustomer"]', 'x,//*[@id="customerlist"]')
            return total
        else:
            return 0

    def get_actual_text_after_click_command(self):
        return self.driver.get_text('x,/html/body/div[1]/div[6]/div/div/div[2]/div[5]/div[1]/div/b')

    def get_actual_text_after_click_set_up_landmark(self):
        return self.driver.get_text('x,//*[@id="marktab"]')

    def get_actual_text_after_click_alarms(self):
        self.driver.switch_to_frame('x,//*[@id="alarmDdetailsFrame"]')
        a = self.driver.get_text('x,/html/body/div[1]/div[1]/div/b')
        self.driver.default_frame()
        return a

    def get_current_account_total_online(self):
        return self.driver.get_text('x,//*[@id="onLine2"]')

    def get_actual_total_online(self):
        # 获取总共的在线数
        first_total = len(list(self.driver.get_elements('x,//*[@id="treeDemo_1_ul"]/li')))
        print(first_total)
        total = []
        for n in range(first_total):
            try:
                self.driver.click_element('x,//*[@id="treeDemo_%s"]/span' % str(n + 2))
                sleep(2)
                second_total = len(list(self.driver.get_elements('x,//*[@id="treeDemo_%s"]/ul/li' % str(n + 2))))
                total.append(second_total)
            except:
                continue
        print(total)
        totals = sum(total) + first_total
        print(totals)
        number = []
        for n2 in range(totals):
            sleep(2)
            self.driver.click_element('x,//*[@id="treeDemo_%s_span"]' % str(n2 + 2))
            num = int(self.driver.get_text('x,//*[@id="onlineCount"]'))
            number.append(num)

        numbers = sum(number) + int(self.driver.get_text('x,//*[@id="onlineCount"]'))
        return numbers

    def get_actual_text_after_click_overtime(self):
        return self.driver.get_text('x,//*[@id="overdueType"]/div/span[1]/div/span[2]')

    def get_actual_total_actved(self):
        return self.driver.get_text('x,//*[@id="activated"]')

    def get_total_all_actived_equipment(self):
        self.driver.click_element(
            'x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[4]/label/div/ins')

        self.driver.click_element(
            'x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[5]/div/div/button')
        sleep(1)
        self.driver.click_element(
            'x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[6]/div[4]/div/div/span[2]')
        sleep(2)
        self.driver.click_element(
            'x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[6]/div[4]/div/div/div/ul/li[2]')

        self.driver.click_element(
            'x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[5]/div/button')
        sleep(3)
        new_paging = NewPaging(self.driver, self.base_url)
        return new_paging.get_total_number('x,//*[@id="paging-dev"]', 'x,//*[@id="markDevTable"]')

    def get_actual_total_inactve(self):
        return self.driver.get_text('x,//*[@id="notActive"]')

    def get_total_all_inactive_equipment(self):
        self.driver.click_element(
            'x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[4]/label/div/ins')

        self.driver.click_element(
            'x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[5]/div/div/button')

        self.driver.click_element(
            'x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[6]/div[4]/div/div/span[2]')
        sleep(2)
        self.driver.click_element(
            'x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[6]/div[4]/div/div/div/ul/li[3]')

        self.driver.click_element(
            'x,/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[5]/div/button')
        sleep(6)
        new_paging = NewPaging(self.driver, self.base_url)
        return new_paging.get_total_number('x,//*[@id="paging-dev"]', 'x,//*[@id="markDevTable"]')

    def get_actual_total_attention(self):
        return self.driver.get_text('x,//*[@id="followNum"]')

    def get_total_all_attention_equipment(self):
        return self.driver.get_text('x,//*[@id="followTotal"]')

    def get_total_dev_number_after_ckick_all_dev_number(self):
        # 获取点击总进货数后，库存数量
        a = self.driver.get_element('x,//*[@id="paging-dev"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_numbers('x,//*[@id="paging-dev"]', 'x,//*[@id="markDevTable"]')
            return total
        elif a == 'display: none;':
            return 0

    def click_report_after_text(self):
        return self.driver.get_text('x,/html/body/div[1]/div[6]/div/div/div[1]/div/div[1]/div')

    def click_safearea_get_vaule(self):
        return self.driver.get_element('x,//*[@id="safemenu"]/li[1]').get_attribute('class')

    def click_dev_manage_get_text(self):
        # return self.driver.get_text('x,//*[@id="allDev"]/div[1]/div/b')
        return self.driver.get_text("x,//*[@id='lowerFlag']")

    def get_coming_overtime_number(self):
        return self.driver.get_text('soonExpiration')

    def click_coming_overtime_get_text(self):
        return self.driver.get_text('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[1]/div/div/span[2]')

    def get_overtime_number(self):
        return self.driver.get_text('x,//*[@id="expiration"]')

    def click_clear_all_button(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[5]/button')
        sleep(2)

    def get_lower_input_value(self):
        return self.driver.get_element('x,//*[@id="lowerFlag"]/div/input').is_selected()

    def click_search_button(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[5]/div/button')
        sleep(2)

    def click_active_get_text(self):
        return self.driver.get_text('x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[2]/div/div/span[2]')

    # 快捷销售--点击添加按钮
    def click_add_button(self):
        self.driver.click_element('x,/html/body/div[1]/div/div/div/div[1]/div[1]/div[2]/button')
        self.driver.wait(1)

    # 快捷销售-新增客户--异常提示
    def get_add_user_exception_prompt(self, add_data):
        # 编辑客户名称、登录账号、密码、确认密码、电话、邮箱、联系人、公司名称
        self.driver.operate_input_element("nickName", add_data["name"])
        self.driver.operate_input_element("account", add_data["account"])
        self.driver.operate_input_element("passWord", add_data["password"])
        self.driver.operate_input_element("pswAgain", add_data["confirm_pwd"])
        self.driver.operate_input_element("email", add_data["email"])
        # 保存
        self.driver.click_element('c,layui-layer-btn0')
        self.driver.wait()

        # 取已存在账号的提示
        # try:
        # text = self.driver.get_element("c,layui-layer-content").text
        # except:
        # text = ""
        # 客户名称--错误提示
        name_prompt2 = self.get_prompt("x,//*[@id='addRole_userForm']/div[3]/div/label")
        account_prompt2 = self.get_prompt("x,//*[@id='addRole_userForm']/div[4]/div/label")
        pwd_prompt2 = self.get_prompt("x,//*[@id='markPassword']/div[1]/div/label")
        pwd2_prompt2 = self.get_prompt("x,//*[@id='markPswAgain']/div/label")
        email_prompt2 = self.get_prompt("x,//*[@id='addRole_userForm']/div[7]/div/label")

        all_prompt = {
            "name_prompt2": name_prompt2,
            "account_prompt2": account_prompt2,
            "pwd_prompt2": pwd_prompt2,
            "pwd2_prompt2": pwd2_prompt2,
            "email_prompt2": email_prompt2,

        }
        print(all_prompt)
        return all_prompt

    # 快速销售（新增客户）--取消
    def click_add_cancel_button(self):
        self.driver.click_element('c,layui-layer-btn1')

    # 账户详情---取提示语
    def get_prompt(self, select):
        try:
            prompt = self.driver.get_text(select)
            return prompt
        except:
            prompt = ""
            return prompt

    # 快速销售（新增客户）--获取长度
    def get_add_user_element_len(self):
        name_len = int(self.driver.get_element("nickName").get_attribute("maxlength"))
        account_len = int(self.driver.get_element("account").get_attribute("maxlength"))
        phone_len = int(self.driver.get_element("phone").get_attribute("maxlength"))
        email_len = int(self.driver.get_element("email").get_attribute("maxlength"))
        contact_len = int(self.driver.get_element("contact").get_attribute("maxlength"))
        companyName_len = int(self.driver.get_element("companyName").get_attribute("maxlength"))
        all_len = {
            "name_len": name_len,
            "account_len": account_len,
            "phone_len": phone_len,
            "email_len": email_len,
            "contact_len": contact_len,
            "companyName_len": companyName_len,
        }
        print(all_len)
        return all_len

    def click_more_in_dev_manage(self):
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[5]/div/div/button')
        sleep(2)

    # 账户中心iframe
    def account_center_iframe(self):
        self.driver.switch_to_frame('x,//*[@id="usercenterFrame"]')

    # 获取app账号的服务商个数
    def get_current_account_service_number(self):
        count = len(self.driver.get_elements("x,//div[@class='media-body']/ul"))
        print("服务商个数", count)
        return count

    # 转移设备
    def shift_facility(self, add_info, search_info):
        # 进入设备管理页面
        self.driver.click_element('x,//*[@id="device"]/a')
        sleep(2)
        self.driver.operate_input_element('deviceManage_cusTreeKey', add_info['account'])
        # 搜索
        self.driver.click_element('deviceManage_cusTreeSearchBtn')
        self.driver.wait()
        # 选中查询结果
        self.driver.click_element("c,autocompleter-item")
        self.driver.wait(1)

        self.driver.operate_input_element('x,//*[@id="searchIMEI"]', search_info['device_imei'])
        self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[5]/div/button')
        sleep(3)
        # 点击转移
        self.driver.click_element('x,//*[@id="markDevTable"]/tr/td[12]/a[2]')
        sleep(2)
        # 转个当前登录账号
        self.driver.click_element("treeDemo_device_sale_id_1_a")
        self.driver.click_element("x,//*[@id='device_sale_id']/div[3]/div[2]/button[3]")

    # 点击账户详情
    def click_account_details(self):
        self.driver.click_element("x,//*[@id='usercenter']/a")
        sleep(2)

    # 获取记住默认参数选项文本
    def get_memorization_default_options_text(self):
        self.driver.switch_to_frame('x,//*[@id="usercenterFrame"]')
        text = self.driver.get_text("x,/html/body/div/div/div[1]/label")
        self.driver.default_frame()
        return text

    # 点击设备型号设置
    def click_facility_Model_number_setting(self):
        self.driver.click_element("devicetype")
        sleep(2)

    # 点击设备型号设置
    def get_facility_Model_number_setting_title(self):
        self.driver.switch_to_frame("x,//*[@id='devicetypeFrame']")
        title = self.driver.get_text("x,/html/body/div/div[1]/div/b")
        self.driver.default_frame()
        return title

    # 点击设置记住默认选项
    def click_memorization_default_option(self):
        self.driver.click_element("x,/html/body/div/div/div[1]/label")
        sleep(1)

    # 选择进入的页面
    def select_overview_or_sell_page(self, page):
        if page == "账户总览":
            self.click_account_pandect()
        elif page == "快速销售":
            self.fast_sales()
        else:
            print("不选择记住默认选项功能")

    # 获取记住默认选项--状态
    def get_memorization_default_option_state(self):
        # 点账户中心
        self.driver.click_element("zSales")
        overview_state = self.driver.get_element("indexView").is_selected()
        sleep(2)
        self.driver.click_element("eSales")
        sell_state = self.driver.get_element("indexView").is_selected()
        state = {
            "overview_state": overview_state,
            "sell_state": sell_state
        }
        return state

    # 账户总览--获取下载app提示
    def get_download_app_hint(self):
        self.driver.switch_to_frame('x,//*[@id="usercenterFrame"]')
        text = self.driver.get_text("x,/html/body/div/div/div[2]/div[1]/div/div[3]/div/div[3]/div/span")
        self.driver.default_frame()
        return text

    # 快速销售--字体“快速销售”
    def get_fast_sale_typeface(self):
        self.driver.switch_to_frame('x,//*[@id="usercenterFrame"]')
        text = self.driver.get_text("x,/html/body/div/div/div[2]/div[2]/div[1]/div/div[1]/b")
        self.driver.default_frame()
        return text

    # 快捷销售-追加设备--编辑设备信息
    def edit_list_add_equipment(self, old_name, new_name, sim):
        self.account_center_iframe()
        count = len(self.driver.get_elements("x,//*[@id='succList']/tr"))
        for i in range(count):
            # 定位设备
            if new_name != "":
                self.driver.operate_input_element("x,/html/body/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/"
                                                  "div/div[2]/table/tr[" + str(i + 1) + "]/td[2]/input",
                                                  old_name[i] + new_name)
            else:
                self.driver.operate_input_element("x,/html/body/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/"
                                                  "div/div[2]/table/tr[" + str(i + 1) + "]/td[2]/input", new_name)

            sleep(1)
            # sim
            self.driver.operate_input_element("x,/html/body/div/div/div[2]/div[2]/div[1]/div/div[2]/"
                                              "div[2]/div/div[2]/table/tr[" + str(i + 1) + "]/td[3]/input", sim)
            sleep(1)
        self.driver.default_frame()

    # 获取列表设备名称和sim
    def get_list_add_equipment_user_and_sim(self):
        imei_list = []
        name_list = []
        sim_list = []
        self.account_center_iframe()
        count = len(self.driver.get_elements("x,//*[@id='succList']/tr"))
        print(count)
        for i in range(count):
            imei = self.driver.get_text("x,/html/body/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/"
                                        "div[2]/table/tr[" + str(i + 1) + "]/td[1]")
            imei_list.append(imei)

            # 定位设备
            name = self.driver.get_element("x,/html/body/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/"
                                           "div/div[2]/table/tr[" + str(i + 1) + "]/td[2]/input").get_attribute("value")
            name_list.append(name)
            # sim
            sim = self.driver.get_element("x,/html/body/div/div/div[2]/div[2]/div[1]/div/div[2]/"
                                          "div[2]/div/div[2]/table/tr[" + str(i + 1) + "]/td[3]/input").get_attribute(
                "value")
            sim_list.append(sim)

        info = {
            "imei": imei_list,
            "name": name_list,
            "sim": sim_list
        }
        print("原数据", info)
        self.driver.default_frame()
        return info

    # 设备管理--获取编辑设备的名称和sim
    def get_dev_manage_equipment_user_and_sim(self, imei_list):
        # 进入设备管理页面
        self.driver.click_element('x,//*[@id="device"]/a')
        sleep(3)
        self.driver.click_element("searchIMEI")
        self.driver.clear("searchIMEI")
        # 查询IMEI
        for imei in imei_list:
            add_sim = self.driver.get_element("searchIMEI")
            self.driver.input_sim('searchIMEI', imei)
            add_sim.send_keys(Keys.ENTER)
        sleep(2)
        # 点击包含下级
        self.driver.click_element("lowerFlag")
        self.driver.click_element("x,//*[@id='allDev']/div[2]/div[1]/div/div[5]/div/button")
        sleep(4)

        # 获取查询设备数据
        name_list = []
        imei_list = []
        sim_list = []
        count = len(self.driver.get_elements("x,//*[@id='markDevTable']/tr"))
        for i in range(count):
            i = i + 1
            name = self.driver.get_text("x,//*[@id='markDevTable']/tr[" + str(i) + "]/td[2]")
            imei = self.driver.get_text("x,//*[@id='markDevTable']/tr[" + str(i) + "]/td[3]")
            sim = self.driver.get_text("x,//*[@id='markDevTable']/tr[" + str(i) + "]/td[6]")
            name_list.append(name)
            imei_list.append(imei)
            sim_list.append(sim)
        data = {
            "dev_name": name_list,
            "dev_imei": imei_list,
            "dev_sim": sim_list

        }
        print("设备管理", data)
        return data

    # 设备管理--编辑
    def dev_manage_edit_equipment_user_and_sim(self, name, sim):
        count = len(self.driver.get_elements("x,//*[@id='markDevTable']/tr"))

        for i in range(count):
            # 点击编辑
            self.driver.click_element("x,//*[@id='markDevTable']/tr[" + str(i + 1) + "]/td[12]/a[1]")
            sleep(5)
            # 修改设备名称、sim卡号
            self.driver.switch_to_iframe("x,/html/body/div[" + str(32 + i) + "]/div[2]/iframe")
            self.driver.operate_input_element("x,//*[@id='device_info_a']/fieldset[1]/div[2]/div[1]/input", name)
            self.driver.operate_input_element("x,//*[@id='device_info_a']/fieldset[1]/div[2]/div[2]/input", sim)
            sleep(2)
            self.driver.default_frame()
            self.driver.click_element("c,layui-layer-btn0")
            sleep(2)

    # 获取设备名称的元素长度
    def get_fast_sale_dev_name_len(self):
        self.account_center_iframe()
        user_len = int(self.driver.get_element("x,/html/body/div/div/div[2]/div[2]/div[1]/div/div[2]/"
                                               "div[2]/div/div[2]/table/tr/td[2]/input").get_attribute("maxlength"))
        self.driver.default_frame()
        return user_len

    # 获取设备SIM卡号的元素长度
    def get_fast_sale_dev_sim_len(self):
        self.account_center_iframe()
        sim_len = int(self.driver.get_element("x,/html/body/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/"
                                              "div/div[2]/table/tr/td[3]/input").get_attribute("maxlength"))
        self.driver.default_frame()
        return sim_len

    # 销售销售--获取用户到期文本
    def get_account_expired_time_text(self):
        text = self.driver.get_text("x,/html/body/div[1]/div/div/div/div[3]/span/div/span[2]")
        return text

    # 快速销售--获取客户类型列表
    def get_fast_sale_acc_user_type_list(self):

        # type_list_len = len(self.driver.get_elements("x,/html/body/div/div/form/div[2]/div/div"))
        self.switch_to_add_account_in_new_center()
        type_list_len = len(self.driver.get_elements("x,//*[@id='addRole_userForm']/div[2]/div/div/label"))
        print(type_list_len)
        display_type_list = []

        for i in range(type_list_len):
            # 获取style状态
            state = self.driver.get_element(
                "x,/html/body/div[1]/div[8]/div[2]/div/div/form/div[2]/div/div/label[" + str(
                    i + 1) + "]").get_attribute('style')
            if state == "display: none;":
                continue
            else:
                display_type_list.append(i)
        display_type_len = len(display_type_list)
        if display_type_len == 2:
            distributor = self.driver.get_text("x,//*[@id='labelSale']")
            user = self.driver.get_text("x,//*[@id='labelDistributor']")
            type_data = {
                "distributor": distributor,
                "user": user,
                "length": display_type_len
            }
            print("222", type_data)

            return type_data
        elif display_type_len == 1:
            user = self.driver.get_text("x,//*[@id='labelDistributor']")
            type_data = {"user": user,
                         "length": display_type_len,

                         }
            print("1111", type_data)

            return type_data

        else:
            sale = self.driver.get_text('x,//*[@id="labelSale"]')
            distributor = self.driver.get_text("x,//*[@id='labelDistributor']")
            user = self.driver.get_text("x,//*[@id='labelUser1']")

            type_data = {"sale": sale,
                         "distributor": distributor,
                         "user": user,
                         "length": display_type_len

                         }
            print("333", type_data)
            return type_data
