# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 00:28:41 2016

@author: zzz20255
"""

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class  Solution : 
    # @param two ListNodes 
    # ​​@return a ListNode 
    def mergeTwoLists (self, l1, l2) :
        nHead = ListNode(0) 
        lt, rt, backHead = l1, l2, nHead 
       
        while lt or rt: 
            if lt is  None : 
                nHead.next, rt = rt, rt.next 
            elif rt is  None : 
                nHead.next, lt = lt, lt.next 
            
            elif lt.val < rt.val: 
                nHead.next, lt = lt, lt.next 
            else : 
                nHead .next, rt = rt, rt.next 
            nHead = nHead.next 

        return backHead.next
"""
nHead = ListNode(0) 
backHead = nHead
lst = 1 -> 2 -> 3
rt = lst[0]

nHead.next = rt (backHead.next也會指向lst[0])
rt =rt.next (nHead.next 還是指向 lst[0]的記憶體位址 rt 則移動到lst[1] 的記憶體位址 )
nHead = nHead.next (nHead.移動到 lst[0] , 所以nHead.next  = lst[0].next = lst[1]  
                    但是backhead 還是在 ListNode(0)上 backHead.next = lst[0] )
                    
總結 :
ptr = node
ptr2 = ptr

當 ptr.next = node2  --> ptr2.next 也會指向node2
當 ptr = node2  or node.next or ptr.next --> ptr2 還是指向node

"""
if __name__ == "__main__":
    s = Solution()
    n=[2,5,9]
    m=[1,2,3]
    first  = map(ListNode,n)
    second = map(ListNode,m)
    lst  = []
    lst2 = []
    
    for i in range(len(first)):
        lst.append(first[i])
        if i >= 1:
            lst[i-1].next = lst[i]
    print lst[0]
    
    for i in range(len(second)):
        lst2.append(second[i])
        if i >= 1:
            lst2[i-1].next = lst2[i]
    print lst2[0]
    
    print s.mergeTwoLists(lst[0],lst2[0]).val