def divide(x, y):
    if y == 0:
        return None
    return x/y

def exponentiation(x, y):
    return x**y
    
def remainder(x, y):
    if y == 0:
        return None
    return x%y
    
def summation(x, y):
    if x > y:
        return None
    return sum(range(x, y + 1))
    

while True:
    print("Choose a Letter")
    print("[D] - Divide")
    print("[E] - Exponentiation")
    print("[R] - Remainder")
    print("[F] - Summation")
    print("[X] - Exit")

    choice = input("Enter your letter: ").upper().strip()

    if choice == 'X':
        print("Exiting")
        break

    if choice in ['D', 'R', 'E', 'F']:
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        if choice == 'D':
            result = divide(x, y)
        elif choice == 'E':
            result = exponentiation(x, y)
        elif choice == 'R':
            result = remainder(x,y)
        elif choice == 'F':
            result = summation(x, y) 
        else:
            print("Invalid choice")
            continue

    if result is None:
        print("Invalid input")
    else:
        print(f"The answer is: {result}")