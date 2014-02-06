class UnaryGate(LogicGate):

    def __init__(self,n):
        super().__init__(n)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate "+ \
                           self.getLabel()+"-->"))
