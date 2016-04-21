# -*- coding: utf-8 -*-
"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

實現字符串匹配函數，並返回一個指針，這個指針指向原字符串中第一次出現待匹配字符串的位置

如：haystack='aabbaa'; needle='bb'。則最後返回的應該是一個字符串，即：'bbaa'。

使用KMP演算法 -> 當字元比對不符時， 我們可以從比對字串 P 中得知某些字元可以略過不需檢查. 如此就不必從文件T的下一個字元重新開始比對
需要一個 table 來記錄
http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html
"""

class  Solution : 
    # @param haystack, a string 
    # @param needle, a string 
    # @return a string or None 
    def  strStr (self, haystack, needle) :
        lenh, lenn = len(haystack), len(needle) 
        if lenn == 0 : 
            return haystack 
        
        next, p = [- 1 ] * (lenn), -1
#=====================建立表==================================        
        for i in range( 1 , lenn): 
            while p >= 0  and needle[i] != needle[p + 1]:#if p = 1 跟 前一個比 沒有匹配就減1 然後繼續跟前前一個比.... 
                p = next[p] 
            if needle[i] == needle[p + 1]: #匹配到 數值加1
                p = p + 1
            next[i] = p #算完存入表裡面
        print next
#========================================================== 
        p = - 1 
        for i in range(lenh):
            while p >= 0  and haystack[i] != needle[p + 1]:#沒有匹配就透過查表往前跳躍 -> 在比較 
                print p
                p = next[p]
                print p
            if haystack[i] == needle[p + 1]: # p = next 的表格索引 -> 匹配就+1 
                p = p + 1 
            if p + 1 == lenn: 
                return haystack[i - p : ] 
        return  None


if __name__ == "__main__":
    s = Solution()
    haystack='BBC ABCDAB ABCDABCDABDE'; needle='AAABAAD'
    needle2='ABCDABD'
    print s.strStr(haystack,needle)
    print s.strStr(haystack,needle2)