# -*- coding: utf-8 -*-
"""
   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
   
刪除鍊錶的第N個元素，只能掃一遍
一個指針先走NK步，然後另一個指針在開頭，一起走直到先走的指針到達末尾，刪除後走的指針
"""

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class  Solution : 
    # @return a ListNode 
    def  removeNthFromEnd (self, head, n) :
        nHead = ListNode(0) 
        nHead.next = head         

        p, t = 0 , head # p拿來計算 t 是否有走n步 , t = 先走的指針

        while p < n: 
            t = t.next 
            p += 1
        pre = nHead #指針在開頭的前一個
        
        while t: # 到尾端時 t.next = None , pre 剛好就是從尾端數來 第 N-1 個
            t, pre = t.next, pre.next 
        pre.next = pre.next.next 
        return nHead.next
"""

移動前(N = 2)


nhead  head
  O ->  1 ->2->3->4->5
 pre           t

移動後(N = 2)

nhead  head
  O ->  1 ->2->3->4->5-> None
              pre         t

"""