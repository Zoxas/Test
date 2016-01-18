# -*- coding: utf-8 -*-
"""
需要用到遞迴的概念
"""
def mergesort(lst):
    print "spilit",lst
    if len(lst) > 1 :
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]
        
        mergesort(left)#先遞迴左半邊
        mergesort(right)#由小-->大-->小-->大(由結果去思考比較容易理解)
        
        i=0
        j=0
        k=0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i=i+1
            else:
                lst[k] = right[j]
                j=j+1
            k = k+1
        while i < len(left):
            lst[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            lst[k]=right[j]
            j=j+1
            k=k+1
    print "Merging ",lst        
            
alist = [54,26,93,17,77,31,44,55,20]
mergesort(alist)
print(alist) 
