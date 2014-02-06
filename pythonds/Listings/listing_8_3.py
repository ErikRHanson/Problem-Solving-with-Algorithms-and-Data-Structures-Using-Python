    def insert(self,idx,val):
        if self.lastIndex > self.maxSize - 1:
            self.__resize()
        for i in range(self.lastIndex,idx-1,-1):              self.myArray[i+1] = self.myArray[i]
        self.lastIndex += 1
        self.myArray[idx] = val
