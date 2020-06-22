from socket import *


class User:
    def __init__(self):
        self.socketfd=socket()
        self.socketfd.connect(("127.0.0.1",8888))

    def main(self):
        self.view1()

    def view1(self):
        while True:
            print("=========== 界面一 ===========")
            print("***         登录          ***")
            print("***         注册          ***")
            print("***         退出          ***")
            print("=============================")

            cmd=input("请输入命令：")
            if cmd=="退出":
                break
            elif cmd == "登录":
                self.log_in()
            elif cmd == "注册":
                self.add_user()
            else:
                print("请输入正确指令。")

    def view2(self):
        while True:
            print("=========== 界面二 ===========")
            print("***         查询          ***")
            print("***         历史          ***")
            print("***         退出          ***")
            print("=============================")

            cmd = input("请输入命令：")
            if cmd == "退出":
                break
            elif cmd == "历史":
                self.history()
            elif cmd =="查询":
                self.look_up()
            else:
                print("请输入正确指令。")

    def log_in(self):
        name=input("请输入姓名：")
        password=input("请输入密码：")
        data="L*#"+name+"*#"+password
        self.socketfd.send(data.encode())
        permit=self.socketfd.recv(1024)
        if permit==b"ok":
            self.view2()
        elif permit==b"not":
            print("用户不存在，请注册。")
        else:
            print("用户名或密码错误。")

    def add_user(self):
        name = input("请输入姓名：")
        while True:
            password = input("请输入密码：")
            if password == "":
                print("密码不能为空。")
            else:
                break
        data = "R*#" + name + "*#"+password
        self.socketfd.send(data.encode())
        permit = self.socketfd.recv(128)
        if permit==b"ok":
            print("注册成功")
        elif permit ==b"not":
            print("用户名字已存在")
            self.add_user()

    def history(self):
        data = "H*#"
        self.socketfd.send(data.encode())


    def look_up(self):
        while True:
            word=input("请输入单词：")
            if word =="##":
                break
            data = "Q*#" + word
            self.socketfd.send(data.encode())
            mean = self.socketfd.recv(1024)
            print(mean.decode())

"""    def add_user(self):
        name = input("请输入姓名：")
        data = "R*#" + name+"*#  "
        self.socketfd.send(data.encode())
        permit = self.socketfd.recv(1024)
        if permit==b"ok":
            while True:
                password = input("请输入密码：")
                if password=="":
                    print("密码不能为空。")
                else:
                    break
            data = "R*#" + name + "*#"+password
            self.socketfd.send(data.encode())
            print("注册成功")
        elif permit == b"not":
            print("用户名已存在，请更换。")
        else:
            pass"""

if __name__ == '__main__':
    user1=User()
    user1.main()

