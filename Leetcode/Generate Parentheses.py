# -*- coding: utf-8 -*-
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"


"""

class Solution:
     # @param an integer 
    # @return a list of string 
    # @draw a decision tree when n == 2, and you can understand it! 
    def helpler(self, l, r, item, res):
        if r < l:
            print item,l,r,"return"
            return 
        if l == 0 and r == 0:
            res.append(item)
            print item,l,r,"append"
        if l > 0:
            print item,l,r,"L call"
            self.helpler(l - 1, r, item + '(' , res)
        if r > 0:
            print item,l,r,"R call"
            self.helpler(l, r - 1, item + ')' , res)

    def generateParenthesis(self, n):
        if n == 0:
             return []
        res = []
        self.helpler(n, n, '' , res)
        return res

if __name__ == "__main__":
    s = Solution()
    print s.generateParenthesis(2)

"""
            2,2
            / \
        1,2   2,1
        / \    (return)
    0,2    1,1
    /      / \
0,1      0,1  1,0
 |        |   (retiurn)
0,0      0,0
(add)    (add)


"""