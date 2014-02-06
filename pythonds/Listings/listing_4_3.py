
def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:              return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]   