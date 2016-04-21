# -*- coding: utf-8 -*-
"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.

For example, given array S = {-1 0 1 2 -1 -4},

A solution set is:
(-1, 0, 1)
(-1,-1, 2)
"""
class Solution(object):
    def mythreeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        dict = {-1:[],0:[],1:[]} 
        
        for i in range(len(nums)):# 負數 放進 -1 正數放進 1  0和重複的放進 0

            if nums[i] < 0 and nums[i] not in dict[-1]:
                dict[-1].append(nums[i])

            elif nums[i] > 0 and nums[i] not in dict[1]:
                dict[1].append(nums[i])
            else:
                dict[0].append(nums[i])
       
        if  0 in dict[0] : #如果 有0存在 就從 -1 和 1 中 挑出相加等於0的
            for i in range(len(dict[-1])):
                for j in range(len(dict[1])):
                    if dict[-1][i] + dict[1][j] == 0:
                        res.add((dict[-1][i],0,dict[1][j]))
            dict[0].remove(0) # 移除0 這樣就只剩下  負數  重複  正數
        
        for i in range(len(dict[0])): # 從3個裡面去挑3個相加等於0的 然後根據大小 放進去list中
            for j in range(len(dict[1])):
                for k in range(len(dict[-1])):
                    if dict[0][i] + dict[1][j] + dict[-1][k] == 0 :
                        m = max(dict[-1][k],dict[0][i],dict[1][j])
                        n = min(dict[-1][k],dict[0][i],dict[1][j])
                        q = -(m+n)
                        res.add((n,q,m))
        
        for j in range(len(dict[1])): #再從 1 和 -1 裡面去挑
            for k in range(len(dict[-1])):
                if (dict[1][j] + dict[-1][k]) != 0  and (-(dict[1][j] + dict[-1][k]) in dict[1] or -(dict[1][j] + dict[-1][k]) in dict[-1]):
                        m = max(dict[-1][k],-(dict[1][j] + dict[-1][k]),dict[1][j])
                        n = min(dict[-1][k],-(dict[1][j] + dict[-1][k]),dict[1][j])
                        q = -(m+n)
                        res.add((n,q,m))
                     
                        
        ans = [list(i) for i in res]   
        return sorted(ans,key = lambda x : x[0])  

    def  mythreeSum2(self, num) :

        numLen, res, dict = len(num), set(), {}
        
        if numLen < 3: return []
        num.sort()
        for p in range(numLen):#建表
             for q in range(p+1 , numLen): 
                 if num[p]+num[q] not  in dict:
                    dict[num[p] +num[q]] = [(p,q)]
                 else :
                    dict[num[p] + num[q]].append((p,q))

        for i in dict: # i 是 num的兩數加總  因為num有排序過 所以 i 大小也有排序過
            T = 0 - i
            if T in num :
                for j in dict[i]:
                    if num[j[1]] >= num[j[0]] >= T :
                        res.add((T,num[j[0]],num[j[1]]))
                        """
                           舉例 dict =  {3: [(0, 1), (0, 3)], 4: [(0, 2), (1, 3)], 5: [(1, 2), (2, 3)]}
                                for k in dict[3]:  print k[0]  --> 得到的是 0 0 都是元組的第一個數
                        """        
        ans = [list(i) for i in res]   
        return sorted(ans,key = lambda x : x[0])            
                    
                    
    def  threeSum (self, num) :
        """
        枚舉第一個數，然後第二個數為這個數的後一個數，第三個數為最後一個數，
        如果和小於0，第二個數後移，如大於0第三個數前移，等於0的話記錄結果並且都向中間移
        """
        num.sort() 
        ans = [] 
        for i in range( 0 , len(num)): 
            if (i > 0  and num[i] == num[i- 1]): #跟上一個重複的話 就跳過
                continue            
            l, r = i + 1 , len(num) - 1 # l為第二個數，r為第三個數
            while l < r: 
                sum = num[l] + num[r] + num[i] 
                if sum == 0 : 
                    ans.append([num[i], num[l], num[r]]) 
                    while l < r and num[l] == num[l + 1 ]: l = l + 1 
                    while l < r and num[r] == num[r - 1 ]: r = r - 1
                    l, r = l + 1 , r - 1 
                elif sum < 0 : 
                    l = l + 1 
                else : 
                    r = r - 1    
        return ans

if __name__ == "__main__":
    s = Solution()
    num = [-3,-1 ,0 ,1 ,2 ,-1 ,-4 , 2 , 3 , 5]
    print s.mythreeSum(num)
    print s.mythreeSum2(num)
    print s.threeSum(num)
    
    
    