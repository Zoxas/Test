# -*- coding: utf-8 -*-
def InsertionSort(lst):
    for index in range(1,len(lst)):#index 0的值預設是在排序好的序列中(會擴增)
        currentvalue = lst[index]#未排序的序列的第一個值
        position = index #未排序的序列第一個
        
        while position > 0 and lst[position-1] > currentvalue:
            lst[position] = lst[position-1]
            position = position -1
        lst[position] = currentvalue
    return lst


lst = [54,26,93,17,77,31,44,55,20]
print lst
print InsertionSort(lst)
            
    
    
        
    
