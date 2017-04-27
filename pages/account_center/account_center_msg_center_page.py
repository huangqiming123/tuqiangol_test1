from automate_driver.automate_driver import AutomateDriver
from pages.base.base_page import BasePage

# 账户中心页面-消息中心的元素及操作
# author:孙燕妮
from pages.base.new_paging import NewPaging


class AccountCenterMsgCenterPage(BasePage):
    def __init__(self, driver: AutomateDriver, base_url):
        super().__init__(driver, base_url)

        self.base_page = BasePage(self.driver, self.base_url)

    # 点击进入“消息中心”
    def enter_msg_center(self):
        self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[1]/div/div[2]/ul/li[2]/a")
        self.driver.wait(1)

    # 获取“消息中心”title
    def get_msg_center_title(self):
        msg_center_title = self.driver.get_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[1]/div/b").text
        return msg_center_title

    # 获取左侧栏目-消息中心-x条未读
    def get_unread_msg_num(self):
        unread_msg_num = self.driver.get_element("unReadTotal").text
        return unread_msg_num

    # 设置搜索项-消息状态-未读
    def set_search_status_unread(self):
        # 点击状态下拉框
        self.driver.click_element(
            "x,/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/form/div[2]/span[2]/div/span[2]")
        self.driver.wait(1)
        # 选中未读
        self.driver.click_element(
            "x,/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/form/div[2]/span[2]/div/div/ul/li[2]")
        self.driver.wait(1)
        # 点击搜索
        self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/form/div[2]/button")
        self.driver.wait()

    # 设置搜索项-消息状态-已读
    def set_search_status_read(self):
        # 点击状态下拉框
        self.driver.click_element(
            "x,/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/form/div[2]/span[2]/div/span[2]")
        self.driver.wait(1)
        # 选中已读
        self.driver.click_element(
            "x,/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/form/div[2]/span[2]/div/div/ul/li[3]")
        self.driver.wait(1)

    # 设置搜索项-消息类型
    def set_search_type(self, type):
        # 点击消息类型下拉框
        self.driver.click_element(
            "x,/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/form/div[2]/span[1]/div/span[2]")
        self.driver.wait(1)
        # 选择消息类型
        if type == '设备到期':
            self.driver.click_element(
                "x,/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/form/div[2]/span[1]/div/div/ul/li[3]")
            self.driver.wait(1)
        elif type == '设备离线':
            self.driver.click_element(
                "x,/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/form/div[2]/span[1]/div/div/ul/li[2]")
            self.driver.wait(1)

    # 设置搜索项-输入设备imei
    def set_search_imei(self, imei):
        self.driver.operate_input_element("remainSearchDeviceInput", imei)
        self.driver.wait(1)

    # 点击搜索
    def click_search(self):
        self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/form/div[2]/button")
        self.driver.wait()

    # 点击“序号”将当前页列表消息全选
    def select_current_page_all_msg(self):
        self.driver.click_element("x,//*[@id='noticeTableHeader']/thead/tr/th[1]/label/div/ins")

    # 获取当前页所有消息的复选框
    def get_current_page_all_msg_checkbox(self):
        select_msg = list(self.driver.get_elements("c,iCheck-helper"))
        return select_msg

    # 点击“标为已读”
    def set_current_page_status_read(self):
        self.driver.click_element(
            "x,/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/form/div[1]/button[1]")
        self.driver.wait()

    # 点击“全部标为已读”
    def set_all_msg_status_read(self):
        self.driver.click_element(
            "x,/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/form/div[1]/button[2]")
        self.driver.wait()

    # 获取操作状态文本内容
    def get_status_text(self):
        status_text = self.driver.get_element("c,layui-layer-content").text
        return status_text

    # 设置消息列表底部每页共x条
    def select_per_page_number(self, number):
        self.base_page.select_per_page_number(number)

    # 获取消息列表共分几页
    def get_total_pages_num(self):
        total_pages_num = self.base_page.get_total_pages_num("x,//*[@id='msg_paging']")
        return total_pages_num

    # 获取业务日志最后一页有几条记录
    def last_page_logs_num(self):
        last_page_logs_num = self.base_page.last_page_logs_num("x,//*[@id='msg_tbody']", "x,//*[@id='msg_paging']")
        return last_page_logs_num

    # 获取消息列表为空时的文本内容
    def get_no_msg_text(self):
        no_msg_text = self.driver.get_element("x,//*[@id='msg_nodata']/div").text
        return no_msg_text

    def get_total_unread_logs_num(self):
        # 获取所有的未读消息
        new_paging = NewPaging(self.driver, self.base_url)
        try:
            total = new_paging.get_total_number("x,//*[@id='msg_paging']", "x,//*[@id='msg_tbody']")
            return total
        except:
            return 0
