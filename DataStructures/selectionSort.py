# -*- coding: utf-8 -*-
def Selectsort(lst):
    for count in range(len(lst)-1,0,-1):
        Max = 0 # 先假定index0 的是最大值
        for location in range(1,count+1):#+1 是因為range函數的關係
            if lst[location] > lst[Max]:
                Max = location
        #已找出最大 所以交換至右邊
        temp = lst[count]
        lst[count] = lst[Max]
        lst[Max] = temp
    return lst


lst = [54,26,93,17,77,31,44,55,20]
print lst
print Selectsort(lst)
                