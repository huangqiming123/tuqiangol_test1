from time import sleep

from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.statistical_form.search_sql import SearchSql


class StatisticalFormPage2(BasePage):
    # 实例化search_sql类
    def instance_search_sql(self):
        search_sql = SearchSql(self.driver, self.base_url)
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

    # 总计--出卫星盲区报警数
    def get_out_satellite_dead_zone_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[5]

    # 列表--出卫星盲区报警数
    def get_list_out_satellite_dead_zone_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollHead"]/table/thead/tr/th[3]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[3]' % str(n + 1))
        return number

    # 总计--开机报警数
    def get_starting_up_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[7]

    # 列表--开机报警数
    def get_list_starting_up_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollHead"]/table/thead/tr/th[4]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[4]' % str(n + 1))
        return number

    # 总计--后视镜震动报警数
    def get_rearview_mirror_vibration_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[9]

    # 列表--后视镜震动报警数
    def get_list_rearview_mirror_vibration_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollHead"]/table/thead/tr/th[5]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[5]' % str(n + 1))
        return number

    # 总计--卫星第一次定位报警数
    def get_satellite_first_positioning_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[11]

    # 列表--卫星第一次定位报警数
    def get_list_satellite_first_positioning_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[6]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[6]' % str(n + 1))
        return number

    # 总计--外电低电报警数
    def get_outer_low_electricity_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[13]

    # 列表--外电低电报警数
    def get_list_outer_low_electricity_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[7]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[7]' % str(n + 1))
        return number

    # 总计--外电低电保护报警数
    def get_outer_low_electricity_protect_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[15]

    # 列表--外电低电保护报警数
    def get_list_outer_low_electricity_protect_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[8]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[8]' % str(n + 1))
        return number

    # 总计--换卡报警数
    def get_change_card_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[17]

    # 列表--换卡报警数
    def get_list_change_card_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[9]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[9]' % str(n + 1))
        return number

    # 总计--关机报警数
    def get_shutdown_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[19]

    # 列表--关机报警数
    def get_list_shutdown_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[10]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[10]' % str(n + 1))
        return number

    # 总计--外电低电保护后飞行模式报警数
    def get_flight_mode_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[21]

    # 列表--外电低电保护后飞行模式报警数
    def get_list_flight_mode_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[11]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[11]' % str(n + 1))
        return number

    # 总计--拆卸报警数
    def get_disassembly_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[23]

    # 列表--拆卸报警数
    def get_list_disassembly_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[12]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[12]' % str(n + 1))
        return number

    # 总计--非法移动报警数
    def get_illegal_move_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[25]

    # 列表--非法移动报警数
    def get_list_illegal_move_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[13]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[13]' % str(n + 1))
        return number

    # 总计--后备电池电量不足告警数
    def get_reserve_battery_low_battery_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[27]

    # 列表--后备电池电量不足告警数
    def get_list_reserve_battery_low_battery_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[14]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[14]' % str(n + 1))
        return number

    # 总计--越界告警数
    def get_across_boundaries_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[29]

    # 列表--越界告警数
    def get_list_across_boundaries_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[15]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[15]' % str(n + 1))
        return number

    # 总计--断电报警数
    def get_power_outages_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[31]

    # 列表--断电报警数
    def get_list_power_outages_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[16]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[16]' % str(n + 1))
        return number

    # 总计--声控报警数
    def get_acoustic_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[33]

    # 列表--声控报警数
    def get_list_acoustic_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[17]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[17]' % str(n + 1))
        return number

    # 总计--伪基站报警数
    def get_pseudo_base_station_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[35]

    # 列表--伪基站报警数
    def get_list_pseudo_base_station_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[18]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[18]' % str(n + 1))
        return number

    # 总计--震动报警数
    def get_vibration_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[37]

    # 列表--震动报警数
    def get_list_vibration_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[19]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[19]' % str(n + 1))
        return number

    # 总计--进入电子围栏报警数
    def get_enter_electronic_fence_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[39]

    # 列表--进入电子围栏报警数
    def get_list_enter_electronic_fence_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[20]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[20]' % str(n + 1))
        return number

    # 总计--离开电子围栏报警数
    def get_leave_electronic_fence_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[41]

    # 列表--离开电子围栏报警数
    def get_list_leave_electronic_fence_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[21]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[21]' % str(n + 1))
        return number

    # 总计--超速报警数
    def get_super_speed_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[43]

    # 列表--超速报警数
    def get_list_super_speed_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[22]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[22]' % str(n + 1))
        return number

    # 总计--位移报警数
    def get_displacement_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[45]

    # 列表--位移报警数
    def get_list_displacement_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[23]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[23]' % str(n + 1))
        return number

    # 总计--低电报警数
    def get_low_electricity_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[47]

    # 列表--低电报警数
    def get_list_low_electricity_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[24]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[24]' % str(n + 1))
        return number

    # 总计--ACC关闭数
    def get_acc_close_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[49]

    # 列表--ACC关闭数
    def get_list_acc_close_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[25]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[25]' % str(n + 1))
        return number

    # 总计--ACC打开数
    def get_acc_open_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[51]

    # 列表--ACC打开数
    def get_list_acc_open_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[26]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[26]' % str(n + 1))
        return number

    # 总计--进入围栏数
    def get_enter_fence_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[53]

    # 列表--进入围栏数
    def get_list_enter_fence_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[27]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[27]' % str(n + 1))
        return number

    # 总计--离线告警数
    def get_offline_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[55]

    # 列表--离线告警数
    def get_list_offline_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[28]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[28]' % str(n + 1))
        return number

    # 总计--离开围栏数
    def get_leave_fence_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[57]

    # 列表--离开围栏数
    def get_list_leave_fence_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[29]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[29]' % str(n + 1))
        return number

    # 总计--黑车围栏数
    def get_illegal_taxis_fence_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[59]

    # 列表--黑车围栏数
    def get_list_illegal_taxis_fence_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[30]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[30]' % str(n + 1))
        return number

    # 总计--停留告警数
    def get_stay_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[61]

    # 列表--停留告警数
    def get_list_stay_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[31]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[31]' % str(n + 1))
        return number

    # 总计--长时间不进数
    def get_long_time_not_enter_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[63]

    # 列表--长时间不进数
    def get_list_long_time_not_enter_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[32]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[32]' % str(n + 1))
        return number

    # 总计--长时间不出数
    def get_long_time_not_out_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[65]

    # 列表--长时间不出数
    def get_list_long_time_not_out_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[33]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[33]' % str(n + 1))
        return number

    def get_imei(self):
        return '123456780012355'

    def get_shut_down_imei(self):
        return '121201230052520'

    def input_imei_to_search_in_mileage_form(self, imei):
        self.driver.operate_input_element('x,//*[@id="imeiInput_travelReport"]', imei)
        self.driver.click_element('x,//*[@id="TravelFrom"]/div[2]/div[2]/div/div/div/div[1]/span/button')
        sleep(5)

    def input_imei_to_search_in_speed_form(self, imei):
        self.driver.operate_input_element('x,//*[@id="imeiInput_overSpeedReport"]', imei)
        self.driver.click_element('x,//*[@id="OverspeedFrom"]/div[2]/div[2]/div/div/div/div[1]/span/button')
        sleep(5)

    def input_imei_to_search_in_stay_form(self, imei):
        self.driver.operate_input_element('x,//*[@id="imeiInput_stopCar"]', imei)
        self.driver.click_element('x,//*[@id="StopCarFrom"]/div[2]/div[2]/div/div/div/div[1]/span/button')
        sleep(5)

    def input_imei_to_search_in_paking_form(self, imei):
        self.driver.operate_input_element('x,//*[@id="imeiInput_stopNotOff"]', imei)
        self.driver.click_element('x,//*[@id="stopNotOffFrom"]/div[2]/div[2]/div/div/div/div[1]/span/button')
        sleep(5)

    def input_imei_to_search_in_acc_form(self, imei):
        self.driver.operate_input_element('x,//*[@id="imeiInput_acc"]', imei)
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[1]/span/button')
        sleep(5)

    def input_imei_to_search_in_alarm_overview_form(self, imei):
        self.driver.operate_input_element('x,//*[@id="imeiInput_alarmOverview"]', imei)
        self.driver.click_element('x,//*[@id="alarmForm"]/div/div[4]/div/div[1]/div/div[1]/span/button')
        sleep(5)

    def mileage_form_validation_times(self, type):
        iframe = "mileageReportFrame"
        start = "startTime_mileage"
        end = "endTime_mileage"
        pull_down = "x,//*[@id='dateSelect_div']/div/span[2]"
        today = "x,//*[@id='dateSelect_div']/div/div/ul/li[2]"
        yesterday = "x,//*[@id='dateSelect_div']/div/div/ul/li[3]"
        this_week = "x,//*[@id='dateSelect_div']/div/div/ul/li[4]"
        last_week = "x,//*[@id='dateSelect_div']/div/div/ul/li[5]"
        this_month = "x,//*[@id='dateSelect_div']/div/div/ul/li[6]"
        last_month = "x,//*[@id='dateSelect_div']/div/div/ul/li[7]"
        random = "x,//*[@id='dateSelect_div']/div/div/ul/li[1]"
        time = self.sport_statistical_validation_times(type, iframe, start, end, pull_down, yesterday,
                                                       this_week, last_week, this_month, last_month, random, today)
        return time

    def input_imei_to_search_in_mileage_forms(self, imei):
        self.driver.operate_input_element('x,//*[@id="imeiInput_mileageReport"]', imei)
        self.driver.click_element('x,//*[@id="MileageFrom"]/div[2]/div[2]/div/div/div/div[1]/span/button')
        sleep(5)

    def sport_statistical_validation_times(self, type, iframe, start, end, pull_down, yesterday, this_week, last_week,
                                           this_month, last_month, random, today):
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
            sql_end_time = search_sql.get_today_end_times()
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
            sql_end_time = search_sql.get_today_end_times()
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
            sql_end_time = search_sql.get_today_end_times()
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

    def input_imei_to_search_in_alarm_detail_form(self, imei):
        self.driver.operate_input_element('x,//*[@id="imeiInput_alarmDetail"]', imei)
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/span/button')
        sleep(5)

    def get_search_imei_in_mileage_form(self):
        text = self.driver.get_text('x,//*[@id="dev_tree_travelReport_1_span"]')
        return text.split('[')[1].split(']')[0]

    def get_dev_user_name(self):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_tuqiang_sql()
        cursor = connect.cursor()
        sql = "SELECT o.nickName FROM equipment_mostly m INNER JOIN user_info o on m.userId = o.userId WHERE m.imei = %s;" % self.get_imei()
        cursor.execute(sql)
        data = cursor.fetchall()
        user_name = data[0][0]
        cursor.close()
        connect.close()
        return user_name

    def get_dev_user_name_web(self):
        return self.driver.get_element('x,//*[@id="search_text"]').get_attribute('value').split('(')[0]

    def get_search_imei_in_speed_form(self):
        text = self.driver.get_text('x,//*[@id="dev_tree_overSpeedReport_1_span"]')
        return text.split('[')[1].split(']')[0]

    def get_search_imei_in_stay_form(self):
        text = self.driver.get_text('x,//*[@id="dev_tree_stopCar_1_span"]')
        return text.split('[')[1].split(']')[0]

    def get_search_imei_in_paking_form(self):
        text = self.driver.get_text('x,//*[@id="dev_tree_stopNotOff_1_span"]')
        return text.split('[')[1].split(']')[0]

    def get_search_imei_in_acc_form(self):
        text = self.driver.get_text('x,//*[@id="dev_tree_acc_1_span"]')
        return text.split('[')[1].split(']')[0]

    def get_search_imei_in_alarm_overview_form(self):
        text = self.driver.get_text('x,//*[@id="dev_tree_alarmOverview_1_span"]')
        return text.split('[')[1].split(']')[0]

    def get_search_imei_in_mileage_forms(self):
        text = self.driver.get_text('x,//*[@id="dev_tree_mileageReport_1_a"]')
        return text.split('[')[1].split(']')[0]

    def get_search_imei_in_alarm_detail_forms(self):
        text = self.driver.get_text('x,//*[@id="dev_tree_alarmDetail_1_span"]')
        return text.split('[')[1].split(']')[0]

    def get_no_active_imei(self):
        return '358740051670098'
