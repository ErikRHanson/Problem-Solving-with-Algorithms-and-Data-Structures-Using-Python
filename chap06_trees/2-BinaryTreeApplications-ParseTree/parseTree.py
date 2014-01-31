from BinaryTree import BinaryTree
from Stack import Stack

def buildParseTree(fpexp):
	fplist = fpexp.split()
	pStack = Stack()
	eTree = BinaryTree('')
	pStack.push(eTree)
	currentTree = eTree
	for i in fplist:
		if i == '(':
			currentTree.insertLeft('')
			pStack.push(currentTree)
			currentTree = currentTree.getLeftChild()
		elif i not in ['+', '-', '*', '/', ')']:
			currentTree.setRootVal(int(i))
			parent = pStack.pop()
			currentTree = parent
		elif i in ['+', '-', '*', '/']:
			currentTree.setRootVal(i)
			currentTree.insertRight('')
			pStack.push(currentTree)
			currentTree = currentTree.getRightChild()
		elif i == ')':
			currentTree = pStack.pop()
		else:
			raise ValueError
	return eTree

def evaluate(parseTree):
	opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

	leftC = parseTree.getLeftChild()
	rightC = parseTree.getRightChild()

	if leftC and rightC:
		fn = opers[parseTree.getRootVal()]
		return fn(evaluate(leftC),evaluate(rightC))
	else:
		return parseTree.getRootVal()

def postordereval(tree):
	opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
	res1 = None
	res2 = None
	if tree:
		res1 = postordereval(tree.getLeftChild())
		res2 = postordereval(tree.getRightChild())
		if res1 and res2:
			return opers[tree.getRootVal()](res1,res2)
		else:
			return tree.getRootVal()

def preorder(tree):
	if tree:
		print(tree.getRootVal())
		preorder(tree.getLeftChild())
		preorder(tree.getRightChild())

def postorder(tree):
	if tree != None:
		postorder(tree.getLeftChild())
		postorder(tree.getRightChild())
		print(tree.getRootVal())

def inorder(tree):
	if tree != None:
		inorder(tree.getLeftChild())
		print(tree.getRootVal())
		inorder(tree.getRightChild())

def printexp(tree):
	sVal = ""
	if tree:
		sVal = '(' + printexp(tree.getLeftChild())
		sVal = sVal + str(tree.getRootVal())
		sVal = sVal + printexp(tree.getRightChild())+')'
	return sVal



inString = "( ( 10 + 5 ) * 3 )"
print(inString)
pt = buildParseTree(inString)
pt.postorder()

print(preorder(pt))
print(postorder(pt))
print(inorder(pt))

print(printexp(pt))





