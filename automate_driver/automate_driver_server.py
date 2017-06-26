import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.select import Select


# webdirver封装
# author:孙燕妮

class AutomateDriverServer(object):
    def __init__(self):
        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                       desired_capabilities=DesiredCapabilities.FIREFOX)
        self.base_url = 'http://www.tuqiangol.com'

    def navigate(self, url):
        self.driver.get(self.base_url + url)

    def navigate_to_page(self, url):
        self.driver.get(url)
        self.wait()

    def quit_browser(self):
        self.driver.quit()

    def close_current_page(self):
        self.driver.close()

    def clear_cookies(self):
        self.driver.delete_all_cookies()

    def refresh_browser(self):
        self.driver.refresh()
        self.wait(1)

    def wait(self, seconds=2):
        time.sleep(seconds)

    def get_current_url(self):
        return self.driver.current_url

    def get_element(self, selector):
        if selector == None:
            return None
        else:
            if "," not in selector:
                element = self.driver.find_element_by_id(selector)
                return element
            else:
                select_by = selector.split(",")[0]
                select_value = selector.split(",")[1]
                if select_by == "s":
                    element = self.driver.find_element_by_css_selector(select_value)
                    return element
                elif select_by == "x":
                    element = self.driver.find_element_by_xpath(select_value)
                    return element
                elif select_by == "l":
                    element = self.driver.find_element_by_link_text(select_value)
                    return element
                elif select_by == "p":
                    element = self.driver.find_element_by_partial_link_text(select_value)
                    return element
                elif select_by == "c":
                    element = self.driver.find_element_by_class_name(select_value)
                    return element

    def get_elements(self, selector):
        if selector == None:
            return None
        else:
            if "," not in selector:
                elements = self.driver.find_elements_by_id(selector)
                return elements
            else:
                select_by = selector.split(",")[0]
                select_value = selector.split(",")[1]
                if select_by == "s":
                    elements = self.driver.find_elements_by_css_selector(select_value)
                    return elements
                elif select_by == "x":
                    elements = self.driver.find_elements_by_xpath(select_value)
                    return elements
                elif select_by == "l":
                    elements = self.driver.find_elements_by_link_text(select_value)
                    return elements
                elif select_by == "p":
                    elements = self.driver.find_elements_by_partial_link_text(select_value)
                    return elements
                elif select_by == "c":
                    elements = self.driver.find_elements_by_class_name(select_value)
                    return elements

    def click_element(self, selector):
        element = self.get_element(selector)
        element.click()

    def operate_input_element(self, selector, value):
        element = self.get_element(selector)
        element.clear()
        element.send_keys(value)

    def go_back(self):
        self.driver.back()
        self.wait(1)

    def to_forward(self):
        self.driver.forward()
        self.wait(1)

    def set_window_max(self):
        self.driver.maximize_window()
        self.wait()

    def get_text(self, selector):
        text = self.get_element(selector).text
        return text

    def get_current_window_handle(self):
        handle = self.driver.current_window_handle
        return handle

    def get_all_window_handles(self):
        all_handles = self.driver.window_handles
        return all_handles

    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)
        self.wait()

    def switch_to_alert(self):
        a = self.driver.switch_to.alert
        return a

    def select_element(self, selector, select_by, select_info):
        element = self.get_element(selector)
        if select_by == 'i':
            Select(element).select_by_index(select_info)
        elif select_by == 'v':
            Select(element).select_by_value(select_info)
        elif select_by == 't':
            Select(element).select_by_visible_text(select_info)

    def is_element_exist(self, selector):
        flag = True
        try:
            self.get_element(selector)
            return flag

        except:
            flag = False
            return flag

    def is_element_exist_and_click(self, selector_01, selector_02):
        flag = True
        try:
            self.get_element(selector_01)
            self.click_element(selector_02)
            return flag

        except:
            flag = False
            return flag

    # 修改不可见元素为可见
    def execute_js_css(self, css_selector):
        self.driver.execute_script("$('" + css_selector + "').attr('style','display:block;')")

    def insert_img(self, file_name):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        base_dir = str(base_dir)
        base_dir = base_dir.replace('\\', '/')
        base = base_dir.split('/TestCases')[0]
        file_path = base + '/test_screenshot_img/' + file_name
        self.driver.get_screenshot_as_file(file_path)

    # 拖动滚动条至可见元素
    def execute_script(self, target_ele):
        self.driver.execute_script("arguments[0].scrollIntoView();", target_ele)

    # 鼠标悬停
    def float_element(self, target_ele):
        chain = ActionChains(self.driver)
        chain.move_to_element(target_ele).perform()

    # 隐式等待 author：zhangAo

    def implicitly_wait(self, sec):

        self.driver.implicitly_wait(sec)

    def switch_to_frame(self, selector):
        # 切换到frame
        el = self.get_element(selector)
        self.driver.switch_to.frame(el)

    def switch_to_iframe(self, selector):
        # 进入iframe
        el = self.get_element(selector)
        self.driver.switch_to.frame(el)

    def default_frame(self):
        # 退出frame
        self.driver.switch_to.default_content()

    def switch_to_actelement(self):
        self.driver.switch_to.active_element()

    def execute_js(self, script):
        """
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script)

    def accept_alarm(self):
        self.driver.switch_to.alert().accept()

    def clear_input(self, selector):
        el = self.get_element(selector)
        el.clear()

    def close_window(self):
        self.driver.close()
