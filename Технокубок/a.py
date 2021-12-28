def fun(m):
	for i in range(0,len(m)//2):
		a=m[2*i] 
		m[2*i]=-m[2*i+1]
		m[2*i+1]=a
	for k in range(0,len(m)):
		print(m[k],end=" ")

n = int(input())
for j in range(n):
	v = int(input())
	a = [int(i) for i in input().split()]
	fun(a)
