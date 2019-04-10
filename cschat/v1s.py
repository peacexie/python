#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
import os
server = socket.socket()#声明socket类型，并且生成socket连接对象
server.bind(('localhost',969))#把服务器绑定到localhost的6969端口上
server.listen(5)#开始监听
print("等待连接中……")
while True:
        conn,addr = server.accept()#接收连接
        print("***连接成功***")
        while True:
                data = conn.recv(512)#接收客户发来的数据
                print("接收到的命令为：",data)
                if not data:
                        print("客户断开连接")
                        break
                com = os.popen(data.decode()).read()#read()读取内存地址的内容
                print(data.decode())#输出结果为字符串dir
                print(os.popen(data.decode()))#输出结果为一个内存地址
                #py3 里socket发送的只有bytes,os.popen又只能接受str,所以要decode一下
                conn.sendall(com.encode('utf-8'))
server.close()
