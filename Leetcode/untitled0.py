# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 23:15:49 2016

@author: zzz20255
"""

class Singleton( object ):
    def __new__( cls , *args, **kwargs):
        if not hasattr ( cls , '_inst' ):
            cls ._inst = super (Singleton, cls ).__new__( cls , *args, **kwargs)
        return cls ._inst

class  Borg ( object ):
    _state = {}
    def  __new__ ( cls , * args , ** kw ):
        ob =  super (Borg, cls ). __new__ ( cls , * args, ** kw)
        ob. __dict__  =  cls ._state
        return ob
        
        

if __name__ == '__main__' :
    class A(Singleton):
        def __init__( self ,s):
            self .s = s
    class B(Borg):
        def __init__( self ,s):
            self .s = s
    print A.mro()
    print B.mro()
    a = A( 'apple' )  
    b = A( 'banana' )
    c = A( 'papaya' )
    print id(a),a.s
    print id(b),b.s
    print ""
    d = B( 'apple' )  
    e = B( 'banana' )
    f = B( 'papaya' )
    print id(d),d.s
    print id(e),e.s
    
    
    
