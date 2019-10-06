# -*- coding: UTF-8 -*-

import threading
import socket
import chatws


# const
HOST = "127.0.0.1"  #192.168.1.228
PORT = 10083  # 192.168.1.228:8830


# 监听消息
def handlerMsg(con1):
    with con1 as conn:
        while True:
            drecv = conn.recv(8096)
            data = ''
            if drecv[0:1] == b"\x81":  # 发送数据
                data = chatws.parseData(drecv)
                print('[get] - ', data)
            elif drecv[0:1]==b"\x88" or drecv[0:1]==b"":  # (客户端)断开连接
                chatws.breakOne(conn, users)
                print('[end] - ', drecv)  # b'\x88\x82uR\xdf\xc6v\xbb'
                return
            else:
                print('[er1] - ', drecv)
            chatws.replyOne(conn, data, users)
        #chatws.recvLoop(conn, users)

# socket监听
def handlerAccept(sock):
    while True:
        conn, addr = sock.accept()  #;print(conn, addr)
        data = conn.recv(8096)  # 获取握手数据
        acinfo = chatws.getAcinfo(data)
        conn.sendall(acinfo)  # 响应【握手】信息
        t = threading.Thread(target=handlerMsg, args=(conn,))
        t.start()

# 多线程监听socket
def multiSocket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(5)
    t = threading.Thread(target=handlerAccept(sock))
    t.start()


users = {}

if __name__ == "__main__":
    multiSocket()


'''



'''
