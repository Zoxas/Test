# -*- coding: utf-8 -*-
"""
Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, 
and there exists one unique longest palindromic substring.
「迴文」在中文當中是指倒正著念和反著念都相同的句子，前後對稱，例如「上海自來水來自海上」。
在英文當中是指正著看和反著看都相同的單字，例如「 madam 」。
"""
class  Solution : 
    # @return a string 
    def  longestPalindrome (self, s) :
        """
        :type s: str
        :rtype: int
        利用回文串的對稱性質
        """
        arr = [ '$' , '#' ] 
        for i in range(len(s)): 
            arr.append(s[i]) 
            arr.append ( '#' ) 
        p = [ 0 ] * len(arr) #->紀錄長度 
        ansp = 0
        for i in range( 1 , len(arr)): 
            p[i] = 1 
            # 從p[i]開始擴散左右兩邊  遇到相同 +1 
            while p[i] + i < len(arr) and arr[i + p[i]] == arr[i - p[i]]: 
                p [i] += 1 
            print i,"p[i] = ",p[i]
            if p[i] > p[ansp]: 
                ansp = i                
        
        st = (ansp - (p[ansp]-1) ) // 2 # st = (2*回文中心點的index -回文長度) // 2 = 原本字串中 回文的開頭index
        return s[st:st + p[ansp] - 1 ]

if __name__ == "__main__":
    s = Solution()
    string = "abcba"
    string2 = "abbageceg"
    print s.longestPalindrome(string2)
    