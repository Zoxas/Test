#-*- coding:utf8 -*-  
  
import  ctypes  
import  random  
import  time  
import  sys  
  
user32 = ctypes.windll.user32  
kernel32 = ctypes.windll.kernel32  
  
# 用於記錄鼠標單擊，鍵盤按鍵和雙擊的總數量  
keystrokes =  0  
mouse_clicks =  0  
double_clicks =  0  
  
# 定義LASTINPUTINFO結構體  
class  LASTINPUTINFO(ctypes.Structure):  
    _fields_ = [  
                ( "cbSize" , ctypes.c_uint),   #結構體大小  
                ( "dwTime" , ctypes.c_ulong)   #系統最後輸入時間  
                ]  
  
def  get_last_input():  
    struct_lastinputinfo = LASTINPUTINFO()  
    struct_lastinputinfo.cbSize = ctypes.sizeof(LASTINPUTINFO)  
  
    # 獲得最後一次偵測到的輸入  
    user32.GetLastInputInfo(ctypes.byref(struct_lastinputinfo))  
  
    # 獲取系統開機以來的時間  
    run_time = kernel32.GetTickCount()  
  
    elapsed = run_time - struct_lastinputinfo.dwTime  
    print  "[*] It's been %d milliseconds since the last input event."  % elapsed  
  
    return  elapsed  
  
# 測試後刪除下面代碼，這只是測試上面代碼能否運行成功  
# while True:  
#   get_last_input()  
#   time.sleep(1)  
  
def  get_key_press():  
    global  mouse_clicks  
    global  keystrokes  
  
    for  i  in  range( 0 , 0xff ):  
        # 檢測某個按鍵是否被按下  
        if  user32.GetAsyncKeyState(i) == - 32767 :  
            # 左鍵點擊代碼為0x1  
            if  i ==  0x1 :  
                # 滑鼠單擊的數目和時間  
                mouse_clicks +=  1  
                return  time.time()  
            # 鍵盤ASCII按鍵是從 23-127（具體可看ASCII表），為可打印字符，這就獲取了鍵盤的敲擊次數  
            elif  i >  32  and  i <  127 :  
                keystrokes +=  1  
  
    return  None  
  
def  detect_sandbox():  
    global  mouse_clicks  
    global  keystrokes  
  
    # 定義鍵盤，單擊，雙擊的最大值（閥值）  
    max_keystrokes = random.randint( 10 , 25 )  
    max_mouse_clicks = random.randint( 5 , 25 )  
    max_double_clicks =  10  
  
    double_clicks =  0  
    double_click_threshold =  0.250  #秒為單位  
    first_double_click =  None  
  
    average_mousetime =  0  
    max_input_threshold =  30000  #毫秒為單位  
  
    previous_timestamp =  None  
    detection_complete =  False  
  
    # 獲取用戶最後一次輸入之後經歷的時間  
    last_input = get_last_input()  
  
    # 超過設定的閥值時強制退出，就是用戶最後一次輸入之後經歷的時間太長，都沒用戶活動了  
    if  last_input >= max_input_threshold:  
        sys.exit( 0 )  
  
    # 循環檢測  
    while  not  detection_complete:  
  
        # 獲取按下滑鼠的時間
        keypress_time = get_key_press()  
  
        if  keypress_time  is  not  None  and  previous_timestamp  is  not  None :  
            # 計算兩次點擊的相隔時間  
            elapsed = keypress_time - previous_timestamp  
            # 間隔時間短的話，則為用戶雙擊  
            if  elapsed <= double_click_threshold:  
                double_clicks +=  1  
                if  first_double_click  is  None :  
                    # 獲取第一次雙擊的時間  
                    first_double_click = time.time()  
                else :  
                    # 是否是沙盒的管理者在沙盒中模仿用戶的點擊（因為普通用戶通常不會雙擊這麼多）  
                    if  double_clicks == max_double_clicks:  
                        # 短時間內，滑鼠雙擊次數達到了我們設定的最大值（最大次數*雙擊間隔）就放棄 
                        if  keypress_time - first_double_click <= (max_double_clicks * double_click_threshold):  
                            sys.exit( 0 )  
            # 有了足夠的使用者互動 就可以繼續下去了  
            if  keystrokes >= max_keystrokes  and  double_clicks >= max_double_clicks  and  mouse_clicks >=max_mouse_clicks:  
                return  
  
            previous_timestamp = keypress_time  
        elif  keypress_time  is  not  None :  
            previous_timestamp = keypress_time  
  
  
  
detect_sandbox()  
print  "We are Ok!"  