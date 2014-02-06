def rebalance(self,node):
  if node.balanceFactor < 0:         if node.rightChild.balanceFactor > 0:
         self.rotateRight(node.rightChild)
          self.rotateLeft(node)
      else:
         self.rotateLeft(node)
  elif node.balanceFactor > 0:        if node.leftChild.balanceFactor < 0:
         self.rotateLeft(node.leftChild)
          self.rotateRight(node)
      else:
         self.rotateRight(node)
