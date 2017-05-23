import random,time

def simpleSearch(text,pattern):
	n, m = len(text), len(pattern)
	answer = []
	for i in range(n-m+1):
		if pattern == text[i:i+m]:
			answer.append(i)
	return answer


def hash_value(s, base):
    v = 0
    p = len(s)-1
    for i in range(p+1):
        v += ord(s[i]) * (base ** p)
        p -= 1
    return v
    
    
def RabinKarpSearch(text, pattern, hash_base=256):
    n = len(text)
    m = len(pattern)
    answer = []
   
    def hash_value(s, base):
		v = 0
		p = len(s)-1
		for i in range(p+1):
			v += ord(s[i]) * (base ** p)
			p -= 1
		return v
   
    htext = hash_value(text[:m], hash_base)
    hpattern = hash_value(pattern, hash_base)
    for i in range(n-m+1):
        if htext == hpattern:
            if text[i:i+m] == pattern: 
                answer.append(i)
        if i < n-m:
            htext = (hash_base * (htext - (ord(text[i]) * (hash_base ** (m-1))))) + ord(text[i+m])
    return answer
    

def automatMatch(T, P):
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


def prefix(x):
    d = {0:0}
    for i in xrange(1,len(x)):
        j = d[i-1]
        while j > 0 and x[j] <> x[i]:
            j = d[j-1]
        if x[j] == x[i]:
            j += 1
        d[i] = j
    return d


def kmpSearch(text, pattern):
    n = len(text)
    m = len(pattern)
    offsets = []
    pi = prefix(pattern)
    q = 0
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q = q + 1
        if q == m:
            offsets.append(i - m + 1)
            q = pi[q-1]
    return offsets
    

def randomString():
    qty = 10**5
    minimum = 65
    maximum = 90
    sample = ''
    for i in range(qty):
        sample = sample + chr(int(random.random() * (maximum - minimum + 1)) + minimum)
    return sample


a = randomString()
b='ABCDEE'*(10**5)
c = 'ABC'

for j in [a,b]:
	t = time.time()
	simpleSearch(j[:],c)
	print 'simpleSearch: %.3f' % (time.time() - t), "sec"

	t = time.time()
	RabinKarpSearch(j[:],c)
	print 'RabinKarpSearch: %.3f' % (time.time() - t), "sec"

	t = time.time()
	kmpSearch(j[:],c)
	print 'kmpSearch: %.3f' % (time.time() - t), "sec"

	t = time.time()
	automatMatch(j[:],c)
	print 'automatMatch: %.3f' % (time.time() - t), "sec\n"













