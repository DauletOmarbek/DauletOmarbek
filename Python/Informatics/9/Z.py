a=input().split()
b=int(input())
for x in range((len(a)-b)%len(a),len(a)):
    print(a[x], end=" ")
for x in range((len(a)-b)%len(a)):
    print(a[x],end=" ") 