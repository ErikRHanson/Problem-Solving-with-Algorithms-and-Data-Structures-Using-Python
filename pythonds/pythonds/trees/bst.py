#!/bin/env python3.1
# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005, 2010
# 

import unittest
class BinarySearchTree:
    '''
    Author:  Brad Miller
    Date:  1/15/2005
    Description:  Imlement a binary search tree with the following interface
                  functions:  
                  __contains__(y) <==> y in x
                  __getitem__(y) <==> x[y]
                  __init__()
                  __len__() <==> len(x)
                  __setitem__(k,v) <==> x[k] = v
                  clear()
                  get(k)
                  items() 
                  keys() 
                  values()
                  put(k,v)
                  in
                  del <==> 
    '''

    def __init__(self):
        self.root = None
        self.size = 0
    
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)
            
    def __setitem__(self,k,v):
        self.put(k,v)

    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
        
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)
            
        
    def __getitem__(self,key):
        res = self.get(key)
        if res:
            return res
        else:
            raise KeyError('Error, key not in tree')
            

    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False
        
    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()
    
    def delete(self,key):
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
        self.delete(key)
    
    def remove(self,currentNode):
        if currentNode.isLeaf(): #leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren(): #interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else: # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                       currentNode.leftChild.payload,
                                       currentNode.leftChild.leftChild,
                                       currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                       currentNode.rightChild.payload,
                                       currentNode.rightChild.leftChild,
                                       currentNode.rightChild.rightChild)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self,tree):
        if tree != None:
            self._inorder(tree.leftChild)
            print(tree.key)
            self._inorder(tree.rightChild)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, tree):
        if tree:
            self._postorder(tree.rightChild)
            self._postorder(tree.leftChild)
            print(tree.key)            

    def preorder(self):
        self._preorder(self,self.root)

    def _preorder(self,tree):
        if tree:
            print(tree.key)            
            self._preorder(tree.leftChild)
            self._preorder(tree.rightChild)

                
