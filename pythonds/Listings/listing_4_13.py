    def isExit(self,row,col):
        return (row == 0 or
                row == self.rowsInMaze-1 or
                col == 0 or
                col == self.columnsInMaze-1 )

   def __getitem__(self,idx):
        return self.mazelist[idx]
