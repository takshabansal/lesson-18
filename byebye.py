valid=False
while not valid:
    try:
        n=float(input("Enter a number: "))
        while n%2==0:
            print("Bye")
        valid=True
    except ValueError:
        print("Invalid")