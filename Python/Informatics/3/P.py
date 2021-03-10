a=int(input())
b=int(input())
if a==0 and b==0:
    print("INF")
    exit()
for x in range(-1000,1000):
    if a*x+b==0:
        print(x)
        exit()
print("NO")

