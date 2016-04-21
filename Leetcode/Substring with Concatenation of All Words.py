# -*- coding: utf-8 -*-
"""
You are given a string, s, and a list of words, words, that are all of the same length. 
Find all starting indices of substring(s) in s that is a concatenation of each word in words 
exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

給出一個字符串集合L和字符串S，找出S從哪些位置開始恰好包含每個字符串各一次。
這類判斷某一段包含了哪些內容的題做法都差不多，一個pre指針，一個last指針，用一個集合記錄這之間出現的值，
last指針不斷往後掃直到掃到多餘的元素，然後pre指針再從之前的位置掃到第一個有這個元素的位置之後，這時候last指針就可以繼續後移了。

這個題就是要做一些變形，將S分成len(L(0))段，每段分別使用以上算法。
比如len(L(0))=3,len(S)=10時，就分成S[0,3,6,9],S[1,4,7],S[2,5,8]三段。
"""

class  Solution : 
    # @param S, a string 
    # @param L, a list of string 
    # @return a list of integer 
    def  findSubstring (self, S, L):
        LS, LL, LL0 = len(S), len(L), len(L[0]) 
        did, ids, dl = {}, 0 , {} 
        # did -> 紀錄 L的value 和 index (Lvalue : Lindex + 1) 
        #dl 紀錄 L 中 VALUE 出現的次數 (Lindex : count) 
        for x in L: 
            id = did.get(x, - 1 ) 
            if id == - 1 : 
                 ids = ids + 1
                 id = ids 
                 did[x] = id # S 是 index , id 是 VALUE 
            dl[id] = dl.get(id , 0) + 1
        
        print did
        print dl

        pos, ans = [ 0 ] * LS, []
        
        for k, v in did.items(): #(Lvalue , Lindex + 1) 
            f = S.find(k)#回傳第一個字詞的index 
            while f != - 1 : 
                pos[f] = v 
                f = S.find(k, f + 1)#繼續往後找 
        print pos
        for sp in range(LL0): 
            np, pp, tot, dt = sp, sp, 0 , {} 
            while np < LS:
                t = pos[np] 
                if t == 0 :
                    tot, dt = 0 , {} 
                    pp, np = np + LL0, np + LL0 
                
                elif dt.get(t, 0) < dl[t]:# dt = {}                   
                    dt[t] = dt.get(t, 0 ) + 1
                    tot = tot + 1
                    print "dt:",dt,pp,np
                    if tot == LL:
                        ans.append(pp) 
                        print ans
                    np = np + LL0 #np 跟 pp 差別
                else:
                    while pos[pp] != t:
                        tot = tot - 1
                        dt[pos[pp]] -= 1
                        pp = pp + LL0 
                    pp = pp + LL0 
                    dt[t] -= 1
                    tot = tot - 1 
        return ans
       
if __name__ == "__main__":
    s = Solution()
    x = "barfoothefoobarman"
    w = ["bar", "the"]
    print s.findSubstring(x,w)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        