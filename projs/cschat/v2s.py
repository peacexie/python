# -*- coding: UTF-8 -*-

import threading
import socket
import chatws


# const
HOST = "127.0.0.1"  #192.168.1.228
PORT = 10083  # 192.168.1.228:8830

# 监听消息
def handlerMsg(conn):
    with conn as con:
        chatws.recvLoop(con, users)

# socket监听
def handlerAccept(sock):
    while True:
        conn, addr = sock.accept()
        #conns.add(conn)  #;print(conn, addr)
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


#conns = set()
users = {}

if __name__ == "__main__":
    multiSocket()


'''

### 基础思路

* 自己是谁？ 
  --- uid(用户)
  --- 或 system(系统消息)

* 发给谁？   
  --- uto
  --- 或(uroom房间号)

### 结构规划

* 用户资料   - user: {uid, uname, thumb...}
* 聊天对方   - ufrom -> {uto, uroom}
* 初始化     - act=initUser: ("conn":conn, "row":val, 'uroom':'') 
* 加入聊天室 - act=joinRoom: (uid, uroom)
* 离开聊天室 - act=exitRoom: (uid, uroom?)
* 更新用户   - act=userUpd: (user, uto) - 由游客到登录
* 设置聊天方 - act=setTo: (uto)
* 发送消息   - act=sendOne: (ufrom, uto, type, msg)
* 发群消息   - act=sendRoom: (ufrom, uroom, type, msg)
* 消息类型   - type=text, pic, video, audio, info
* info类型   - info=news, house, rent, sale...

### 辅助方法

* pullConversationList, setTopConversation, delConversation
* pullUnreads, pullHistoryMessages, clearUnreadStatus


'''
