#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket
import struct
import hashlib
import base64
import threading

def get_headers(data):
    headers = {}
    data = str(data, encoding="utf-8")
    header, body = data.split("\r\n\r\n", 1)
    header_list = header.split("\r\n")
    for i in header_list:
        item = i.split(":", 1)
        if len(item) >= 2:
            headers[item[0]] = "".join(item[1::]).strip()
        else:
            item = i.split(" ", 1)
            if item and len(item) == 2:
                headers["method"] = item[0]
                headers["protocol"] = item[1]
    return headers


def parse_payload(payload):
    payload_len = payload[1] & 127
    if payload_len == 126:
        extend_payload_len = payload[2:4]
        mask = payload[4:8]
        decoded = payload[8:]

    elif payload_len == 127:
        extend_payload_len = payload[2:10]
        mask = payload[10:14]
        decoded = payload[14:]
    else:
        extend_payload_len = None
        mask = payload[2:6]
        decoded = payload[6:]

    # 这里我们使用字节将数据全部收集，再去字符串编码，这样不会导致中文乱码
    bytes_list = bytearray()

    for i in range(len(decoded)):
        # 解码方式
        chunk = decoded[i] ^ mask[i % 4]
        bytes_list.append(chunk)
    body = str(bytes_list, encoding='utf-8')
    return body


def send_msg(conn, msg_bytes):
    # 接收的第一字节，一般都是x81不变
    first_byte = b"\x81"
    length = len(msg_bytes)
    if length < 126:
        first_byte += struct.pack("B", length)
    elif length <= 0xFFFF:
        first_byte += struct.pack("!BH", 126, length)
    else:
        first_byte += struct.pack("!BQ", 127, length)

    msg = first_byte + msg_bytes
    conn.sendall(msg)
    return True

sock_pool = []


def handler_accept(sock):

    while True:
        conn, addr = sock.accept()

        data = conn.recv(8096)
        headers = get_headers(data)
        # 对请求头中的sec-websocket-key进行加密
        response_tpl = "HTTP/1.1 101 Switching Protocols\r\n" \
                       "Upgrade:websocket\r\n" \
                       "Connection: Upgrade\r\n" \
                       "Sec-WebSocket-Accept: %s\r\n" \
                       "WebSocket-Location: ws://%s\r\n\r\n"

        # 第一次连接发回报文
        magic_string = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
        if headers.get('Sec-WebSocket-Key'):
            value = headers['Sec-WebSocket-Key'] + magic_string

        ac = base64.b64encode(hashlib.sha1(value.encode('utf-8')).digest())
        response_str = response_tpl % (ac.decode('utf-8'), headers.get("Host"))
        conn.sendall(bytes(response_str, encoding="utf-8"))
        t = threading.Thread(target=handler_msg, args=(conn, ))
        t.start()


def handler_msg(conn):
        with conn as c:
            while True:
                data_recv = c.recv(8096)

                if data_recv[0:1] == b"\x81":
                    data_parse = parse_payload(data_recv)
                    print(data_parse)
                send_msg(c, bytes("recv: {}".format(data_parse), encoding="utf-8"))


def server_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("127.0.0.1", 10083))
    sock.listen(5)
    t = threading.Thread(target=handler_accept(sock))
    t.start()
        # data = conn.recv(8096)
        # headers = get_headers(data)
        #
        # # 对请求头中的sec-websocket-key进行加密
        # response_tpl = "HTTP/1.1 101 Switching Protocols\r\n" \
        #                "Upgrade:websocket\r\n" \
        #                "Connection: Upgrade\r\n" \
        #                "Sec-WebSocket-Accept: %s\r\n" \
        #                "WebSocket-Location: ws://%s\r\n\r\n"
        #
        # # 第一次连接发回报文
        # magic_string = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
        # if headers.get('Sec-WebSocket-Key'):
        #     value = headers['Sec-WebSocket-Key'] + magic_string
        #
        # ac = base64.b64encode(hashlib.sha1(value.encode('utf-8')).digest())
        # response_str = response_tpl % (ac.decode('utf-8'), headers.get("Host"))
        # conn.sendall(bytes(response_str, encoding="utf-8"))


if __name__ == "__main__":
    server_socket()