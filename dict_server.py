from signal import *
from socket import *
from multiprocessing import Process
from dict_db import Dict_db


db = Dict_db()
def main():
    socketfd = socket()
    socketfd.bind(("0.0.0.0", 8888))
    socketfd.listen(3)
    signal(SIGCHLD, SIG_IGN)
    while True:
        try:
            connfd,addr=socketfd.accept()
            print(addr)
        except KeyboardInterrupt as e:
            socketfd.close()
        p=Process(target=control,args=(connfd,))
        p.daemon=True
        p.start()



def control(connfd):
    while True:
        data=connfd.recv(1024).decode()
        split_data=data.split("*#")
        if split_data =="":
            break
        elif split_data[0]=="L":
            permit = db.log_in(split_data[1:3])
            print(permit)
            connfd.send(permit.encode())
        elif split_data[0]=="R":
            permit=db.add_user(split_data[1:3])
            print(permit)
            connfd.send(permit.encode())
        elif split_data[0]=="Q":
            permit = db.look_up(split_data[2])
            print(permit)
            connfd.send(permit[0].encode())
        elif split_data[0]=="H":
            permit = db.history(split_data[1])
            print(permit)
            connfd.send(permit[0].encode())


def link_database():
    pass


if __name__ == '__main__':
    main()
