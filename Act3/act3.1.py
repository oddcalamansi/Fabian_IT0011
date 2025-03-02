firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
age = input("Enter your age: ")
fullname = firstname + " " + lastname
slicedname = firstname[0:3]
greetingmessage = "Hello, " + slicedname + "! Welcome. You are " + age + " years old."

print("")
print("Full Name: " + fullname)
print("Sliced Name: " + slicedname)
print(greetingmessage)
