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
try :
    while  True :
        # 讀取數據包
        raw_buffer =  sniffer.recvfrom( 65565 )[ 0 ]

        # 將緩衝區的前20個字節按IP頭進行解析
        ip_header = IP(raw_buffer[ 0 : 20 ])

        # 輸出協議和通信雙方IP地址
        print   "Protocol: %s  %s ->  %s "  % (ip_header.protocol, ip_header.src_address, ip_header.dst_address)

# 處理CTRL-C
except   KeyboardInterrupt :

    # 如果運行再Windows上,關閉混雜模式
    if os.name ==  "nt" :
        sniffer.ioctl(socket. SIO_RCVALL , socket. RCVALL_OFF )


"""
struct模塊中最重要的三個函數是

pack() pack(fmt,v1,v2,...)
將變數轉成對應的格式

unpack(fmt,string)
將對應的格式轉回數據

calcsize(fmt)
計算目前的格式用了多少記憶體

上述fmt中，支持的格式為：
FORMAT  [C TYPE]            [PYTHON TYPE]   [STANDARD SIZE]     [NOTES]
x       pad byte            no value        
c       char                string of length    1               1    
b       signed char         integer             1               (3)
B       unsigned char       integer             1               (3)
?       _Bool               bool                1               (1)
h       short               integer             2               (3)
H       unsigned short      integer             2               (3)
i       int                 integer             4               (3)
I       unsigned int        integer             4               (3)
l       long                integer             4               (3)
L       unsigned long       integer             4               (3)
q       long long           integer             8               (2), (3)
Q       unsigned long       long integer        8                (2), (3)
f       float               float               4               (4)
d       double              float               8               (4)
s       char[]              string        
p       char[]              string        
P       void *              integer                             (5), (3)


為了同c中的結構體交換數據，還要考慮有的c或c++編譯器使用了字節對齊，通常是以4個字節為單位的32位系統，故而struct根據本地機器字節順序轉換.可以用格式中的第一個字符來改變對齊方式.定義如下：
CHARACTER   [BYTE ORDER]            [SIZE]      [ALIGNMENT]
@           native                  native      native
=           native                  standard    none
<           little-endian           standard    none
>           big-endian              standard    none
!           network(=big-endian)    standard    none
使用方法是放在fmt的第一個位置，就像'@5s6sif'


"""