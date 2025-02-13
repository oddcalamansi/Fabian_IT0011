def is_palindrome(num):
    return str(num) == str(num)[::-1]

with open("numbers.txt") as file:
    for x, line in enumerate(file, start = 1):
        numbs = list(map(int, line.strip().split(',')))  
        total = sum(numbs)
        result = "Palindrome" if is_palindrome(total) else "Not a Palindrome"
        print(f"Line {x}: {', '.join(map(str, numbs))} (sum {total}) - {result}")