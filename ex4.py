try:
    from random import randint
    a = randint(1, 500 + 1)
    b = int(input('Guess the number: '))
    while a != b:
        if a > b:
            print ('My number is higher')
        else:
            print ('My number is smaller')
        b = int(input('Guess the number: '))
    print ('Congratulations! The number is correct!')
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')