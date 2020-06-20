from socket import *
from select import select

s=socket()
s.bind(("0.0.0.0",8888))
s.listen(3)

s.setblocking(False)

rlist=[s]
wlist=[]
xlist=[]

while True:
    rs,ws,xs=select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            connfd, addr = r.accept()
            print("Connect from",addr)
            rlist.append(connfd)
        else:
            data=r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
            wlist.append(r)

    for w in ws:
        w.send(b"ok")
        wlist.remove(w)
