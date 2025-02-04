num=5
print("a.")
for i in range(1, num + 1):
    for j in range(num - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print(k, end="")
    print()  

print()

print("b.")
n = 1

while n <= 7:
    count = 1
    while count <= n:
        print(n, end="")
        count += 1
        
    print()
    
    if n == 5:
        n = 6
    elif n == 6:
        n = 7
    else:
        n += 2
