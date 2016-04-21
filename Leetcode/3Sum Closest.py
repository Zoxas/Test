# -*- coding: utf-8 -*-
"""
   For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution(object):
    def threeSumClosest(self, num, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        num.sort() 
        ans = None 
        for i in range( 0 , len(num)): 
            l, r = i + 1 , len(num) - 1 # l為第二個數，r為第三個數
            while l < r: 
                sum = num[l] + num[r] + num[i] 
                if ans == None or abs(ans -target) > abs(sum - target) :
                    ans = sum         
                elif sum <= target:
                    l = l+1
                else:
                    r=r-1
                
        return ans
if __name__ == "__main__":
    s = Solution()
    num = [-3,-1 ,0 ,1 ,2 ,-1 ,-4 , 2]
    print s.threeSumClosest(num,2)
    print s.threeSumClosest(num,6)
    print s.threeSumClosest(num,-2)    
                        