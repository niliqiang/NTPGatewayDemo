#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket


serverAddr = 'ntp1.aliyun.com'

mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mySocket.bind(('0.0.0.0', 123))
print('Bind NTP on 123...')
		
# NTP 测试
#data = b'\x1B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xD0\xAF\x5F\xF5\x23\xD7\x08\x00'
#s.sendto(data, ('ntp1.aliyun.com', 123))
#print(list(s.recv(48)))


def Func():
	
	while True:
		# 接收数据
		print('Receiving client data...')
		clientData, clientAddr = mySocket.recvfrom(48)
		print('Received from %s:%s.' % clientAddr)
		mySocket.sendto(clientData, (serverAddr, 123))
		print('Receiving server data...')
		serverData = mySocket.recv(48)
		print('Received from %s' % serverAddr)
		mySocket.sendto(serverData, clientAddr)
		print('Client time synchronization succeed')
		print('\n')

if __name__ == '__main__':
    try:
        Func()

    except KeyboardInterrupt:   #按下ctrl+C时需将socket关闭
        mySocket.close()
        print('Socket is closed')

