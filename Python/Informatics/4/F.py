n=int(input())
k=int(input())
nfak=int(1)
kfak=int(1)
z=int(1)
for x in range(n,0,-1):
    nfak*=x
for x in range(k,0,-1):
    kfak*=x
for x in range(n-k,0,-1):
    z*=x
print(int(nfak/(kfak*z)))