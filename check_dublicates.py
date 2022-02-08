#check dublicates
lists= ['a','b','c','d','e','a','c']
dublicates = []
for value in lists:
    if lists.count(value)>1:
        if value not in dublicates:
            dublicates.append(value)
print(dublicates)