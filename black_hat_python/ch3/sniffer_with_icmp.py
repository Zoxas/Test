#-*- coding:utf8 -*-

import socket
import os
import struct
from ctypes import  *

# 監聽的主機
host =  "192.168.40.138"

# ip header 的定義 參考C語言的定義
class  IP ( Structure ):
    _fields_ = [
        ( "ihl" , c_ubyte, 4 ),     #ip head length
        ( "version" , c_ubyte, 4 ), #版本
        ( "tos" , c_ubyte),         #服務類型
        ( "len" , c_ushort),        #ip數據包總長度
        ( "id" , c_ushort),         #標識符
        ( "offset" , c_ushort),     #偏移量
        ( "ttl" , c_ubyte),         #生存時間
        ( "protocol_num" , c_ubyte),#這裡用數字來代表時哪個協議,下面構造函數有設置映射表
        ( "sum" , c_ushort),        #頭部校驗和
        ( "src" , c_ulong),         #來源ip地址
        ( "dst" , c_ulong)          #目的ip地址
    ]

    # __new__(cls, *args, **kwargs) 創建對象時會調用，返回當前對象的一個實例;注意：這裡的第一個參數是cls即class本身
    def  __new__ ( self , socket_buffer = None ):
        return   self.from_buffer_copy(socket_buffer)

    # __init__(self, *args, **kwargs) 創建完對像後調用，對當前對象的實例的一些初始化，無返回值,即在調用__new__之後，根據返回的實例初始化；注意，這裡的第一個參數是self即對象本身【注意和new的區別】
    def  __init__ ( self , socket_buffer = None ):
        #協議常數與協議名稱的對應
        self.protocol_map = { 1 : "ICMP" , 6 : "TCP" , 17 : "UDP" }

        # 可讀性更強的ip地址(socket.inet_ntoa -> 轉換32位打包的IPV4地址為IP地址的標準點號分隔字符串表示。)
        self.src_address = socket.inet_ntoa(struct.pack( "<L" , self.src))
        self.dst_address = socket.inet_ntoa(struct.pack( "<L" , self.dst))

        # 協議類型
        try :
            self.protocol =  self.protocol_map[self.protocol_num]
        except :
            self.protocol =  str (self.protocol_num)


class  ICMP ( Structure ):
    #
    _fields_ = [
        ( "type" , c_ubyte),        #類型
        ( "code" , c_ubyte),        #代碼值
        ( "checksum" , c_ubyte),    #頭部校驗和
        ( "unused" , c_ubyte),      #未使用
        ( "next_hop_mtu" , c_ubyte) #下一跳的MTU
    ]

    def  __new__ ( self , socket_buffer ):
        return  self.from_buffer_copy(socket_buffer)

    def  __init__ ( self , socket_buffer ):
        pass


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

try :
    while  True :
        # 讀取數據包
        raw_buffer =  sniffer.recvfrom( 65565 )[ 0 ]

        # 將緩衝區的前20個字節按IP頭進行解析
        ip_header = IP(raw_buffer[ 0 : 20 ])

        # 輸出協議和通信雙方IP地址
        print   "Protocol: %s  %s ->  %s "  % (ip_header.protocol, ip_header.src_address, ip_header.dst_address)

        # 如果為ICMP,進行處理
        if ip_header.protocol ==  "ICMP" :

            # 計算ICMP包的起始位置,並獲取ICMP包的數據
            offset = ip_header.ihl * 4  #ihl代表 IP header之中 32 bit word(即 4 -byte 區塊)的個數
            buf = raw_buffer[offset: offset + sizeof(ICMP)]

            # 建立ICMP架構
            icmp_header = ICMP(buf)

            print  " ICMP -> Type: %d Code: %d "  % (icmp_header.type, icmp_header.code)

# 處理CTRL-C
except   KeyboardInterrupt :

    # 如果運行再Windows上,關閉混雜模式
    if os.name ==  "nt" :
        sniffer.ioctl(socket. SIO_RCVALL , socket. RCVALL_OFF )