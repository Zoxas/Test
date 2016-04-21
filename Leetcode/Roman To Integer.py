# -*- coding: utf-8 -*-
"""
羅馬數字共有7個，即I（1）、V（5）、X（10）、L（50）、C（100）、D（500）和M（1000）
重複數次：一個羅馬數字重複幾次，就表示這個數的幾倍。
右加左減：
在較大的羅馬數字的右邊記上較小的羅馬數字，表示大數字加小數字。
在較大的羅馬數字的左邊記上較小的羅馬數字，表示大數字減小數字。
左減的數字有限制，僅限於I、X、C。比如45不可以寫成VL，只能是XLV


CCLXVII ＝267（100+100+50+10+5+1+1）
DCLXXV=675 (500+100+50+10+10+5)
MMCDLXIX=2469（1000+1000+[500-100]+50+10+[10-1]）
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {"M": 1000 , "D":500 , "C":100 , "L":50 ,"X":10 , "V":5 ,"I":1}

        ans = dict[s[len(s)-1]] #羅馬數字最右邊可以直接先加
        
        for i in range(len(s)-1):
            
            if  dict.get(s[i]) < dict.get(s[i+1]):
                ans -= dict.get(s[i])

            else:
                ans += dict.get(s[i])

        return ans


if __name__ == "__main__":
    s = Solution()
    num1 = "MMCDLXIX"
    num2 = "DCLXXV"
    num3 = "CCLXVII"
    num4 = "IX"
    
    print s.romanToInt(num1)
    print s.romanToInt(num2)
    print s.romanToInt(num3)
    print s.romanToInt(num4)
                 
            