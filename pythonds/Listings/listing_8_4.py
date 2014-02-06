def encrypt(m):
   s = 'abcdefghijklmnopqrstuvwxyz'
   n = ''
   for i in m:
       j = (s.find(i)+13)%26
       n = n + s[j]   
   return n   
