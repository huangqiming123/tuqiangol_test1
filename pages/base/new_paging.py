from time import sleep

from pages.base.base_page import BasePage


class NewPaging(BasePage):
    # 最新的分页功能
    def get_li_total_number(self, selector_li):
        # 获取分页的所有的li便签，为了获取最后一个页码的路径
        # 可能搜索无结果，需要try
        try:
            total_number = list(self.driver.get_elements(selector_li + "/ul/li"))
            number = len(total_number) - 3
            return number
        except:
            return 0

    def get_last_page_number(self, selector_tr):
        # 获取最后一个有多少条记录，查询列表里tr标签
        try:
            total_number = list(self.driver.get_elements(selector_tr + "/tr"))
            number = len(total_number)
            return number
        except:
            return 0

    def get_total_number(self, selector_li, selector_tr):
        # 获取总共有多少条记录
        # 如果没有记录 就返回0
        if self.get_li_total_number(selector_li) == 0:
            return 0

        # 如果页面就一条记录，就返回这一页tr标签的总数
        elif self.get_li_total_number(selector_li) == 1:
            return self.get_last_page_number(selector_tr)

        else:
            for n in range(10000):
                page = self.get_li_total_number(selector_li)
                self.driver.click_element(selector_li + "/ul/li[" + str(int(page) + 1) + "]/a")
                try:
                    sleep(10)
                    self.driver.get_text('l,下一页') == '下一页'
                    continue
                except:
                    break

            # 获取最后一页前一页的页码
            page_01 = self.get_li_total_number(selector_li)
            pages = self.driver.get_text(selector_li + "/ul/li[" + str(int(page_01)) + "]/a")
            # 获取最后一页总共有多少条记录
            last_page_number = self.get_last_page_number(selector_tr)

            # 计算总共有多少条记录
            total = int(pages) * 10 + last_page_number
            return total

    def get_total_page(self, selector_li):
        if self.get_li_total_number(selector_li) == 0:
            return 0

        # 如果页面就一条记录，就返回这一页tr标签的总数
        elif self.get_li_total_number(selector_li) == 1:
            return 1

        else:
            for n in range(10000):
                page = self.get_li_total_number(selector_li)
                self.driver.click_element(selector_li + "/ul/li[" + str(int(page) + 1) + "]/a")
                try:
                    sleep(5)
                    self.driver.get_text('l,下一页') == '下一页'
                    continue
                except:
                    break

            # 获取最后一页前一页的页码
            page_01 = self.get_li_total_number(selector_li)
            pages = self.driver.get_text(selector_li + "/ul/li[" + str(int(page_01)) + "]/a")

            return int(pages) + 1

    def get_total_numbers(self, selector_li, selector_tr):
        # 获取总共有多少条记录
        # 如果没有记录 就返回0
        if self.get_li_total_number(selector_li) == 0:
            return 0

        # 如果页面就一条记录，就返回这一页tr标签的总数
        elif self.get_li_total_number(selector_li) == 1:
            return self.get_last_page_number(selector_tr)

        else:
            for n in range(10000):
                page = self.get_li_total_number(selector_li)
                self.driver.click_element(selector_li + "/ul/li[" + str(int(page) + 1) + "]/a")
                try:
                    sleep(5)
                    self.driver.get_text('l,下一页') == '下一页'
                    continue
                except:
                    break

            # 获取最后一页前一页的页码
            page_01 = self.get_li_total_number(selector_li)
            pages = self.driver.get_text(selector_li + "/ul/li[" + str(int(page_01)) + "]/a")
            # 获取最后一页总共有多少条记录
            last_page_number = self.get_last_page_number(selector_tr)

            # 计算总共有多少条记录
            total = int(pages) * 20 + last_page_number
            return total

    def get_totals_number(self, param, param1):
        # 获取总共有多少条记录
        # 如果没有记录 就返回0
        if self.get_li_total_number(param) == 0:
            return 0

        # 如果页面就一条记录，就返回这一页tr标签的总数
        elif self.get_li_total_number(param) == 1:
            return self.get_last_page_number(param1)

        else:
            for n in range(10000):
                page = self.get_li_total_number(param)
                self.driver.click_element(param + "/ul/li[" + str(int(page) + 1) + "]/a")
                try:
                    sleep(25)
                    self.driver.get_text('l,下一页') == '下一页'
                    continue
                except:
                    break

            # 获取最后一页前一页的页码
            page_01 = self.get_li_total_number(param)
            pages = self.driver.get_text(param + "/ul/li[" + str(int(page_01)) + "]/a")
            # 获取最后一页总共有多少条记录
            last_page_number = self.get_last_page_number(param1)

            # 计算总共有多少条记录
            total = int(pages) * 10 + last_page_number
            return total

    def get_total_page_and_total_number(self, selector_li, selector_tr):
        if self.get_li_total_number(selector_li) == 0:
            return [0, 0]

        # 如果页面就一条记录，就返回这一页tr标签的总数
        elif self.get_li_total_number(selector_li) == 1:
            last_page_number = self.get_last_page_number(selector_tr)
            return [1, last_page_number]

        else:
            for n in range(10000):
                page = self.get_li_total_number(selector_li)
                self.driver.click_element(selector_li + "/ul/li[" + str(int(page) + 1) + "]/a")
                try:
                    sleep(5)
                    self.driver.get_text('l,下一页') == '下一页'
                    continue
                except:
                    break

            # 获取最后一页前一页的页码
            page_01 = self.get_li_total_number(selector_li)
            pages = self.driver.get_text(selector_li + "/ul/li[" + str(int(page_01)) + "]/a")
            last_page_number = self.get_last_page_number(selector_tr)
            # 计算总共有多少条记录
            total = int(pages) * 10 + last_page_number
            total_number = [int(pages) + 1, total]
            return total_number
