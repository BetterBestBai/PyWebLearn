#coding=utf-8
'''
Created on 2016年4月20日

@author: PI
'''
'''
python编写client的步骤：
1. 创建一个socket以连接服务器：socket = socket.socket( family, type )
2.使用socket的connect方法连接服务器。对于AF_INET家族,连接格式如下：
socket.connect( (host,port) )
3. 处理阶段，客户和服务器将通过send方法和recv方法通信。
4. 传输结束，客户通过调用socket的close方法关闭连接。

'''
import socket

s = socket.socket()

host = socket.gethostname()
port = 1244
s.connect((host, port))
print s.recv(1024)

