def search(self,key):
    current = self.head
    found = False
    stop = False
    while not found and not stop:
        if current == None:
            stop = True
        else:
            if current.getNext() == None:
                current = current.getDown()
            else:
                if current.getNext().getKey() == key:
                    found = True
                else:
                    if key < current.getNext().getKey():
                        current = current.getDown()
                    else:
                        current = current.getNext()
    if found:
        return current.getNext().getData()
    else:
        return None
