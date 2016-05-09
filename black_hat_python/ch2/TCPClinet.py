# -*- coding: utf-8 -*-
import socket

target_host =  "www.yahoo.com"
target_port =   80 

#建立一個 socket 物件 (AF_INET:使用標準IPV4地址和主機名， SOCK_STREAM：TCP客戶端)
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

# 讓客戶端連到server
client.connect((target_host,target_port))

# 發送一些數據
client.send("GET / HTTP/1.1 \r\n Host: yahoo.com \r\n\r\n")


# 接收一些數據（4096個字符）
response = client.recv(4096)

print response