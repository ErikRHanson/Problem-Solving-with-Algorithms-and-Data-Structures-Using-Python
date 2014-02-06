    def getPinA(self):
        if self.pinA == None:
            return input("Enter Pin A input for gate "+ \
                               self.getName()+"-->")
        else:
            return self.pinA.getFrom().getOutput()
