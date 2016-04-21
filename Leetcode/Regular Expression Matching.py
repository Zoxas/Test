# -*- coding: utf-8 -*-
"""
實現 . 和 * 的正則表達式匹配，其中.匹配任一字符，*表示重複之前內容0次以上。
動態規劃，dp[i][j]表示s[1..i]和p[1..j]匹配，需要考慮的情況還是比較複雜的，搜索應該也可行。

"""
class  Solution : 
    # @return a boolean 
    def  isMatch (self, s, p) :
        s, p = ' ' + s, ' ' + p 
        dp = [[ False ] * (len(p)) for i in range(len (s))] # len(s) x len(p) 的大小
        dp[ 0 ][ 0 ] = True
        ind = 2 
        
        while ind < len(p) and p[ind] == '*' : #如果遇到 p 是 * 則 邊界值 從 0 -> 1 
            dp[ 0 ][ind], ind = True , ind + 2 


        for i in range( 1 , len(s)): 
            for j in range( 1 , len(p)): 
                
                #動態規劃中 對角線為為true 且 有匹配或是p[j] = . 就 0 -> 1
                if (s[i] == p[j] or p[j] == '.' ) and dp[i- 1][j- 1]:
                    dp[i][j] = True 

                
                if p[j] == '*'  and (dp[i][j- 2] or ((p[j- 1] == '.'  or p[j- 1] == s[i]) and (dp[i- 1 ][j- 2 ] or dp[i- 1 ][j]))): 
                    dp[i ][j] = True 
        
        return dp[len(s) - 1][len(p) - 1]

if __name__ == "__main__":
    s = Solution() 
    print s.isMatch( "aa" , "a" )               # False 
    print s.isMatch( "aa" , "aa" )              # True 
    print s.isMatch( "aaa" , "aa" )              # False 
    print s.isMatch( "aa" , "a*" )              # True 
    print s.isMatch( "aa" , ".*" )              # True 
    print s.isMatch( "ab" , ".*" )              # True 
    print s .isMatch( "aab" , "c*a*b" )          # True 
    print s.isMatch( "aaa" , "ab*a" )           # Fasle 
    print s.isMatch( "aaba" , "ab*a*c* a" )      # False 
    print s.isMatch( "" , ".*" )                # True 
    print s.isMatch( "bbab" , "b*a*" )          # False 
    print s.isMatch( "aab" , "b. *" )            # False
    
    
"""
1.對角線為true 且 目前的s[i]和p[j]匹配 或是 目前p[j]是 .  就可以 0 -> 1

2.當遇到 目前p[j] 是 * 時  

dp[i][j- 2] 是 True(即格子中，目前向左2格是True)  -> 經測試為非必要條件 下面兩個條件都符合就好

或是
＝＝＝
p[j- 1] == '.'  or p[j- 1] == s[i] (即格子中，目前向左1格是匹配 或是 目前向左1格的p是 . )  

且

dp[i- 1][j- 2] or dp[i- 1][j]  (即格子中，目前對角線向左1格是True 或是 目前向上1格是true)
＝＝＝
"""