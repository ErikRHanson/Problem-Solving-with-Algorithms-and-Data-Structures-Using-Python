def RSAgenKeys(p,q):   
   n = p * q
   pqminus = (p-1) * (q-1)
   e = int(random.random() * n)
   while gcd(pqminus,e) != 1:
      e = int(random.random() * n)
   d,a,b = ext_gcd(pqminus,e)
   if b < 0:
      d = pqminus+b
   else:
      d = b
   return ((e,d,n))

def RSAencrypt(m,e,n):
   ndigits = len(str(n))
   chunkSize = ndigits - 1
   chunks = toChunks(m,chunkSize)
   encList = []
   for messChunk in chunks:
      print messChunk
      c = modexp(messChunk,e,n)
      encList.append(c)
   return encList
   
def RSAdecrypt(clist,d,n):
   rList = []
   for c in clist:
      m = modexp(c,d,n)
      rList.append(m)
   return rList
