
def qsort1(list):
	"""Quicksort using list comprehensions"""
	if list == []:
		return []
	else:
		pivot = list[0]
		lesser = qsort1([x for x in list[1:] if x < pivot])
		greater = qsort1([x for x in list[1:] if x >= pivot])
		return lesser + [pivot] + greater

def qsort2(list):
	"""Quicksort using a partitoning function"""
	if list == []:
		return []
	else:
		pivot = list[0]
		lesser, equal, greater = partition(list[1:], [], [pivot], [])
		return qsort2(lesser) + equal + qsort2(greater)

# def partition(list, l, e, g):
# 	"""Recursive Partition"""
# 	if list == []:
# 		return (l, e, g)
# 	else:
# 		head = list[0]
# 		if head < e[0]:
# 			return partition(list[1:], l + [head], e, g)
# 		elif head > e[0]:
# 			return partition(list[1:], l, e, g + [head])
# 		else:
# 			return partition(list[1:], l, e + [head], g)

def partition(list, l, e, g):
	while list != []:
		head = list.pop(0)
		if head < e[0]:
			l = [head] + l
		elif head > e[0]:
			g = [head] + g
		else:
			e = [head] + g
	return (l, e, g)



numbers = [5,33,6,2,4,7,8,9,12,41,25,64,57,86,79,1]


print(numbers)
print(qsort1(numbers))


