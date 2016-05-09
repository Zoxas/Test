#-*- coding:utf8 -*-

import socket
import os

# 監聽主機，即監聽那個網絡接口，下面的為我的kali的ip
host =  " 192.168.40.138"

# 判別作業系統 ， 建立raw_socket , 然後綁定在公開介面
if   os.name ==  "nt" :
    socket_protocol = socket. IPPROTO_IP
else :
    socket_protocol = socket. IPPROTO_ICMP

sniffer = socket.socket(socket. AF_INET , socket. SOCK_RAW , socket_protocol)    

sniffer.bind((host, 0 )) # port為 0 , 應該是監聽所有port

# 希望在補追的內容中包含 IP header
sniffer.setsockopt(socket. IPPROTO_IP , socket. IP_HDRINCL , 1 )

# 在Windows平台上,我們需要設置IOCTL以啟用混雜模式
if os.name ==  "nt" :
    sniffer.ioctl(socket. SIO_RCVALL , socket. RCVALL_ON )

# 讀取單個數據包
print sniffer.recvfrom( 65565 )

# 在Windows平台上關閉混雜模式
if os.name ==  "nt" :
    sniffer.ioctl(socket. SIO_RCVALL , socket. RCVALL_OFF )