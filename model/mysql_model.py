import pymysql


class DBHelper(object):
    def read_db_for_mysql(self):
        # 创建连接
        connect = pymysql.connect(host="",
                                  port=3306,
                                  user="",
                                  passwd="",
                                  db="")

        # 创建数据库游标
        cur = connect.cursor()

        # 执行sql脚本
        cur.execute("select account,realname from sys_user limit 0,1000;")

        # 读取数据
        data = cur.fetchall()

        # 遍历数据
        for row in data:
            user = {
                "account": row[0],
                "realname": row[1]
            }

        # 关闭游标和连接
        cur.close()
        connect.close()
