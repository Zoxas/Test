# -*- coding: utf-8 -*-
"""
Implement  atoi  to convert a string to an integer.

Hint:  Carefully consider all possible input cases. 
If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes:  It is intended for this problem to be specified vaguely (ie, no given input specs). 
You are responsible to gather all the input requirements up front.

atoi()函數會掃描參數str字符串，跳過前面的空白字符（例如空格，tab縮進等
直到遇上數字或正負符號才開始做轉換，而再遇到非數字或字符串結束時('\0')才結束轉換，並將結果返回。 
【返回值】返迴轉換後的整型數；如果str不能轉換成int或者str為空字符串，那麼將返回0

主要是以下幾個：
1.前面有空格；
2.遇到非法字符就不再分析後面的；
3.有可能越界。

"""
class  Solution : 
    # @return an integer 
    def  atoi (self, str) : 
        if len(str) == 0 : 
            return  0
        sgn, num, p = 0 , 0 , 0
        imin, imax = - 1 << 31 , ( 1 << 31 )- 1 
        
        while str[p] == ' ' : 
            p = p + 1 
        
        if str[p] == '-'  or str[p] == '+' : 
            sgn = 1  if str[p] == '-'  else  0
            p = p + 1 

        while p < len(str) and str[p] >= '0'  and str[p] <= '9' : 
            num = num * 10 + ord(str[p]) - ord( '0' ) 
            x = -num if sgn else num 
            if x < imin: return imin 
            if x > imax: return imax 
            p = p + 1 
        return -num if sgn else num


if __name__ == "__main__":
    s = Solution()
    a = "    +1238"
    print s.atoi(a)       
