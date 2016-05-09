# -*- coding: utf-8 -*-
import socket
import threading 

bind_ip = "0.0.0.0" #綁定ip：這裡代表任何ip地址
bind_port =  9999

sever = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sever.bind((bind_ip,bind_port))

# 連線的排隊上限 = 5
sever.listen(5)

print "[*] listen on %s : %d " % (bind_ip,bind_port)

# 這裡是處理 client 端的 Thread 
def handle(client_socket):

    #client 端傳來的data
    request = client_socket.recv(1024)

    print "[*] Received %s" % request

    #回傳ACK
    client_socket.send("ACK!")
    client_socket.close()

while True:
	# client = client端的 socket  ; addr = (client_ip , client_port)
    client , addr = sever.accept()

    print "[*] Accepted connection from %s : %d " % (addr[0],addr[1])

    #啟動 client thread 處理 傳來的資料  ; *參數 args是 (client,) 
    client_handler = threading.Thread(target = handle , args = (client,))
    client_handler.start()



