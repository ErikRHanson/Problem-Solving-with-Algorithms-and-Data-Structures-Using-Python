     class otNode:
     def __init__(self,parent=None,level=0,outer=None):
         self.red = 0
         self.green = 0
         self.blue = 0
         self.count = 0
         self.parent = parent
         self.level = level
         self.oTree = outer
         self.children = [None]*8
