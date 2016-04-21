# -*- coding: utf-8 -*-
"""
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return None
        sz = 0
        for i  in range(0,len(nums)):
            if nums[i] == val:
                continue
            else:
                nums[sz] = nums[i]
                sz  += 1
        return sz


if __name__ == "__main__":
    s = Solution()
    m=[1,2,2,5,5]
    print s.removeElement(m,5)