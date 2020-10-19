import pymysql
from config import readConfig
class DB:
    def __init__(self):
        host = readConfig.getConfig("SQL","host")
        print(host)
        user = readConfig.getConfig("SQL", "user")
        print(user)
        port = readConfig.getConfig("SQL", "port")
        print(port)
        password = readConfig.getConfig("SQL","password")
        print(type(password))
        db = readConfig.getConfig("SQL", "db")
        charset = readConfig.getConfig("SQL", "charset")
        self.conn = pymysql.connect(host=host,
                      user=user,
                      port=int(port),
                      password=password,
                      db=db,
                      charset=charset)
        self.cur = self.conn.cursor()

    def __del__(self): #析构函数，实例删除时触发
        self.cur.close()
        self.conn.close()
    #查询方法
    def query(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    #更新方法

    def excal(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(str(e))
    def check_user(self,name):
        result = self.cur.execute("select * from anc_info where name='{}'".format(name))
        print(result)
        return True if result else False
if __name__=="__main__":
    db = DB()
    result=db.query("select *from blade_user where phone='18657186386'")
    print(type(result))
    print(result)
    print(db.check_user("李云龙"))
    name = db.query("select *from anc_info where name='李云龙'")
    print(name)
