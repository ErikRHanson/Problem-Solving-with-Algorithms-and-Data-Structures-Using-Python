'''
	This is an example of a binary tree data structure created with 
	python lists as the underlying data structure.

'''

def BinaryTree(r):
	return [r, [], []]

def insertLeft(root,newBranch):
	t = root.pop(1)
	if len(t) > 1:
		root.insert(1,[newBranch,t,[]])
	else:
		root.insert(1,[newBranch, [], []])
	return root

def insertRight(root,newBranch):
	t = root.pop(2)
	if len(t) > 1:
		root.insert(2,[newBranch,[],t])
	else:
		root.insert(2,[newBranch,[],[]])
	return root

def getRootVal(root):
	return root[0]

def setRootVal(root,newVal):
	root[0] = newVal

def getLeftChild(root):
	return root[1]

def getRightChild(root):
	return root[2]


r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
l = getLeftChild(r)
print(l)

setRootVal(l,9)
print(r)
insertLeft(l,11)
print(r)
print(getRightChild(getRightChild(r)))


b = BinaryTree('a')
# Build up the left side of this tree
insertLeft(b,'b')
insertRight(getLeftChild(b),'d')

# Build up the right side of this tree
insertRight(b,'c')
insertLeft(getRightChild(b),'e')
insertRight(getRightChild(b),'f')

print(b)
