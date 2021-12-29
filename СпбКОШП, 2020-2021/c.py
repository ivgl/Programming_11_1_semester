m = [int(i) for i in input().split()]
k=m[0]
n=m[1]
v = [int(i) for i in input().split()]
a=0
b=n
for i in range (0,len(v)):
	if i == len(v) - 1:
		if b == v[i]:
			print(a+1)
			print(0)
		elif b > v[i]:
			print(a)
			print(b-v[i])
		else:
			print(a)
			print(b)
	elif b == v[i]:
		a+=1
		b=n
	elif b > v[i]:
		b=b-v[i]
	else:
		None
