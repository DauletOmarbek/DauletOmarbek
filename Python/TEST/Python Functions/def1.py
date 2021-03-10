def foo(a):
    for x in range(len(a)):
        print(a[x],end="")

a=input().split()

foo(a)