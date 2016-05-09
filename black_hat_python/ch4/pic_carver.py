#-*- coding:utf8 -*-  
import  re  
import  zlib  
from  scapy.all  import  *  
  
pictures_directory =  "./pictures/"  
pcap_file =  "test.pcap"  
  
  
def  get_http_headers(http_payload):  
    try :  
        #如果為http流量，提取http headers  
        headers_raw = http_payload[:http_payload.index( "\r\n\r\n" )+ 2 ]  
  
        #對 http headers進行切分  
        headers = dict(re.findall(r"(?P<name>.*?):(?P<value>.*?)\r\n" , headers_raw))  
  
    except :  
        return  None  
  
    if  "Content-Type"  not  in  headers:  
        return  None  
  
    return  headers  
  
def  extract_image(headers, http_payload):  
    image =  None  
    image_type =  None  
   
    try :  
        if  "image"  in  headers[ 'Content-Type' ]:  
            #獲取圖像類型和圖像數據  
            image_type = headers[ 'Content-Type' ].split( "/" )[ 1 ]  
            image = http_payload[http_payload.index( "\r\n\r\n" )+ 4 :]  
  
            #如果數據進行了壓縮則解壓  
            try :  
                if  "Content-Encoding"  in  headers.keys():  
                    if  headers[ 'Content-Encoding' ] ==  "gzip" :  
                        image = zlib.decompress(image,  16 +zlib.MAX_WBITS)  
                    elif  headers[ 'Content-Encoding' ] ==  "deflate" :  
                        image = zlib.decompress(image)  
            except :  
                pass  
    except :  
        return  None ,  None  
    
    return  image,image_type  

def  http_assembler(pcap_file):   

    carved_images =  0  
    faces_detected =  0  

    a = rdpcap(pcap_file)    
    sessions = a.sessions()  
  
  
    for  session  in  sessions:  
        http_payload = ""  
        for  packet  in  sessions[session]:  
            try :  
                if  packet[TCP].dport ==  80  or  packet[TCP].sport ==  80 :  
                    # 重組stream  
                    http_payload += str(packet[TCP].payload)  
            except :  
                pass  
   
        headers = get_http_headers(http_payload)  
  
        if  headers  is  None :  
            continue  
        image, image_type = extract_image(headers, http_payload)  
        if  image  is  not  None  and  image_type  is  not  None :  
            # 存儲圖像  
            file_name =  "%s-pic_carver_%d.%s"  % (pcap_file, carved_images, image_type)  
            fd = open( "%s/%s"  % (pictures_directory, file_name),  "wb" )  
            fd.write(image)  
            fd.close() 
            carved_images +=  1  

    return  carved_images, faces_detected  
  
  
carved_images, faces_detected = http_assembler(pcap_file)  

print  "Extracted: %d images"  % carved_images  
