def __contains__(self,key):
    if self._get(key,self.root):
        return True
    else:
        return False

