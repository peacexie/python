#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
import struct
import hashlib
import base64
import threading

# const
HOST = "192.168.1.228"
PORT = 10083 # 192.168.1.228:8830
WSKEY = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
# see:https://tools.ietf.org/html/rfc6455

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


def sendMsg(conn, mbytes):
    # 接收的第一字节，一般都是x81不变
    firstb = b"\x81"
    length = len(mbytes)
    if length < 126:
        firstb += struct.pack("B", length)
    elif length <= 0xFFFF:
        firstb += struct.pack("!BH", 126, length)
    else:
        firstb += struct.pack("!BQ", 127, length)
    msg = firstb + mbytes
    conn.sendall(msg)
    return True


def handlerMsg(conn):
    with conn as c:
        while True:
            drecv = c.recv(8096)
            if drecv[0:1] == b"\x81":
                dparse = parseData(drecv)
                print(dparse)
            sendMsg(c, bytes("recv: {}".format(dparse), encoding="utf-8"))


def handlerAccept(sock):
    while True:
        conn, addr = sock.accept()
        data = conn.recv(8096)
        headers = getHeaders(data)
        # 对请求头中的sec-websocket-key进行加密
        tpl = "HTTP/1.1 101 Switching Protocols\r\n" \
            "Upgrade:websocket\r\n" \
            "Connection: Upgrade\r\n" \
            "Sec-WebSocket-Accept: %s\r\n" \
            "WebSocket-Location: ws://%s\r\n\r\n"
        # 第一次连接发回报文
        if headers.get('Sec-WebSocket-Key'):
            value = headers['Sec-WebSocket-Key'] + WSKEY
        ac = base64.b64encode(hashlib.sha1(value.encode('utf-8')).digest())
        res = tpl % (ac.decode('utf-8'), headers.get("Host"))
        conn.sendall(bytes(res, encoding="utf-8"))
        t = threading.Thread(target=handlerMsg, args=(conn, ))
        t.start()


def multiSocket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(5)
    t = threading.Thread(target=handlerAccept(sock))
    t.start()


sock_pool = []

if __name__ == "__main__":
    multiSocket()


'''


'''
