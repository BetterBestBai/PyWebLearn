#coding=utf-8
'''
Created on 2016年4月20日

@author: PI
'''
import socket
host = socket.gethostname()
port = 1244

c=socket.socket()
c.connect((host,port))
data = c.recv(1024)
print data
