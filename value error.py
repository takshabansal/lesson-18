try:
    number=int(input("Enter a number: "))
    number=number**number
    print("The number entered is", number)
except ValueError as ex:
    print("Exception:", ex)