a=float(input())
b=float(input())
c=float(input())
d=b*100+c
print(int((d*(1+a/100))//100), int((d*(1+a/100))%100))