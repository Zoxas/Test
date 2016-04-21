# -*- coding: utf-8 -*-
"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. 
You may not modify the values in the list, only nodes itself can be changed.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self,head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        nHead = ListNode(0) 
        nHead.next = head
        p = nHead

        while p.next and p.next.next:
            tmp = p.next.next
            p.next.next = tmp.next
            tmp.next = p.next
            p.next = tmp
            p = p.next.next

        return nHead.next
    def  swapPairs2(self, head) : 
        if head is  None  or head.next is  None : 
            return head 
        nHead = ListNode( 0 ) 
        nHead.next = head 
        p1, p2 = nHead , head 
        while p2 and p2.next: 
            p2 = p2.next.next 
            p1.next.next.next = p1.next 
            p1.next = p1.next.next 
            p1.next.next.next = p2 
            p1 = p1.next .next 
        return nHead.next
    
    def  swapPairs3( self , head ):
        if head !=  None  and head.next !=  None :
            next  = head.next
            print next.val,"next"
            head.next =  self.swapPairs3( next.next) # 1 -> swap(3) ; 3 -> swap(None)
            next.next = head
            return  next
        return head    
"""
Listnode 與 指標的觀念   EX:  1 -> 2 -> 3
(XXX = OOO.next  -> 等號左邊 = 指向or等於  等號右邊 = node)
如: tmp = p.next.next  -> tmp 等於 2這個節點 (所以tmp.next = 3)
如: tmp.next = p.next  -> tmp 的箭頭指向 1這個節點
如: p.next.next = tmp.next  -> p.next的箭頭指向 tmp.next = 3 這個節點

p = nHead(nHead.next = head)
p = 0 -> 1 -> 2 -> 3
p = 0 -> 1 -> 2 -> 3 -> 4 

tmp = p.next.next  
tmp = 2 -> 3

tmp = 2 -> 3 -> 4
************************************
p.next.next = tmp.next
p = 0 -> 1     
          \    
tmp = 2 -> 3

p = 0 -> 1     
          \    
tmp = 2 -> 3 -> 4
************************************
tmp.next = p.next
p = 0 -> 1     
        ^ \
       /   v
tmp = 2     3

p = 0 -> 1     
        ^ \
       /   v
tmp = 2     3 -> 4
************************************
p.next = tmp

p = 0     1     
    \    ^ \
     v  /   v
tmp = 2     3
=======================
p = 0     1     
    \    ^ \
     v  /   v
tmp = 2     3 -> 4


   0  p = 1     
    \    ^ \
     v  /   v
tmp = 2     3 -> 4

   0      1     
    \    ^ \
     v  /   v
tmp = 2     4 -> 3 = p


"""
if __name__ == "__main__":
    s = Solution()
    m=[1,2,3,4]
    second = map(ListNode,m)
    lst2 = []  
    for i in range(len(second)):
        lst2.append(second[i])
        if i >= 1:
            lst2[i-1].next = lst2[i]
#    print lst2[0].next.next.next.val
    x = s.swapPairs3(lst2[0])
    print x.val
    print x.next.val
    print x.next.next.val
    print x.next.next.next.val
    #print x.next.next.next.val

