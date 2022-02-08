def my_decorators(func):
    def wrap_func(*args,**kwargs):
        print('*******')
        func(*args,**kwargs)
        print('*******')
    return wrap_func
@my_decorators
def hello(greeting, emoji=':)'):
    print(greeting,emoji)

hello('hii')

