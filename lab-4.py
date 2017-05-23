import random
import time




def CountSort(a, k):
	c = [0 for i in xrange(k)]
	b = [0 for i in a]
	for i in a:
		c[i] += 1
	for i in xrange(1, k):
		c[i] += c[i-1]
	for i in a:
		c[i] -= 1
		b[c[i]] = i
	return b

	
def CountSort2(a, d):
	k = 10
	c = [0 for i in xrange(k)]
	b = [0 for i in a]
	for i in a:
		c[int(i[d])] += 1
	for i in xrange(1, k):
		c[i] += c[i-1]
	for i in reversed(a):
		c[int(i[d])] -= 1
		b[c[int(i[d])]] = i
	return b


def RadixSort(a, d):
	a = map(lambda x: str(x).zfill(d), a)
	for i in xrange(d-1, -1, -1):
		a = CountSort2(a, i)
	return map(int, a)
	

def BucketSortSimple(a):
	bucket1,bucket2,bucket3 = [],[],[]
	for i in xrange(len(a)):
		if a[i] in range(31):
			bucket1.append(a[i])
		elif a[i] in range(61):
			bucket2.append(a[i])
		elif a[i] in range(101):
			bucket3.append(a[i])
		elif a[i] in range(141):
			bucket3.append(a[i])
	
	SelectSort(bucket1)
	SelectSort(bucket2)
	SelectSort(bucket3)
	final = bucket1 + bucket2 + bucket3
	return final
		


class Node:
	def __init__(self,value=None, next=None, prev=None):
		self.value = value
		self.next = next
		self.prev = prev

def insertSortList(head):
	i = head.next
	while i.next:
		j = i.next
		while j.prev != head and j.value < j.prev.value:
			j.value, j.prev.value = j.prev.value, j.value
			j = j.prev
		i = i.next
		
		
def bucketSort(a, k):
	n = len(a)
	m = max(a)
	b = [Node() for i in xrange(k)]
	for i in a:
		index = int((k-1)*(float(i)/m))
		x = b[index]
		while x.next:	x = x.next
		x.next = Node(i)
		x.next.prev = x
	for i in b:
		if i.next: insertSortList(i)
	tmp = 0
	for i in b:
		x = i.next
		while x:
			a[tmp] = x.value
			tmp += 1
			x = x.next
	return a



q = 10**4
a = range(q)
random.shuffle(a)


t = time.clock()
CountSort(a[:],q)
print  "CountSort :" , time.clock() - t  ,"sec\n"

t = time.clock()
RadixSort(a[:],4)
print  "RadixSort :" , time.clock() - t  ,"sec\n"

t = time.clock()
bucketSort(a[:],q)
print  "BucketSort :" , time.clock() - t  ,"sec\n"
