def foo(a):
    for x in range(3):
        print(a[x]/2,end="  ")


a=list(map(int, input().split()))
a.sort()
foo(a)