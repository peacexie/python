# -*- coding: UTF-8 -*-

import json
import base64
import hashlib
import struct

WSKEY = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
# see:https://tools.ietf.org/html/rfc6455


# ------------------------------------------------------------------------------


# xxx
def xxx(conn, xxx):
    pass


# ------------------------------------------------------------------------------


# 发送一条消息
def sendMsg(conn, mstr):
    #if not conn in conns:
    #    return True
    mbytes = bytes(format(mstr), encoding="utf-8")
    bstr = bstring(mbytes)
    conn.sendall(bstr)
    return True

# 发送一个提示
def sendTips(conn, msg, room=''):
    tips = '{"key":"tips","val":"'+msg+'"}'  # json.dumps(dict)
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
            uid = val['uid']
            if uid in users:
                del users[uid]
            users[uid] = {"conn":conn, "row":val, 'uroom':''}
    elif key=='sendOne' and 'uto' in val:  # 发单个人
        uto = val['uto']
        if uto in users:
            sendMsg(users[uto]['conn'], data)
        else:
            tips = 'Send fail!'
    elif key=='joinRoom' and 'uid' in val and 'uroom' in val:  # 进入聊天室
        users[val['uid']]['uroom'] = val['uroom']
    elif key=='exitRoom' and 'uid' in val:  # 退出聊天室
        sendTips(0, '['+val['uid']+'] Exit chat-room')
        users[val['uid']]['uroom'] = ''
    elif key=='sendRoom' and 'uroom' in val:  # 发聊天室
        for uid in users:
            if(users[uid]['uroom']==val['uroom']):
                sendMsg(users[uid]['conn'], data)
    else:
        pass
    return tips;

# 处理(应答)一次数据
def replyOne(conn, data, users):
    tips, key = '', '';
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

def exitOne(conn, users):
    for uid in users:
        if(users[uid]['conn']==conn):
            sendTips(0, '['+uid+'] Client interrupt!')  # broken,interrupt
            del users[uid]  # conns.remove(conn)

# 循环接受数据
def recvLoop(conn, users):
    while True:
        drecv = conn.recv(8096)
        data = ''
        if drecv[0:1] == b"\x81":  # 发送数据
            data = parseData(drecv)
            print('x81 - data: ', data)
        elif drecv[0:1] == b"\x88":  # 断开连接
            exitOne(conn, users)
            break
            print('x88 - end: ', drecv)  # b'\x88\x82uR\xdf\xc6v\xbb'
            return
        else:
            print('else - recv: ', drecv)
            exitOne(conn, users)
            break
        replyOne(conn, data, users)


# ------------------------------------------------------------------------------


# 将请求头格式化成字典
def getHeaders(data):
    headers = {}
    data = str(data, encoding="utf-8")
    header, body = data.split("\r\n\r\n", 1)
    hlist = header.split("\r\n")
    for i in hlist:
        hitem = i.split(":", 1)
        if len(hitem) >= 2:
            headers[hitem[0]] = "".join(hitem[1::]).strip()
        else:
            hitem = i.split(" ", 1)
            if hitem and len(hitem) == 2:
                headers["method"] = hitem[0]
                headers["protocol"] = hitem[1]
    return headers

# 对数据进行解密
def parseData(payload):
    plen = payload[1] & 127
    if plen == 126:
        exlen = payload[2:4]
        mask = payload[4:8]
        decoded = payload[8:]
    elif plen == 127:
        exlen = payload[2:10]
        mask = payload[10:14]
        decoded = payload[14:]
    else:
        exlen = None
        mask = payload[2:6]
        decoded = payload[6:]
    # 这里我们使用字节将数据全部收集，再去字符串编码，这样不会导致中文乱码
    blist = bytearray()
    for i in range(len(decoded)):
        # 解码方式
        chunk = decoded[i] ^ mask[i % 4]
        blist.append(chunk)
    body = str(blist, encoding='utf-8')
    return body

# 组装加密的握手信息
def getAcinfo(data):
    headers = getHeaders(data)
    # 对请求头中的sec-websocket-key进行加密
    tpl = "HTTP/1.1 101 Switching Protocols\r\n" \
        "Upgrade:websocket\r\n" \
        "Connection: Upgrade\r\n" \
        "Sec-WebSocket-Accept: %s\r\n" \
        "WebSocket-Location: ws://%s\r\n\r\n"
    # 第一次连接发回报文
    value = ''
    if headers.get('Sec-WebSocket-Key'):
        value = headers['Sec-WebSocket-Key'] + WSKEY
    ac = base64.b64encode(hashlib.sha1(value.encode('utf-8')).digest())
    res = tpl % (ac.decode('utf-8'), headers.get("Host"))
    return bytes(res, encoding="utf-8")

# 网络字节流包装
def bstring(mbytes):
    # 接收的第一字节，一般都是x81不变
    firstb = b"\x81"
    length = len(mbytes)
    if length < 126:
        firstb += struct.pack("B", length)
    elif length <= 0xFFFF:
        firstb += struct.pack("!BH", 126, length)
    else:
        firstb += struct.pack("!BQ", 127, length)
    bstr = firstb + mbytes
    return bstr


# ------------------------------------------------------------------------------


'''



'''
