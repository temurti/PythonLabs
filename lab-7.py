import math
import random
import time
import sys

def check(s,t):
	x1,y1,x2,y2,x3,y3,x4,y4 = s[0],s[1],s[2],s[3],t[0],t[1],t[2],t[3]
	a1 = y2 - y1
	b1 = x1 - x2
	c1 = -a1 * x1 - b1 * y1
	a2 = y4 - y3
	b2 = x3 - x4
	c2 = -a2 * x3 - b2 * y3
	d  = a1*b2 - a2*b1
	if abs(d) >= sys.float_info.epsilon:
		dx = -c1 * b2 + c2 * b1
		dy = -a1 * c2 + a2 * c1
		x  = dx / d
		y  = dy / d
		if (min(x1, x2) - sys.float_info.epsilon < x) and (x < max(x1, x2) + sys.float_info.epsilon) and (min(y1, y2) - sys.float_info.epsilon < y) and (y < max(y1, y2) + sys.float_info.epsilon) and (min(x3, x4) - sys.float_info.epsilon < x) and (x < max(x3, x4) + sys.float_info.epsilon) and (min(y3, y4) - sys.float_info.epsilon < y) and (y < max(y3, y4) + sys.float_info.epsilon):
			res1, res2 = x, y
			return True #res1,res2
	if abs(c1 * b2 - c2 * b1) < sys.float_info.epsilon:
		if (abs(x1 - x3) < sys.float_info.epsilon) or (abs(x1 - x4) < sys.float_info.epsilon):
			return x1,y1
		if (abs(x2 - x3) < sys.float_info.epsilon) or (abs(x2 - x4) < sys.float_info.epsilon):
			return x2,y2


def crossLines(A):
	n = len(A)
	P = range(n)
	for i in xrange(0,n-1):
		for j in xrange(i+1,n):
			check(A[i],A[j])
	return None

def above(a,s):
	n = len(a)
	for i in xrange(0,n-1):
		x = max(min(s[0],s[2]),min(a[i][0],a[i][2]))
		Ys = (((x - s[0]) * (s[3]-s[1]))/(s[2]-s[0])) + s[1]
		Ya = (((x - a[i][0]) / (a[i][2] - a[i][0]))*(a[i][3]-a[i][1])) + a[i][1]
		if Ya > Ys:
			return a[i]
	return None
	


def below(a,s):
	n = len(a)
	for i in xrange(0,n-1):
		x = max(min(s[0],s[2]),min(a[i][0],a[i][2]))
		Ys = (((x - s[0]) * (s[3]-s[1]))/(s[2]-s[0])) + s[1]
		Ya = (((x - a[i][0]) / (a[i][2] - a[i][0]))*(a[i][3]-a[i][1])) + a[i][1]
		if Ya < Ys:
			return a[i]
	return None


def crossLines2(A):
	n = len(A)
	P = range(n)
	for i in xrange(0,n-1):
		for j in xrange(i+1,n):
			x1,y1,x2,y2,x3,y3,x4,y4 = A[P[i]][0],A[P[i]][1],A[P[i]][2],A[P[i]][3],A[P[j]][0],A[P[j]][1],A[P[j]][2],A[P[j]][3]
			if (x2 > x4): A[P[i]], A[P[j]] = A[P[j]], A[P[i]]
			if (x2 == x4) and (y2>=y4): A[P[i]], A[P[j]] = A[P[j]], A[P[i]]
	Begins, Ends, S = [],[],[]
	for i in xrange(0,n): Ends.append(A[i][2:])
	for j in xrange(0,n): Begins.append(A[j][2:])
	for p in Ends:
		for e in xrange(0,n):
			if p == A[e][:2]: # levo
				S.append(A[e])
				if ((above(S,A[e]) != None) and check(A[e],(above(S,A[e])))) or (below(S,A[e])!= None and check(S,A[e])): 
					return A[e],s
			if p == A[e][2:]: # pravo
				if above(A,A[e]) != None and below (A,A[e]) != None and check(above(A,A[e]),below(A,A[e])):
					return True
					S.remove(A[e])
	return False


def rotate(A,B,C):
  return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])
  
