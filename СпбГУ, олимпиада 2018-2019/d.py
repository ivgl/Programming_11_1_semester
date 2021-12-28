def f(b,c):
    s = 0
    for i in range(0,min(len(b),len(c))):
        if b[i] == c[i]:
            s += 1
        else:
            break
    return s

n = int(input())
for j in range(n):
  a,b,c = [str(i) for i in input().split()]
  a = int(a)

  if (len(b) + len(c) - 2*(f(b,c))) % 2 == a % 2:
      print("Yes")
  else:
      print("No") 

	
