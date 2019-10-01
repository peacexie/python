#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket ,os
server = socket.socket() #声明socket类型并生产连接对象
server.bind(('192.168.1.228',8930)) #绑定ip和port
server.listen()#监听
print('等待连接……')

#循环接入
while True:
    conn,addr = server.accept()
    print('new conn:',addr)
    
    #循坏等待指令
    while True:
        print("等待新指令")
        data = conn.recv(1024)#接收比特流数据
        #没有接收到比特流数据，则无数据在传输即断开连接
        if not data:
            print("客户已经断开")
            break
        print("执行指令：",data)
        cmd_res = os.popen(data.decode()).read()#把比特流数据转为str，再执行指令，最后读取到内存赋值给变量cmd_res
        print("before send:",len(cmd_res))
        #判断cmd_res是否为 0，popen函数执行失败返回 0
        if len(cmd_res) == 0:
            cmd_res = "cmd has no output..."
        #cmd_res为字符串，.encode()后变为比特流，再用len计算出比特流的大小，再把这个整数转为字符串，最后转为比特流发送出去
        conn.send( str(len(cmd_res.encode())).encode("utf-8") )
        #把指令执行内容编译成比特流发送出去
        conn.send(cmd_res.encode("utf-8"))
        print("send done")

server.close()
