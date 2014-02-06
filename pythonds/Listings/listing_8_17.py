def insert(self,key,data):
    if self.head == None:
        self.head = HeaderNode()
        temp = DataNode(key,data)
        self.head.setNext(temp)
        top = temp
        while flip() == 1:
            newhead = HeaderNode()
            temp = DataNode(key,data)
            temp.setDown(top)
            newhead.setNext(temp)
            newhead.setDown(self.head)
            self.head = newhead
            top = temp
    else:
