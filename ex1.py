try:
    a = int(input('Enter number: '))
    for i in range(1, 11):
        print(a,'*',i,'=',a*i)
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')

