# -*- coding: utf-8 -*-
class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            #新多出一個newNode 舊左 -> 新左  newNode -> 新左
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            #新多出一個newNode 舊右 -> 新右  newNode -> 新右
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
    
    def preorder(self):
        print self.key,
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()
            
    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print self.key,
     
    def inorder(self):  
        if self.leftChild:
            self.leftChild.inorder()
        print self.key,   
        if self.rightChild:
            self.rightChild.inorder()
      
if __name__ == "__main__":
    r = BinaryTree('a')
    print"===check  root==="    
    print(r.getRootVal()),"\n"
    
    print"===check left substree==="    
    print(r.getLeftChild()),"\n"
   
    r.insertLeft('b')
    print"===check left substree===\n"
    print(r.getLeftChild()),"\n"
    print"===check the root of left substree==="
    print(r.getLeftChild().getRootVal()),"\n"
    
    r.insertRight('c')
    print"===check right substree===\n"
    print(r.getRightChild()),"\n"
    print"===check the root of right substree==="
    print(r.getRightChild().getRootVal()),"\n"
    
    r.getRightChild().setRootVal('hello')
    print"===check the root of right substree==="    
    print(r.getRightChild().getRootVal()),"\n"
     

