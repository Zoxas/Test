# -*- coding: utf-8 -*-
"""
Determine whether an integer is a palindrome. Do this without extra space.
"""
class Solution(object):
    def myisPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        st = ""
        if string[0] == "-":
            return False
            
        else:
            st = string[::-1]
            ts = int(st)
            if x == ts:            
                return True
            else:
                return False

    def  isPalindrome (self, x) : 
        if x <= 0 : 
            return  False  if x < 0  else  True
        a, b = x, 0         
        while a: 
            b, a = b * 10 + a % 10 , a / 10 #b從a的後面取回來  a從個位數逐漸縮減 
        return b == x    
                

if __name__ == "__main__":
    s = Solution()
    a = 12321
    print s.isPalindrome(a)       
