# -*- coding: utf-8 -*-
"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
class Solution:
     # @return a list of strings, [s1, s2] 
    def letterCombinations(self, digits):
         def dfs(num, string, res):
             if num == length:
                res.append(string) # adg 
                return #不回傳任何東西 -> 函式到這中止
             for letter in dict[digits[num]]:
                    dfs(num +1, string + letter, res) # a -> ad -> adg
                    
         dict = { '2' :[ 'a' , 'b' , 'c' ],
                 '3' :[ 'd' , 'e' , 'f' ],
                 '4' :[ 'g' , 'h' , 'i' ],
                 '5' :[ 'j' , 'k' , 'l' ],
                 '6' :[ 'm' , 'n' , 'o' ],
                 '7' :[ 'p' , 'q' , 'r' , 's' ],
                 '8' :[  't' , 'u' , 'v' ],
                 '9' :[ 'w' , 'x' , 'y' , 'z' ]
                }
         res = []
         length = len(digits)
         dfs(0, '' , res)
         return res
"""
dfs 示意圖
num     digits[num]     string
                          ""
0           2             "a"
1           3             "ad"
2           4             "adg"          "adh"
3           空            res 加入adg    res加入adh .....


"""

if __name__ == "__main__":
    s = Solution()
    print s.letterCombinations("234")
    print len("234")