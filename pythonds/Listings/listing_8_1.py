class ArrayList:
    
    def __init__(self, ):
        self.sizeExponent = 0
        self.maxSize = 0
        self.lastIndex = 0
        self.myArray = []

    def append(self,val):
        if self.lastIndex > self.maxSize-1:              self.__resize()
        self.myArray[self.lastIndex] = val
        self.lastIndex += 1


    def __resize(self):
        newsize = 2 ** self.sizeExponent
        print("newsize = ", newsize)
        newarray = [0]*newsize
        for i in range(self.maxSize):               newarray[i] = self.myArray[i]

        self.maxSize = newsize
        self.myArray = newarray
        self.sizeExponent += 1

