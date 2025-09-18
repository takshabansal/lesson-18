def check_age():
    try:
        age = int(input("Enter your age: "))
        if age < 1 or age > 150:
            raise ValueError("Age must be between 0 and 150.")
        
        if age % 2 == 0:
            print(f"Your age ({age}) is even.")
        else:
            print(f"Your age ({age}) is odd.")
    
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

check_age()
