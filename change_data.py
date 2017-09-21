import pymysql


class ChangeData(object):
    # 为了切换测试和线上环境准备
    def switch_tuqiang_url(self):
        # 测试
        return 'http://172.16.0.116:8690'
        # return 'http://tujunsat.jimicloud.com'

        # 线上
        # return 'http://120.76.232.176:8180'
        # return 'http://www.tuqiangol.com'

        # 天眼在线测试
        # return 'http://www.skyzaixian.com:8680'
        # 天眼在线线上
        # return 'http://www.skyzaixian.com'

    def switch_tuqiang_mysql(self):
        # 测试
        connect = pymysql.connect(
            host='172.16.10.103',
            port=3306,
            user='root',
            passwd='123456',
            db='tracker-web',
            charset='utf8'
        )
        return connect

        # 线上
        '''connect = pymysql.connect(
            host='120.24.75.214',
            port=3306,
            user='tuqiang_query',
            passwd='tuqiang_query',
            db='tracker-web',
            charset='utf8'
        )
        return connect'''

    def switch_tuqiang_form_mysql(self):
        # 测试
        connect = pymysql.connect(
            host='172.16.0.116',
            port=8066,
            user='jimi',
            passwd='jimi',
            db='his',
            charset='utf8'
        )
        return connect

        # 线上
        '''connect = pymysql.connect(
            host='119.23.127.137',
            port=8066,
            user='test',
            passwd='test@123',
            db='his',
            charset='utf8'
        )
        return connect'''
