a=int(input())
if a//1000==a%10 and (a-(a//1000)*1000)//100==(a//10)%10:
    print(1)
else:
    print(2)