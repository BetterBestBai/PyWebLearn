#coding=utf-8
'''
Created on 2016年4月20日

@author: PI
'''
import socket

s = socket.socket()

host = socket.gethostname()
print host
port = 1244
s.connect((host, port))
print s.recv(1024)

