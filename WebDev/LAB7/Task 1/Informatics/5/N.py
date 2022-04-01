a=int(input())
b=int(0)
for x in range(1,a+1):
    if x%2==1:
        b+=1/x
    if x%2==0:
        b+=(-1)/x
print(b)