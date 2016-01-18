# -*- coding: utf-8 -*-
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last: #index

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]#pivot value固定選第一個

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1 #左指標移動

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1#右指標移動

       if rightmark < leftmark:
           done = True
       else:#左指標值大於 pivot 且 右指標值小於pivot
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp
   #pivot 與 右指標互換 
   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark #左邊皆小於此值 右邊皆大於此值
if __name__ == "__main__":
    alist = [54,26,93,17,77,31,44,55,20]
    quickSort(alist)
    print(alist)