class BinaryGate(LogicGate):

    def __init__(self,n):
        super().__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input("Enter Pin A input for gate "+ \
                           self.getLabel()+"-->"))

    def getPinB(self):
        return int(input("Enter Pin B input for gate "+ \
                           self.getLabel()+"-->"))
