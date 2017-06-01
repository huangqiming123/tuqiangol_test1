from time import sleep
from pages.base.base_page import BasePage
from pages.statistical_form.search_sql import SearchSql


class StatisticalFormPage2(BasePage):
    # 实例化search_sql类
    def instance_search_sql(self):
        search_sql = SearchSql()
        return search_sql

    # 取开始--结束时间
    def get_sport_statistical_time(self, start_element, end_element):
        # 页面的时间
        start_time = self.driver.get_element(start_element).get_attribute('value')
        end_time = self.driver.get_element(end_element).get_attribute('value')
        time = {"page_start_time": start_time, "page_end_time": end_time}
        return time

    # 统计报表--验证时间
    def sport_statistical_validation_time(self, type, iframe, start, end, pull_down, yesterday, this_week, last_week,
                                          this_month, last_month, random, today=""):
        search_sql = self.instance_search_sql()
        # 定位iframe
        try:
            self.driver.switch_to_iframe(iframe)
            print("执行了iframe")
        except:
            print("没有执行iframe")
        # 点击下拉框
        self.driver.click_element(pull_down)
        self.driver.wait()

        if type == "今天":
            self.driver.click_element(today)
            # 获取页面显示的时间
            page_time = self.get_sport_statistical_time(start, end)
            # 获取实际时间（今天）
            sql_start_time = search_sql.get_today_begin_date()
            sql_end_time = search_sql.get_today_end_time()
            time = {
                "page_time": page_time,
                "sql_time": {"sql_start_time": sql_start_time, "sql_end_time": sql_end_time}
            }
            print(time)
            return time

        elif type == "昨天":
            self.driver.click_element(yesterday)
            # 获取页面显示的时间
            page_time = self.get_sport_statistical_time(start, end)
            # 获取实际时间（昨天）
            sql_start_time = search_sql.get_yesterday_begin_time()
            sql_end_time = search_sql.get_yesterday_end_time()
            time = {
                "page_time": page_time,
                "sql_time": {"sql_start_time": sql_start_time, "sql_end_time": sql_end_time}
            }
            print(time)
            return time

        elif type == "本周":
            self.driver.click_element(this_week)
            page_time = self.get_sport_statistical_time(start, end)
            # 获取实际时间(本周)
            sql_start_time = search_sql.get_this_week_begin_time()
            sql_end_time = search_sql.get_this_week_end_time()
            time = {
                "page_time": page_time,
                "sql_time": {"sql_start_time": sql_start_time, "sql_end_time": sql_end_time}
            }
            print(time)
            return time

        elif type == "上周":
            self.driver.click_element(last_week)
            self.driver.wait(1)
            page_time = self.get_sport_statistical_time(start, end)
            # 获取实际时间(上周)
            sql_start_time = search_sql.get_last_week_begin_time()
            sql_end_time = search_sql.get_last_week_end_time()
            time = {
                "page_time": page_time,
                "sql_time": {"sql_start_time": sql_start_time, "sql_end_time": sql_end_time}
            }
            print(time)
            return time

        elif type == "本月":
            self.driver.click_element(this_month)
            page_time = self.get_sport_statistical_time(start, end)
            # 获取实际时间(本月)
            sql_start_time = search_sql.get_this_month_begin_time()
            sql_end_time = search_sql.get_this_month_end_time()
            time = {
                "page_time": page_time,
                "sql_time": {"sql_start_time": sql_start_time, "sql_end_time": sql_end_time}
            }
            print(time)
            return time

        elif type == "上月":
            self.driver.click_element(last_month)
            page_time = self.get_sport_statistical_time(start, end)
            # 获取实际时间(本周)
            sql_start_time = search_sql.get_last_month_begin_time()
            sql_end_time = search_sql.get_last_month_end_time()
            time = {
                "page_time": page_time,
                "sql_time": {"sql_start_time": sql_start_time, "sql_end_time": sql_end_time}
            }
            print(time)
            return time

        elif type == "自定义":
            # 获取点击自定义之前的时间
            page_time = self.get_sport_statistical_time(start, end)
            self.driver.click_element(random)
            time = {
                "page_time": page_time,
                "sql_time": {"sql_start_time": page_time["page_start_time"], "sql_end_time": page_time["page_end_time"]}
            }
            return time
        # 退出frame
        self.driver.default_frame()

    # 运动总览--搜索用户
    def search_inexistence_user(self, user_data):
        # self.driver.switch_to_frame('x,//*[@id="sportOverviewFrame"]')
        # 点下拉
        try:
            self.driver.click_element("search_text")
            sleep(1)
        except:
            pass
        # 搜索用户
        self.driver.operate_input_element("search_user_text", user_data)
        sleep(2)
        self.driver.click_element("search_user_btn")
        sleep(2)
        # 获取提示
        if user_data != "暂无数据":
            # 有数据
            text = self.driver.get_text('c,autocompleter-item')
        else:
            # 暂无数据
            text = self.driver.get_text('c,autocompleter-nodata')

        sleep(2)
        # self.driver.default_frame()
        return text

    # 运动总览--验证时间
    def sport_overview_validation_time(self, type):
        iframe = "sportOverviewFrame"
        start = "startTime_sport"
        end = "endTime_sport"
        pull_down = "x,//*[@id='runForm']/div[1]/div/div/div"
        yesterday = "x,//*[@id='runForm']/div[1]/div/div/div/div/ul/li[2]"
        this_week = "x,//*[@id='runForm']/div[1]/div/div/div/div/ul/li[3]"
        last_week = "x,//*[@id='runForm']/div[1]/div/div/div/div/ul/li[4]"
        this_month = "x,//*[@id='runForm']/div[1]/div/div/div/div/ul/li[5]"
        last_month = "x,//*[@id='runForm']/div[1]/div/div/div/div/ul/li[6]"
        random = "x,//*[@id='runForm']/div[1]/div/div/div/div/ul/li[1]"
        time = self.sport_statistical_validation_time(type, iframe, start, end, pull_down, yesterday, this_week,
                                                      last_week, this_month, last_month, random)
        return time

    # 里程报表--验证时间
    def mileage_form_validation_time(self, type):
        iframe = "tracelReportFrame"
        start = "startTime_travel"
        end = "endTime_travel"
        pull_down = "x,//*[@id='dateSelect_div']/div/span[2]"
        today = "x,//*[@id='dateSelect_div']/div/div/ul/li[2]"
        yesterday = "x,//*[@id='dateSelect_div']/div/div/ul/li[3]"
        this_week = "x,//*[@id='dateSelect_div']/div/div/ul/li[4]"
        last_week = "x,//*[@id='dateSelect_div']/div/div/ul/li[5]"
        this_month = "x,//*[@id='dateSelect_div']/div/div/ul/li[6]"
        last_month = "x,//*[@id='dateSelect_div']/div/div/ul/li[7]"
        random = "x,//*[@id='dateSelect_div']/div/div/ul/li[1]"
        time = self.sport_statistical_validation_time(type, iframe, start, end, pull_down, yesterday,
                                                      this_week, last_week, this_month, last_month, random, today)
        return time

    # 点击搜索中的用户
    def click_search_user(self, coumt):
        # self.driver.click_element("x,//*[@id='tree_%s']"  %str(coumt+1))
        self.driver.click_element("x,/html/body/div/div[2]/div[1]/form/div[2]/div[1]/"
                                  "div/div[2]/div[2]/ul/li/ul/li[%s]" % str(coumt + 1))

        print("搜索中的用户点。。", str(coumt + 1))

    # 根据选择用户，验证设备数
    # def search_user_and_imei_number(self,pull_down,user,search):
    def search_user_and_imei_number(self, coumt):
        # 点下拉框
        self.driver.click_element("x,//*[@id='MileageFrom']/div[2]/div[1]/div/div[1]/span/button")
        self.driver.wait()
        # 点击搜索中的用户
        self.click_search_user(coumt)
        self.driver.wait(1)
        # 点击imei搜索图标
        self.driver.click_element("x,//*[@id='MileageFrom']/div[2]/div[2]/div/div/div/div[1]/span/button")
        self.driver.wait(1)
        # 获取分组
        style = self.driver.get_element("nodata_mileageReport").get_attribute("style")
        if style == "display: block;":
            self.driver.wait(1)
            text = self.driver.get_text("x,//*[@id='nodata_mileageReport']/span")
            print("text", text)
            return text

        elif style == "display: none;":
            grouping_len = len(self.driver.get_elements("x,//*[@id='dev_tree_mileageReport']/li"))
            print("分组长度", grouping_len)
            for count in range(grouping_len):
                # 获取分组数据
                grouping_data = self.driver.get_text("x,/html/body/div/div[2]/div[1]/form/div[2]/div[2]/"
                                                     "div/div/div/div[2]/div[1]/ul/li[" + str(
                    count + 1) + "]/a/span[2]")
                print("分组数据", grouping_data)
                data = grouping_data.split("(")[1]
                grouping_count = int(data.split(")")[0])

                # 点击显示分组列表
                self.driver.click_element("x,/html/body/div/div[2]/div[1]/form/div[2]/div[2]/div/div/"
                                          "div/div[2]/div[1]/ul/li[" + str(count + 1) + "]/span[1]")
                # 获取分组imei数
                imei_number = self.get_grouping_list_count()

                # 点击显示分组列表
                self.driver.click_element("x,/html/body/div/div[2]/div[1]/form/div[2]/div[2]/div/div/"
                                          "div/div[2]/div[1]/ul/li[" + str(count + 1) + "]/span[1]")
                number = {
                    "grouping_count": grouping_count,
                    "imei_number": imei_number
                }
                return number

    def iframe(self):
        self.driver.switch_to_iframe("speedingReportFrame")

    # 点击里程报表搜索下拉
    def click_mileage_pull_down(self):
        self.driver.click_element('x,//*[@id="TravelFrom"]/div[2]/div[1]/div/div[1]/span/button')

    def get_grouping_list_count(self):
        # 获取分组imei数
        imei_number = len(self.driver.get_elements("x,/html/body/div/div[2]/div[1]/form/div[2]/div[2]/div/div/"
                                                   "div/div[2]/div[1]/ul/li[1]/ul/li"))
        return imei_number

    def get_mileage_form_imei_number(self):
        pull_down = "x,//*[@id='MileageFrom']/div[2]/div[1]/div/div[1]/span/button"
        user = "x,//*[@id='tree_1_ul']/li"

    # 超速报表--验证时间
    def speed_form_validation_time(self, type):
        iframe = "speedingReportFrame"
        start = "startTime_overspeed"
        end = "endTime_overspeed"
        pull_down = "x,//*[@id='OverspeedFrom']/div[1]/div[1]/div/div/div/span[2]"
        today = "x,//*[@id='OverspeedFrom']/div[1]/div[1]/div/div/div/div/ul/li[2]"
        yesterday = "x,//*[@id='OverspeedFrom']/div[1]/div[1]/div/div/div/div/ul/li[3]"
        this_week = "x,//*[@id='OverspeedFrom']/div[1]/div[1]/div/div/div/div/ul/li[4]"
        last_week = "x,//*[@id='OverspeedFrom']/div[1]/div[1]/div/div/div/div/ul/li[5]"
        this_month = "x,//*[@id='OverspeedFrom']/div[1]/div[1]/div/div/div/div/ul/li[6]"
        last_month = "x,//*[@id='OverspeedFrom']/div[1]/div[1]/div/div/div/div/ul/li[7]"
        random = "x,//*[@id='OverspeedFrom']/div[1]/div[1]/div/div/div/div/ul/li[1]"
        time = self.sport_statistical_validation_time(type, iframe, start, end, pull_down, yesterday,
                                                      this_week, last_week, this_month, last_month, random, today)
        return time

    # 停留报表--验证时间
    def stay_form_validation_time(self, type):
        iframe = "stayReportFrame"
        start = "startTime_stopCar"
        end = "endTime_stopCar"
        pull_down = "x,//*[@id='StopCarFrom']/div[1]/div[1]/div/div/div/span[2]"
        today = "x,//*[@id='StopCarFrom']/div[1]/div[1]/div/div/div/div/ul/li[2]"
        yesterday = "x,//*[@id='StopCarFrom']/div[1]/div[1]/div/div/div/div/ul/li[3]"
        this_week = "x,//*[@id='StopCarFrom']/div[1]/div[1]/div/div/div/div/ul/li[4]"
        last_week = "x,//*[@id='StopCarFrom']/div[1]/div[1]/div/div/div/div/ul/li[5]"
        this_month = "x,//*[@id='StopCarFrom']/div[1]/div[1]/div/div/div/div/ul/li[6]"
        last_month = "x,//*[@id='StopCarFrom']/div[1]/div[1]/div/div/div/div/ul/li[7]"
        random = "x,//*[@id='StopCarFrom']/div[1]/div[1]/div/div/div/div/ul/li[1]"
        time = self.sport_statistical_validation_time(type, iframe, start, end, pull_down, yesterday,
                                                      this_week, last_week, this_month, last_month, random, today)
        return time

    # 停车未熄火报表--验证时间
    def parking_not_shut_down_form_validation_time(self, type):
        iframe = "parkingReportFrame"
        start = "startTime_stopNotOff"
        end = "endTime_stopNotOff"
        pull_down = "x,//*[@id='stopNotOffFrom']/div[1]/div[1]/div/div/div/span[2]"
        today = "x,//*[@id='stopNotOffFrom']/div[1]/div[1]/div/div/div/div/ul/li[2]"
        yesterday = "x,//*[@id='stopNotOffFrom']/div[1]/div[1]/div/div/div/div/ul/li[3]"
        this_week = "x,//*[@id='stopNotOffFrom']/div[1]/div[1]/div/div/div/div/ul/li[4]"
        last_week = "x,//*[@id='stopNotOffFrom']/div[1]/div[1]/div/div/div/div/ul/li[5]"
        this_month = "x,//*[@id='stopNotOffFrom']/div[1]/div[1]/div/div/div/div/ul/li[6]"
        last_month = "x,//*[@id='stopNotOffFrom']/div[1]/div[1]/div/div/div/div/ul/li[7]"
        random = "x,//*[@id='stopNotOffFrom']/div[1]/div[1]/div/div/div/div/ul/li[1]"
        time = self.sport_statistical_validation_time(type, iframe, start, end, pull_down, yesterday,
                                                      this_week, last_week, this_month, last_month, random, today)
        return time

    # ACC报表--验证时间
    def acc_form_validation_time(self, type):
        iframe = "AccReportFrame"
        start = "startTime_acc"
        end = "endTime_acc"
        pull_down = "x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/span[2]"
        today = "x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div/ul/li[2]"
        yesterday = "x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div/ul/li[3]"
        this_week = "x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div/ul/li[4]"
        last_week = "x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div/ul/li[5]"
        this_month = "x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div/ul/li[6]"
        last_month = "x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div/ul/li[7]"
        random = "x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div/ul/li[1]"
        time = self.sport_statistical_validation_time(type, iframe, start, end, pull_down, yesterday,
                                                      this_week, last_week, this_month, last_month, random, today)
        return time

    # 告警总览报表--验证时间
    def alarm_overview_validation_time(self, type):
        iframe = "alarmOverviewFrame"
        start = "startTime_alarmReport"
        end = "endTime_alarmReport"
        pull_down = "x,//*[@id='alarmForm']/div/div[1]/div/div/div/span[3]"
        today = "x,//*[@id='alarmForm']/div/div[1]/div/div/div/div/ul/li[2]"
        yesterday = "x,//*[@id='alarmForm']/div/div[1]/div/div/div/div/ul/li[3]"
        this_week = "x,//*[@id='alarmForm']/div/div[1]/div/div/div/div/ul/li[4]"
        last_week = "x,//*[@id='alarmForm']/div/div[1]/div/div/div/div/ul/li[5]"
        this_month = "x,//*[@id='alarmForm']/div/div[1]/div/div/div/div/ul/li[6]"
        last_month = "x,//*[@id='alarmForm']/div/div[1]/div/div/div/div/ul/li[7]"
        random = "x,//*[@id='alarmForm']/div/div[1]/div/div/div/div/ul/li[1]"
        time = self.sport_statistical_validation_time(type, iframe, start, end, pull_down, yesterday,
                                                      this_week, last_week, this_month, last_month, random, today)
        return time

    # 点击选择告警类型
    def click_setting_alarm_type(self):
        self.driver.switch_to_iframe("alarmOverviewFrame")
        self.driver.click_element("x,/html/body/div[1]/div[2]/div[3]/div[2]/div[3]/table/thead/tr/th/span")
        self.driver.default_frame()
        self.driver.wait()

    # 点击搜索用户--下拉框
    def click_alarm_overview_pull_down(self):
        self.driver.click_element("x,//*[@id='alarmForm']/div/div[3]/div/div[1]/span/button")

    # 点击设置告警类型---全选
    def click_alarm_type_all(self):
        self.driver.click_element("x,//*[@id='serAlarmTypeModal']/div/label/div/ins")

        # 设置告警类型---全选验证

    def setting_alarm_type(self, type):
        list = []
        count = len(self.driver.get_elements("x,//*[@id='serAlarmTypeModal']/ul/li"))
        print(count)
        # selected = self.driver.get_element("x,//*[@id='allCheck']").is_selected()
        # if selected == True:
        for c in range(count):
            # 定位、获取状态
            self.driver.get_element("x,//*[@id='alarmTypeReport']/li[" + str(c + 1) + "]")
            before_selected = self.driver.get_element(
                "x,//*[@id='alarmTypeReport']/li[" + str(c + 1) + "]/label/div/input").is_selected()
            list.append(before_selected)

        if type == "保存":
            # 点保存
            self.driver.click_element("c,layui-layer-btn0")
            self.driver.wait()
        elif type == "取消":
            self.driver.click_element("c,layui-layer-btn1")
            self.driver.wait()
        return list

    # 告警统计--搜索用户
    def alarm_search_user(self, user_data):
        # 点下拉
        try:
            self.driver.click_element("userTreeName")
            sleep(1)
        except:
            pass
        sleep(1)
        # 搜索用户
        self.driver.operate_input_element("cusTreeKey", user_data)
        sleep(2)
        self.driver.click_element("cusTreeSearchBtn")
        sleep(2)
        # 获取提示
        if user_data != "暂无数据":
            # 有数据
            text = self.driver.get_text('c,autocompleter-item')
        else:
            # 暂无数据
            text = self.driver.get_text('c,autocompleter-nodata')

        sleep(2)
        return text
