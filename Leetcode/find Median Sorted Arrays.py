# -*- coding: utf-8 -*-
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively. 
Find the median of the two sorted arrays. 
The overall run time complexity should be O(log (m+n)).
===============================================================================
Let's do an example: a = [2,3,6,8] and b = [1,4,5,7,9].

Merged, they'd be [1,2,3,4,5,6,7,8,9]. I can't afford to actually merge, because of the O(log(m+n)), 
but imagine we'd merge. The usual way. Then after the first four numbers, the next one is the median.

What could the status of the merging be after having merged the first four numbers? 
We'd have used i numbers from a and 4-i numbers from b. The five candidate statuses are:

     Remaining    Remaining     Last used    Last used
i    a[i, ...]   b[4-i, ...]    from b       from a

0    [2,3,6,8]           [9]    7            None
1      [3,6,8]         [7,9]    5            2
2        [6,8]       [5,7,9]    4            3
3          [8]     [4,5,7,9]    1            6
4           []   [1,4,5,7,9]    None         8

To be possible, a status must obey two rules:

1.The last number used from b can't be larger than the next remaining number in a 
(because it would've been a mistake to use it first).
2.The last number used from a can't be larger than the next remaining number in b.

You can see that only the first two statuses (i=0 and i=1) violate rule 1. 
And of course with growing i, the last-used b-number shrinks and the next remaining a-number grows. 
So it's monotone - from small to large i, 
first you have the rule-1-violaters and then you have the rule-1-obeyers. 
And for rule 2 it's the other way around.

Of course after merging the first four numbers, we must be in some status. 
So there must be some status that obeys both rules. 
And we can simply take the first one that obeys rule 1. 
And we can use binary search to find it. In the code, for a given i, 

the next remaining number in a is a[i] and the last-used number from b is b[after-i-1], 

and my bsearch simply tests rule 1.

So in our example we get that after merging four numbers, 
we'd have [6,8] and [5,7,9] left to merge. 
What I do is I take the next (up to) two numbers from each, and sort that. 
So the next few numbers in the imagined merge would be [5,6,7,8]. 
Now if I overall have an odd number of numbers, 
I could just take the first number, the 5. 
And if I overall have an even number of numbers (like if a had an additional 10), 
I take the mean of the first two numbers, (5+6)/2.0. For slightly simpler code, 
I unify the two cases: Instead of taking the 5, I compute (5+5)/2.0.

*edited Jan 6 by StefanPochmann
===============================================================================
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a, b = sorted((nums1, nums2), key=len) #根據序列的長度分配給 a,b
        m, n = len(a), len(b) # m < n 
        after = (m + n - 1) / 2 #中位數的位置 減1 是因為index的關係
        lo, hi = 0, m
        
        while lo < hi:
            i = (lo + hi) / 2
            if after-i-1 < 0 or a[i] >= b[after-i-1]:
                hi = i
            else:
                lo = i + 1
        i = lo
        
        nextfew = sorted(a[i:i+2] + b[after-i:after-i+2])
        return (nextfew[0] + nextfew[1 - (m+n)%2]) / 2.0
        
if __name__ == "__main__":
    s = Solution()
    n=[2,5,9]
    m=[1,2,3]
    print s.findMedianSortedArrays(n,m)        
        