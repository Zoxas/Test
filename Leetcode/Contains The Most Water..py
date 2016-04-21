# -*- coding: utf-8 -*-
"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 

n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 

Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

解題思路：兩個隔板的矮的那一個的高度乘以兩個隔板的間距就是儲水量。
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0; right = len(height)-1 
        res = 0
        
        while left < right:
            water = min(height[left], height[right]) * (right- left)
            print water
            if water > res: 
                res = water

            if height[left] < height[right]:
                left += 1

            else :
                right -= 1
        return res
        
if __name__ == "__main__":
    s = Solution()
    a = [1,2,3,4,5,6,7,8]
    print s.maxArea(a)