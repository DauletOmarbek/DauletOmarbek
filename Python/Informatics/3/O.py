n=int(input())
m=int(input())
k=int(input())
for x in range(1,n*m):
    if (n*m)-x*n==k:
        print("YES")
        exit()
    if (n*m)-x*m==k:
        print("YES")
        exit()
print("NO")
