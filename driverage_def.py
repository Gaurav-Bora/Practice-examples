def DriverAge():
    age = int(input('enter your age: '))
    if age < 18:
        print('sorry You are under age')
    elif age > 18:
        print('powering on ')
    elif age == 18:
        print('congratulations on your first year of driving')
DriverAge()