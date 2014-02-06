def add(self,item):
    temp = Node(item)
    temp.setNext(self.head)
    self.head = temp
