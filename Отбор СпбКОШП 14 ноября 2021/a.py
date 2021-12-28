n = int(input())
m = int(input())
k = int(input())
if k > min(n,m):
	print("Impossible")
else:	
	print("Possible")
	for i in range (0,k):
		a='.'*m
		a=list(a)
		a[i]="*"
		print(a)
