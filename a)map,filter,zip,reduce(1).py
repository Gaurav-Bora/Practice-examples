from functools import reduce
#capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi','gigi']
def capitalize(string):
    return string.upper()
print(list(map(capitalize, my_pets)))

#zip 2 lists into list of tuple but sort no in assending order
my_string = ['a','b','c','d']
my_num = [5,9,3,4]
print(list(zip(my_string,sorted(my_num))))

#filter the score that pass over 50%
score = [50,60,20,48,98,78]
def percent(score):
    return score > 50
print(list(filter(percent,score)))

#combine all the nos that are in the list that is in file using reduce    
def accumulator(acc,item):
    return acc + item
print(reduce(accumulator,(my_num+score)))
