# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 17:49:44 2016

@author: zzz20255
"""

class Solution:
     # @return an integer 
    def divide(self, dividend, divisor):
        
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):#負數情況的處理
             if abs(dividend) < abs(divisor):
                 return 0

        sum = 0; count = 0; res = 0        
        a = abs(dividend); b = abs(divisor)

        while a >= b:
            sum = b
            count = 1

            while sum + sum <= a: # sum , count 是雙倍成長 
                sum += sum
                count += count
                print (sum,count)
            
            a -= sum
            res += count
            
        
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = 0 - res
        return res

if __name__ == "__main__":
    s = Solution()
    print s.divide(100,3)