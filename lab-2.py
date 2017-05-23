import random
import time
import heapq



def heapify(a, i, size, k=2):
	childs = [k*i+j for j in xrange(1, k+1) if k*i+j < size]
	largest = i 
	for j in childs:
		if a[j] > a[largest]:
			largest = j
	if largest > i:
		a[i], a[largest] = a[largest], a[i]
		heapify(a, largest, size, k)

def buildHeap(a, k=2):
	size = len(a)
	for i in xrange( len(a) / k, -1, -1):
		heapify(a, i, size, k)
	return a
	
def insert(a,value, k=2):
	a.append(value)
	i = len(a) - 1
	parent = (i-1) / k
	while i > 0 and a[parent] < a[i]:
		a[parent], a[i] = a[i], a[parent]
		i = parent
		parent = (i-1) / k
		
def maxElem(a,k=2):
	if not len(a):
		print "Heap is empty"
	maxElem , a[0] = a[0], a[-1]
	a.pop(0)
	heapify(a, 0, len(a), k)
	return maxElem

def pythonHeapSort(iterable):
	h = []
	for value in iterable:
		heapq.heappush(h, value)
	return [heapq.heappop(h) for i in xrange(len(h))]

def pythonHeapBuild(a):
	pythonheap = []
	for i in a:
		heapq.heappush(pythonheap, i)
	return pythonheap

def SelectSort(a):
	size = len(a)
	for i in xrange(size-1):
		elem = i 
		for j in xrange(i+1, size):
			if a[j] < a[elem]:
				elem = j
		if elem != i:
			a[elem], a[i] = a[i], a[elem]
	return a

def heapSort(a):
	buildHeap(a)
	for i in xrange(len(a)-1, 0, -1):
		a[i], a[0] = a[0], a[i]
		heapify(a, 0, i)
	return a
	
a= range(10**3)
random.shuffle(a)
#a = [3,2,4,5,6,7,8,9]

t = time.clock()
buildHeap(a[:]) 
print  "My heap build :" , time.clock() - t  ,"sec"

t = time.clock()
pythonHeapBuild(a[:])
print  "Python heap build:" , time.clock() - t , "sec" 

t=time.clock()
buildHeap(a[:],10)
print "My 10 heap build:" , time.clock()-t, "sec"

t= time.clock()
SelectSort(a[:])
print "Select Sort : ", time.clock()-t, "sec"

t= time.clock()
heapSort(a[:])
print "heapSort: " , time.clock()-t, "sec"

