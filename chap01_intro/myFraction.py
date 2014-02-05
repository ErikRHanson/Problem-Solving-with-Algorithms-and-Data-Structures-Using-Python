
class Fraction:
    def __init__(self,top,bottom):
        
        self.num= top
        self.den = bottom
        
    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def __add__(self,otherfraction):

        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common, newden//common)

    def __sub__(self,otherfraction):
        
        newnum = self.num*otherfraction.den - self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common, newden//common)
    
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __mul__(self,other):
        newnum = self.num * other.num
        newden = self.den* other.den
        common = gcd(newnum,newden)
        return Fraction(newnum // common, newden//common)

    def __trudiv__(self,other):
        newnum = self.num * other.den
        newden = self.den * other.num

        common = gcd(newnum, newnen)
        return Fraction(newnum//common,newden//comon)

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum < secondnum

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den
    
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n


def main():    
    f = Fraction(1,3)
    g = Fraction(1,5)
    h = f+g
    print(f.getNum())
    print(g.getDen())
    j = Fraction(2,6)
    
    print(h)
    
    print(f<g)
    print(g<f)
    print(g==f)
    print(f==j)
    print(f!=j)
    print(f*j)
    
    print(f)
    
    print("I ate", f, "of the pizza")
    
    print(f.__str__())
    
    print(str(f))
    
    f1=Fraction(1,4)
    f2=Fraction(1,2)
    f3=f1+f2
    print(f3)

main()
