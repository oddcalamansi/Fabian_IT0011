lastname = input("Enter last name: ")
firstname = input("Enter first name: ")
age = input("Enter age: ")
contactnumber = input("Enter contact number: ")
course = input("Enter course: ")

studentinformation=f"Last Name: {lastname}\nFirst Name: {firstname}\nAge: {age}\nContact Number: {contactnumber}\nCourse: {course}\n"

with open("students.txt", "a") as file:
    file.write(studentinformation)

print("\nStudent information has been saved to 'students.txt'.")