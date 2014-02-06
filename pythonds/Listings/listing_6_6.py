    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:              t = BinaryTree(newNode)
            t.left = self.leftChild
            self.leftChild = t
