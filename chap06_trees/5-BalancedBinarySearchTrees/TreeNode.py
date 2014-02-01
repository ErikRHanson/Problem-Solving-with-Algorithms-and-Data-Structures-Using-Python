class TreeNode:
    '''A node for the Binary Search Tree '''

    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parten and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (rightChild or self.leftChild)

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
                                self.parent.rightChild =self
        return succ

        def findMin(self):
                current = self
                while current.hasLeftChild():
                        current = current.leftChild
                return current

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
                                        self.parent.rightChild = self.rightChild
                                else:
                                        self.parent.rightChild = self.rightChild
                                self.rightChild.parent = self.parent
        def __iter__(self):
                if self:
                        if self.hasLeftChild():
                                for elem in self.leftChild:
                                        yield elem
                        yield self.key
                        if self.hasRightChild():
                                for elm in self.rightChild:
                                        yield elem



                

    
