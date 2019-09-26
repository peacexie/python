#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
client = socket.socket()#声明socket类型并生产连接对象
client.connect(('192.168.1.228',8930))#发起连接

#循环输入指令
while True:
    cmd = input('>>:').strip()
    if len(cmd) == 0: continue#如果输入为空则跳过本次循环，重新返回输入指令
    client.send(cmd.encode("utf-8"))#把字符串编译成比特流发送
    cmd_res_size = client.recv(1024)#接收服务器发来的指令内容比特流大小
    print("命令结果大小：",cmd_res_size)
    received_size = 0#接收到的大小为0
    received_data = b''#接收到的数据内容为空
    #根据接收到的数据大小，循环接受数据使其生成完整的内容再跳出循环
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        received_size += len(data)
        received_data += data
    #跳出循环后执行
    else:
        print("cmd res receive done……",received_size)
        print(received_data.decode())

client.close()
