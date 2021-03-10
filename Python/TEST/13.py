def generator_example():
    n = 1
    print("first print")
    yield n
    n = 2
    print("second print")
    yield n
    n = 3
    print("third print")
    yield n

a = generator_example() # a -> iterator
print(next(a))
print(next(a))
print(next(a))
