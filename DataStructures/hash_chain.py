# -*- coding: utf-8 -*-
class ChainHashTable:

    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = [ ]
        for i in range(self.capacity):
            self.slots.append([])

    def __str__(self):
        info = ""
        for items in self.slots:
            info += str(items)
        return info

    def __len__(self):
        count = 0
        for i in self.slots:
            count += len(i)
        return count

    def hash_function(self, key):
        i = key % self.capacity
        return i
    
    def insert(self, key):
        slot = self.hash_function(key)
        if key in self.slots[slot]:
            return False
        else:
            self.slots[slot].append(key)
            message =  "insert to slot %d"%(slot+1)
            return message
    
    def search(self,key):
        slot = self.hash_function(key)
        if key in self.slots[slot]:
            message =  "%d It's in the slot %d"%(key,(slot+1))
            return message
        else:
            return False
    def rm(self,key):
        slot = self.hash_function(key)
        if key in self.slots[slot]:
            self.slots[slot].remove(key)
        else:
            return False
        
        

        
if __name__ == "__main__":
    x = ChainHashTable(2)
    print "Add 3 -->", x.insert(3)
    print "Add 3, -->:", x.insert(3)
    print "Add 1, -->:", x.insert(1)
    print "Add 2, -->:", x.insert(2)
    print "Hashtable:", x.__str__()
    print x.search(1)
    print x.search(4)
    print x.rm(1)
    print "Hashtable:", x.__str__()