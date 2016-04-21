# -*- coding: utf-8 -*-
"""
Merge  k  sorted linked lists and return it as one sorted list. 
Analyze and describe its complexity.

解題思路：歸併k個已經排好序的鍊錶。使用堆這一數據結構，
首先將每條鍊錶的頭節點進入堆中，然後將最小的彈出，並將最小的節點這條鍊錶的下一個節點入堆，
依次類推，最終形成的鍊錶就是歸併好的鍊錶。

(跳過 還想不清楚)
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def  mergeKLists (self, lists) :
        #將 lists 中 非None的node index 和 值 加入到heap
        self.heap = [[i, lists[i].val] for i in range(len(lists)) if lists [i] != None ] 
        self.hsize = len(self.heap) 
        # i 從 hsize -1 到 0
        for i in range(self.hsize - 1 , - 1 , -1): 
            self.adjustdown(i) #heapify
        
        nHead = ListNode(0) 
        head = nHead 
        
        while self.hsize > 0 : 
            ind , val = self.heap[0][0], self.heap[0][1] #self.heap[0] = [i, lists[i].val]
            head.next = lists[ind] 
            head = head.next 
            lists[ind] = lists[ind].next

            if lists[ind] is  None : #list[ind]只有一個node時
                self.heap[ 0 ] = self.heap[self.hsize- 1 ] # 將heap最後一個index 填來 heap[0]-> recall heap的數據結構比較好理解
                self.hsize = self.hsize - 1 
            else : 
                self.heap[ 0 ] = [ind,lists[ind].val] 
            self.adjustdown( 0 ) 
        return nHead.next 
            
    def  adjustdown (self, p) :
        lc = lambda x: (x + 1 ) * 2 - 1
        rc = lambda x: (x + 1 ) * 2 
        while  True : 
            np, pv = p, self.heap[p][1] # np = index ; pv = value
            
            if lc(p) < self.hsize and self.heap[lc(p)][ 1 ] < pv: 
                np, pv = lc(p), self .heap[lc(p)][ 1 ] 

            if rc(p) < self.hsize and self.heap[rc(p)][ 1 ] < pv: 
                np = rc(p) 

            if np == p: 
                break 
            else : 
                self.heap[np], self.heap[p] = self.heap[p], self.heap[np] 
                p = np
    




