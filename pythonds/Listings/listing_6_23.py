class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0
    
   def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()
