def fib():
    first = 1
    second = 1
    while True:
        yield second
        first, second = second, first + second

it_fib = fib()
print(next(it_fib))
print(next(it_fib))
print(next(it_fib))
print(next(it_fib))
print(next(it_fib))