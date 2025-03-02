file = open("students.txt", "r")

print("Reading Student Information:")

lines = file.readlines()

for line in lines:
    print(line.strip())
