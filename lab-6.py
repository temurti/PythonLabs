import bintrees,time, random


# SEARCH TREE-------------
class Node(object):
	def __init__(self, key=None):
		self.parent = None
		self.left = None
		self.right = None
		self.key = key



class Tree(object):
	nil = None
	p = []
	
	def __init__(self, root=None):
		self.root = root

	def minimum(self, x):
		while x.left != self.nil:
			x = x.left
		return x

	def maximum(self, x):
		while x.right != self.nil:
			x = x.right
		return x

	def insert(self, x):
		b = self.nil
		a = self.root
		while a != self.nil:
			b = a
			a = a.left if x.key < a.key else a.right
		x.parent = b
		if b == self.nil: self.root = x
		elif x.key < b.key: b.left = x
		else: b.right = x

	def search(self, x, k):
		while x != self.nil and k != x.key:
			if k < x.key: x = x.left
			else: x = x.right
		return x

	def delete(self, z):
		if z.left == self.nil or z.right == self.nil:
			y = z
		else:
			y = self.successor(z)
		if y.left:
			x = y.left
		else:
			x = y.right
		if x != self.nil:
			x.parent = y.parent
		if not y.parent:
			self.root = x
		elif y == y.parent.left:
			y.parent.left = x
		else:
			y.parent.right = x
		if y != z:
			z.key = y.key
		return y

	def successor(self, x):
		if x.right != self.nil:
			return self.minimum(x.right)
		y = x.parent
		while y != self.nil and x.right != self.nil:
			x = y
			y = x.parent
		return y
		
	def predecessor(self, x):
		if x.left != self.nil:
			return self.maximum(x.left)
		y = x.parent
		while y != self.nil and x.left != self.nil:
			x = y
			y = x.parent
		return y

	def inorderTreeWalk(self, x):
		if x != self.nil:
			self.inorderTreeWalk(x.left)
			print x.key,
			self.inorderTreeWalk(x.right)

	def printTree(self, x, level=0):
		if x != self.nil:
			self.printTree(x.right, level+1)
			print ' ' * 4 * level,
			print x.key
			self.printTree(x.left, level+1)


#RED-BLACK TREE--------------

class RBNode(object):
	def __init__(self, key=None, color='red'):
		self.parent = None
		self.left = None
		self.right = None
		self.key = key
		self.color = color

class RBTree(object):
	nil = RBNode('*', color='black')
	
	def __init__(self, root=None):
		self.root = root if root else self.nil
		
	def insert(self, z):
		y = self.nil
		x = self.root
		while x != self.nil:
			y = x
			x = x.left if z.key < x.key else x.right
			
		z.parent = y
		if y == self.nil:
			self.root = z
		elif z.key < y.key:
			y.left = z
		else:
			y.right = z
		z.left = self.nil
		z.right = self.nil
		self.insertFixUp(z)
			
	def leftRotate(self, x):
		y = x.right
		x.right = y.left
		if y.left:
			y.left.parent = x
		y.parent = x.parent
		if x.parent == self.nil:
			self.root = y
		elif x == x.parent.left:
			x.parent.left = y
		else:
			x.parent.right = y
		y.left = x
		x.parent = y
		
	def rightRotate(self, x):
		y = x.left
		x.left = y.right
		if y.right:
			y.right.parent = x
		y.parent = x.parent
		if x.parent == self.nil:
			self.root = y
		elif x == x.parent.right:
			x.parent.right = y
		else:
			x.parent.left = y
		y.right = x
		x.parent = y
	
	def insertFixUp(self, z):
		while z.parent.color == 'red':
			if z.parent == z.parent.parent.left:
				y = z.parent.parent.right
				if y.color == 'red':
					z.parent.color = 'black'
					y.color = 'black'
					z.parent.parent.color = 'red'
					z = z.parent.parent
				else:
					if z == z.parent.right:
						z = z.parent
						self.leftRotate(z)
					z.parent.color = 'black'
					z.parent.parent.color = 'red'
					self.rightRotate(z.parent.parent)
			else:
				y = z.parent.parent.left
				if y.color == 'red':
					z.parent.color = 'black'
					y.color = 'black'
					z.parent.parent.color = 'red'
					z = z.parent.parent
				else:
					if z == z.parent.left:
						z = z.parent
						self.rightRotate(z)
					z.parent.color = 'black'
					z.parent.parent.color = 'red'
					self.leftRotate(z.parent.parent)
		self.root.color = 'black'
		
	def delete(self, z):
		if z.left == self.nil or z.right == self.nil:
			y = z
		else:
			y = self.successor(z)
		if y.left != self.nil:
			x = y.left
		else:
			x = y.right
		x.parent = y.parent
		if y.parent == self.nil:
			self.root = x
		elif y == y.parent.left:
			y.parent.left = x
		else:
			y.parent.right = x
		if y != z:
			z.key = y.key
		if y.color == 'black':
			self.deleteFixUp(x)
		return y
		
	def deleteFixUp(self, x):
		while x != self.root and x.color == 'black':
			if x == x.parent.left:
				w = x.parent.right
				if w.color == 'red':
					w.color = 'black'
					x.parent.color = 'red'
					self.leftRotate(x.parent)
					w = x.parent.right
				if w.left.color == 'black' and w.right.color == 'black':
					w.color = 'red'
					x = x.parent
				else:
					if w.right.color == 'black':
						w.left.color = 'black'
						w.color = 'red'
						self.rightRotate(w)
						w = x.parent.right
					w.color = x.parent.color
					x.parent.color = 'black'
					w.right.color = 'black'
					self.leftRotate(x.parent)
					x = self.root
			else:
				w = x.parent.left
				if w.color == 'red':
					w.color = 'black'
					x.parent.color = 'red'
					self.rightRotate(x.parent)
					w = x.parent.left
				if w.left.color == 'black' and w.right.color == 'black':
					w.color = 'red'
					x = x.parent
				else:
					if w.left.color == 'black':
						w.right.color = 'black'
						w.color = 'red'
						self.leftRotate(w)
						w = x.parent.left
					w.color = x.parent.color
					x.parent.color = 'black'
					w.left.color = 'black'
					self.rightRotate(x.parent)
					x = self.root
		x.color = 'black'


