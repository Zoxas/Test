# -*- coding: utf-8 -*-
"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):# harsh table  value存的是index
            if dict.get(target - nums[i],None) == None : 
                dict[nums[i]] = i 
            else : 
                return (dict[target-nums[i]] + 1 , i + 1)
    
    
    def mytwoSum(self, nums, target):
        for i in range(len(nums)):
            if target - nums[i] < 0: #nums[i] 大於 target 就跳過
                continue
            else:
                for j in range(i+1,len(nums)):#固定 num[i] 跳到下一個 找num[j]
                    if  nums[j] > target:
                        continue
                    else:
                        if nums[i] + nums[j] == target:
                            return (i+1,j+1)
                        else:
                            return None




if __name__ == "__main__":
    s = Solution()
    numbers=[2, 11, 15 , 7]
    target=9
    print s.mytwoSum(numbers,target)