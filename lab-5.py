import random
import time


def divMethod(k,s):
	result  = k % s
	return result


def multMethod(k,s, c = 0.61):
	b = (k*c)  % s
	return int(k*(b-int(b)))


def universalMethod(k, size, x, y, p):
	return ((x*k+y) % p) % size


class HashTable(object):
	def __init__(self, size):
		self.size = size
		self.table = [[] for i in xrange(size)]

	def use(self, method, **k):
		self.method = method
		self.method_params = k

	def insert(self, x):
		if not isinstance(x, list): x = [x]
		for i in x:
			index = self.method(i, self.size, **self.method_params)
			self.table[index].append(i)
			
	def remove(self, x):
		i = self.method(x, self.size, **self.method_params)
		self.table[i].remove(x)
	
	def search(self, x):
		j = self.method(x, self.size, **self.method_params)
		return x in self.table[j]

	def __str__(self):
		return '{\n\t' + '\n\t'.join('%s: %s' % (i, j) for i, j in enumerate(self.table)) + '\n}'


def linMethod(k, i, size, method, method_p):
	return (method(k, size, **method_p)+i) % size
	
def quadMethod(k, i, c1, c2, size, method, method_p):
	return (method(k, size, **method_p)+c1*i+c2*i**2) % size
	
def doubleMethod(k, i, size, method1, method2, method1_p, method2_p):
	return (method1(k, size, **method1_p)+i*method2(k, size, **method2_p)) % size

	
class HashTableOpen(object):	
	def __init__(self, size):
		self.size = size
		self.table = [None for i in xrange(size)]
		self.delsign = 'del'

	def use(self, function, **k):
		self.method = function
		self.method_params = k
	
	def insert(self, x):
		i = 0
		while i != self.size:
			j = self.method(x, i, size=self.size, **self.method_params)
			if self.table[j] is None or self.table[j] == self.delsign:
				self.table[j] = x
				return j
			i += 1
		return "Error"
		
	def search(self, x):
		i = 0
		while True:
			j = self.method(x, i, size=self.size, **self.method_params)
			if self.table[j] == x:
				return j
			i += 1
			if self.table[j] is None and i == self.size:
				break
		return None
		
	def remove(self, x):
		i = self.search(x)
		if i:
			tmp = self.table[i]
			self.table[i] = self.delsign
			return tmp
		return None
			
	def __str__(self):
		return '{\n\t' + '\n\t'.join('%s: %s' % (i, j) for i, j in enumerate(self.table)) + '\n}'

	
M=10**4
range1 = range(M)
random.shuffle(range1)
range2 = range(M/2) + range(M/2, M)[::-1]

print 'HashTable:'
for i in [range1,range2]:
	p = 6563087
	param = [{}, {}, {'p': p, 'x': random.randint(1, p-1), 'y': random.randint(0, p-1)}]
	for j in zip([divMethod, multMethod, universalMethod], param):
		hashtable = HashTable(M)
		hashtable.use(method=j[0], **j[1])
		t = time.time()
		for k in i:
			hashtable.insert(k)
		print '%s: %.3f' % (j[0].__name__, time.time()-t) , 'sec'
	print '\n'
	
print 'HashTableOpen:'
for i in [range1, range2]:
	p = 6563087
	params = [
		{	'method': universalMethod,
			'method_p': {'p': p, 'x': random.randint(1, p-1), 'y': random.randint(0, p-1)}
		},
		{	'method': universalMethod,
			'method_p': {'p': p, 'x': random.randint(1, p-1), 'y': random.randint(0, p-1)},
			'c1': 2,
			'c2': 3
		},
		{	'method1': universalMethod,
			'method1_p': {'p': p, 'x': random.randint(1, p-1), 'y': random.randint(0, p-1)},
			'method2': divMethod,
			'method2_p': {},

		}	]
	for j in zip([linMethod, quadMethod, doubleMethod], params):
		hashtable = HashTableOpen(M*2)
		hashtable.use(function=j[0], **j[1])
		t = time.time()
		for k in i:
			hashtable.insert(k)
		print '%s: %.3f' % (j[0].__name__, time.time()-t) , 'sec'
	print
