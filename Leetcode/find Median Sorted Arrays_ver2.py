# -*- coding: utf-8 -*-
"""
題意：There are two sorted arrays A and B of size m and n respectively. 
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

解題思路：這道題要求兩個已經排好序的數列的中位數。
中位數的定義：如果數列有偶數個數，那麼中位數為中間兩個數的平均值；如果數列有奇數個數，那麼中位數為中間的那個數。
比如{1，2，3，4，5}的中位數為3。{1，2，3，4，5，6}的中位數為（3+4）/ 2 = 3.5。
那麼這題最直接的思路就是將兩個數列合併在一起，然後排序，然後找到中位數就行了。
可是這樣最快也要O((m+n)log(m+n))的時間複雜度，而題目要求O(log(m+n))的時間複雜度。
這道題其實考察的是二分查找，是《算法導論》的一道課後習題，難度還是比較大的。
　　　　   
首先我們來看如何找到兩個數列的第k小個數，即程序中getKth(A, B , k)函數的實現。
用一個例子來說明這個問題：A = {1，3，5，7}；B = {2，4，6，8，9，10}；
如果要求第7個小的數，A數列的元素個數為4，B數列的元素個數為6；
k/2 = 7/2 = 3，而A中的第3個數A[2]=5；B中的第3個數B[2]= 6； ---> 應該為第4個數 k-3 = 4 所以下面敘述有些也有誤,以程式碼為主
而A[2]<B[2]；則A[0]，A[1]，A[2]中必然不可能有第7個小的數。
因為A[2]<B[2]，所以比A[2]小的數最多可能為A[0], A[1], B[0], B[1]這四個數，
也就是說A[2]最多可能是第5個大的數，由於我們要求的是getKth(A, B, 7)；現在就變成了求getKth(A', B, 4)；即A' = {7 }；B不變，
求這兩個數列的第4個小的數，因為A[0]，A[1]，A[2]中沒有解，所以我們直接刪掉它們就可以了。這個可以使用遞歸來實現
"""
class Solution:
     # @return a float 
    # @line20 must multiply 0.5 for return a float else it will return an int 
    def getKth(self, A, B, k):

        lenA = len(A); lenB = len(B)
        if lenA > lenB: return self.getKth(B, A, k)
        if lenA == 0: return B[k - 1]        
        if k == 1: return min (A[0], B[0])

        pa = min(k/2, lenA)
        pb = k - pa
        
        if A[pa - 1] <= B[pb - 1 ]:
            return self.getKth(A[pa:], B, pb)
        else :
            return self.getKth(A, B[pb:], pa)
    
    def findMedianSortedArrays(self, A, B):
        lenA = len(A); lenB = len(B)
        
        if (lenA + lenB) % 2 == 1 : 
            return self.getKth(A, B, (lenA + lenB)/2 + 1 )
        else :
            return (self. getKth(A, B, (lenA + lenB)/2) + self.getKth(A, B, (lenA + lenB)/2 + 1)) * 0.5

if __name__ == "__main__":
    s = Solution()
    n=[2,5,9]
    m=[1,2,3]
    print s.findMedianSortedArrays(n,m)   
