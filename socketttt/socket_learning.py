#coding=utf-8
'''
Created on 2016年4月20日

@author: PI
'''
import socket

s = socket.socket()

host = socket.gethostname()
#print host
port = 1244
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print 'Got connection from', addr
    no = c.send('Thank you for connecting')
    print no
    c.close()
    