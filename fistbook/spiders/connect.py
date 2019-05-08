import pymysql


def getConnect():
    connection = pymysql.connect(
        host='47.106.74.12',  # 连接的是本地数据库
        user='bookadmin',        # 自己的mysql用户名
        passwd='book',  # 自己的密码
        db='collectnovel',      # 数据库的名字
        charset='utf8mb4',     # 默认的编码方式：
        cursorclass=pymysql.cursors.DictCursor)
    return connection
def testss():
    con = getConnect()
    with con.cursor() as cursor:
        sql1 = 'Create Table If Not Exists %s(id int,zjm varchar(20),body text)' % '最强特种兵王'
        cursor.execute(sql1)
    con.commit()
    con.close()
'''
if __name__ == '__main__':
    testss()
'''
