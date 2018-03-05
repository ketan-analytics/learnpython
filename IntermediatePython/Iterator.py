def generator_function():
    for i in range(10):
        yield i


#for item in generator_function():
 #   print(item)


def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

gen=fibon(10)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))