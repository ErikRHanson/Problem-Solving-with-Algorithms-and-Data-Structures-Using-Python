    class OctTree:
    def __init__(self):
        self.root = None
        self.maxLevel = 5
        self.numLeaves = 0
        self.leafList = []
    
    def insert(self,r,g,b):
        if not self.root:
            self.root = self.otNode(outer=self)
        self.root.insert(r,g,b,0,self)

    def find(self,r,g,b):
        if self.root:
            return self.root.find(r,g,b,0)
    
    def reduce(self,maxCubes):            while len(self.leafList) > maxCubes:
            smallest = self.findMinCube()
            smallest.parent.merge()              self.leafList.append(smallest.parent)
            self.numLeaves = self.numLeaves + 1

    def findMinCube(self):
        minCount = sys.maxint
        maxLev = 0
        minCube = None
        for i in self.leafList:
            if i.count <= minCount and i.level >= maxLev:
                minCube = i
                minCount = i.count
                maxLev = i.level
        return minCube        
