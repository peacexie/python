#coding=UTF-8

# 导入socket库:
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:http://txjia.com/proxy/pcheck.php
s.connect(('txjia.com', 80))

# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: txjia.com\r\nPath: /proxy/pcheck.php\r\nConnection: close\r\n\r\n')

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('imcat.htm', 'wb') as f:
    f.write(html)

