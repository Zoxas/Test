import requests
from bs4 import BeautifulSoup
import json
import re
import urlparse
import shutil

x = 0
x = raw_input(">>> Input Youtube https: ")
print "get : " , x
res = requests.get(x)
soup =  BeautifulSoup(res.text,"html.parser")
name = soup.select("title")[0].text
print name[1:5]

m = re.search('"args":({.*?})',res.text)
jd = json.loads(m.group(1)) 
a = urlparse.parse_qs(jd["url_encoded_fmt_stream_map"])
print a['url'][0]

res2 = requests.get( a['url'][0],stream = True)
names = name[0:5] + ".mp4"
f = open(names,"wb")
shutil.copyfileobj(res2.raw,f)
f.close()

print " Finish !!"