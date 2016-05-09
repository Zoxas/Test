#!/usr/bin/python
#-*- coding:utf8 -*-

import socket
import paramiko
import threading
import sys

# 使用Paramiko示例文件的密鑰
#host_key = paramiko.RSAKey(filename='test_rsa.key')
#host_key = paramiko.RSAKey( filename = '/root/.ssh/id_rsa' )
host_key = paramiko.RSAKey( filename = '/etc/ssh/ssh_host_rsa_key' )
class  Server ( paramiko.ServerInterface ):
    def  __init__ ( self ):
        self .event = threading.Event()
    
    def  check_channel_request ( self , kind , chanid ):
        if kind ==  'session' :
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
    
    def  check_auth_password ( self , username , password ):
        if (username ==  'root' ) and (password ==  'zzz20255' ):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

server = sys.argv[ 1 ]
ssh_port =  int (sys.argv[ 2 ])

try :
    sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM )     #TCP socket
   
    #這裡value設置為1，表示將SO_REUSEADDR標記為TRUE，操作系統會在服務器socket被關閉或服務器進程終止後馬上釋放該服務器的端口，否則操作系統會保留幾分鐘該端口。
    sock.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1 )
    
    sock.bind((server, ssh_port))    #綁定ip和端口
    
    sock.listen( 100 )     #最大連接數為100
    
    print  ' [+] Listening for connection ... '
    client, addr = sock.accept()

except  Exception , e:
    print  ' [-] Listen failed: '  +  str (e)
    sys.exit( 1 )
print  ' [+] Got a connection! '


try :
    bhSession = paramiko.Transport(client)
    bhSession.add_server_key(host_key)
    server = Server()
    try :
        bhSession.start_server( server = server)
    except paramiko.SSHException, x:
        print  ' [-] SSH negotiation failed '
    chan = bhSession.accept( 20 ) #設置超時值為20
    print  ' [+] Authenticated! '
    print chan.recv( 1024 )
    chan.send( " Welcome to my ssh " )
    while  True :
        try :
            command =  raw_input ( " Enter command: " ).strip( "\n" )    #strip移除字符串頭尾指定的字符（默認為空格）,這裡是換行
            if command !=  'exit' :
                chan.send(command)
                print chan.recv( 1024 ) +  '\n'
            else :
                chan.send( 'exit' )
                print  'exiting'
                bhSession.close()
                raise  Exception ( 'exit' )
        except  KeyboardInterrupt :
            bhSession.close()
except  Exception , e:
    print  ' [-] Caught exception: '  +  str (e)
    try :
        bhSession.close()
    except :
        pass
    sys.exit( 1 )