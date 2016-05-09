#-*- coding:utf8 -*-

from scapy.all import  *

# 定義數據包回調函數
def  packet_callback ( packet ):
    print packet.show()

# 開啟 sniffer
sniff( prn = packet_callback, count = 1 )