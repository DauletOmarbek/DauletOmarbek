a=input().split()
print("NO")
for x in range(1,len(a)):
    for y in range(x):
        if a[x]==a[y]:
            print("YES")
            break 
        if y==x-1:
            print("NO") 
    
    
    