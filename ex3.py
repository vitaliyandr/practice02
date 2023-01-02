try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    while True:
     c = int(input("Enter the number: "))
     if c >= a and c <= b:
        break
     else:
        print("Enter the number again")
    for i in range(a, b + 1):
     if i == c:
        print("!", i, "!", sep="", end=" ")
     else:
        print(i, end=" ")
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
