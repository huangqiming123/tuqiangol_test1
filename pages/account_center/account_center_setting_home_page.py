from time import sleep
from automate_driver.automate_driver_server import AutomateDriverServer

# 账户中心页面-默认首页设置的元素及操作
# author:戴招利
from pages.base.base_page_server import BasePageServer


class AccountCenterSettingHomePage(BasePageServer):
    def __init__(self, driver: AutomateDriverServer, base_url):
        super().__init__(driver, base_url)

    # 点击默认首页设置
    def click_home_page_setting(self):
        self.driver.click_element('x,/html/body/div[1]/div[5]/div/div/div[1]/div/div[2]/ul/li[5]/a')
        self.driver.wait()

    # 点击默认设置
    def click_setting_default(self, number):
        self.driver.click_element("x,//*[@id='defaultPageList_tbody']/tr[" + str(number) + "]/td[2]/a")
        self.driver.wait()
        prompt = self.driver.get_element("c,layui-layer-content").text
        return prompt

    # 取首页名称、设置默认文本
    def get_default_setting_text(self, number):
        name = self.driver.get_text("x,//*[@id='defaultPageList_tbody']/tr[" + str(number) + "]/td[1]")
        state = self.driver.get_text("x,//*[@id='defaultPageList_tbody']/tr[" + str(number) + "]/td[2]")
        text = {
            "page_name": name,
            "state": state
        }
        print(text)
        return text

    # 获取列表全部设置默认文本
    def get_home_page_list_all_state(self):
        list_data = []
        count = len(self.driver.get_elements("x,//*[@id='defaultPageList_tbody']/tr"))
        print(count)
        for c in range(count):
            # 定位、获取状态
            text = self.driver.get_text("x,//*[@id='defaultPageList_tbody']/tr[" + str(c + 1) + "]/td[2]")
            list_data.append(text)
        print(list_data)
        return list_data

    def get_expect_url(self, title):
        if title == "账户中心":
            url = self.driver.base_url + "/customer/toAccountCenter"
            return url
        if title == "设备管理":
            url = self.driver.base_url + "/device/toDeviceManage"
            return url
        if title == "客户管理":
            url = self.driver.base_url + "/customer/toSearch"
            return url
        if title == "控制台":
            url = self.driver.base_url + "/console"
            return url
        if title == "统计报表":
            url = self.driver.base_url + "/deviceReport/statisticalReport"
            return url
        if title == "安全区域":
            url = self.driver.base_url + "/safearea/geozonemap?flag=0"
            return url
        if title == "设备分布图":
            url = self.driver.base_url + "/deviceReport/deviceDistribution"
            return url
