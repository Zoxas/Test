# -*- coding: utf-8 -*-
# a Stack in Python
"""
Stack() creates a new stack that is empty. It needs no parameters and returns an empty stack.

push(item) adds a new item to the top of the stack. It needs the item and returns nothing.

pop() removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.

peek() returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.

isEmpty() tests to see whether the stack is empty. It needs no parameters and returns a boolean value.

size() returns the number of items on the stack. It needs no parameters and returns an integer.
"""

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


if __name__ == "__main__":
    s = Stack()
    print s.isEmpty()
    print s.items
    
    s.push("Zoxas")
    print s.items
    
    s.push(5566)
    print s.items
    print "The last item is: ", s.peek()
    print "The stack size is: ", s.size()
    
    s.pop()
    print s.items

