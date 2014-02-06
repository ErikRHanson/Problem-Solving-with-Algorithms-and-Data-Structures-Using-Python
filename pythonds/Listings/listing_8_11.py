def toChunks(m,chunkSize):
   byteMess = bytes(m,'utf-8')
   hexString = ''
   for b in byteMess:
      hexString = hexString + ("%02x" % b)

   numChunks = len(hexString) // chunkSize
   chunkList = []
   for i in range(0,numChunks*chunkSize+1,chunkSize):
      chunkList.append(hexString[i:i+chunkSize])
   chunkList = [eval('0x'+x) for x in chunkList if x]
   return chunkList

   
def chunksToPlain(clist,chunkSize):
   hexList = []
   for c in clist:
      hexString = hex(c)[2:]
      clen = len(hexString)
      hexList.append('0' * ((chunkSize - clen) % 2)
                      + hexString)
   
   hstring = "".join(hexList)
   messArray = bytearray.fromhex(hstring)
   return messArray.decode('utf-8')   

