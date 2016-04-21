# -*- coding: utf-8 -*-
"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        string = str(x)
        strlen =  len(string)
        st = ""
        if string[0] == "-":
            st = string[0]
            st += string[strlen:0:-1]
            
        else:
            st = string[::-1]
        return int(st)

if __name__ == "__main__":
    s = Solution()
    a = -12355568
    print s.reverse(a)       

            