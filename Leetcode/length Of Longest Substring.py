# -*- coding: utf-8 -*-
"""
Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
For "bbbbb" the longest substring is "b", with the length of 1.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        維護兩個指針，保證兩個指針之間的串沒有重複字符，
        後指針掃到某個字符重複時就將前指針向後移到第一個和當前字符相同的字符之後
        """
        dict, ans, p1, p2 = {}, 0 , 0 , 0 # P1 前指標  P2 後指標
        lst = []           
        while p2 < len(s): 
            p = dict.get(s[p2] , None ) # p 回傳 是否有有重複字母 -> 有就回傳index
            if p == None : 
                dict[s[p2]] = p2 
                p2 += 1
                ans = max(ans, p2 - p1) # ans 目前存的最大length 和 新的length做比較
            else :
                lst.append(s[p1:p2])
                while p1 <= p: #遇到重複的字母 將最一開始出現重複字母之前的字串都拋棄 
                    dict.pop(s[p1]) 
                    p1 += 1#移到第一個和當前字符相同的字符之後

        lst.append(s[p1:p2])
 
        index = 0
        LongestSubstring  = ""       
        for  i  in range(len(lst)):
            if len(lst[i]) >= len(LongestSubstring):
                LongestSubstring = lst[i]
                index = i


                
            
        return ans,lst,LongestSubstring,index    
        

if __name__ == "__main__":
    s = Solution()
    string = "abcabcbb"
    string2 = "abcdaefg"
    print s.lengthOfLongestSubstring(string)
    
    
    