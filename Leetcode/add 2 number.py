# -*- coding: utf-8 -*-
"""
You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
(會有進位考量 個十百....)
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        nHead = ListNode(0) #指向 新 Listnode 的頭  nHead -> O->O->O
        flag = 0 #進位的值
        ptr = nHead #移動用的指標
        
        while flag or l1 or l2: 
            node = ListNode(flag) 
            if l1: 
                node.val += l1.val 
                l1 = l1.next 
            if l2: 
                node.val += l2.val 
                l2 = l2.next            
            flag = node.val // 10
            node.val %= 10
            ptr.next = node # nHead and ptr ->None  變成  nHead and ptr -> O
            ptr = node     #nHead -> O(ptr移動到這) -> None 

        return nHead.next
        
if __name__ == "__main__":
    s = Solution()
    n=[2,9,5]
    m=[1,2,3]
    first  = map(ListNode,n)
    second = map(ListNode,m)
    lst  = []
    lst2 = []
    
    for i in range(len(first)):
        lst.append(first[i])
        if i >= 1:
            lst[i-1].next = lst[i]
    print lst[0].next
    
    for i in range(len(second)):
        lst2.append(second[i])
        if i >= 1:
            lst2[i-1].next = lst2[i]
    print lst2[0].next
    
    print s.addTwoNumbers(lst[0],lst2[0]).next.next.val    


    