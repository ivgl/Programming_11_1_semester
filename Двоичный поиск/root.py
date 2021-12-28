a = int(input())
b = int(input())
y = int(input())

def func(x):
	return int(x*x*x)


def root(a,b,func,y):
	if b-a <= 1:
		return a		
	n = ((a+b)//2)
	m = func(n)
	if m > y:
		return root(a,n,func,y)
	else:
		if m < y:
			return root(n,b,func,y)
		else:
			return n
print(root(a,b,func,y))

*Ищет максимальное целое число func() от которого <= исходного, сделал именно про фунцию, так как помнил эту формулировку на паре
