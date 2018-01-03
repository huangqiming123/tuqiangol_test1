from time import sleep

from automate_driver.automate_driver import AutomateDriver

# 基础页面的操作封装，主要是一些公共方法
# author:孙燕妮
from automate_driver.automate_driver_server import AutomateDriverServer


class BasePageServer(object):
    def __init__(self, driver: AutomateDriverServer, base_url):
        self.driver = driver
        self.base_url = base_url

    # 公共的打开页面方法
    def open_page(self):
        self.driver.navigate("/")
        sleep(2)

    def click_chinese_button(self):
        self.driver.click_element('x,/html/body/footer/div[1]/ul/li[1]/a')
        sleep(2)

    # 列表分页

    # 设置列表底部每页共x条
    def select_per_page_number(self, number):
        if number == '10':
            # 选择select列表中的每页10条
            self.driver.select_element("c,page-select", "v", "10")
        elif number == '30':
            # 选择select列表中的每页30条
            self.driver.select_element("c,page-select", "v", "30")
        elif number == '50':
            # 选择select列表中的每页50条
            self.driver.select_element("c,page-select", "v", "50")
        elif number == '100':
            # 选择select列表中的每页100条
            self.driver.select_element("c,page-select", "v", "100")

    # 获取结果共分几页
    def get_total_pages_num(self, selector):
        # 将该分页条下ul标签内的所有li标签获取到列表中
        paging_list = list(self.driver.get_elements(selector + "/ul/li"))
        print(paging_list)
        pages_num = len(paging_list) - 3
        return pages_num

    def get_actual_pages_number(self, selector):
        # 获取真实的页面总数
        page_number = self.get_total_pages_num(selector)

        if page_number == 1:
            print(page_number)
            return page_number
        else:
            total_number = self.driver.get_text(selector + "/ul/li[" + str(int(page_number) + 1) + "]/a")
            print(total_number)
            return total_number

    def get_actual_pages_number_span(self, selector):
        # 获取真实的页面总数
        page_number = self.get_total_pages_num(selector)

        if page_number == 1:
            print(page_number)
            return page_number
        else:
            total_number = self.driver.get_text(selector + "/ul/li[" + str(int(page_number) + 1) + "]/span")
            print(total_number)
            return total_number

    def get_actual_pages_number_with_serach(self, selector):
        # 获取真实的页面总数
        page_number = self.get_total_pages_num(selector)

        if page_number == 1:
            print(page_number)
            return page_number
        else:
            total_number = self.driver.get_text(selector + "/ul/li[" + str(int(page_number)) + "]/a")
            print(total_number)
            return total_number

    # 获取最后一页有几条记录
    def last_page_logs_num_with_search(self, selector01, selector02):
        total_pages_num = self.get_total_pages_num(selector02)
        # 进入到最后一页
        if total_pages_num == 1:
            # 获取当前页共几条记录
            # 获取到日志list的tbody下所有的tr标签保存在列表中
            page_logs = list(self.driver.get_elements(selector01 + "/tr"))
            page_logs_num = len(page_logs)
            print("当前仅一页记录共：" + str(page_logs_num))
            return page_logs_num
        else:
            # 获取最后一页共几条记录
            # 获取到日志list的tbody下所有的tr标签保存在列表中
            last_page_logs = list(self.driver.get_elements(selector01 + "/tr"))
            last_page_logs_num = len(last_page_logs)
            print("当前最后一页记录共：" + str(last_page_logs_num))
            return last_page_logs_num

    # 获取最后一页有几条记录
    def last_page_logs_num(self, selector01, selector02):
        total_pages_num = self.get_total_pages_num(selector02)
        # 进入到最后一页
        if total_pages_num == 1:
            # 获取当前页共几条记录
            # 获取到日志list的tbody下所有的tr标签保存在列表中
            page_logs = list(self.driver.get_elements(selector01 + "/tr"))
            page_logs_num = len(page_logs)
            print("当前仅一页记录共：" + str(page_logs_num))
            return page_logs_num
        else:
            self.driver.click_element(selector02 + "/ul/li[" + str(int(total_pages_num) + 1) + "]/a")
            self.driver.wait(30)
            # 获取最后一页共几条记录
            # 获取到日志list的tbody下所有的tr标签保存在列表中
            last_page_logs = list(self.driver.get_elements(selector01 + "/tr"))
            last_page_logs_num = len(last_page_logs)
            print("当前最后一页记录共：" + str(last_page_logs_num))
            return last_page_logs_num

    # 获取最后一页有几条记录
    def last_page_logs_num_span(self, selector01, selector02):
        total_pages_num = self.get_actual_pages_number_span(selector02)
        # 进入到最后一页
        if total_pages_num == 1:
            # 获取当前页共几条记录
            # 获取到日志list的tbody下所有的tr标签保存在列表中
            page_logs = list(self.driver.get_elements(selector01 + "/tr"))
            page_logs_num = len(page_logs)
            print("当前仅一页记录共：" + str(page_logs_num))
            return page_logs_num
        else:
            self.driver.click_element(selector02 + "/ul/li[" + str(int(total_pages_num) + 1) + "]/span")
            self.driver.wait(20)
            # 获取最后一页共几条记录
            # 获取到日志list的tbody下所有的tr标签保存在列表中
            last_page_logs = list(self.driver.get_elements(selector01 + "/tr"))
            last_page_logs_num = len(last_page_logs)
            print("当前最后一页记录共：" + str(last_page_logs_num))
            return last_page_logs_num

    # 计算当前结果共几条
    def total_num(self, total_pages_num, last_page_logs_num):
        total_num = (int(total_pages_num) - 1) * 10 + last_page_logs_num
        return total_num

    # 重置用户密码后首次登录强制修改密码
    def force_reset_passwd(self, passwd):
        self.driver.operate_input_element("newPwd_advise", passwd)
        self.driver.wait()
        self.driver.operate_input_element("x,/html/body/div[1]/div[3]/div/div/div[2]/form/div[2]/div/input", passwd)

        self.driver.wait(1)
        self.driver.click_element("x,/html/body/div[1]/div[3]/div/div/div[3]/button")
        self.driver.wait(1)

    # 强制修改密码成功后获取弹框文本
    def reset_passwd_stat_cont(self):
        stat_cont = self.driver.get_element("c,layui-layer-content").text
        return stat_cont

    # 强制修改密码成功弹框点击确定
    def reset_passwd_succ_ensure(self):
        self.driver.click_element("c,layui-layer-btn0")
        self.driver.wait(1)

    def change_windows_handle(self, current_handle):
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.close_current_page()
                sleep(1)
                self.driver.switch_to_window(handle)
