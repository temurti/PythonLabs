
import string
from random import choice, randint
import time

genString = lambda num, alf: ''.join(choice(alf) for i in xrange(num))
def genDString(num, alf, s):
	o = []
	i = 0
	n = len(s)
	while i < num:
		if randint(0, 1):
			o.append(s)
			i += n
		else:
			o.append(choice(alf))
			i += 1
	return ''.join(o)[:num]

def brutefoceMatch(a, b):
	n = len(a)
	m = len(b)
	o = []
	for i in xrange(n - m + 1):
		if b == a[i:i + m]:
			o.append(i)
	return o

def RKMatch(a, b, d=67, q=1305307):
	global alf
	n = len(a)
	m = len(b)
	h = pow(d, m - 1, q)
	tmp = p = 0
	o = []
	for i in xrange(m):
		p = (p * d + alf.index(b[i])) % q
		tmp = (tmp * d + alf.index(a[i])) % q
	for i in xrange(n-m+1):
		if p == tmp and b == a[i:i+m]:
			o.append(i)
		if i < n - m:
			tmp = (d * (tmp - alf.index(a[i]) * h) + alf.index(a[i+m])) % q
	return o

def automatonMatch(T, P):
	m = len(P)
	def deltaFunc(q, a):
		k = min(m + 1, q + 2)
		while True:
			k -= 1
			if (P[:q] + a).endswith(P[:k]): break
		return k
	n = len(T)
	q = 0
	o = []
	for i in xrange(n):
		q = deltaFunc(q, T[i])
		if q == m:
			o.append(i - m + 1)
	return o

def KMPMatch(T, P):
	def prefix(s):
		n = len(s)
		v = [0] * n
		k = 0
		for i in xrange(1, n):
			while k > 0 and s[k] != s[i]:
				k = v[k-1]
			if s[k] == s[i]:
				k += 1
			v[i] = k
		return v
	n = len(T)
	m = len(P)
	p = prefix(P)
	q = 0
	o = []
	for i in xrange(n):
		while q > 0 and P[q] != T[i]:
			q = p[q-1]
		if P[q] == T[i]:
			q += 1
		if q == m: 
			o.append(i-m+1)
			q = p[q-1]
	return o

N1, N2 = pow(10, 6), pow(10, 3)

alf = '0123456789abcdef'
a, b = genString(N1, alf), genString(N2, alf)
for f in [brutefoceMatch, RKMatch, automatonMatch, KMPMatch]:
	t = time.time()
	f(a, b)
	print '%20s: %.5f' % (f.__name__, time.time() - t)
print	
alf = string.ascii_letters
a, b = genString(N1, alf), genString(N2, alf)
for f in [brutefoceMatch, RKMatch, automatonMatch, KMPMatch]:
	t = time.time()
	f(a, b)
	print '%20s: %.5f' % (f.__name__, time.time() - t)
print
alf = string.ascii_letters
s = genString(25, alf)
a, b = genDString(N1, alf, s), genDString(N2, alf, s)
for f in [brutefoceMatch, RKMatch, automatonMatch, KMPMatch]:
	t = time.time()
	f(a, b)
	print '%20s: %.5f' % (f.__name__, time.time() - t)
