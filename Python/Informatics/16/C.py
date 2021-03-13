        

def intersection(lst1, lst2):

    lst3 = [value for value in lst1 if value in lst2]

    lst3.sort()
    for x in lst3:
        print(x,end=' ')


lst1=list(map(int, input().split()))
lst2=list(map(int, input().split()))
intersection(lst1, lst2)