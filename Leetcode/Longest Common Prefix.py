# -*- coding: utf-8 -*-
"""
暴力法直接一位位掃，直到遇到某位有不同的字符或者某個字符串結尾
"""

class  Solution : 
    # @return a string 

    def  longestCommonPrefix2(self, strs) : 
        if len(strs) <= 1 : 
            return strs[ 0 ] if len(strs) == 1  else  ""
        
        end, minl = 0 , min([ len(s) for s in strs]) #關鍵

        while end < minl: 
            for i in range( 1 , len(strs)):             

                if strs[i][end] != strs[i- 1][end]: 
                    return strs [0][:end]
            end = end + 1 

        return strs[ 0 ][:end]
        
if __name__ == "__main__":
    s = Solution()
    strs = ["acabbc","acabbc","acabb","acabb"]
    print s.longestCommonPrefix2(strs)