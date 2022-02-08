def sum(num1,num2):
    return num1 / num2
try:
    print(sum(5,0))
except (TypeError, ZeroDivisionError) as err:
    print(err)
    
    