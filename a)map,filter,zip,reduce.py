#map, filter, zip, reduce

from functools import reduce
my_list = [1,2,3]
new_list = [10,20,30]
def multiply_by2(item):
    return item *2
def only_odd(item):
    return item % 2 != 0
def accumulator(acc,item):
    print(acc,item) #to show acc + item be executed
    return acc + item


print(list(filter(only_odd, my_list)))
print(list(map(multiply_by2, [1,2,3])))
print(list(zip(my_list,new_list)))
print(reduce(accumulator, my_list,0 ))
    