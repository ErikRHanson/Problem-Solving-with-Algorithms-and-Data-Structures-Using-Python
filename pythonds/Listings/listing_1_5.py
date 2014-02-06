   def __add__(self,otherfraction):

        newnum = self.num*otherfraction.den + \
                    self.den*otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum,newden)
