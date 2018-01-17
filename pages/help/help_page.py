from time import sleep
from automate_driver.automate_driver_server import AutomateDriverServer
from model.connect_sql import ConnectSql
from pages.base.base_page_server import BasePageServer
from pages.base.new_paging import NewPaging


# 帮助页面
# author：邓肖斌
class HelpPage(BasePageServer, NewPaging):
    def __init__(self, driver: AutomateDriverServer, base_url):
        super().__init__(driver, base_url)

    # 点击帮助
    def click_help(self):
        self.driver.click_element('x,/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a[2]')
        sleep(2)

    # 点击业务日志
    def click_business_log(self):
        self.driver.click_element('x,//*[@id="servicelogReport"]/a')
        sleep(2)

    # 点击客户管理（默认-修改）
    def log_cust_modify(self):
        self.driver.switch_to_frame('x,//*[@id="servicelogReportFrame"]')
        self.driver.click_element('x,//*[@id="tab_nav_business"]/li[2]/a')
        sleep(2)
        self.driver.default_frame()

    # 点击登录日志
    def click_log_in_log(self):
        self.driver.click_element('x,//*[@id="loginReport"]/a')
        sleep(2)

    # 设备管理################################################################################################################

    # 搜索设备管理日志
    def search_equipment_manager_log(self, search_data):
        self.driver.switch_to_frame('x,//*[@id="servicelogReportFrame"]')
        if search_data['type'] == '1':
            self.driver.click_element('x,//*[@id="devDiv_modify_1"]')
        if search_data['type'] == '5':
            self.driver.click_element('x,//*[@id="devDiv_allot_5"]')

        # 填写开始时间，结束时间
        js = 'document.getElementById("createTimeStart_xf").removeAttribute("readonly")'
        self.driver.execute_js(js)
        if search_data['begin_time'] != '':
            self.driver.operate_input_element('x,//*[@id="createTimeStart_xf"]', search_data['begin_time'])
            sleep(1)
            self.driver.click_element('x,//*[@id="selectUserName_xf"]')
            sleep(1)
        if search_data['begin_time'] == '':
            self.driver.click_element('x,//*[@id="createTimeStart_xf"]')
            sleep(1)
            self.driver.click_element('x,//*[@id="laydate_clear"]')
            sleep(1)

        js = 'document.getElementById("createTimeEnd_xf").removeAttribute("readonly")'
        self.driver.execute_js(js)
        if search_data['end_time'] != '':
            self.driver.operate_input_element('x,//*[@id="createTimeEnd_xf"]', search_data['end_time'])
            sleep(1)
            self.driver.click_element('x,//*[@id="selectUserName_xf"]')
            sleep(1)
        if search_data['end_time'] == '':
            self.driver.click_element('x,//*[@id="createTimeEnd_xf"]')
            sleep(1)
            self.driver.click_element('x,//*[@id="laydate_clear"]')
            sleep(1)

        # 填写其他的搜索条件
        self.driver.operate_input_element('x,//*[@id="selectUserName_xf"]', search_data['more'])
        sleep(30)
        self.driver.click_element('x,/html/body/div/div/div[2]/div[1]/div[1]/form/div[2]/div/span')
        sleep(30)
        self.driver.default_frame()

    # 获取当前的业务日志个数
    def get_current_business_log(self):
        self.driver.switch_to_frame('x,//*[@id="servicelogReportFrame"]')
        a = self.driver.get_element('x,//*[@id="paging_xf"]').get_attribute('style')
        if a == 'display: block;':
            total = self.get_equipment_manager_log_total_number('x,//*[@id="paging_xf"]', 'x,//*[@id="logslist_xf"]')
            self.driver.default_frame()
            return total
        elif a == 'display: none;':
            self.driver.default_frame()
            return 0

    # 获取设备管理日志总共有多少条记录
    def get_equipment_manager_log_total_number(self, param, param1):
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
                    sleep(40)
                    self.driver.get_text('l,下一页') == '下一页'
                    continue
                except:
                    sleep(10)
                    break

            # 获取最后一页前一页的页码
            page_01 = self.get_li_total_number(param)
            pages = self.driver.get_text(param + "/ul/li[" + str(int(page_01)) + "]/a")
            # 获取最后一页总共有多少条记录
            last_page_number = self.get_last_page_number(param1)

            # 计算总共有多少条记录
            total = int(pages) * 10 + last_page_number
            print(int(pages))
            return total

            # 客户管理###############################################################################################################

    # 搜索客户管理日志
    def search_customer_manager_log(self, search_data):
        self.driver.switch_to_frame('x,//*[@id="servicelogReportFrame"]')
        # 添加
        if search_data['type'] == '0':
            self.driver.click_element('x,//*[@id="custDiv"]/button[2]')
        # 修改
        elif search_data['type'] == '1':
            self.driver.click_element('x,//*[@id="custDiv"]/button[1]')
        # 删除
        elif search_data['type'] == '2':
            self.driver.click_element('x,//*[@id="custDiv"]/button[3]')
        # 修改密码
        elif search_data['type'] == '3':
            self.driver.click_element('x,//*[@id="custDiv"]/button[4]')
        # 重置密码
        elif search_data['type'] == '4':
            self.driver.click_element('x,//*[@id="custDiv"]/button[5]')
        sleep(10)

        # 填写开始时间，结束时间
        js = 'document.getElementById("createTimeStart_fp").removeAttribute("readonly")'
        self.driver.execute_js(js)
        if search_data['begin_time'] != '':
            self.driver.operate_input_element('x,//*[@id="createTimeStart_fp"]', search_data['begin_time'])
            sleep(1)
            self.driver.click_element('x,//*[@id="selectUserName_fp"]')
            sleep(1)
        if search_data['begin_time'] == '':
            self.driver.click_element('x,//*[@id="createTimeStart_fp"]')
            sleep(1)
            self.driver.click_element('x,//*[@id="laydate_clear"]')
            sleep(1)

        js = 'document.getElementById("createTimeEnd_fp").removeAttribute("readonly")'
        self.driver.execute_js(js)
        if search_data['end_time'] != '':
            self.driver.operate_input_element('x,//*[@id="createTimeEnd_fp"]', search_data['end_time'])
            sleep(1)
            self.driver.click_element('x,//*[@id="selectUserName_fp"]')
            sleep(1)
        if search_data['end_time'] == '':
            self.driver.click_element('x,//*[@id="createTimeEnd_fp"]')
            sleep(1)
            self.driver.click_element('x,//*[@id="laydate_clear"]')
            sleep(1)

        # 填写其他的搜索条件
        self.driver.operate_input_element('x,//*[@id="selectUserName_fp"]', search_data['more'])

        self.driver.click_element('x,//*[@id="search_fp"]')
        sleep(15)
        self.driver.default_frame()

    # 获取当前的业务日志-客户管理日志个数
    def get_current_customer_log(self):
        # 设置列表底部每页共10条
        self.driver.switch_to_frame('x,//*[@id="servicelogReportFrame"]')
        a = self.driver.get_element('x,//*[@id="paging_xf"]').get_attribute('style')

        if a == 'display: block;':
            total = self.get_customer_manager_log_total_number('x,//*[@id="paging_xf"]', 'x,//*[@id="logslist_xf"]')
            self.driver.default_frame()
            return total
        elif a == 'display: none;':
            self.driver.default_frame()
            return 0

    def get_customer_manager_log_total_number(self, selector_li, selector_tr):
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
            total = int(pages) * 10 + last_page_number
            return total

            # 登录日志###############################################################################################################

    # 搜索登录日志
    def search_login_log(self, search_data):
        self.driver.switch_to_frame('x,//*[@id="loginReportFrame"]')
        self.driver.operate_input_element('x,//*[@id="loginAccount_sport"]', search_data['account'])
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="startTime_sport"]', search_data['begin_time'])
        sleep(1)
        self.driver.click_element('x,//*[@id="loginAccount_sport"]')
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="endTime_sport"]', search_data['end_time'])
        sleep(1)
        self.driver.click_element('x,//*[@id="loginAccount_sport"]')
        sleep(1)
        self.driver.click_element('x,/html/body/div/div/div[2]/div/div[1]/form/div/div/span')
        sleep(15)
        self.driver.default_frame()

    # 获取登录日志的条数
    def get_current_login_log(self):

        self.driver.switch_to_frame('x,//*[@id="loginReportFrame"]')
        a = self.driver.get_element('x,//*[@id="paging_login_log"]').get_attribute('style')

        if a == 'display: block;':
            total = self.get_login_log_total_number('x,//*[@id="paging_login_log"]', 'x,//*[@id="loginLog-tbody"]')
            self.driver.default_frame()
            return total
        elif a == 'display: none;':
            self.driver.default_frame()
            return 0

    def get_login_log_total_number(self, param, param1):
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
                    sleep(20)
                    self.driver.get_text('l,下一页') == '下一页'
                    continue
                except:
                    sleep(10)
                    break

            # 获取最后一页前一页的页码
            page_01 = self.get_li_total_number(param)
            pages = self.driver.get_text(param + "/ul/li[" + str(int(page_01)) + "]/a")
            # 获取最后一页总共有多少条记录
            last_page_number = self.get_last_page_number(param1)

            # 计算总共有多少条记录
            total = int(pages) * 10 + last_page_number
            print(int(pages))
            return total

            # 业务日志###############################################################################################################

    # 搜索业务日志
    def search_business_log(self, search_data):

        # 选择业务日志类型
        self.driver.switch_to_frame('x,//*[@id="servicelogReportFrame"]')
        self.driver.click_element('x,//*[@id="serviceType"]/div/span[2]')
        sleep(2)
        if search_data["search_type"] == '设备管理-设备修改':
            self.driver.click_element('x,//*[@id="serviceType"]/div/div/ul/li[1]')
            sleep(2)
            self.driver.click_element('x,//*[@id="logType"]/div/span[2]')
            sleep(1)
            self.driver.click_element('x,//*[@id="logType"]/div/div/ul/li[1]')
            sleep(2)
        elif search_data["search_type"] == '设备管理-设备分配':
            self.driver.click_element('x,//*[@id="serviceType"]/div/div/ul/li[1]')
            sleep(2)
            self.driver.click_element('x,//*[@id="logType"]/div/span[2]')
            sleep(1)
            self.driver.click_element('x,//*[@id="logType"]/div/div/ul/li[2]')
            sleep(2)
        elif search_data["search_type"] == '客户管理-新增客户':
            self.driver.click_element('x,//*[@id="serviceType"]/div/div/ul/li[2]')
            sleep(2)
            self.driver.click_element('x,//*[@id="logType"]/div/span[2]')
            sleep(1)
            self.driver.click_element('x,//*[@id="logType"]/div/div/ul/li[1]')
            sleep(2)
        elif search_data["search_type"] == '客户管理-修改用户信息':
            self.driver.click_element('x,//*[@id="serviceType"]/div/div/ul/li[2]')
            sleep(2)
            self.driver.click_element('x,//*[@id="logType"]/div/span[2]')
            sleep(1)
            self.driver.click_element('x,//*[@id="logType"]/div/div/ul/li[2]')
            sleep(2)
        elif search_data["search_type"] == '客户管理-删除用户信息':
            self.driver.click_element('x,//*[@id="serviceType"]/div/div/ul/li[2]')
            sleep(2)
            self.driver.click_element('x,//*[@id="logType"]/div/span[2]')
            sleep(1)
            self.driver.click_element('x,//*[@id="logType"]/div/div/ul/li[3]')
            sleep(2)
        elif search_data["search_type"] == '客户管理-修改密码':
            self.driver.click_element('x,//*[@id="serviceType"]/div/div/ul/li[2]')
            sleep(2)
            self.driver.click_element('x,//*[@id="logType"]/div/span[2]')
            sleep(1)
            self.driver.click_element('x,//*[@id="logType"]/div/div/ul/li[4]')
            sleep(2)
        elif search_data["search_type"] == '客户管理-重置密码':
            self.driver.click_element('x,//*[@id="serviceType"]/div/div/ul/li[2]')
            sleep(2)
            self.driver.click_element('x,//*[@id="logType"]/div/span[2]')
            sleep(1)
            self.driver.click_element('x,//*[@id="logType"]/div/div/ul/li[5]')
            sleep(2)
        elif search_data["search_type"] == '客户管理-转移客户':
            self.driver.click_element('x,//*[@id="serviceType"]/div/div/ul/li[2]')
            sleep(2)
            self.driver.click_element('x,//*[@id="logType"]/div/span[2]')
            sleep(1)
            self.driver.click_element('x,//*[@id="logType"]/div/div/ul/li[6]')
            sleep(2)
        elif search_data["search_type"] == '安全区域-新增、编辑区域':
            self.driver.click_element('x,//*[@id="serviceType"]/div/div/ul/li[3]')
            sleep(2)
            self.driver.click_element('x,//*[@id="logType"]/div/span[2]')
            sleep(1)
            self.driver.click_element('x,//*[@id="logType"]/div/div/ul/li[1]')
            sleep(2)
        elif search_data["search_type"] == '安全区域-删除区域':
            self.driver.click_element('x,//*[@id="serviceType"]/div/div/ul/li[3]')
            sleep(2)
            self.driver.click_element('x,//*[@id="logType"]/div/span[2]')
            sleep(1)
            self.driver.click_element('x,//*[@id="logType"]/div/div/ul/li[2]')
            sleep(2)
        elif search_data["search_type"] == '安全区域-关联设备':
            self.driver.click_element('x,//*[@id="serviceType"]/div/div/ul/li[3]')
            sleep(2)
            self.driver.click_element('x,//*[@id="logType"]/div/span[2]')
            sleep(1)
            self.driver.click_element('x,//*[@id="logType"]/div/div/ul/li[3]')
            sleep(2)
        elif search_data["search_type"] == '告警设置-推送设置':
            self.driver.click_element('x,//*[@id="serviceType"]/div/div/ul/li[4]')
            sleep(2)
            self.driver.click_element('x,//*[@id="logType"]/div/span[2]')
            sleep(1)
            self.driver.click_element('x,//*[@id="logType"]/div/div/ul/li[1]')
            sleep(2)

        # 填写开始时间，结束时间
        js = 'document.getElementById("createTimeStart_xf").removeAttribute("readonly")'
        self.driver.execute_js(js)
        '''if search_data['begin_time'] != '':
            self.driver.operate_input_element('x,//*[@id="createTimeStart_xf"]', search_data['begin_time'])
            sleep(1)
            self.driver.click_element('x,//*[@id="key"]')
            sleep(1)
        if search_data['begin_time'] == '':
            self.driver.click_element('x,//*[@id="createTimeStart_xf"]')
            sleep(1)
            self.driver.click_element('x,//*[@id="laydate_clear"]')
            sleep(1)'''
        self.driver.operate_input_element('x,//*[@id="createTimeStart_xf"]', search_data['begin_time'])

        js = 'document.getElementById("createTimeEnd_xf").removeAttribute("readonly")'
        self.driver.execute_js(js)
        '''if search_data['end_time'] != '':
            self.driver.operate_input_element('x,//*[@id="createTimeEnd_xf"]', search_data['end_time'])
            sleep(1)
            self.driver.click_element('x,//*[@id="key"]')
            sleep(1)
        if search_data['end_time'] == '':
            self.driver.click_element('x,//*[@id="createTimeEnd_xf"]')
            sleep(1)
            self.driver.click_element('x,//*[@id="laydate_clear"]')
            sleep(1)'''
        self.driver.operate_input_element('x,//*[@id="createTimeEnd_xf"]', search_data['end_time'])

        # 填写其他的搜索条件
        try:
            self.driver.operate_input_element('x,//*[@id="createdAccount"]', search_data['operation_account'])
        except:
            pass
        try:
            self.driver.operate_input_element('x,//*[@id="account"]', search_data['account'])
        except:
            pass
        try:
            self.driver.operate_input_element('x,//*[@id="imei"]', search_data['imei'])
        except:
            pass

        # 点搜索
        self.driver.click_element('x,//*[@id="search_xf"]')
        sleep(15)
        self.driver.default_frame()

    def get_all_user_id(self, current_account):
        self.connect_sql = ConnectSql()
        connect = self.connect_sql.connect_tuqiang_sql()
        # 创建数据库游标
        cursor = connect.cursor()
        get_id_sql = "select o.userId,o.fullParentId from user_info o where o.account = '" + current_account + "';"
        cursor.execute(get_id_sql)
        current_user_id_data = cursor.fetchall()
        current_user_id = current_user_id_data[0][0]
        full_parent_id = current_user_id_data[0][1]

        get_all_user_id_sql = "select o.userId from user_info o where o.fullParentId LIKE '" + full_parent_id + current_user_id + "%';"
        cursor.execute(get_all_user_id_sql)
        all_user_id = []
        data = cursor.fetchall()
        for range in data:
            for range1 in range:
                all_user_id.append(range1)
        all_user_id.append(current_user_id)
        cursor.close()
        connect.close()
        return tuple(all_user_id)

    def get_search_log_in_log_query_data(self, all_user_id, search_data):
        should = []
        for id in all_user_id:
            should.append({
                "match": {
                    "loginUserId": {
                        "query": id,
                        "type": "phrase"
                    }
                }
            })
        must = [{
            "bool": {
                "should": should
            }
        }]
        if search_data['begin_time'] != '' and search_data['end_time'] != "":
            must.append({
                "range": {
                    "loginTime": {
                        "from": search_data['begin_time'] + ":00",
                        "to": search_data['end_time'] + ":59",
                        "include_lower": True,
                        "include_upper": True
                    }
                }
            })
        elif search_data['begin_time'] != '' and search_data['end_time'] == "":
            must.append({
                "range": {
                    "loginTime": {
                        "from": search_data['begin_time'] + ":00",
                        "to": None,
                        "include_lower": True,
                        "include_upper": True
                    }
                }
            })
        elif search_data['begin_time'] == '' and search_data['end_time'] != "":
            must.append({
                "range": {
                    "loginTime": {
                        "from": None,
                        "to": search_data['end_time'] + ":59",
                        "include_lower": True,
                        "include_upper": True
                    }
                }
            })
        if search_data['account'] != "":
            must.append({
                "wildcard": {
                    "loginAccount": "*" + search_data['account'] + "*"
                }
            })

        query = {
            "bool": {
                "filter": {
                    "bool": {
                        "must": {
                            "bool": {
                                "must": must
                            }
                        }
                    }
                }
            }
        }
        return query

    def get_search_operation_log_query_data(self, all_user_id, search_data):
        should = []
        for id in all_user_id:
            should.append({
                "match": {
                    "createdBy": {
                        "query": id,
                        "type": "phrase"
                    }
                }
            })
        must = [{
            "bool": {
                "should": should
            }
        }]
        if search_data['begin_time'] != '' and search_data['end_time'] != "":
            must.append({
                "range": {
                    "creationDate": {
                        "from": search_data['begin_time'] + ":00",
                        "to": search_data['end_time'] + ":59",
                        "include_lower": True,
                        "include_upper": True
                    }
                }
            })

        if search_data["search_type"] == '设备管理-设备修改':
            must.append({
                "match": {
                    "serviceType": {
                        "query": "1",
                        "type": "phrase"
                    }
                }
            })
            must.append({
                "match": {
                    "operType": {
                        "query": "1",
                        "type": "phrase"
                    }
                }
            })

        if search_data["search_type"] == '设备管理-设备分配':
            must.append({
                "match": {
                    "serviceType": {
                        "query": "1",
                        "type": "phrase"
                    }
                }
            })
            must.append({
                "match": {
                    "operType": {
                        "query": "5",
                        "type": "phrase"
                    }
                }
            })

        if search_data["search_type"] == '客户管理-新增客户':
            must.append({
                "match": {
                    "serviceType": {
                        "query": "2",
                        "type": "phrase"
                    }
                }
            })
            must.append({
                "match": {
                    "operType": {
                        "query": "0",
                        "type": "phrase"
                    }
                }
            })

        if search_data["search_type"] == '客户管理-修改用户信息':
            must.append({
                "match": {
                    "serviceType": {
                        "query": "2",
                        "type": "phrase"
                    }
                }
            })
            must.append({
                "match": {
                    "operType": {
                        "query": "1",
                        "type": "phrase"
                    }
                }
            })

        if search_data["search_type"] == '客户管理-删除用户信息':
            must.append({
                "match": {
                    "serviceType": {
                        "query": "2",
                        "type": "phrase"
                    }
                }
            })
            must.append({
                "match": {
                    "operType": {
                        "query": "2",
                        "type": "phrase"
                    }
                }
            })

        if search_data["search_type"] == '客户管理-修改密码':
            must.append({
                "match": {
                    "serviceType": {
                        "query": "2",
                        "type": "phrase"
                    }
                }
            })
            must.append({
                "match": {
                    "operType": {
                        "query": "3",
                        "type": "phrase"
                    }
                }
            })

        if search_data["search_type"] == '客户管理-重置密码':
            must.append({
                "match": {
                    "serviceType": {
                        "query": "2",
                        "type": "phrase"
                    }
                }
            })
            must.append({
                "match": {
                    "operType": {
                        "query": "4",
                        "type": "phrase"
                    }
                }
            })

        if search_data["search_type"] == '客户管理-转移客户':
            must.append({
                "match": {
                    "serviceType": {
                        "query": "2",
                        "type": "phrase"
                    }
                }
            })
            must.append({
                "match": {
                    "operType": {
                        "query": "5",
                        "type": "phrase"
                    }
                }
            })

        if search_data["search_type"] == '安全区域-新增、编辑区域':
            must.append({
                "match": {
                    "serviceType": {
                        "query": "3",
                        "type": "phrase"
                    }
                }
            })
            must.append({
                "match": {
                    "operType": {
                        "query": "1",
                        "type": "phrase"
                    }
                }
            })

        if search_data["search_type"] == '安全区域-删除区域':
            must.append({
                "match": {
                    "serviceType": {
                        "query": "3",
                        "type": "phrase"
                    }
                }
            })
            must.append({
                "match": {
                    "operType": {
                        "query": "2",
                        "type": "phrase"
                    }
                }
            })

        if search_data["search_type"] == '安全区域-关联设备':
            must.append({
                "match": {
                    "serviceType": {
                        "query": "3",
                        "type": "phrase"
                    }
                }
            })
            must.append({
                "match": {
                    "operType": {
                        "query": "3",
                        "type": "phrase"
                    }
                }
            })

        if search_data["search_type"] == '告警设置-推送设置':
            must.append({
                "match": {
                    "serviceType": {
                        "query": "4",
                        "type": "phrase"
                    }
                }
            })
            must.append({
                "match": {
                    "operType": {
                        "query": "1",
                        "type": "phrase"
                    }
                }
            })
        if search_data['account'] != "":
            must.append({
                "match": {
                    "account": {
                        "query": search_data['account'],
                        "type": "phrase"
                    }
                }
            })
        if search_data['operation_account'] != "":
            must.append({
                "match": {
                    "account": {
                        "query": search_data['operation_account'],
                        "type": "phrase"
                    }
                }
            })
        if search_data['imei'] != "":
            must.append({
                "match": {
                    "account": {
                        "query": search_data['imei'],
                        "type": "phrase"
                    }
                }
            })
        query = {
            "bool": {
                "filter": {
                    "bool": {
                        "must": {
                            "bool": {
                                "must": must
                            }
                        }
                    }
                }
            }
        }
        return query
