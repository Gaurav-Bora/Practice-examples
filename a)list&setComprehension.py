#list, set, dict
#my_list = [param for param in iterable]
#my_set = {param for param in iterable}  only brackets changes

my_list = [char for char in 'helloo']
my_list2 = [num for num in range(0,10)]
my_list3 = [num*2 for num in range(0,10)]
my_list4 = [num*2 for num in range(0,10) if num %2 ==0]

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)
