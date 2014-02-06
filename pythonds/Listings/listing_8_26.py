def find(self,r,g,b,level):
   if level < self.oTree.maxLevel:
       idx = self.computeIndex(r,g,b,level)
       if self.children[idx]:
           return self.children[idx].find(r,g,b,level+1)
       elif self.count > 0:
           return ((self.red//self.count, 
                    self.green//self.count, 
                    self.blue//self.count))         else:
           print("error: No leaf node for this color")
   else:
       return ((self.red//self.count,
                self.green//self.count,
                self.blue//self.count))    