class HeaderNode:
    def __init__(self):
        self.next = None
        self.down = None

    def getNext(self):
        return self.next

    def getDown(self):
        return self.down

    def setNext(self,newnext):
        self.next = newnext

    def setDown(self,newdown):
        self.down = newdown
