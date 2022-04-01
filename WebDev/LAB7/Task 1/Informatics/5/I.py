a=int(input())
b=int(input())
c=int(input())
y=int(input())
d=int(b*100+c)

for x in range(y):
    d=int(d*(1+a/100))
    

print(int(d//100), int(d%100))