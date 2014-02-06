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
