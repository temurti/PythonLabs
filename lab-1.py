import random
import time
import copy

def buble(arr):
	newarr = arr[:]
	l = len(newarr)
	while l > 1:
		 for i in range(l-1):
			  if newarr[i] > newarr[i+1]:
				   newarr[i],newarr[i+1] = newarr[i+1],newarr[i]
		 l -= 1
	return newarr




def shaker(arr):
	newarr = arr[:]
	i = 0
	j = len(arr) - 1
	s = True
	while (i < j) and s :
		s = False
		k=i
		for k in range(k,j,1):
			if newarr[k] > newarr[k+1] :
				newarr[k],newarr[k+1] = newarr[k+1], newarr[k]
				s = True
		j = j - 1
		if s :
			s = False
			k = j
			for k in range(k,i,-1):
				if newarr[k]<newarr[k-1] :
					newarr[k],newarr[k-1] = newarr[k-1], newarr[k]
					s = True
		i = i+1
	return newarr


def comb(arr):
    b = True
    newarr = arr[:]
    s = len(newarr)
    while s > 1 or b:
        s = int(s/1.247330950103979) # (1-exp(-(sqrt(5)+1)/2))**(-1)
        if s in [9, 10]:
            s = 11
        elif s < 1:
            s = 1
            b = False
        for i in range(0, len(arr)-s):
            if newarr[i] > newarr[i+s]:
                newarr[i], newarr[i+s] = newarr[i+s], newarr[i]
                b = True
    return newarr


def insert(arr):
	newarr = arr[:]
	for i in range(len(newarr)):
		k = newarr[i]
		j = i;
		while (newarr[j-1]> k) and (j>0): 
			newarr[j] = newarr[j-1]
			j = j - 1
		newarr[j] = k
	return newarr


def binary(arr):
    for i in range(1,len(arr)):
		left = 0
		right = i
		while left < right:
			m = (left + right) / 2
			if arr[m] > arr[i]:
				right = m
			else:
				left = m + 1
		b = arr.pop(i)
		arr.insert(left, b)
    return arr
    



def shell(arr):
	newarr = arr[:]
	b = len(newarr)
	k = int(len(newarr) / 2)
	while k > 0 :
		for i in range(b-k):
			j = i
			while (j>=1) and (newarr[j] > newarr[j+k]):
				newarr[j],newarr[j+k] = newarr[j+k], newarr[j]
				j = j -1 
		k = int(k / 2)
	return newarr
	
	
	
def gnome(arr):
	newarr = arr[:]
	i = 1
	j = 2
	while i<len(newarr):
		if newarr[i-1] < newarr[i]:
			i = j
			j = j + 1
		else:
			newarr[i-1],newarr[i] = newarr[i], newarr[i-1]
			i = i - 1
			if i == 0 :
				i = j
				j = j + 1
	return newarr

arr= range(10**3)
random.shuffle(arr)

a = time.clock()
buble(arr)
print  "Buble Sort : ", time.clock() - a  ,"sec" 
a = time.clock()
shaker (arr)
print  "Shaker Sort : ", time.clock() - a  ,"sec" 
a = time.clock()
comb(arr)
print  "Comb Sort : ", time.clock() - a  ,"sec" 
a = time.clock()
insert (arr)
print  "Insert Sort : ", time.clock() - a  ,"sec" 
a = time.clock()
shell(arr)
print  "Shell Sort : ", time.clock() - a  ,"sec" 
a = time.clock()
gnome (arr)
print  "Gnome Sort : ", time.clock() - a  ,"sec" 
a = time.clock()
binary(arr)
print  "Binary Sort : ", time.clock() - a  ,"sec" 
