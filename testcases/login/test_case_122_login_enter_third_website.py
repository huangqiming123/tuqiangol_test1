import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page_server import BasePageServer
from pages.login.login_page import LoginPage


# 登录页底部第三方链接测试
# author:孙燕妮

class TestCase122LoginEnterThirdWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_third_website(self):
        '''测试登录页底部第三方链接'''

        websites = ["可信网站", "网络警察", "公共信息网络安全监察", "不良信息举报中心", "工商网监"]

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 获取当前窗口句柄
        tuqiang_handle = self.driver.get_current_window_handle()

        # 点击底部第三方链接-可信网站
        expect_url_00 = "https://ss.knet.cn/verifyseal.dll?sn=e16112844030065399aooh000000&ct=df&a=1&pa=0.5438364866062911"
        self.login_page.enter_third_party_website(websites[0])
        self.driver.wait()
        # 获取当前所有窗口句柄
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != tuqiang_handle:
                self.driver.switch_to_window(handle)
                self.driver.wait(1)
                web_url_00 = self.driver.get_current_url()
                # 判断当前第三方链接跳转是否正确
                self.assertEqual(expect_url_00, web_url_00, "当前第三方链接跳转错误")

                self.driver.close_window()
                self.driver.switch_to_window(tuqiang_handle)

        # 点击底部第三方链接-01
        expect_url_01 = "http://www.cyberpolice.cn/wfjb/"
        self.login_page.enter_third_party_website(websites[1])
        self.driver.wait()
        # 获取当前所有窗口句柄
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != tuqiang_handle:
                self.driver.switch_to_window(handle)
                self.driver.wait(1)
                web_url_01 = self.driver.get_current_url()
                # 判断当前第三方链接跳转是否正确
                self.assertEqual(expect_url_01, web_url_01, "当前第三方链接跳转错误")
                self.driver.wait()

                self.driver.close_window()
                self.driver.switch_to_window(tuqiang_handle)

        # 点击底部第三方链接-02
        self.driver.switch_to_window(tuqiang_handle)
        self.assertEqual(self.base_url + "/", self.driver.get_current_url(), "回到原窗口失败")

        expect_url_02 = "http://www.500wan.com/pages/info/about/wangan/index.htm"
        self.login_page.enter_third_party_website(websites[2])
        self.driver.wait()
        # 获取当前所有窗口句柄
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != tuqiang_handle:
                self.driver.switch_to_window(handle)
                self.driver.wait(1)
                web_url_02 = self.driver.get_current_url()
                # 判断当前第三方链接跳转是否正确
                self.assertEqual(expect_url_02, web_url_02, "当前第三方链接跳转错误")
                self.driver.wait()

                self.driver.close_window()
                self.driver.switch_to_window(tuqiang_handle)

        # 点击底部第三方链接-03
        self.driver.switch_to_window(tuqiang_handle)
        self.assertEqual(self.base_url + "/", self.driver.get_current_url(), "回到原窗口失败")

        expect_url_03 = "http://www.12377.cn/"
        self.login_page.enter_third_party_website(websites[3])
        self.driver.wait()
        # 获取当前所有窗口句柄
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != tuqiang_handle:
                self.driver.switch_to_window(handle)
                self.driver.wait(1)
                web_url_03 = self.driver.get_current_url()
                # 判断当前第三方链接跳转是否正确
                self.assertEqual(expect_url_03, web_url_03, "当前第三方链接跳转错误")
                self.driver.wait()

                self.driver.close_window()
                self.driver.switch_to_window(tuqiang_handle)

        self.driver.switch_to_window(tuqiang_handle)
        self.assertEqual(self.base_url + "/", self.driver.get_current_url(), "回到原窗口失败")

        expect_url_04 = "http://szcert.ebs.org.cn/2a950f00-00fb-495c-8e30-5a04100f9b17"
        self.login_page.enter_third_party_website(websites[4])
        self.driver.wait()
        # 获取当前所有窗口句柄
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != tuqiang_handle:
                self.driver.switch_to_window(handle)
                self.driver.wait(1)
                web_url_04 = self.driver.get_current_url()
                # 判断当前第三方链接跳转是否正确
                self.assertEqual(expect_url_04, web_url_04, "当前第三方链接跳转错误")
                self.driver.wait()

                self.driver.close_window()
                self.driver.switch_to_window(tuqiang_handle)

        self.driver.switch_to_window(tuqiang_handle)
        self.assertEqual(self.base_url + "/", self.driver.get_current_url(), "回到原窗口失败")