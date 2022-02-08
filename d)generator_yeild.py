#generator
def generator_func(num):
    for i in range(num):
        yield i
a = generator_func(100)
next(a)
next(a)
next(a)
next(a)
print(next(a))