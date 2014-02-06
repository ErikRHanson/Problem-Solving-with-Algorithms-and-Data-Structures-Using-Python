def __getitem__(self,idx):
    if idx < self.lastIndex:
        return self.myArray[idx]
    else:
        raise LookupError('index out of bounds')

def __setitem__(self,idx,val):
    if idx < self.lastIndex:
        self.myArray[idx] = val
    else:
        raise LookupError('index out of bounds')
