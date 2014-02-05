
class UnaryGate(LogicGate):
    
    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate " + self.getLabel()+"-->"))

