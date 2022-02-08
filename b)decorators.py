# decorator

def my_decorator(func):
    def wrap_func():
        print('#######')
        func()
        print('#######')
    return wrap_func()

@my_decorator
def hello():
    print('helloo')
@my_decorator
def bye():
    print('byeee')
    
    
# this is same as 
# hello2 = my_decorators(hello)
# print(hello2)