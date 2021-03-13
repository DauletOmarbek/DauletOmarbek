a=int(input())
b=int(0)
for x in range(a+1):
    b+=(pow((-1),x)/(2*x+1))
print(b*4)