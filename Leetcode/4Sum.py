# -*- coding: utf-8 -*-
"""
For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

A solution set is:
(-1,  0, 0, 1)
(-2, -1, 1, 2)
(-2,  0, 0, 2)
    
要用到哈希表的思路，這樣可以空間換時間，以增加空間複雜度的代價來降低時間複雜度。
首先建立一個字典dict，字典的key值為數組中每兩個元素的和，每個key對應的value為這兩個元素的下標組成的元組，元組不一定是唯一的。

如對於num=[1,2,3,2]來說，dict={3:[(0,1),(0,3)], 4:[(0,2),(1,3)] , 5:[(1,2),(2,3)]}。

這樣就可以檢查target-key這個值在不在dict的key值中，如果target-key在dict中並且下標符合要求，那麼就找到了這樣的一組解。

由於需要去重，這裡選用set()類型的數據結構，即無序無重複元素集。最後將每個找出來的解(set()類型)轉換成list類型輸出即可。
"""

class Solution:
     # @return a list of lists of length 4, [[val1,val2,val3,val4]] 
    def fourSum(self, num, target):

        numLen, res, dict = len(num), set(), {}
        
        if numLen < 4: return []
        num.sort()
        for p in range(numLen):#建表
             for q in range(p+1 , numLen): 
                 if num[p]+num[q] not  in dict:
                    dict[num[p] +num[q]] = [(p,q)]
                 else :
                    dict[num[p] + num[q]].append((p,q))

        for i in dict: # i 是 num的兩數加總  因為num有排序過 所以 i 大小也有排序過
            T = target-i
            if T in dict:
                for j in dict[i]:
                    for k in dict[T]:
                        if k[0] > j[1]: #避免重複 列出情況為 j[0] <= j[1] < k[0] <= k[1] 
                            res.add((num[j[0]],num[j[1]],num[k[0]],num[k[1]]))
                            """
                           舉例 dict =  {3: [(0, 1), (0, 3)], 4: [(0, 2), (1, 3)], 5: [(1, 2), (2, 3)]}
                                for k in dict[3]:  print k[0]  --> 得到的是 0 0 都是元組的第一個數
                            """
        return [list(i) for i in res]           

if __name__ == "__main__":
    s = Solution()
    num = [-3,-1 ,0 ,1 ,2 ,-1 ,-4 , 2]   
    print s.fourSum(num,-1)