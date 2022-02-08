#error handling

while True:
    try:
        age = int(input('what is your age? '))
        10/age
    except ValueError:
        print('please enter number.')
    except ZeroDivisionError:
        print('please enter higher number.')
    else:
        print('thank you')
        break