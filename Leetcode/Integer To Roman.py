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

class Solution:
    # @return a string
    def intToRoman(self, num):
        value = [  1000 ,   900 ,   500 ,    400 ,   100 ,    90 ,     50 ,    40 ,     10 ,     9 ,     5 ,     4 ,      1 ]
        roman = [ " M " , " CM " , " D " , " CD " , " C " , " XC " , " L " , " XL " , " X " , " IX " , " V " , " IV " , " I " ]
        str = ""
        for i in range(len(value)):
            while num >= value[i]:
                num -= value[i]
                str += roman[i]
        return str
    
    def intToRoman2(self, num):
        ronum  = [['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
                  ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
                  ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
                  ['', 'M', 'MM', 'MMM', '  ', ' ', '  ', '   ', '    ', '  ']]
        ans, ind = '', 0
        while num:
            ans = ronum[ind][num%10] + ans
            num, ind = num / 10, ind + 1
        return ans


if __name__ == "__main__":
    s = Solution()
    num1 = 2469
    num2 = 675
    num3 = 267
    
    print s.intToRoman(num1)
    print s.intToRoman(num2)
    print s.intToRoman(num3)
                 



