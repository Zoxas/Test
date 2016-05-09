#-*- coding:utf8 -*-  
  
import  win32gui  
import  win32ui  
import  win32con  
import  win32api  
  
# 獲取桌面窗口的 handle  
hdesktop = win32gui.GetDesktopWindow()  
  
# 判斷螢幕的總大小，單位是像素  
width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)  
height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)  
left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)  
top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)  
  
# 建立裝置環境 (device context)
desktop_dc = win32gui.GetWindowDC(hdesktop)  
img_dc = win32ui.CreateDCFromHandle(desktop_dc)  
  
# 建立放在記憶體的裝置環境 ，用於儲存我們捕獲到的圖片的數據，直到我們保存到文件  
mem_dc = img_dc.CreateCompatibleDC()  
  
# 把螢幕內容複製到記憶體的裝置環境
screenshot = win32ui.CreateBitmap()  
screenshot.CreateCompatibleBitmap(img_dc, width, height)  
mem_dc.SelectObject(screenshot)  
  
#把點陣圖存為檔案 
mem_dc.BitBlt(( 0 , 0 ), (width,height), img_dc, (left, top), win32con.SRCCOPY)  
  
# 將位圖保存到文件中  
screenshot.SaveBitmapFile(mem_dc,  "C:\\test.bmp" )  
  
# 釋放物件
mem_dc.DeleteDC()  
win32gui.DeleteObject(screenshot.GetHandle())  