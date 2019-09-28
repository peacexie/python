# -*- coding: UTF-8 -*-

import json
import base64
import hashlib
import struct

WSKEY = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
# see:https://tools.ietf.org/html/rfc6455

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
    '''
    print('bstr:::', bstr)
    bdic = json.loads(bstr)  #unicode(bstr, errors='ignore')
    if 'key' in bdic:
        return bdic
    else:
        return {'key':'', 'val':''}
    '''

'''


#json字符串转换成字典
json.loads(json_str) 
 
#字典转换成json字符串 
json.dumps(dict)


'''
