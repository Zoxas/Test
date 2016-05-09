#-*- coding:utf8 -*-
import socket

target_host =  " 127.0.0.1"
target_port =  9999

#建立一個socket 物件 (SOCK_DGRAM:UDP客戶端)
client = socket.socket(socket.AF_INET , socket.SOCK_DGRAM )

# 發送數據
client.sendto( "TEST TEST  UDP " , (target_host,target_port))

# 接收一些數據(4096個字符)
data, addr = client.recvfrom( 4096 )

# *應該要收到 回傳的數據 和 遠程主機的 message 和 port
print data
print addr