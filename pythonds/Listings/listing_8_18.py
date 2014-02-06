        towerStack = Stack()
        current = self.head
        stop = False
        while not stop:
            if current == None:
                stop = True
            else:
                if current.getNext() == None:
                    towerStack.push(current)
                    current = current.getDown()
                else:
                    if current.getNext().getKey() > key:
                        towerStack.push(current)
                        current = current.getDown()
                    else:
                        current = current.getNext()

        lowestLevel = towerStack.pop()
        temp = DataNode(key,data)
        temp.setNext(lowestLevel.getNext())
        lowestLevel.setNext(temp)
        top = temp
