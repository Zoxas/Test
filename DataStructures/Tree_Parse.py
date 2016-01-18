# -*- coding: utf-8 -*-
import sys
from Stack import *
from BinaryTree import *
sys.path.append('D:\Git\test\DataStructures')

def buildParseTree(fpexp):
    fplist = fpexp.split()#將str以sep分割成子字串，回傳儲存子字串的串列
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent

        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()

        else:
            raise ValueError
    return eTree

if __name__ == "__main__":
    pt = buildParseTree("( ( 10 + 5 ) * 3 )")
    print pt
    print"""
    Tree:
              *    

           +     3

        10   5  
    
    """
    print"\n==========inorder============="    
    pt.inorder()
    print"\n==========preorder============="
    pt.preorder()
    print"\n==========postorder============="
    pt.postorder()
