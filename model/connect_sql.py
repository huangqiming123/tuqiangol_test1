import pymysql


class ConnectSql(object):

    def connect_tuqiang_sql(self):

        # 连接图强的第一台数据库
        connect = pymysql.connect(
            host='120.24.75.214',
            port=3306,
            user='tuqiang_query',
            passwd='tuqiang_query',
            db='tracker-web',
            charset='utf8'
        )
        return connect

    def connect_tuqiang_form(self):
        # 链接图强在线第二台数据库，主要查报表、告警
        connect = pymysql.connect(
            host='119.23.127.137',
            port=8066,
            user='test',
            passwd='test@123',
            db='his',
            charset='utf8'
        )
        return connect


'''
    def connect_tuqiang_sql(self):
        # 连接图强测试环境的第一台数据库
        connect = pymysql.connect(
            host='172.16.0.110',
            port=3306,
            user='root',
            passwd='123456',
            db='tracker-web',
            charset='utf8'
        )
        return connect

    def connect_tuqiang_form(self):
        # 链接图强在线第二台数据库，主要查报表、告警
        connect = pymysql.connect(
            host='172.16.0.116',
            port=8066,
            user='jimi',
            passwd='jimi',
            db='his',
            charset='utf8'
        )
        return connect'''
