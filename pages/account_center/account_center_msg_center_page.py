from time import sleep

from automate_driver.automate_driver import AutomateDriver
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page import BasePage

# 账户中心页面-消息中心的元素及操作
# author:孙燕妮
from pages.base.base_page_server import BasePageServer
from pages.base.new_paging import NewPaging


class AccountCenterMsgCenterPage(BasePageServer):
    def __init__(self, driver: AutomateDriverServer, base_url):
        super().__init__(driver, base_url)

        self.base_page = BasePage(self.driver, self.base_url)

    # 点击进入“消息中心”
    def enter_msg_center(self):
        self.driver.click_element('x,//*[@id="systemTools"]/a')
        self.driver.wait()

    # 获取“消息中心”title
    def get_msg_center_title(self):
        self.driver.wait(1)
        msg_center_title = self.driver.get_element('x,/html/body/div[6]/div[1]/div/b').text
        return msg_center_title

    # 获取左侧栏目-消息中心-x条未读
    def get_unread_msg_num(self):
        unread_msg_num = self.driver.get_element('x,//*[@id="unReadTotal"]').text
        return unread_msg_num

    # 设置搜索项-消息状态-未读
    def set_search_status_unread(self):
        # 点击状态下拉框
        self.driver.click_element(
            "x,/html/body/div/div[2]/div[1]/form/div[2]/span[2]/div/span[2]")
        self.driver.wait(1)
        # 选中未读
        self.driver.click_element(
            "x,/html/body/div/div[2]/div[1]/form/div[2]/span[2]/div/div/ul/li[2]")
        self.driver.wait(2)
        # 点击搜索
        self.driver.click_element("x,/html/body/div/div[2]/div[1]/form/div[2]/button")
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
            "x,/html/body/div/div[2]/div[1]/form/div[1]/button[1]")
        self.driver.wait()

    # 点击“全部标为已读”
    def set_all_msg_status_read(self):
        self.driver.click_element(
            "x,/html/body/div/div[2]/div[1]/form/div[1]/button[2]")
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

    # 取长度
    def get_length(self, element):
        len = int(self.driver.get_element(element).get_attribute("maxlength"))
        return len

    # 消息中心--编辑--获取长度
    def get_message_edit_element_len(self):
        # 点击第一条的imei
        self.driver.click_element("x,//*[@id='msg_tbody']/tr[1]/td[4]/div/a")
        sleep(4)
        # 切换到iframe
        self.driver.switch_to_iframe('x,/html/body/div[8]/div[2]/iframe')
        # self.driver.switch_to_iframe('x,/html/body/div[7]/div[2]/iframe')

        # 基本信息
        device_name = self.get_length("x,//*[@id='device_info_b']/fieldset[1]/div[2]/div[1]/input")
        sim = self.get_length("x,//*[@id='device_info_a']/fieldset[2]/div[1]/div[1]/input")
        remark = self.get_length("reMark")

        # 点击客户信息
        self.driver.click_element("x,/html/body/div[1]/ul/li[2]/a")
        self.driver.wait()

        # 客户信息
        driver_name = self.get_length("x,//*[@id='device_info_b']/fieldset[1]/div[1]/div[1]/input")
        vehicle_number = self.get_length("x,//*[@id='device_info_b']/fieldset[1]/div[2]/div[1]/input")
        sn = self.get_length("x,//*[@id='device_info_b']/fieldset[1]/div[3]/div[1]/input")
        engine_number = self.get_length("x,//*[@id='engineNumber']")
        phone = self.get_length("x,//*[@id='device_info_b']/fieldset[1]/div[1]/div[2]/input")
        # id_card = self.get_length('x,//*[@id="device_info_b]/fieldset[1]/div[2]/div[2]/input')
        car_frame = self.get_length("x,//*[@id='device_info_b']/fieldset[1]/div[3]/div[2]/input")
        total_mileage = self.get_length("totalKm")


        # 安装信息
        install_company = self.get_length("x,//*[@id='device_info_b']/fieldset[2]/div[2]/div[1]/input")
        install_personnel = self.get_length("x,//*[@id='device_info_b']/fieldset[2]/div[3]/div/input")
        install_address = self.get_length("x,//*[@id='device_info_b']/fieldset[2]/div[1]/div[2]/input")
        install_position = self.get_length("x,//*[@id='device_info_b']/fieldset[2]/div[2]/div[2]/input")
        all_len = {
            "device_name": device_name,
            "sim": sim,
            "remark": remark,
            "driver_name": driver_name,
            "vehicle_number": vehicle_number,
            "sn": sn,
            "engine_number": engine_number,
            "phone": phone,
            # "id_card": id_card,
            "car_frame": car_frame,
            "total_mileage": total_mileage,
            "install_company": install_company,
            "install_personnel": install_personnel,
            "install_address": install_address,
            "install_position": install_position
        }
        print(all_len)
        # 退出frame
        self.driver.default_frame()
        # 点保存
        self.driver.click_element("c,layui-layer-btn0")

        return all_len

    # 消息中心iframe
    def message_center_iframe(self):
        self.driver.switch_to_frame('x,//*[@id="usermessageFrame"]')