#AVL-TREE -------
			
class AVLNode(object):
	
	def __init__(self, key=None, height=0):
		self.parent = None
		self.left = None
		self.right = None
		self.key = key
		self.height = height
		
class AVLTree(Tree):
	nil = None

	def __init__(self, root=None):
		self.root = root if root else self.nil
	
	def height(self, x):
		return x.height if x else 0
	
	def fixHeight(self, x):
		hl = self.height(x.left)
		hr = self.height(x.right)
		x.height = max(hl, hr) + 1
		
	def rotateLeft(self, x):
		y = x.right
		x.right = y.left
		if y.left:
			y.left.parent = x
		
		y.left = x
		
		if x.parent:
			if x == x.parent.right:
				x.parent.right = y
			else:
				x.parent.left = y
		y.parent = x.parent
		x.parent = y
		self.fixHeight(x)
		self.fixHeight(y)
		return y
		
	def rotateRight(self, x):
		y = x.left
		x.left = y.right
		if y.right:
			y.right.parent = x
		y.right = x
		if x.parent:
			if x == x.parent.right:
				x.parent.right = y
			else:
				x.parent.left = y
		y.parent = x.parent
		x.parent = y
		self.fixHeight(x)
		self.fixHeight(y)
		return y
		
	def balanceFactor(self, x):
		return self.height(x.right) - self.height(x.left)
		
	def balanceNode(self, x):
		while x:
			self.fixHeight(x)
			balance = self.balanceFactor(x)
			if balance == 2:
				if x.right and self.balanceFactor(x.right) < 0:
					x.right = self.rotateRight(x.right)
				x = self.rotateLeft(x)
			elif balance == -2:
				if x.left and self.balanceFactor(x.left) > 0:
					x.left = self.rotateLeft(x.left)
				x = self.rotateRight(x)
			if not x.parent: self.root = x
			x = x.parent
		
	def insert(self, x):
		b = self.nil
		a = self.root
		while a != self.nil:
			b = a
			a = a.left if x.key < a.key else a.right
		x.parent = b
		if b == self.nil: self.root = x
		elif x.key < b.key: b.left = x
		else: b.right = x
		self.balanceNode(x)
			
	def removeMin(self, x):
		while x.left:
			x = x.left
		y = x.parent
		if y.left == x:
			y.left = None
		else:
			y.right = None
		self.balanceNode(y)
		return x
			
	def delete(self, z):
		if not z.left and not z.right:
			if z.parent:
				if z == z.parent.left:
					z.parent.left = self.nil
				else:
					z.parent.right = self.nil
				z = z.parent
				self.balanceNode(z)
			else:
				self.root = self.nil
		else:
			y = self.removeMin(z.right)
			z.key = y.key
			self.balanceNode(z)
	
	def printTree1(self, x, level=0):
		if x != self.nil:
			self.printTree(x.right, level+1)
			print ' ' * 4 * level,
			print '%s %s' % (x.key, x.size)
			self.printTree(x.left, level+1)
			

class AVLNodeR(object):
	
	def __init__(self, key=None, height=0):
		self.parent = None
		self.left = None
		self.right = None
		self.key = key
		self.height = height
		self.size = 0
		
