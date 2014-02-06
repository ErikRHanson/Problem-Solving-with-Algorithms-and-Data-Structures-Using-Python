def insert(self,r,g,b,level,outer):
   if level < self.oTree.maxLevel:
      idx = self.computeIndex(r,g,b,level)
      if self.children[idx] == None:
        self.children[idx] = outer.otNode(parent=self,
                                         level=level+1,
                                         outer=outer)
      self.children[idx].insert(r,g,b,level+1,outer)
   else:
      if self.count == 0:
         self.oTree.numLeaves = self.oTree.numLeaves + 1
         self.oTree.leafList.append(self)
      self.red += r
      self.green += g
      self.blue += b
      self.count = self.count + 1

def computeIndex(self,r,g,b,level):      shift = 8 - level
   rc = r >> shift-2 & 0x4
   gc = g >> shift-1 & 0x2
   bc = b >> shift & 0x1
   return(rc | gc | bc)