def jarvismarch(A):
	n = len(A)
	P = range(n)
	for i in xrange(1,n):
		if A[P[i]][0]<A[P[0]][0]: 	# start point
			P[i], P[0] = P[0], P[i]   
	H = [P[0]] # new array
	del P[0]
	P.append(H[0]) # start point to the end
	while True:
		right = 0
		for i in xrange(1,len(P)):
			if rotate(A[H[-1]],A[P[right]],A[P[i]])<0:
				right = i
		if P[right]==H[0]: 
			break
		else:
			H.append(P[right])
			del P[right]
	#for j in H: print A[j] 
	# n*log(n)
	return H


def grahamscan(A):
	n = len(A)
	P = range(n)
	for i in xrange(1,n):
		if A[P[i]][0]<A[P[0]][0]:
			P[i],P[0] = P[0], P[i]
	for i in xrange(2,n): # insert sort
		j = i
		while j>1 and (rotate(A[P[0]],A[P[j-1]],A[P[j]])<0): 
			P[j], P[j-1] = P[j-1], P[j]
			j -= 1
	S = [P[0],P[1]] # stek
	for i in xrange(2,n):
		while rotate(A[S[-2]],A[S[-1]],A[P[i]])<0:
			del S[-1] # pop(S)
		S.append(P[i]) # push(S,P[i])
	#for j in S: print A[j]
	#n*h
	return S

def dist(a,b):
	return math.sqrt((b[0]-a[0])**2 + (b[1] - a[1])**2)

def closestPoints(A):
	n = len(A)
	P = range(n)
	dmin = float("infinity")
	for i in xrange(1,n-1):
		for j in xrange(i+1,n):
			d = dist(A[P[i]], A[P[j]])
			if d < dmin:
				dmin = d
				res1 = A[P[i]]
				res2 = A[P[j]]
	return res1,res2


def binaryY(arr):
    for i in range(1,len(arr)):
		left = 0
		right = i
		while left < right:
			m = (left + right) / 2
			if arr[m][1] > arr[i][1]:
				right = m
			else:
				left = m + 1
		b = arr.pop(i)
		arr.insert(left, b)
    return arr

def closestPointsDecomp(A):
	sorted(A)
	INF = 2**31 - 2
	c_y = lambda x: x[1]
	def start(a):
		n = len(a)
		if n == 2:
			return  dist(a[0],a[1]),a[0], a[1]
		elif n == 1:
			return INF, a[0], None	
		m = n / 2
		f_left, p1_left, p2_left = start(a[:m])
		f_right, p1_right, p2_right = start(a[m:])
		if f_left > f_right:
			f, p1, p2 = f_right, p1_right, p2_right
		else:
			f, p1, p2 = f_left, p1_left, p2_left
		s = [i for i in a if i[0] - a[m][0] <= f]
		binaryY(s)
		ns = len(s)
		for i in xrange(ns - 1):
			for j in xrange(i + 1, min(ns, i + 7)):
				tmp = dist(s[i],s[j])
				if tmp < f:
					f, p1, p2 = tmp, s[i], s[j]
		return f, p1, p2
	return start(A)
	 

	
def list_random_integers():
    qty = 1000
    minimum = 1
    maximum = qty
    sample = []
    for i in range(qty):
        sample.append((int(random.random() * (maximum - minimum + 1)) + minimum, int(random.random() * (maximum - minimum + 1)) + minimum))
    return sample
    
def list_random_segments():
    qty = 1000
    minimum = 1
    maximum = qty
    sample = []
    for i in range(qty):
        sample.append((int(random.random() * (maximum - minimum + 1)) + minimum, int(random.random() * (maximum - minimum + 1)) + minimum,int(random.random() * (maximum - minimum + 1)) + minimum,int(random.random() * (maximum - minimum + 1)) + minimum))
    return sample
    


#a = [(34,0),(1,8),(1,33),(0,1)]
a = list_random_integers()
b = list_random_segments()



t = time.time()
crossLines(b[:])
print 'crossLines: %.3f' % (time.time() - t), "sec"

t = time.time()
crossLines2(b[:])
print 'crossLines2: %.3f' % (time.time() - t), "sec"

t = time.time()
jarvismarch(a[:])
print 'Jarvis: %.3f' % (time.time() - t), "sec"

t = time.time()
grahamscan(a[:])
print 'Graham: %.3f' % (time.time() - t), "sec"


t = time.time()
closestPoints(a[:])
print 'Closest Points: %.3f' % (time.time() - t), "sec"

t = time.time()
closestPointsDecomp(a[:])
print 'closestPointsDecomp: %.3f' % (time.time() - t), "sec"



