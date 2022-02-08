def highest_even(li):
    evens = []
    for item in li :
        if item % 2 == 0:
            evens.append(item)
    print(max(evens))
highest_even([2,5,6,8,9,12,13])
            