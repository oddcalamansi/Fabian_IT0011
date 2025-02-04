input = input("Input: ")
sum = 0
for i in input:
    if "0" <= i <= "9":  
        sum += int(i) 
print()
print("Sum of digits:", sum)
