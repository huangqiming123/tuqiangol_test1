from automate_driver.automate_driver import AutomateDriver
from pages.base.base_page import BasePage


# 全局搜索-APP用户搜索功能的元素及操作
# author:孙燕妮

class GlobalAppAccountSearchPage(BasePage):
    def __init__(self, driver: AutomateDriver, base_url):
        super().__init__(driver, base_url)
        self.base_page = BasePage(self.driver, self.base_url)

    # 全局搜索栏-APP用户搜索按钮
    def click_app_account_search(self):
        self.driver.click_element("x,//*[@id='complexQuery']/div/button[2]")
        self.driver.wait(1)

    # APP用户搜索对话框-搜索按钮
    def click_app_acc_dial_search(self):
        self.driver.click_element("x,//*[@id='searchUserEquipment']/div/div/div[2]/div[2]/div/div/span/button")
        self.driver.wait(5)

    # APP用户搜索对话框-APP用户搜索
    def account_dial_search(self, search_keyword):
        # 在用户名称/账号输入框内输入搜索关键词信息
        self.driver.operate_input_element('x,//*[@id="searchUserEquipment"]/div/div/div[2]/div[2]/div/div/input',
                                          search_keyword)
        # 点击搜索按钮
        self.driver.click_element('x,//*[@id="searchUserEquipment"]/div/div/div[2]/div[2]/div/div/span/button')
        self.driver.wait(1)

    # APP用户搜索对话框-关闭
    def close_dev_search(self):
        self.driver.click_element("x,//*[@id='searchUserEquipment']/div/div/div[1]/button")
        self.driver.wait(1)

    # APP用户精确搜索结果获取
    # 获取其用户名称
    def get_exact_search_name(self):
        name_text = self.driver.get_element(
            'x,/html/body/div[10]/div/div/div[2]/div[5]/div/div[2]/div[2]/div/div[1]/table/tbody/tr/td[4]').text
        return name_text

    # APP用户搜索-获取搜索结果共多少条
    def easy_search_result(self):
        # 当搜索结果只有一条时，必可获取到设备列表
        try:
            # 获取设备列表
            self.driver.get_element("x,complex_mobileUser_device_tbody")
            result_num = 1
            return result_num
        # 当搜索结果大于1条时
        except:
            # 将滚动条拖动到分页栏
            target = self.driver.get_element("complex_paging_mobileUser")
            self.driver.execute_script(target)  # 拖动到可见的元素去

            # 设置每页10条
            self.base_page.select_per_page_number(10)
            # 获取搜索结果共分几页
            total_pages_num = self.base_page.get_total_pages_num("x,//*[@id='complex_paging_mobileUser']")
            # 获取搜索结果最后一页有几条
            last_page_logs_num = self.base_page.last_page_logs_num("x,//*[@id='complex_mobileUser_tbody']",
                                                                   "x,//*[@id='complex_paging_mobileUser']")
            # 计算当前搜索结果共几条
            total_num = self.base_page.total_num(total_pages_num, last_page_logs_num)
            return total_num

    # APP用户详情-控制台
    def click_app_acc_and_dev_link(self, link_name):
        if link_name == '控制台':
            self.driver.click_element('x,//*[@id="complex_mobileUser_detail_tbody"]/tr/td[7]/a[1]')
            self.driver.wait()
        elif link_name == '轨迹回放':
            self.driver.click_element('x,//*[@id="complex_mobileUser_device_tbody"]/tr[1]/td[8]/a[2]')
            self.driver.wait()
        elif link_name == '实时跟踪':
            self.driver.click_element('x,//*[@id="complex_mobileUser_device_tbody"]/tr[1]/td[8]/a[3]')
            self.driver.wait()
        elif link_name == '查看告警':
            self.driver.click_element('x,//*[@id="complex_mobileUser_device_tbody"]/tr[1]/td[8]/a[4]')
            self.driver.wait()

    # APP用户详情-当前用户-“重置密码”
    def curr_acc_reset_passwd(self):
        self.driver.click_element("x,//*[@id='complex_mobileUser_detail_tbody']/tr/td[7]/a[3]")
        self.driver.wait()

    # APP用户详情当前用户-“重置密码”弹框文本内容
    def reset_passwd_content(self):
        reset_passwd_content = self.driver.get_element("c,layui-layer-content").text
        return reset_passwd_content

    # APP用户详情-当前用户-“重置密码”-确定
    def reset_passwd_ensure(self):
        self.driver.click_element("c,layui-layer-btn0")
        self.driver.wait(1)

    # APP用户详情-当前用户-“重置密码”-确定-操作状态
    def get_reset_status(self):
        reset_status = self.driver.get_element("c,layui-layer-content").text
        return reset_status

    # APP用户详情-当前用户-“重置密码”-取消
    def reset_passwd_dismiss(self):
        self.driver.click_element("c,layui-layer-btn1")
        self.driver.wait()

    # APP用户详情-当前设备-详情
    def app_dev_details(self):
        self.driver.click_element("x,//*[@id='complex_mobileUser_device_tbody']/tr/td[8]/a[1]")
        self.driver.wait(5)
        # 点击设备详情的返回列表
        self.driver.click_element('x,//*[@id="searchUserEquipment"]/div/div/div[2]/div[4]/div[2]/div[1]/button')
        self.driver.wait()

    # APP用户详情-当前设备-解绑
    def app_dev_dis_bind(self):
        self.driver.click_element("x,/html/body/div[13]/div/div/div[2]/div[5]/div/div[2]/div[2]/div/"
                                  "div[2]/div[2]/table/tbody/tr/td[9]/a[5]")
        self.driver.wait(1)

    # APP用户详情-当前设备-获取解绑操作状态
    def get_app_dev_dis_bind_status(self):
        status = self.driver.get_element("c,layui-layer-content").text
        return status

    # APP用户列表-控制台链接点击
    def click_acc_list_console_link(self):
        self.driver.click_element("x,/html/body/div[10]/div/div/div[2]/div[5]/div/div[1]/table/tbody/tr[1]/td[7]/a[1]")
        self.driver.wait()

    # APP用户列表-详情
    def click_acc_details(self):
        self.driver.click_element("x,/html/body/div[10]/div/div/div[2]/div[5]/div/div[1]/table/tbody/tr[1]/td[7]/a[2]")
        self.driver.wait(1)

    # APP用户列表-重置密码
    def click_acc_reset_pwd(self):
        self.driver.click_element("x,/html/body/div[10]/div/div/div[2]/div[5]/div/div[1]/table/tbody/tr[1]/td[7]/a[3]")
        self.driver.wait(1)

    # APP用户列表-详情-点击返回列表
    def return_list(self):
        self.driver.click_element("x,/html/body/div[13]/div/div/div[2]/div[5]/div/div[2]/div[1]/button")

    # APP用户列表-导出
    def acc_list_export(self):
        # 将滚动条拖动到分页栏
        target = self.driver.get_element("complex_paging_mobileUser")
        self.driver.execute_script(target)  # 拖动到可见的元素去

        # 点击导出
        self.driver.click_element("x,/html/body/div[10]/div/div/div[2]/div[5]/div/div[1]/div/button")
        self.driver.wait()
