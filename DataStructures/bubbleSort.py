# -*- coding: utf-8 -*-
def BubbleSort(lst):
    for count in range(len(lst)-1,0,-1):#要交換到次數(遞減)
        for i in range(count):#根據要交換的次數 開始交換
            if lst[i] > lst[i+1]:
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
    return lst


lst = [54,26,93,17,77,31,44,55,20]
print lst
print BubbleSort(lst)


            
        
    