from time import time
def performance(fn):
    def wrap(*args, **kwargs):
        t1 = time()
        result = fn(*args,**kwargs)
        t2 = time()
        print (f'print{t2-t1}')
        return result
    return wrap
@performance
def long_time():
    for i in range(100000000):
        i*5
long_time()

    