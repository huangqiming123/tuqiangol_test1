from time import sleep

from automate_driver.automate_driver import AutomateDriver
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page import BasePage

# 账户中心页面-业务日志的元素及操作
# author:孙燕妮
from pages.base.base_page_server import BasePageServer
from pages.base.new_paging import NewPaging


class AccountCenterOperationLogPage(BasePageServer):
    def __init__(self, driver: AutomateDriverServer, base_url):
        super().__init__(driver, base_url)

        self.base_page = BasePage(self.driver, self.base_url)

    # 招呼栏业务日志
    def business_log(self):
        # 点击招呼栏的业务日志（默认列表为设备管理--分配）
        self.driver.click_element("x,/html/body/div[1]/header/div/div[3]/div/div[1]/a[2]")
        self.driver.wait(5)

    # 点击设备管理-修改
    def log_device_modify(self):
        self.driver.click_element("devDiv_modify_1")
        self.driver.wait(5)

    # 点击客户管理（默认-修改）
    def log_cust_modify(self):
        self.driver.switch_to_frame('x,//*[@id="servicelogReportFrame"]')
        self.driver.click_element('x,//*[@id="tab_nav_business"]/li[2]/a')
        sleep(2)
        self.driver.default_frame()

    # 点击客户管理-添加
    def log_cust_add(self):
        self.driver.click_element("x,//*[@id='custDiv']/button[2]")
        self.driver.wait(5)

    # 点击客户管理-删除
    def log_cust_delete(self):
        self.driver.click_element("x,//*[@id='custDiv']/button[3]")
        self.driver.wait(5)

    # 点击客户管理-修改密码
    def log_cust_modify_passwd(self):
        self.driver.click_element("x,//*[@id='custDiv']/button[4]")
        self.driver.wait(5)

    # 点击客户管理-重置密码
    def log_cust_reset_passwd(self):
        self.driver.click_element("x,//*[@id='custDiv']/button[5]")
        self.driver.wait(5)

    # 输入搜索条件来查询设备管理日志
    def search_device_log(self, search_info):
        # 点击结束时间
        self.driver.click_element("createTimeEnd_xf")
        # 选择时间
        self.driver.click_element("x,//*[@id='laydate_hms']/li[2]/input")
        # 选择20时
        self.driver.click_element("x,//*[@id='laydate_hmsno']/span[21]")
        # 点击确定
        self.driver.click_element("laydate_ok")
        # 输入操作人/目标账号/IMEI号
        self.driver.operate_input_element("selectUserName_xf", search_info)
        # 点击搜索按钮
        self.driver.click_element("search_xf")
        self.driver.wait(5)

    # 输入搜索条件来查询客户管理日志
    def search_cust_log(self, search_info):
        # 点击结束时间
        self.driver.click_element("createTimeEnd_fp")
        # 选择时间
        self.driver.click_element("x,//*[@id='laydate_hms']/li[2]/input")
        # 选择20时
        self.driver.click_element("x,//*[@id='laydate_hmsno']/span[21]")
        # 点击确定
        self.driver.click_element("laydate_ok")
        # 输入账号
        self.driver.operate_input_element("selectUserName_fp", search_info)
        # 点击搜索按钮
        self.driver.click_element("search_fp")
        self.driver.wait(5)

    # 点击登录日志
    def login_log(self):
        self.driver.click_element("x,//*[@id='loginLogs']/a")

    # 输入搜索条件来查询登录日志
    def search_login_log(self, account):
        # 输入搜索账号
        self.driver.operate_input_element("loginAccount_sport", account)
        # 点击结束时间
        self.driver.click_element("endTime_sport")
        # 选择时间
        self.driver.click_element("x,//*[@id='laydate_hms']/li[2]/input")
        # 选择20时
        self.driver.click_element("x,//*[@id='laydate_hmsno']/span[21]")
        # 点击确定
        self.driver.click_element("laydate_ok")
        # 点击搜索按钮
        self.driver.click_element("x,//*[@id='tab_con_command']/div/div[1]/form/div/div/span/button")
        self.driver.wait(5)

    # 获取当前的业务日志个数
    def count_curr_busi_log_num(self):
        self.driver.switch_to_frame('x,//*[@id="servicelogReportFrame"]')
        a = self.driver.get_element('x,//*[@id="paging_xf"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_totals_number('x,//*[@id="paging_xf"]', 'x,//*[@id="logslist_xf"]')
            self.driver.default_frame()
            return total
        elif a == 'display: none;':
            self.driver.default_frame()
            return 0

    # 获取当前的业务日志-客户管理日志个数
    def count_curr_busi_cust_log_num(self):
        # 设置列表底部每页共10条
        self.driver.switch_to_frame('x,//*[@id="servicelogReportFrame"]')
        a = self.driver.get_element('x,//*[@id="paging_fp"]').get_attribute('style')

        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_number('x,//*[@id="paging_fp"]', 'x,//*[@id="logslist_fp"]')
            self.driver.default_frame()
            return total
        elif a == 'display: none;':
            self.driver.default_frame()
            return 0

    # 获取当前的业务日志个数
    def count_curr_busi_log_num_span(self):
        # 设置列表底部每页共10条
        self.base_page.select_per_page_number(10)
        # 获取结果共分几页
        total_pages_num = self.base_page.get_actual_pages_number_span("x,//*[@id='paging_xf']")
        # 获取最后一页有几条记录
        last_page_num = self.base_page.last_page_logs_num_span("x,//*[@id='logslist_xf']", "x,//*[@id='paging_xf']")
        # 计算当前结果共几条
        count = self.base_page.total_num(total_pages_num, last_page_num)
        return count

    # 获取当前的业务日志-客户管理日志个数
    def count_curr_busi_cust_log_num_span(self):
        # 设置列表底部每页共10条
        self.base_page.select_per_page_number(10)
        # 获取结果共分几页
        total_pages_num = self.base_page.get_actual_pages_number_span("x,//*[@id='paging_fp']")
        print(total_pages_num)
        # 获取最后一页有几条记录
        last_page_num = self.base_page.last_page_logs_num_span("x,//*[@id='logslist_fp']", "x,//*[@id='paging_fp']")
        # 计算当前结果共几条
        count = self.base_page.total_num(total_pages_num, last_page_num)
        return count

    # 客户管理日志-点击回到第一页
    def click_cust_log_first_page(self):
        self.driver.click_element("x,//*[@id='paging_fp']/ul/li[2]")
        self.driver.wait(30)

    # 设备管理日志-点击回到第一页
    def click_dev_log_first_page(self):
        self.driver.click_element("x,//*[@id='paging_xf']/ul/li[2]")
        self.driver.wait(30)

    '''# 设置业务日志列表底部每页共x条
    def select_per_page_number(self,number):
        self.base_page.select_per_page_number(number)

    # 获取业务日志共分几页
    def get_total_pages_num(self,selector):
        total_pages_num = self.base_page.get_total_pages_num("x,//*[@id='paging_xf']")
        return total_pages_num

    # 获取业务日志最后一页有几条记录
    def last_page_logs_num(self,selector01,selector02):
        last_page_logs_num = self.base_page.last_page_logs_num("x,//*[@id='logslist_xf']",
                                                               "x,//*[@id='paging_xf']")
        return last_page_logs_num'''

    # 设置登录日志列表底部每页共x条
    def select_login_per_page_number(self, number):
        self.base_page.select_per_page_number(number)

    # 获取登录日志共分几页
    def get_total_login_pages_num(self):
        total_login_pages_num = self.base_page.get_total_pages_num("x,//*[@id='paging_login_log']")
        return total_login_pages_num

    # 获取登录日志最后一页有几条记录
    def last_login_page_logs_num(self):
        last_login_page_logs_num = self.base_page.last_page_logs_num("x,//*[@id='loginLog-tbody']",
                                                                     "x,//*[@id='paging_login_log']")
        return last_login_page_logs_num

    def get_log_in_log_total(self):
        # 获取登录日志的条数
        self.driver.switch_to_frame('x,//*[@id="loginReportFrame"]')
        a = self.driver.get_element('x,//*[@id="paging_login_log"]').get_attribute('style')

        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_totals_number('x,//*[@id="paging_login_log"]', 'x,//*[@id="loginLog-tbody"]')
            self.driver.default_frame()
            return total
        elif a == 'display: none;':
            self.driver.default_frame()
            return 0

    def add_data_to_search_equipment_manager_log(self, search_data):
        # 搜索设备管理日志
        self.driver.switch_to_frame('x,//*[@id="servicelogReportFrame"]')
        if search_data['type'] == '1':
            self.driver.click_element('x,//*[@id="devDiv_modify_1"]')

        # 填写开始时间，结束时间
        js = 'document.getElementById("createTimeStart_xf").removeAttribute("readonly")'
        self.driver.execute_js(js)
        self.driver.operate_input_element('x,//*[@id="createTimeStart_xf"]', search_data['begin_time'])

        js = 'document.getElementById("createTimeEnd_xf").removeAttribute("readonly")'
        self.driver.execute_js(js)
        self.driver.operate_input_element('x,//*[@id="createTimeEnd_xf"]', search_data['end_time'])

        # 填写其他的搜索条件
        self.driver.operate_input_element('x,//*[@id="selectUserName_xf"]', search_data['more'])

        self.driver.click_element('x,//*[@id="search_xf"]')
        sleep(15)
        self.driver.default_frame()

    def add_data_to_search_cus_manager_log(self, search_data):
        self.driver.switch_to_frame('x,//*[@id="servicelogReportFrame"]')
        if search_data['type'] == '0':
            # 添加
            self.driver.click_element('x,//*[@id="custDiv"]/button[2]')
        elif search_data['type'] == '1':
            self.driver.click_element('x,//*[@id="custDiv"]/button[1]')

        elif search_data['type'] == '2':
            self.driver.click_element('x,//*[@id="custDiv"]/button[3]')

        elif search_data['type'] == '3':
            self.driver.click_element('x,//*[@id="custDiv"]/button[4]')

        elif search_data['type'] == '4':
            self.driver.click_element('x,//*[@id="custDiv"]/button[5]')
        sleep(5)

        # 填写开始时间，结束时间
        js = 'document.getElementById("createTimeStart_fp").removeAttribute("readonly")'
        self.driver.execute_js(js)
        self.driver.operate_input_element('x,//*[@id="createTimeStart_fp"]', search_data['begin_time'])

        js = 'document.getElementById("createTimeEnd_fp").removeAttribute("readonly")'
        self.driver.execute_js(js)
        self.driver.operate_input_element('x,//*[@id="createTimeEnd_fp"]', search_data['end_time'])

        # 填写其他的搜索条件
        self.driver.operate_input_element('x,//*[@id="selectUserName_fp"]', search_data['more'])

        self.driver.click_element('x,//*[@id="search_fp"]')
        sleep(10)
        self.driver.default_frame()

    def add_data_to_search_log_in_log(self, search_data):
        self.driver.switch_to_frame('x,//*[@id="loginReportFrame"]')
        self.driver.operate_input_element('x,//*[@id="loginAccount_sport"]', search_data['account'])
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="startTime_sport"]', search_data['begin_time'])
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="endTime_sport"]', search_data['end_time'])
        sleep(1)
        self.driver.click_element('x,/html/body/div/div/div[2]/div/div[1]/form/div/div/span/button')
        sleep(10)
        self.driver.default_frame()

    def add_data_to_search_massages(self, search_data):
        # 搜索消息
        self.driver.operate_input_element('x,//*[@id="remainSearchDeviceInput"]', search_data['imei'])

        self.driver.click_element(
            'x,/html/body/div/div[2]/div[1]/form/div[2]/span[1]/div/span[2]')
        sleep(1)
        if search_data['type'] == '':
            self.driver.click_element(
                'x,/html/body/div/div[2]/div[1]/form/div[2]/span[1]/div/div/ul/li[1]')
        elif search_data['type'] == '1':
            self.driver.click_element(
                'x,/html/body/div/div[2]/div[1]/form/div[2]/span[1]/div/div/ul/li[3]')
        elif search_data['type'] == '2':
            self.driver.click_element(
                'x,/html/body/div/div[2]/div[1]/form/div[2]/span[1]/div/div/ul/li[2]')
        elif search_data["type"] == '3':
            self.driver.click_element(
                'x,/html/body/div/div[2]/div[1]/form/div[2]/span[1]/div/div/ul/li[4]')
        elif search_data["type"] == '4':
            self.driver.click_element(
                'x,/html/body/div/div[2]/div[1]/form/div[2]/span[1]/div/div/ul/li[5]')    

        self.driver.click_element(
            'x,/html/body/div/div[2]/div[1]/form/div[2]/span[2]/div/span[2]')
        sleep(1)
        if search_data['status'] == '':
            self.driver.click_element(
                # 'x,/html/body/div[1]/div[5]/div/div/div[2]/div[2]/div[2]/div[1]/form/div[2]/span[2]/div/div/ul/li[1]')
                'x,/html/body/div/div[2]/div[1]/form/div[2]/span[2]/div/div/ul/li[1]')
        elif search_data['status'] == '0':
            self.driver.click_element(
                'x,/html/body/div/div[2]/div[1]/form/div[2]/span[2]/div/div/ul/li[2]')
        elif search_data['status'] == '1':
            self.driver.click_element(
                'x,/html/body/div/div[2]/div[1]/form/div[2]/span[2]/div/div/ul/li[3]')

        self.driver.click_element('x,/html/body/div/div[2]/div[1]/form/div[2]/button')
        sleep(10)

    def get_msg_number(self):
        a = self.driver.get_element('x,//*[@id="msg_paging"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_number('x,//*[@id="msg_paging"]', 'x,//*[@id="msg_tbody"]')
            return total
        elif a == 'display: none;':
            return 0

    def click_help_button(self):
        self.driver.click_element('x,/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a[2]')
        sleep(2)

    def click_business_log(self):
        self.driver.click_element('x,//*[@id="servicelogReport"]/a')
        sleep(2)

    def click_log_in_log(self):
        self.driver.click_element('x,//*[@id="loginReport"]/a')
        sleep(2)
