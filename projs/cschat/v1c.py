#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
client = socket.socket()#声明socket类型，同时生成socke连接t对象
client.connect(('localhost',969))  #连接到localhost主机的6969端口上去
while True:
        msg = input(">>:").strip()
        if len(msg) == 0:continue
        client.send(msg.encode('utf-8'))#把编译成utf-8的数据发送出去
        data = client.recv(512)#接收数据
        print("从服务器接收到的数据为：",data.decode())
client.close()
