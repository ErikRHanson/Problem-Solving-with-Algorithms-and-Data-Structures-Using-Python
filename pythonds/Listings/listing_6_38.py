def rotateLeft(self,rotRoot):
    newRoot = rotRoot.rightChild                      rotRoot.rightChild = newRoot.leftChild
    if newRoot.leftChild != None:
        newRoot.leftChild.parent = rotRoot
    newRoot.parent = rotRoot.parent
    if rotRoot.isRoot():
        self.root = newRoot
    else:
        if rotRoot.isLeftChild():                            rotRoot.parent.leftChild = newRoot
        else:
            rotRoot.parent.rightChild = newRoot     newRoot.leftChild = rotRoot
    rotRoot.parent = newRoot
    rotRoot.balanceFactor = rotRoot.balanceFactor + 1 \                                 - min(newRoot.balanceFactor, 0)
    newRoot.balanceFactor = newRoot.balanceFactor + 1 \
                          + max(rotRoot.balanceFactor, 0)  
