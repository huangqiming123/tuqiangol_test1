from time import sleep

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

    # 账户总览页面跳转

    def account_overview(self, link_name):

        if link_name == '库存':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/"
                                      "div[1]/div/div[1]/div/div[1]/a/i")
            self.driver.wait(1)
        elif link_name == '总进货数':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/"
                                      "div[1]/div/div[1]/div/div[2]/a")
            self.driver.wait(1)
        elif link_name == '在线':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/"
                                      "div[1]/div/div[1]/div/div[3]/a/i")
            self.driver.wait(1)
        elif link_name == '离线':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/"
                                      "div[1]/div/div[1]/div/div[4]/a")
            self.driver.wait(1)
        elif link_name == '即将到期':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/"
                                      "div[1]/div/div[1]/div/div[5]/a")
            self.driver.wait(1)
        elif link_name == '已过期':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/"
                                      "div[1]/div/div[1]/div/div[6]/a")
            self.driver.wait(1)
        elif link_name == '已激活':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/"
                                      "div[1]/div/div[1]/div/div[7]/a")
            self.driver.wait(1)
        elif link_name == '未激活':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/"
                                      "div[1]/div/div[1]/div/div[8]/a")
            self.driver.wait(1)
        elif link_name == '告警车辆':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/"
                                      "div[1]/div/div[1]/div/div[9]/a")
            self.driver.wait(1)
        elif link_name == '重点关注车辆':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/"
                                      "div[1]/div/div[1]/div/div[10]/a")
            self.driver.wait(1)
        elif link_name == '控制台':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/"
                                      "div[1]/div/div[2]/div/div[1]/a")
            self.driver.wait(1)
        elif link_name == '统计报表':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/"
                                      "div[1]/div/div[2]/div/div[2]/a")
            self.driver.wait(1)
        elif link_name == '围栏':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/"
                                      "div[1]/div/div[2]/div/div[3]/a")
            self.driver.wait(1)
        elif link_name == '下级客户管理':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/"
                                      "div[1]/div/div[2]/div/div[4]/a")
            self.driver.wait(1)
        elif link_name == '设备管理':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/"
                                      "div[1]/div/div[2]/div/div[5]/a")
            self.driver.wait(1)
        elif link_name == '指令管理':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/"
                                      "div[1]/div/div[2]/div/div[6]/a")
            self.driver.wait(1)
        elif link_name == '地标设置':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/"
                                      "div[1]/div/div[2]/div/div[7]/a")
            self.driver.wait(1)
        elif link_name == '告警':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/"
                                      "div[1]/div/div[2]/div/div[8]/a")
            self.driver.wait(1)

    # 快捷销售
    def fast_sales(self):
        self.driver.click_element("x,//*[@id='eSales']/a")

    # 快捷销售-账户查找
    def fast_sales_find_account(self, search_account):
        # 点击“销售给”下拉箭头图标
        self.driver.click_element("showTree-btn")
        # 下拉搜索框内输入精确的用户名/账号
        self.driver.operate_input_element("ac_putDevice_globalSearch_SalesName", search_account)
        # 点击搜索按钮
        self.driver.click_element("ac_putDevice_globalSearch_btn")
        self.driver.wait(1)
        # 点击搜索结果列表中唯一的账户
        self.driver.click_element("c,autocompleter-item")
        self.driver.wait(1)

    '''# 已选中账户后获取账户框内显示的账户名文本内容
    def get_selected_account(self):
        selected_account_text = self.driver.get_element("x,//*[@id='autocompleter-1']/div").text
        return selected_account_text'''

    # 快捷销售-设备查找、添加
    def fast_sales_find_and_add_device(self, device_imei):
        # 在“追加设备”框内输入账号下存在的设备imei号（一个/多个）
        self.driver.operate_input_element("searchIMEI", device_imei)
        imei_count = self.get_device_imei_count()
        # 点击“添加”按钮
        self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/"
                                  "div/div[2]/div[1]/div[2]/div/div/div/div[3]/button[1]")
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
        self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/"
                                  "div/div[2]/div[1]/div[2]/div/div/div/div[3]/button[2]")

    # 快捷销售-设备列表-删除
    def delete_list_device(self):
        self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/"
                                  "div/div[2]/div[2]/div/div[2]/table/tr/td[4]/a")

    # 快捷销售-设备查找-获取imei计数
    def get_device_imei_count(self):
        dev_num = self.driver.get_element("ac_dev_num").text
        return dev_num

    # 快捷销售-设备查找-获取已选设备个数
    def get_selected_device_num(self):
        dev_num = self.driver.get_element("selectedCount").text
        return dev_num

    # 快捷销售-选择用户到期时间
    def choose_account_expired_time(self, account_expired_time):
        self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/div[2]"
                                  "/div[1]/div/div[2]/div[3]/span/div/span[2]")
        self.driver.wait(1)
        if account_expired_time == '一个月':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]"
                                      "/div/div[2]/div[3]/span/div/div/ul/li[2]")
        elif account_expired_time == '两个月':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]"
                                      "/div/div[2]/div[3]/span/div/div/ul/li[3]")
        elif account_expired_time == '三个月':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]"
                                      "/div/div[2]/div[3]/span/div/div/ul/li[4]")
        elif account_expired_time == '半年':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]"
                                      "/div/div[2]/div[3]/span/div/div/ul/li[5]")
        elif account_expired_time == '一年':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]"
                                      "/div/div[2]/div[3]/span/div/div/ul/li[6]")
        elif account_expired_time == '不限制':
            self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]"
                                      "/div/div[2]/div[3]/span/div/div/ul/li[7]")

    # 快捷销售-销售按钮
    def sale_button(self):
        self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div"
                                  "/div[2]/div[3]/button[3]")

    # 获取销售成功操作状态弹框的文本内容
    def get_sale_status(self):
        sale_status_text = self.driver.get_element("c,layui-layer-content").text
        return sale_status_text

    # 快捷销售-重置
    def reset_device(self):
        self.driver.click_element("resetDevice")

    # 快捷销售-新增客户
    def add_cust(self, acc_type, acc_name, account, pwd, phone, email, conn, com):
        # 点击新增客户
        self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div/"
                                  "div[2]/div[1]/div[1]/div[2]/button")
        self.driver.wait(1)
        sleep(2)

        # 选择客户类型
        if acc_type == '销售':
            self.driver.click_element("x,/html/body/div[4]/div/div/div[2]/div/form/div[2]/div/div/label[1]/div/ins")
        elif acc_type == '代理商':
            self.driver.click_element("x,/html/body/div[4]/div/div/div[2]/div/form/div[2]/div/div/label[2]/div/ins")
        elif acc_type == '用户':
            self.driver.click_element('x,/html/body/div[4]/div/div/div[2]/div/form/div[2]/div/div/label[2]/div/ins')
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
        self.driver.click_element("addUserBtn")
        self.driver.wait(1)

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
        return self.driver.get_text('x,//*[@id="stock2"]')

    def get_actual_current_account_all_equipment(self):
        # 获取当前的用户库存总数
        a = self.driver.get_element('x,//*[@id="paging-dev"]').get_attribute("style")
        if a == 'display: none;':
            return 0
        else:
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_number("x,//*[@id='paging-dev']", "x,//*[@id='markDevTable']")
            return total

    def get_current_account_online_all_equipment(self):
        # 获取当前用户在线的设备总数
        return self.driver.get_text('x,//*[@id="onLine2"]')

    def get_actual_current_account_online_all_equipment(self):
        return self.driver.get_text('x,//*[@id="onlineCount"]')

    def get_current_account_total_equipment(self):
        return self.driver.get_text('x,//*[@id="repertory2"]')

    def get_actual_text_after_click_alarm(self):
        return self.driver.get_text('x,//*[@id="safemenu"]/li[1]/a')

    def get_current_account_next(self):
        # 获取左侧列表的下级用户总数
        a = list(self.driver.get_elements('x,//*[@id="treeDemo_1_ul"]/li'))
        return len(a)

    def get_actual_current_account_next(self):
        a = self.driver.get_element('x,//*[@id="pagingCustomer"]').get_attribute("style")
        if a == 'display: none;':
            return 0
        else:
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_number('x,//*[@id="pagingCustomer"]', 'x,//*[@id="markUserTable"]')
            return total

    def get_actual_text_after_click_command(self):
        return self.driver.get_text('x,/html/body/div[1]/div[4]/div/div/div[2]/div[5]/div[1]/div/b')

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
        return self.driver.get_text('x,//*[@id="active2"]')

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
        return self.driver.get_text('x,//*[@id="noActive2"]')

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
        return self.driver.get_text('x,//*[@id="attentions"]')
