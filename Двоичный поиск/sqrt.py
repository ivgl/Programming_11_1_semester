a = int(input())
b = int(input())
k = int(input())

def sq(a,b,k):
	if abs(a-b) <= 1:
		return a 
	else:
	    if (((a+b)//2)*((a+b)//2)) > k:
		    return sq(a,((a+b)//2),k)
	    else:
		    return sq(((a+b)//2),b,k)

print(sq(a,b,k))

*Ищет максимальное целое число, квадрат которого <= данного
