# -*- coding: utf-8 -*-
"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, 
with the first two elements of nums being 1 and 2 respectively. 
It doesn't matter what you leave beyond the new length.

"""

class Solution(object):
    def myremoveDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        res = set(nums)
        lst = list(res)
        return len(res)
    
    def  removeDuplicates (self, A) : 
        if len(A) == 0 : 
            return  0
        sz = 1 
        for i in range( 1 , len(A)): 
            if A[i] != A[i- 1]: 
                A[sz] = A[i] 
                sz += 1 
        return sz
if __name__ == "__main__":
    s = Solution()
    m=[1,2,2,5,5]
    print s.myremoveDuplicates(m)
    print s.removeDuplicates(m)    