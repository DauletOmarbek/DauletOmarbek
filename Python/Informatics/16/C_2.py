a=list(map(int, input().split()))
b=list(map(int, input().split()))
c = []
for i in a:
    if i in c:
        continue
    for j in b:
        if i == j:
            c.append(i)
            break

c.sort()
for x in c:
    print(x, end=" ")