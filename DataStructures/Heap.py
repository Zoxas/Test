# -*- coding: utf-8 -*-
"""
BinaryHeap() creates a new, empty, binary heap.

insert(k) adds a new item to the heap.
Once a new item is appended to the tree, [percUp] takes over and positions the new item properly.

delMin() returns the item with the minimum key value, removing the item from the heap.

buildHeap(list) builds a new heap from a list of keys.

delMin() or buildHeap(list) -> [percdown] takes over and positions the new item properly.
"""
class BinHeap:
    def __init__(self):
        self.heapList = [0] #list[0] = 0 , List[1]=root
        self.currentSize = 0


    def percUp(self,i):
        while i // 2 > 0: #parent index > 0 
          if self.heapList[i] < self.heapList[i // 2]: #parent > child -> swap
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i) #根據大小判斷 選擇右邊或是左邊-child
          if self.heapList[i] > self.heapList[mc]: #如果本身大於child 就swap
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):#判斷左-child 和 右-child哪個小 回傳index
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      retval = self.heapList[1] #root
      self.heapList[1] = self.heapList[self.currentSize] #root = 序列中最後的最後的值
      self.currentSize = self.currentSize - 1
      self.heapList.pop()#移除序列中最後面的值
      self.percDown(1)#維持heap的性質
      return retval#回傳被移除的Min

    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):#由下而上建立Heap Tree
          self.percDown(i)
          i = i - 1
      print "After Heap :",self.heapList[1:] 
    

bh = BinHeap()
bh.buildHeap([9,5,6,2,3])

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
