# -*- coding: UTF-8 -*-

import json
import threading
import socket
import chats


# const
HOST = "127.0.0.1"  #192.168.1.228
PORT = 10083  # 192.168.1.228:8830


def sendMsg(conn, mbytes):
    msg = chats.b2str(mbytes)
    conn.sendall(msg)
    return True


def handlerMsg(conn):
    with conn as c:
        while True:
            drecv = c.recv(8096)
            data = ''
            if drecv[0:1] == b"\x81":
                data = chats.parseData(drecv)
                print('aaa - data: ', data)
            else:
                print('bbb - drecv: ', drecv)
            #c.sendall('')
            #bits = bytes(format(data), encoding="utf-8") if data else drecv
            #sendMsg(c, drecv)
            sendMsg(c, bytes(format(data),encoding="utf-8"))


def handlerAccept(sock):
    while True:
        conn, addr = sock.accept()
        users.append(conn) #;print(users)
        data = conn.recv(8096)  # 获取握手数据
        acinfo = chats.getAcinfo(data)
        conn.sendall(acinfo)  # (第一次)连接发回报文
        t = threading.Thread(target=handlerMsg, args=(conn, ))
        t.start()


def multiSocket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(5)
    t = threading.Thread(target=handlerAccept(sock))
    t.start()


users = []

if __name__ == "__main__":
    multiSocket()


'''

### 基础思路

* 自己是谁？ --- id, (或系统消息-system)
* 发给谁？   --- id, (或房间号)

### 结构规划

* 用户资料   - user: {uid, uname, thumb...}
* 聊天对方   - uto: {toid, toroom}
* 初始化     - act=initUser: (user, uto)
* 更新用户   - act=userUpd: (user, uto) - 由游客到登录
* 设置聊天方 - act=setTo: (uto)
* 发送消息   - act=sendMsg: (fid, uto, type, msg)
* 消息类型   - type=text, pic, video, audio, info
* info类型   - info=news, house, rent, sale...

### 辅助方法

* pullConversationList, setTopConversation, delConversation
* pullUnreads, pullHistoryMessages, clearUnreadStatus


'''
