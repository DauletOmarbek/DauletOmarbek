import random




def coin_random(car2_x):
    y = int(random.randint(0,10))
    if (0<=y and y<car2_x-1)  or (car2_x+1 < y and y <=10):
        return y
    else:
        return coin_random(car2_x)

car2_x = int(input())
print(coin_random(car2_x))