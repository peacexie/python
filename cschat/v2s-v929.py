# -*- coding: UTF-8 -*-

import json
import threading
import socket
import chatws


# const
HOST = "127.0.0.1"  #192.168.1.228
PORT = 10083  # 192.168.1.228:8830


def sendMsg(conn, mstr):
    #if not conn in conns:
    #    return True
    mbytes = bytes(format(mstr), encoding="utf-8")
    bstr = chatws.bstring(mbytes)
    conn.sendall(bstr)
    return True

# 消息处理转发
def opMsg(conn, mstr):
    
    remsg = '';
    try:
        mdic = json.loads(mstr)
    except Exception as e1:
        print('Exception: ', e1)
    else:
        if 'key' in mdic and 'val' in mdic:
            key, val = mdic['key'], mdic['val']
            if key=='initUser':
                if 'uid' in val:
                    users[val['uid']] = {"conn":conn, "row":val, 'uroom':''}
                remsg = ''
            elif key=='sendOne' and 'uto' in val:  # 发单个人
                uto = val['uto']
                if uto in users:
                    sendMsg(users[uto]['conn'], mstr)
                    remsg = '成功!'
                else:
                    remsg = '未成功'
            elif key=='joinRoom' and 'uid' in val and 'uroom' in val:  # 进入聊天室
                users[val['uid']]['uroom'] = val['uroom']
            elif key=='exitRoom' and 'uid' in val:  # 退出聊天室
                users[val['uid']]['uroom'] = ''
            elif key=='sendRoom' and 'uroom' in val:  # 发聊天室
                for uid in users:  # 推荐用 key in dic, 但是循环中可能被删除? users.keys()
                    if(users[uid]['uroom']==val['uroom']):
                        sendMsg(users[uid]['conn'], mstr)
                remsg = '成功!'
            else:
                pass
        else:
            print('Error: ', mdic)
    finally:
        pass
    if remsg:
        sendMsg(conn, remsg)
    else:
        sendMsg(conn, mstr)

def handlerMsg(conn):
    
    with conn as con:
        while True:
            drecv = con.recv(8096)
            data = ''
            if drecv[0:1] == b"\x81":  # 发送数据
                data = chatws.parseData(drecv)
                print('x81 - data: ', data)
            elif drecv[0:1] == b"\x88":  # 断开连接
                for uid in users:
                    if(users[uid]['conn']==con):
                        del users[uid]
                        break
                #conns.remove(conn)
                print('x88 - end: ', drecv, con)  # b'\x88\x82uR\xdf\xc6v\xbb'
                return
            else:
                print('else - drecv: ', drecv)
            opMsg(con, data)

def handlerAccept(sock):
    while True:
        conn, addr = sock.accept()
        #conns.add(conn)  #;print(conn, addr)
        data = conn.recv(8096)  # 获取握手数据
        acinfo = chatws.getAcinfo(data)
        conn.sendall(acinfo)  # 响应【握手】信息
        t = threading.Thread(target=handlerMsg, args=(conn, ))
        t.start()


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

* 自己是谁？ --- id, (或系统消息-system)
* 发给谁？   --- id, (或房间号)

### 结构规划

* 用户资料   - user: {uid, uname, thumb...}
* 聊天对方   - uto: {toid, toroom}
* 初始化     - act=initUser: (user, uto)
* 更新用户   - act=joinRoom: (user, uto) - 加入聊天室
* 更新用户   - act=userUpd: (user, uto) - 由游客到登录
* 设置聊天方 - act=setTo: (uto)
* 发送消息   - act=sendMsg: (fid, uto, type, msg)
* 消息类型   - type=text, pic, video, audio, info
* info类型   - info=news, house, rent, sale...

### 辅助方法

* pullConversationList, setTopConversation, delConversation
* pullUnreads, pullHistoryMessages, clearUnreadStatus


'''
