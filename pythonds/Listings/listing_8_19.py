        while flip() == 1:
            if towerStack.isEmpty():
                newhead = HeaderNode()
                temp = DataNode(key,data)
                temp.setDown(top)
                newhead.setNext(temp)
                newhead.setDown(self.head)
                self.head = newhead
                top = temp
            else:
                nextLevel = towerStack.pop()
                temp = DataNode(key,data)
                temp.setDown(top)
                temp.setNext(nextLevel.getNext())
                nextLevel.setNext(temp)
                top = temp
