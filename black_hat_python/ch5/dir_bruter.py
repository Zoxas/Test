#-*- coding:utf8 -*-    
    
import  urllib2    
import  threading    
import  Queue    
import  urllib    
    
threads =  50    
target_url =  "http://testphp.vulnweb.com"    
wordlist_file =  "./all.txt"    
resume =  None    #網絡中斷時，延續上一個嘗試的字符串，而不用從頭開始，這裡好像沒用到    
user_agent =  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"    
    
    
def  built_wordlist(wordlist_file):    
    #讀入字典文件    
    fd = open(wordlist_file,  "rb" )    
    raw_words = fd.readlines()    
    fd.close()    
    
    found_resume =  False    
    words = Queue.Queue()    
    
    for  word  in  raw_words:    
        #刪除字符串末尾的空格    
        word = word.rstrip()    
        #如果是延續上一次  
        if  resume  is  not  None :    
    
            if  found_resume:    
                words.put(word)    
            else :    
                if  word == resume:    
                    found_resume =  True    
                    print  "Resuming wordlist from: %s"  % resume    
        else :    
            words.put(word)    
    return  words    
    
def  dir_bruter(word_queue, extentsions= None ):    
    
    while  not  word_queue.empty():    
        attempt = word_queue.get()   
  
        #用於儲存要嘗試的url  
        attempt_list = []    
    
        #檢查是否有文件擴展名，如果沒有就是我們要暴力破解路徑，否則暴力破解文件    
        if  "."  not  in  attempt:    
            attempt_list.append( "/%s/"  % attempt)    
        else :    
            attempt_list.append( "/%s"  % attempt)    
    
        #如果我們想暴力破解檔名結尾    
        if  extentsions:    
            for  extentsion  in  extentsions:    
                attempt_list.append( "/%s%s"  % (attempt, extentsion))    
    
        #迭代我們要嘗試的文件列表    
        for  brute  in  attempt_list:    
            #構造url  
            url =  "%s%s"  % (target_url, urllib.quote(brute))    
            #print url    
            try :    
                headers = {}    
                headers[ 'User-Agent' ] = user_agent    
                r = urllib2.Request(url, headers=headers)    
    
                response = urllib2.urlopen(r)    
                #print response.__dict__  
                if  len(response.read()):    
                    print  "[%d] ＝> %s"  % (response.code, url)   
            #用ｅ接收URLError的信息   
            except  urllib2.URLError,e:    
                # code屬性存在，並且code不是404    
                if  hasattr(e,  'code' )  and  e.code !=  404 :    
                    print  "!!! %d => %s"  % (e.code, url)    
                pass    
    
    
word_queue = built_wordlist(wordlist_file)    
extentsions = [ ".php" ,  ".bak" ,  ".orig" , ".inc" ]    
  
#開啟多線程掃描  
for  i  in  range(threads):    
    t = threading.Thread(target=dir_bruter, args=(word_queue, extentsions))    
    t.start()    