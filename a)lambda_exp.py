#lambda expression  
#square
my_list = [5,6,9]
new_list = list(map(lambda item: item**2, my_list))
print(new_list)

#list sorting
a = [(0,2),(4,3),(9,9),(10,-1)]
a.sort(key=lambda x: x[1])
print(a)