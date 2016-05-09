#-*- coding:utf8 -*-

import urllib2
try :
    body = urllib2.urlopen( "http://www.google.com" )
    print body.read()
except urllib2.URLError, e:
    print (e.code)