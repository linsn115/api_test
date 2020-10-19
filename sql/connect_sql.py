import pymysql

#获取链接方法

def get_db_conn():
    conn =pymysql.connect(host='192.168.2.73',
                      user="root",
                      port=3306,
                      password='123456',
                      db='lxsj',
                      charset='utf8')
    return conn

#封装数据库查询操作

def query_db(sql):
    conn = get_db_conn()
    # 建立游标
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result



#查询


#获取查询结果
result =query_db("select *from blade_user where phone='18657186386'")
print(type(result))
print(result)

#提交更改
