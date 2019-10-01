# -*- coding: UTF-8 -*-

import json
import threading
import socket
import chatws


# const
HOST = "127.0.0.1"  #192.168.1.228
PORT = 10083  # 192.168.1.228:8830

# 发送一条消息
def sendMsg(conn, mstr):
    #if not conn in conns:
    #    return True
    mbytes = bytes(format(mstr), encoding="utf-8")
    bstr = chatws.bstring(mbytes)
    conn.sendall(bstr)
    return True

# 发送一个提示
def sendTips(conn, msg, room=''):
    tips = '{"key":"tips","val":"'+msg+'"}'
    if conn:  # 单独发
       sendMsg(conn, tips)
    else:  # 群发或按房间发
        for uid in users:
            if not room or (room and users[uid]['uroom']==room):
                sendMsg(users[uid]['conn'], tips)

# 处理自定义消息体
def opMsg(key, val, data, conn, users):
    tips = ''
    if key=='initUser':
        if 'uid' in val:
            users[val['uid']] = {"conn":conn, "row":val, 'uroom':''}
    elif key=='sendOne' and 'uto' in val:  # 发单个人
        uto = val['uto']
        if uto in users:
            sendMsg(users[uto]['conn'], data)
        else:
            tips = '失败'
    elif key=='joinRoom' and 'uid' in val and 'uroom' in val:  # 进入聊天室
        users[val['uid']]['uroom'] = val['uroom']
    elif key=='exitRoom' and 'uid' in val:  # 退出聊天室
        sendTips(0, '['+val['uid']+']退出聊天室')
        users[val['uid']]['uroom'] = ''
    elif key=='sendRoom' and 'uroom' in val:  # 发聊天室
        for uid in users:  # 推荐用 key in dic, 但是循环中可能被删除? users.keys()
            if(users[uid]['uroom']==val['uroom']):
                sendMsg(users[uid]['conn'], data)
    else:
        pass
    return tips;

# 处理一次消息
def handlerOne(conn, data):
    tips = '';
    try:
        mdic = json.loads(data)
    except Exception as e1:
        print('Exception: ', e1)
    else:
        if 'key' in mdic and 'val' in mdic:
            key, val = mdic['key'], mdic['val']
            tips = opMsg(key, val, data, conn, users)
        else:
            print('Error: ', mdic)
    finally:
        pass
    if key!='sendRoom':  # 群发不重复发送
        sendMsg(conn, data)
    if tips:  # 发送提示
        sendTips(conn, tips)

# 监听消息
def handlerMsg(conn):
    with conn as con:
        while True:
            drecv = conn.recv(8096)
            data = ''
            if drecv[0:1] == b"\x81":  # 发送数据
                data = chatws.parseData(drecv)
                print('x81 - data: ', data)
            elif drecv[0:1] == b"\x88":  # 断开连接
                for uid in users:
                    if(users[uid]['conn']==con):
                        sendTips(0, '['+uid+']中断连接')
                        del users[uid]
                        break
                #conns.remove(con)
                print('x88 - end: ', drecv)  # b'\x88\x82uR\xdf\xc6v\xbb'
                return
            else:
                print('else - recv: ', drecv)
            handlerOne(con, data)

# socket监听
def handlerAccept(sock):
    while True:
        conn, addr = sock.accept()
        #conns.add(conn)  #;print(conn, addr)
        data = conn.recv(8096)  # 获取握手数据
        acinfo = chatws.getAcinfo(data)
        conn.sendall(acinfo)  # 响应【握手】信息
        t = threading.Thread(target=handlerMsg, args=(conn, ))
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