class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = 0
        
    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild
    
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild
    
    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
        
    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ


    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def __iter__(self):
        """The standard inorder traversal of a binary tree."""
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

            
class BinaryTreeTests(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()
        
    def testgetput(self):
        print('testgetput')
        self.bst.put(50,'a')
        self.bst.put(10,'b')
        self.bst.put(70,'c')
        self.bst.put(30,'d')
        self.bst.put(85,'d')
        self.bst.put(15,'e')
        self.bst.put(45,'f')
        print(self.bst.get(50))
        assert self.bst.get(50) == 'a'
        assert self.bst.get(45) == 'f'
        assert self.bst.get(85) == 'd'
        assert self.bst.get(10) == 'b'
        assert self.bst.root.key == 50
        assert self.bst.root.leftChild.key == 10
        assert self.bst.root.rightChild.key == 70
        
    def testputoper(self):
        print('testputoper')
        self.bst[25] = 'g'
        assert self.bst[25] == 'g'
        
    def testFindSucc(self):
        print('testing findSucc')
        x = BinarySearchTree()
        x.put(10,'a')
        x.put(15,'b')
        x.put(6,'c')
        x.put(2,'d')
        x.put(8,'e')
        x.put(9,'f')
        assert x.root.leftChild.leftChild.findSuccessor().key == 6
        assert x.root.leftChild.rightChild.findSuccessor().key == 9
        assert x.root.leftChild.rightChild.rightChild.findSuccessor().key == 10
        
    def testSize(self):
        print('testing testSize')
        self.bst.put(50,'a')
        self.bst.put(10,'b')
        self.bst.put(70,'c')
        self.bst.put(30,'d')
        self.bst.put(85,'d')
        self.bst.put(15,'e')
        self.bst.put(45,'f')
        assert self.bst.length() == 7
        
    def testDelete(self):
        print('testing delete')
        self.bst.put(50,'a')
        self.bst.put(10,'b')
        self.bst.put(70,'c')
        self.bst.put(30,'d')
        self.bst.put(85,'d')
        self.bst.put(15,'e')
        self.bst.put(45,'f')
        self.bst.put(5,'g')
        print('initial inorder')
        self.bst.inorder()
        assert (10 in self.bst) == True        
        self.bst.delete_key(10)
        print('delete 10 inorder')
        self.bst.inorder()        
        assert (10 in self.bst) == False
        assert self.bst.root.leftChild.key == 15
        assert self.bst.root.leftChild.parent == self.bst.root
        assert self.bst.root.leftChild.rightChild.parent == self.bst.root.leftChild
        assert self.bst.get(30) == 'd'
        self.bst.delete_key(15)
        print('delete 15 inorder')
        self.bst.inorder()
        assert self.bst.root.leftChild.key == 30
        assert self.bst.root.leftChild.rightChild.key == 45
        assert self.bst.root.leftChild.rightChild.parent == self.bst.root.leftChild
        self.bst.delete_key(70)
        print('delete 70 inorder')        
        self.bst.inorder()        
        assert (85 in self.bst) == True
        assert self.bst.get(30) == 'd'
        print('root key = ', self.bst.root.key)
        print('left = ',self.bst.root.leftChild.key)
        print('left left = ',self.bst.root.leftChild.leftChild.key)
        print('left right = ',self.bst.root.leftChild.rightChild.key)        
        print('right = ',self.bst.root.rightChild.key)
        self.bst.delete_key(50)
        assert self.bst.root.key == 85
        assert self.bst.root.leftChild.key == 30
        assert self.bst.root.rightChild == None
        assert self.bst.root.leftChild.leftChild.key == 5
        assert self.bst.root.leftChild.rightChild.key == 45
        assert self.bst.root.leftChild.leftChild.parent == self.bst.root.leftChild
        assert self.bst.root.leftChild.rightChild.parent == self.bst.root.leftChild
        print('new root key = ', self.bst.root.key)
        self.bst.inorder()
        self.bst.delete_key(45)
        assert self.bst.root.leftChild.key == 30
        self.bst.delete_key(85)
        assert self.bst.root.key == 30
        print('xxxx ',self.bst.root.leftChild.parent.key, self.bst.root.key)
        assert self.bst.root.leftChild.parent == self.bst.root
        self.bst.delete_key(30)
        assert self.bst.root.key == 5
        self.bst.inorder()
        print("final root = " + str(self.bst.root.key))
        assert self.bst.root.key == 5
        self.bst.delete_key(5)
        assert self.bst.root == None

    def testDel2(self):
        self.bst.put(21,'a')
        self.bst.put(10,'b')
        self.bst.put(24,'c')
        self.bst.put(11,'d')
        self.bst.put(22,'d')
        self.bst.delete_key(10)
        assert self.bst.root.leftChild.key == 11
        assert self.bst.root.leftChild.parent == self.bst.root
        assert self.bst.root.rightChild.key == 24
        self.bst.delete_key(24)
        assert self.bst.root.rightChild.key == 22
        assert self.bst.root.rightChild.parent == self.bst.root
        self.bst.delete_key(22)
        self.bst.delete_key(21)
        print("del2 root = ",self.bst.root.key)
        assert self.bst.root.key == 11
        assert self.bst.root.leftChild == None
        assert self.bst.root.rightChild == None        

    def testLarge(self):
        import random
        print('testing a large random tree')
        i = 0
        randList = []
        while i < 10000:
            nrand = random.randrange(1,10000000)
            if nrand not in randList:
                randList.append(nrand)
                i += 1
        print(randList)
        for n in randList:
            self.bst.put(n,n)
        sortList = randList[:]
        sortList.sort()
        random.shuffle(randList)
        for n in randList:
            minNode = self.bst.root.findMin()
            if minNode:
                assert minNode.key == sortList[0]
            rootPos = sortList.index(self.bst.root.key)
            succ = self.bst.root.findSuccessor()
            if succ:
                assert succ.key == sortList[rootPos+1]
            else:
                assert self.bst.root.rightChild == None
            self.bst.delete_key(n)
            sortList.remove(n)
            
        assert self.bst.root == None

    def testIter(self):
        import random
        i = 0
        randList = []
        while i < 100:
            nrand = random.randrange(1,10000)
            if nrand not in randList:
                randList.append(nrand)
                i += 1
        for n in randList:
            self.bst.put(n,n)
        sortList = randList[:]
        sortList.sort()

        i = 0
        for j in self.bst:
            assert j == sortList[i]
            i += 1
# the following exercises all of the branches in deleting a node with one child
    def testCase1(self):
        self.bst.put(10,10)
        self.bst.put(7,7)
        self.bst.put(5,5)
        self.bst.put(1,1)
        self.bst.put(6,6)
        self.bst.delete_key(7)
        assert self.bst.root.leftChild.key == 5
        assert self.bst.root == self.bst.root.leftChild.parent
        assert self.bst.root.leftChild.leftChild.key == 1
        assert self.bst.root.leftChild.rightChild.key == 6

    def testCase2(self):
        self.bst = BinarySearchTree()
        self.bst.put(10,10)
        self.bst.put(15,15)
        self.bst.put(12,12)
        self.bst.put(11,11)
        self.bst.put(13,13)
        self.bst.delete_key(15)
        assert self.bst.root.rightChild.key == 12
        assert self.bst.root.rightChild.parent == self.bst.root
        assert self.bst.root.rightChild.leftChild.key == 11
        assert self.bst.root.rightChild.rightChild.key == 13

    def testCase3(self):
        self.bst = BinarySearchTree()
        self.bst.put(10,10)
        self.bst.put(6,6)
        self.bst.put(8,8)
        self.bst.put(7,7)
        self.bst.put(9,9)
        self.bst.delete_key(6)
        assert self.bst.root.leftChild.key == 8
        assert self.bst.root.leftChild.parent == self.bst.root
        assert self.bst.root.leftChild.leftChild.key == 7
        assert self.bst.root.leftChild.rightChild.key == 9

    def testCase4(self):
        self.bst = BinarySearchTree()
        self.bst.put(10,10)
        self.bst.put(15,15)
        self.bst.put(20,20)
        self.bst.put(17,17)
        self.bst.put(22,22)
        self.bst.delete_key(15)
        assert self.bst.root.rightChild.key == 20
        assert self.bst.root.rightChild.parent == self.bst.root
        assert self.bst.root.rightChild.rightChild.key == 22
        assert self.bst.root.rightChild.leftChild.key == 17

    def testCase5(self):
        self.bst.put(10,10)
        self.bst.put(20,20)
        self.bst.put(17,17)
        self.bst.put(22,22)
        self.bst.delete_key(10)
        assert self.bst.root.key == 20
        assert self.bst.root.leftChild.parent == self.bst.root
        assert self.bst.root.rightChild.parent == self.bst.root
        assert self.bst.root.leftChild.key == 17
        assert self.bst.root.rightChild.key == 22

    def testCase6(self):
        self.bst.put(10,10)
        self.bst.put(5,5)
        self.bst.put(1,1)
        self.bst.put(7,7)
        self.bst.delete_key(10)
        assert self.bst.root.key == 5
        assert self.bst.root.leftChild.parent == self.bst.root
        assert self.bst.root.rightChild.parent == self.bst.root
        assert self.bst.root.leftChild.key == 1
        assert self.bst.root.rightChild.key == 7

    def testBadDelete(self):
        self.bst.put(10,10)
        with self.assertRaises(KeyError):
            self.bst.delete_key(5)
        self.bst.delete_key(10)
        with self.assertRaises(KeyError):
             self.bst.delete_key(5)

if __name__ == '__main__':
    import platform
    print(platform.python_version())
    unittest.main()

### Local Variables:
### End:
