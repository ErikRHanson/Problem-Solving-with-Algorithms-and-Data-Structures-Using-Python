def gcd(a,b):
   if b == 0:
      return a
   elif a < b:
      return gcd(b,a)
   else:
      return gcd(a-b,b)
