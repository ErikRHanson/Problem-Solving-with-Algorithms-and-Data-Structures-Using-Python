class Map:
    def __init__(self):
        self.collection=SkipList()

    def put(self,key,value):
        self.collection.insert(key,value)

    def get(self,key):
        return self.collection.search(key)
