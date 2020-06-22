import pymysql

# host="106.53.246.226",port=3306,
class Dict_db:
    def __init__(self):
        self.db=pymysql.connect(
                                user="root",password="123456",
                                database="dict",charset="utf8")

    def cursor_n(self):
        self.cur = self.db.cursor()

    def close(self):
        self.db.close()

    def add_user(self,user_data):
        try:
            self.cursor_n()
            sql = "select * from user where name=%s;"
            self.cur.execute(sql, [user_data[0]])
            self.db.commit()
            data=self.cur.fetchone()
            print(data)
            if data:
                return "not"
            sql="insert into user(name,passwd) values (%s,%s);"
            self.cur.execute(sql,user_data)
            self.db.commit()
            return "ok"
        except:
            print("q")

    def log_in(self,user_data):
        self.cursor_n()
        sql = "select * from user where name=%s;"
        self.cur.execute(sql, [user_data[0]])
        self.db.commit()
        data = self.cur.fetchone()
        print("用户信息"+str(user_data))
        print("数据库信息"+str(data))
        if data[2]==user_data[1]:
            return "ok"
        elif data==None:
            return "not"
        else:
            return "no"

    def look_up(self,name,word):
        self.cursor_n()
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql, [word])
        self.db.commit()
        data = self.cur.fetchone()
        if data:
            sql="insert into hist(name,word) values (%s,%s);"
            self.cur.execute(sql, [name,word])
            self.db.commit()
            return data
        else:
            return "no"

    def history(self,name):

        sql = "select * from hist where name=%s;"
        self.cur.execute(sql, [word])
        self.db.commit()

if __name__ == '__main__':
    test=Dict_db()
    test.add_user(["lily","123456"])
    test.add_user(["tom","123456"])