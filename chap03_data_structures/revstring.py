
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def revstring(mystr):
    s = Stack()
    rev = []
    for c in mystr:
        s.push(c)

    while not s.isEmpty():
        rev.append(s.pop())
    return "".join(rev)

testString = "This is the test string. It is pretty good"

print (revstring(testString))
        
