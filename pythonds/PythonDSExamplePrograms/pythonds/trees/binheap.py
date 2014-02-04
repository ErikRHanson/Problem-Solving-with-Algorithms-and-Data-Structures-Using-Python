# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
# 
import unittest

# this heap takes key value pairs, we will assume that the keys are integers
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        print(len(self.heapList), i)
        while (i > 0):
            print(self.heapList, i)
            self.percDown(i)
            i = i - 1
        print(self.heapList,i)
                        
    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
                
    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
               tmp = self.heapList[i // 2]
               self.heapList[i // 2] = self.heapList[i]
               self.heapList[i] = tmp
            i = i // 2
 
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
        
    def isEmpty(self):
        if currentSize == 0:
            return True
        else:
            return False

class FooThing:
    def __init__(self,x,y):
        self.key = x
        self.val = y
        

    def __lt__(self,other):
        if self.key < other.key:
            return True
        else:
            return False

    def __gt__(self,other):
        if self.key > other.key:
            return True
        else:
            return False
        
    def __hash__(self):
        return self.key

class TestBinHeap(unittest.TestCase):
    def setUp(self):
        self.theHeap = BinHeap()
        self.theHeap.insert(FooThing(5,'a'))                               
        self.theHeap.insert(FooThing(9,'d'))                  
        self.theHeap.insert(FooThing(1,'x'))
        self.theHeap.insert(FooThing(2,'y'))
        self.theHeap.insert(FooThing(3,'z'))

    def testInsert(self):
        assert self.theHeap.currentSize == 5

    def testDelmin(self):
        assert self.theHeap.delMin().val == 'x'
        assert self.theHeap.delMin().val  == 'y'
        assert self.theHeap.delMin().val  == 'z'
        assert self.theHeap.delMin().val  == 'a'

    def testMixed(self):
        myHeap = BinHeap()
        myHeap.insert(9)
        myHeap.insert(1)
        myHeap.insert(5)
        assert myHeap.delMin() == 1
        myHeap.insert(2)
        myHeap.insert(7)
        assert myHeap.delMin() == 2
        assert myHeap.delMin() == 5

    def testDupes(self):
        myHeap = BinHeap()
        myHeap.insert(9)
        myHeap.insert(1)
        myHeap.insert(8)
        myHeap.insert(1)
        assert myHeap.currentSize == 4
        assert myHeap.delMin() == 1
        assert myHeap.delMin() == 1
        assert myHeap.delMin() == 8

    def testBuildHeap(self):
        myHeap = BinHeap()
        myHeap.buildHeap([9,5,6,2,3])
        f = myHeap.delMin()
        print("f = ", f)
        assert f == 2
        assert myHeap.delMin() == 3
        assert myHeap.delMin() == 5
        assert myHeap.delMin() == 6
        assert myHeap.delMin() == 9                        
        
if __name__ == '__main__':
    d = {}
    d[FooThing(1,'z')] = 10
    unittest.main()
