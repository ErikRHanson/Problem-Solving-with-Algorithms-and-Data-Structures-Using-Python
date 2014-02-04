#!/bin/env python3.1
# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005, 2010
# 

import unittest
from .bst import BinarySearchTree, TreeNode

class AVLTree(BinarySearchTree):
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
                  has_key(k)
                  items() 
                  keys() 
                  values()
                  put(k,v)
    '''


    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.rightChild)                

    def updateBalance(self,node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1

            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rebalance(self,node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                # Do an LR Rotation
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                # single left
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                # Do an RL Rotation
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                # single right
                self.rotateRight(node)

    def rotateLeft(self,rotRoot):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)


    def rotateRight(self,rotRoot):
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isRightChild():
                rotRoot.parent.rightChild = newRoot
            else:
                rotRoot.parent.leftChild = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 - max(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + min(rotRoot.balanceFactor, 0)
        

class BinaryTreeTests(unittest.TestCase):
    def setUp(self):
        self.bst = AVLTree()

    def testAuto1(self):
        self.bst.put(30,'a')
        self.bst.put(50,'b')
        self.bst.put(40,'c')
        assert self.bst.root.key == 40

    def testAuto2(self):
        self.bst.put(50,'a')
        self.bst.put(30,'b')
        self.bst.put(40,'c')
        assert self.bst.root.key == 40

    def testAuto3(self):
        self.bst.put(50,'a')
        self.bst.put(30,'b')
        self.bst.put(70,'c')
        self.bst.put(80,'c')
        self.bst.put(60,'d')
        self.bst.put(90,'e')
        assert self.bst.root.key == 70

    def testAuto3(self):
        self.bst.put(40,'a')
        self.bst.put(30,'b')
        self.bst.put(50,'c')
        self.bst.put(45,'d')
        self.bst.put(60,'e')
        self.bst.put(43,'f')
        assert self.bst.root.key == 45
        assert self.bst.root.leftChild.key == 40
        assert self.bst.root.rightChild.key == 50
        assert self.bst.root.balanceFactor == 0
        assert self.bst.root.leftChild.balanceFactor == 0
        assert self.bst.root.rightChild.balanceFactor == -1

    def testAuto4(self):
        self.bst.put(40,'a')
        self.bst.put(30,'b')
        self.bst.put(50,'c')
        self.bst.put(10,'d')
        self.bst.put(35,'e')
        self.bst.put(37,'f')
        assert self.bst.root.key == 35
        assert self.bst.root.leftChild.key == 30
        assert self.bst.root.rightChild.key == 40
        assert self.bst.root.balanceFactor == 0
        assert self.bst.root.leftChild.balanceFactor == 1
        assert self.bst.root.rightChild.balanceFactor == 0


if __name__ == '__main__':
    import platform
    print(platform.python_version())
    unittest.main()

# Local Variables:
# py-which-shell: "python3"
# End:
