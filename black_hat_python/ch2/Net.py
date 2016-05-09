#!/usr/bin/python
#-*- coding:utf8 -*-
import sys
import socket
import getopt
import threading
import subprocess


#全域變數
listen =  False
command =  False
execute =  ""

target =  ""
port =  0


def  usage ():
    print  " 用法: Net.py -t target_host  -p port "
    print  " -l --listen - 在 [host]:[port] 監聽連線 "
    print  " -e --execute = file_to_run - 接到連線時執行指定檔案 "
    print  " -c --command - 啟動命令列 shell "
    print
    print
    print  " 範例: "
    print  " Net.py -t 192.168.0.1 -p 5555 -l -c "
    print  " Net.py -t 192.168.0.1 -p 5555 -l -e \"cat /etc/passwd\" "
    print  " echo 'ABCDEFGHI' | ./Net.py -t 192.168.11.12 -p 135 "
    sys.exit( 0 )


def  main ():
    global listen
    global port
    global execute
    global command
    global target

    if  not   len (sys.argv[ 1 :]):
        usage()

    # 讀取命令行選項,若沒有該選項 則顯示用法
    try :
        opts, args = getopt.getopt(sys.argv[ 1 :], " hle:t:p:c" ,[ "help" , "listen" , "execute" , "target" , "port" , "command" ])
    except getopt.GetoptError as err:
        print  str (err)
        usage()


    for o,a in opts:
        if o in ( "-h" , "--help" ):
            usage()
        elif o in ( "-l" , "--listen" ):
            listen =  True
        elif o in ( "-e" , "--execute" ):
            execute = a
        elif o in ( "-c" , "--commandshell" ):
            command =  True
            print a
        elif o in ( "-t" , "--target" ):
            target = a
        elif o in ( "-p" , "--port" ):
            port =  int (a)
        else :
            assert  False , "Unhandled Option"



    # 我們開始監聽 執行命令,提供shell 等
    if listen:
        server_loop()
    
    if  not listen and  len (target) and port >  0 :
    	client = socket.socket(socket. AF_INET , socket. SOCK_STREAM )
    	try :
        	#連接
        	client.connect((target, port))

        	while  True :

				recv_len =  1
				response =  ""
				while  recv_len:
					data = client.recv( 4096 )
					recv_len =  len (data)
					response += data

					if recv_len <  4096 :
						break
				print   response
        		
				# 等待輸入
				buffer =  raw_input ( "" )
				#這是為了方便 command 的應用 所以自動加了 \n
				buffer +=  "\n"
				# 發送
				client.send(buffer)
        except :
        	print  " [*] Exception! Exiting. "

    	#關閉連接
    	client.close()       

def  server_loop ():
    global target

    # 如果沒有定義目標,那我們監聽所有port
    if  not  len (target):
        target =  "0.0.0.0"

    server = socket.socket(socket. AF_INET , socket. SOCK_STREAM)
    server.bind((target, port))

    server.listen( 5 )

    while  True :
        client_socket, addr = server.accept()
        # 啟動一個 Thread 處理新的客戶端
        client_thread = threading.Thread(target = client_handler, args = (client_socket,))
        client_thread.start()


def  client_handler ( client_socket ):
    global execute
    global command

    # 檢查命令
    if  len (execute):
        # 執行命令
        output = run_command(execute)
        client_socket.send(output)


    # 如果需要shell,那麼我們進入另一個迴圈
    if command:
        while  True :
            # 簡單的提示
            client_socket.send( " <BHP:#> " )

            cmd_buffer =  ""
            while  "\n"  not  in cmd_buffer:
                cmd_buffer += client_socket.recv( 1024 )
            # 取得命令輸出
            response = run_command(cmd_buffer)
            # 回傳
            client_socket.send(response)

def  run_command ( command ):

    # 刪除字符串末尾的空格
    command = command.rstrip()
    # 執行命令並取回輸出
    try :
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell= True )
    except :
        output =  " Failed to execute command. \r\n "
    # 輸出回傳
    return output



#調用main函數
main()