import random
import time
import math



def merge_sort(a):
	if len(a) <= 1:
		return a
	m = int(len(a)/2)
	left = merge_sort(a[:m])
	right= merge_sort(a[m:])
	return merge(left,right)

def merge(left , right):
	result = []
	while len(left)>0 and len(right)>0:
		if left[0] <= right[0]:
			result.append(left[0])
			left = left[1:]
		else:
			result.append(right[0])
			right = right[1:]
	if len(left)>0:
		result +=left
	if len(right)>0:
		result +=right
	return result



def quicksort(a):
	if a:
		return quicksort([i for i in a[1:] if i<a[0]]) + a[0:1] + quicksort([j for j in a[1:] if j>=a[0]])
	return []

def partition(a, l, r):
	x = a[r]
	i = l - 1
	for j in xrange(l, r):
		if x >= a[j]:
			i += 1
			a[i], a[j] = a[j], a[i]
	a[i+1], a[r] = a[r], a[i+1]
	return i + 1


def qsort(a, l, r, t_partition):
	if l < r:
		q = t_partition(a, l, r)
		qsort(a, l, q-1, t_partition)
		qsort(a, q+1, r, t_partition)
	return a


def randomPartition(a, l, r):
	i = random.randint(l, r)
	a[i], a[r] = a[r], a[i]
	return partition(a, l, r)
	

def medianPartition(a, l, r):
	y = (r-l) / 2
	m = max(a[l],a[y],a[r])
	"""
	if (a[l]<=a[y]) and (a[y]<=a[r]):
		m = y	
	elif (a[l] >= a[y]) and (a[l]<=a[r]):
		m = l
	else:
		m = r
	"""		
	a[m], a[r] = a[r], a[m]
	return partition(a, l, r)


def stackQsort(a, t_partition):
	depth = 4 * math.ceil(math.log(len(a), 2))
	stack = [0 for x in xrange(int(depth))]
	stack[0] = (0, len(a) - 1)
	k = 0
	while k >= 0:
		l, r = stack[k]
		q = t_partition(a, l, r)
		r1, r2 = q + 1 if q != r else r,r
		l1, l2 = l, q - 1 if q != l else l
		k -= 1
		if r1 != r2: k += 1; stack[k] = (r1, r2)
		if l1 != l2: k += 1; stack[k] = (l1, l2)
	
		

def stackQsort2(a):
	depth = 4 * math.ceil(math.log(len(a), 2))
	stack = [0 for x in xrange(int(depth))]
	stack[0] = (0, len(a) - 1)
	k = 0
	while k >= 0:
		l, r = stack[k]
		q = QuickSortPos(a, l, r)
		r1, r2 = q + 1 if q != r else r,r
		l1, l2 = l, q - 1 if q != l else l
		k -= 1
		if r1 != r2: k += 1; stack[k] = (r1, r2)
		if l1 != l2: k += 1; stack[k] = (l1, l2)
	

def StackQuickSort(a):
	depth = 4 * math.ceil(math.log(len(a), 2))
	stack = [0 for x in xrange(int(depth))]
	k = 0
	stack[0] = 0
	stack[1] = len(a) - 1
	while (k >= 0):
		i = QuickSortPos(a, stack[k], stack[k+1])
		if(i != stack[k + 1]):RL =i + 1
		else:RL = stack[k + 1]
		RR = stack[k + 1]
		LL = stack[k]
		if(i != stack[k]):LR =i - 1
		else:LR =stack[k]
		k -= 2
		if (RL != RR):k += 2; stack[k] = RL; stack[k + 1] = RR
		if (LL != LR):k += 2; stack[k] = LL; stack[k + 1] = LR
	



def QuickSortPos(a, l, r):
    i = l
    j = r - 1
    while (True):
        while (a[i] < a[r]): i+=1
        while (a[j] > a[r] and j > l): j-=1
        if (i >= j): break
        a[i],a[j] = a[j],a[i]
    a[r],a[i]  = a[i],a[r]
    return i
    

a= range(10**4)
random.shuffle(a)

#a = [5,73,1,7,8,9]



t=time.clock()
merge_sort(a[:])
print "MergeSort: " , time.clock()-t, "sec \n"


partitions = [partition, randomPartition, medianPartition]
for i in partitions:
	print i.__name__,
	t= time.clock()
	qsort(a[:],0,len(a)-1, i)
	print "Qsort : ", time.clock()-t, "sec"
	t=time.clock()
	stackQsort(a[:],i)
	print "Stack Qsort: ", time.clock()-t, " sec \n" 
	
t=time.clock()
stackQsort2(a[:])
print "Stack Qsort new: ", time.clock()-t, "sec \n"

t=time.clock()
quicksort(a[:])
print "Python QuickSort", time.clock()-t, "sec \n"
