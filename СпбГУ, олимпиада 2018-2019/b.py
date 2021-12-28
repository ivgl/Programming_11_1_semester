import math

a = int(input())
b = int(input())

if math.sqrt(a+2*b) % 1 == 0:
	print(4*(math.sqrt(a+2*b)))
else:
	if ((math.floor(math.sqrt(a+2*b)))*(math.ceil(math.sqrt(a+2*b))) >= a+2*b):
		print(2*(math.floor(math.sqrt(a+2*b)))+2*(math.ceil(math.sqrt(a+2*b))))
	else:
		print(4*(math.ceil(math.sqrt(a+2*b))))
	