import time
from random import randrange

myList1 = [4,5,2,1,6,7,8,9,]
myList2 = [0,1,2,3,4,5,6,7,8]

def findMin(alist):
    overallmin = alist[0]
    for i in alist:
        issmallest = True
        for j in alist:
            if i > j:
                issmallest = False
        if issmallest:
            overallmin = i
    return overallmin


def findMin2(alist):
    minsofar = alist[0]
    for i in alist:
        if i < minsofar:
            minsofar = i
    return minsofar


for listSize in range(1000,10001,1000):
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(findMin(alist))
    end = time.time()
    print("size: %d time: %f" % (listSize, end-start))

for listSize2 in range(1000,10001,1000):
    alist = [randrange(100000) for x in range(listSize2)]
    start = time.time()
    print(findMin2(alist))
    end = time.time()
    print("size: %d time: %f" % (listSize2, end-start))