class AVLTreeR(Tree):
	nil = None
	
	def __init__(self, root=None):
		self.root = root if root else self.nil
	
	def height(self, x):
		return x.height if x else 0
	
	def fixHeight(self, x):
		hl = self.height(x.left)
		hr = self.height(x.right)
		x.height = max(hl, hr) + 1
		
	def fixSize(self, x):
		x.size = 1
		if x.left:
			x.size += (x.left.size)
		if x.right:
			x.size += (x.right.size)
		
	def rotateLeft(self, x):
		y = x.right
		x.right = y.left
		if y.left:
			y.left.parent = x
		
		y.left = x
		
		if x.parent:
			if x == x.parent.right:
				x.parent.right = y
			else:
				x.parent.left = y
		y.parent = x.parent
		x.parent = y
		self.fixHeight(x)
		self.fixHeight(y)
		self.fixSize(x)
		self.fixSize(y)
		return y
		
	def rotateRight(self, x):
		y = x.left
		x.left = y.right
		if y.right:
			y.right.parent = x
		y.right = x
		if x.parent:
			if x == x.parent.right:
				x.parent.right = y
			else:
				x.parent.left = y
		y.parent = x.parent
		x.parent = y
		self.fixHeight(x)
		self.fixHeight(y)
		self.fixSize(x)
		self.fixSize(y)
		return y
		
	def balanceFactor(self, x):
		return self.height(x.right) - self.height(x.left)
		
	def balanceNode(self, x):
		while x:
			self.fixHeight(x)
			self.fixSize(x)
			balance = self.balanceFactor(x)
			if balance == 2:
				if x.right and self.balanceFactor(x.right) < 0:
					x.right = self.rotateRight(x.right)
				x = self.rotateLeft(x)
			elif balance == -2:
				if x.left and self.balanceFactor(x.left) > 0:
					x.left = self.rotateLeft(x.left)
				x = self.rotateRight(x)
			if not x.parent: self.root = x
			x = x.parent
		
	def insert(self, x):
		b = self.nil
		a = self.root
		while a != self.nil:
			b = a
			a = a.left if x.key < a.key else a.right
		x.parent = b
		if b == self.nil: self.root = x
		elif x.key < b.key: b.left = x
		else: b.right = x
		self.balanceNode(x)
			
	def removeMin(self, x):
		while x.left:
			x = x.left
		y = x.parent
		if y.left == x:
			y.left = None
		else:
			y.right = None
		self.balanceNode(y)
		return x
			
	def delete(self, z):
		if not z.left and not z.right:
			if z.parent:
				if z == z.parent.left:
					z.parent.left = self.nil
				else:
					z.parent.right = self.nil
				z = z.parent
				self.balanceNode(z)
			else:
				self.root = self.nil
		else:
			y = self.removeMin(z.right)
			z.key = y.key
			self.balanceNode(z)
	
	def select(self, x, i):
		r = (x.left.size if x.left else 0) + 1
		if i == r:
			return x
		else:
			if i < r:
				return self.select(x.left, i)
			else:
				return self.select(x.right, i-r)
				
	def rank(self, x):
		r = (x.left.size if x.left else 0) + 1
		y = x
		while y != self.root:
			if y == y.parent.right:
				r = r + (y.parent.left.size if y.parent.left else 0) + 1
			y = y.parent
		return r
		
	def printTree1(self, x, level=0):
		if x != self.nil:
			self.printTree(x.right, level+1)
			print ' ' * 4 * level,
			print '%s %s' % (x.key, x.size)
			self.printTree(x.left, level+1)
		
		
def buildBinaryTree(a):
	tree = Tree()
	for i in a:
		tree.insert(Node(i))
	
def buildRBTree(a):
	tree = RBTree()
	for i in a:
		tree.insert(RBNode(i))
	
def buildAVLTree(a):
	tree  = AVLTree()
	for i in a:
		tree.insert(AVLNode(i))


def buildPyBinTree(a):
	tree = bintrees.BinaryTree()
	for i in a:
		tree.insert(i, i)
		
def buildPyRBTree(a):
	tree = bintrees.rbtree.RBTree()
	for i in a:
		tree.insert(i, i)
				
def buildPyAVLTree(a):
	tree = bintrees.avltree.AVLTree()
	for i in a:
		tree.insert(i, i)
		

q = 10**4
a = range(q);random.shuffle(a)
#a = [8,3,1,6,4,7,10,14,13]

t = time.time()
buildBinaryTree(a[:])
print "BinTree: %.3f" % (time.time() - t), "sec"

t = time.time()
buildRBTree(a[:])
print "RBtree : %.3f" % (time.time() - t), "sec"

t = time.time()
buildAVLTree(a[:])
print 'AVLtree: %.3f' % (time.time() - t), "sec"

t = time.time()
buildPyBinTree(a[:])
print 'PythonBinTree: %.3f' % (time.time() - t), "sec"

t = time.time()
buildPyRBTree(a[:])
print 'PythonRBtree: %.3f' % (time.time() - t), "sec"

t = time.time()
buildPyAVLTree(a[:])
print 'PythonAVLtree: %.3f' % (time.time() - t), "sec"


a = [1,3,2,4,55,7,6,8,99]
tree = AVLTreeR()
for i in a:
	tree.insert(AVLNodeR(i))
	
tree.printTree(tree.root)
print tree.rank(tree.search(tree.root, 55))
