

import sys
from math import sqrt

f= open(sys.argv[1],'r')
lista=[]
for t in f.readlines():
	t=t.rstrip('\n')
	t=t.split()
	for i in range(len(t)):
		t[i]=float(t[i])
	lista.append(tuple(t))
f.close()

print(lista)

def dist(t,p):
	return sqrt((abs(t[0]-p[0]))**2 + (abs(t[1]-p[1]))**2)

def ldedist(a):
	if len(a)==1:
		return []
	else:	
		l=[]
		i=1
		while i<len(a):
			l.append(dist(a[0],a[i]))
			i+=1
		return l+ldedist(a[1:])

print(ldedist(lista))

def distanciaMinima(a):
	if len(a)==1:
		return a[0]
	else:	
		mini = distanciaMinima(a[1:])
		if a[0] <= mini:
			return a[0]
		else:
			return mini

print(distanciaMinima(ldedist(lista)))

def upsort(a):
	pos=len(a)-1
	i=0
	while pos>0:
		i=maxpos(a,pos)
		a[i],a[pos]=a[pos],a[i]
		pos-=1
	return a

def maxpos(a,pos):
	return maxx(a[:pos+1])

def maxx(a):
	i=0 ; maxi=None ; maxposi=None
	while i<len(a):
		if not(maxi) or maxi[0]<a[i][0]:
			maxposi=i
			maxi=a[i]
		i+=1
	return maxposi

print(maxx(lista))
print(upsort(lista))





