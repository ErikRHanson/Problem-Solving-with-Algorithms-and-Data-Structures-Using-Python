from pythonds.trees.binaryTree import BinaryTree
import operator

x = BinaryTree('*')
x.insertLeft('+')
l = x.getLeftChild()
l.insertLeft(4)
l.insertRight(5)
x.insertRight(7)


def printexp(tree):
  sVal = ""
  if tree:
      sVal = '(' + printexp(tree.getLeftChild())
      sVal = sVal + str(tree.getRootVal())
      sVal = sVal + printexp(tree.getRightChild())+')'
  return sVal

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

print(printexp(x))

print(postordereval(x))
