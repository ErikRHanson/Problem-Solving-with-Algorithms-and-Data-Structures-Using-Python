

def qnth(sample, n):
	pivot = sample[0]
	below = [s for s in sample if s < pivot]
	above = [s for s in sample if s > pivot]
	i, j = len(below), len(sample)-len(above)

	if n < i: 
		return qnth(below, n)
	elif n >= j: 
		return qnth(above, n-j)
	else:
		return pivot


if __name__ == "__main__":
	import random
	n, mid = 2048, 7
	sample = [random.random() for _ in range(n)]
	partial = qnth(sample,mid)
	# sample.sort(); sorted = sample[mid]
	# print(partial, sorted, partial == sorted)
	print(partial)

