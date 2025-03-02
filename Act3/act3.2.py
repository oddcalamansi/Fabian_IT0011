firstname = input("Enter first name: ")
lastname = input("Enter last name: ")
fullname = firstname + " " + lastname
fullnameuppercase = fullname.upper()
fullnamelowercase = fullname.lower()
lengthoffullname = len(fullname)

print("")
print("Full Name: " + fullname)
print("Full Name (Upper Case): " + fullnameuppercase)
print("Full Name (Lower Case): " + fullnamelowercase)
print("Length of Full Name: " + str(lengthoffullname))