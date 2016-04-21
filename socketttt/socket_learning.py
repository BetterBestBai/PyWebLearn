#coding=utf-8
'''
Created on 2016年4月20日

@author: PI
'''
import socket

s = socket.socket()  #1. 第一步是创建socket对象。调用socket构造函数

host = socket.gethostname()
port = 1244
s.bind((host, port))   #2. 第二步是将socket绑定到指定地址。

s.listen(1)   #3. 第三步是使用socket套接字的listen方法接收连接请求。
while True:
    c, addr = s.accept()   #4. 第四步是服务器套接字通过socket的accept方法等待客户请求一个连接。
    print 'Got connection from', addr
    c.send('Thank you for connecting')  #5. 第五步是处理阶段，服务器和客户端通过send和recv方法通信(传输 数据)。服务器调用send，并采用字符串形式向客户发送信息。
    c.close()   #6. 传输结束，服务器调用socket的close方法关闭连接。
    