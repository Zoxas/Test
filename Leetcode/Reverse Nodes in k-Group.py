# -*- coding: utf-8 -*-
"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

到每第K個元素的時候掉個頭就行，中間就是正常的鍊錶逆置，注意最後幾個不要處理
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode

    def reverse(self, start, end): 
    #               start       end   end        start
    # 會對List進行反轉 1  -> 2  -> 3  => 3  -> 2  -> 1  而 1->2  => 2 -> 1 以此類推
        newhead=ListNode(0) 
        newhead.next=start

        while newhead.next!=end:
            tmp=start.next
            start.next=tmp.next
            tmp.next=newhead.next
            newhead.next=tmp
        print end.val
        print start.val
        return [end, start]
    
    def reverseKGroup(self, head, k):
        if head==None: 
            return None

        nhead=ListNode(0) 
        nhead.next=head 
        start=nhead

        while start.next:#透過 K 來取區間
            end=start
            for i in range(k-1):
                end=end.next
                if end.next==None: 
                    return nhead.next
            res=self.reverse(start.next, end.next)
            start.next=res[0]#node(0) 指向反轉後的end
            start=res[1]#start跳去反轉後的start
        return nhead.next
        
if __name__ == "__main__":
    s = Solution()
    m=[1,2,3,4,5]
    second = map(ListNode,m)
    lst2 = []  
    for i in range(len(second)):
        lst2.append(second[i])
        if i >= 1:
            lst2[i-1].next = lst2[i]   
    x = s.reverseKGroup(lst2[0],5)
    print x.val
    print x.next.val
    print x.next.next.val
    #print x.next.next.ne
        
        
        
        
        
        
        