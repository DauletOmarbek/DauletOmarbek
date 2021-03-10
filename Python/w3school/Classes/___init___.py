class Person:
    def __init__(self, name, surname, age):
        self.name=name
        self.surname=surname
        self.age=age


x=str(input())
y=str(input())
z=int(input())
k=Person(x, y, z)

print(k.name ,k.surname, k.age ,"Year old")