import os

records = []
filename = ''

while True:
    print("")
    print("1 - Open File")
    print("2 - Save File")
    print("3 - Save As File")
    print("4 - Show All Students Record")
    print("a - Order by last name")
    print("b - Order by grade")
    print("5 - Show Student Record")
    print("6 - Add Record")
    print("7 - Edit Record")
    print("8 - Delete Record")
    print("9 - Exit")
    
    enternumber = input("\nEnter a number: ")

    if enternumber == "1":  
        filenames = input("\nEnter filename: ")
        if os.path.exists(filenames):
            with open(filenames, 'r') as file:
                records.clear()
                studentinfo = file.read().strip()
                for data in studentinfo:
                    lines = data.strip().split("\n")
                    if len(lines) == 4:
                        studentid = lines[0].split(": ")[1]
                        studentname = lines[1].split(": ")[1]
                        classstanding = lines[2].split(": ")[1]
                        majorexamgrade = lines[3].split(": ")[1]
                        records.append((studentid, (studentname), classstanding, majorexamgrade))
            filename = filenames
            print(f"File '{filenames}' loaded")
        else:
            print("\nFile not found")

    elif enternumber == "2":  
        if filename:
            with open(filename, 'w') as file:
                for studentid, (studentname), classstanding, majorexamgrade in records:
                    file.write(
                        f"Student ID: {studentid}\n"
                        f"Student Name: {studentname}\n"
                        f"Class Standing: {classstanding}\n"
                        f"Major Exam: {majorexamgrade}\n"
                    )
            print("\nRecords saved")
        else:
            print("\nUse 'Save As' when saving for the first time.")

    elif enternumber == "3":  
        filename = input("\nEnter filename: ")
        with open(filename, 'w') as file:
            for studentid, (studentname), classstanding, majorexamgrade in records:
                file.write(
                   f"Student ID: {studentid}\n"
                   f"Student Name: {studentname}\n"
                   f"Class Standing: {classstanding}\n"
                   f"Major Exam: {majorexamgrade}\n"
                )
        print("Records saved")

    elif enternumber == "4":  
        if not records:
            print("No records")
        else:
            print("All Student Records: ")
            print("")
            for studentid, (studentname), classstanding, majorexamgrade in records:
                print(
                   f"Student ID: {studentid}\n"
                   f"Student Name: {studentname}\n"
                   f"Class Standing: {classstanding}\n"
                   f"Major Exam: {majorexamgrade}\n"
                )

    elif enternumber == "a":  
        print("Records ordered by last name")

    elif enternumber == "b":   
        print("Records ordered by final grade.")

    elif enternumber == "5":  
        studentid = input("\nEnter Student ID: ")
        found = False
        for studentrecords, (studentname), classstanding, majorexamgrade in records:
            if studentrecords == studentid:
                print(
                   f"Student ID: {studentid}\n"
                   f"Student Name: {studentname}\n"
                   f"Class Standing: {classstanding}\n"
                   f"Major Exam: {majorexamgrade}\n"
                )
                found = True
                break
        if not found:
            print("No student record")

    elif enternumber == "6":  
        studentid = input("\nEnter 6 digit student ID: ")
        if not studentid.isdigit() or len(studentid) != 6:
            print("Student ID should be 6 digits.")
            continue
        if any(record[0] == studentid for record in records):
            print("Student ID already used")
            continue

        studentname = input("Enter Student Name: ")
        classstanding = input("Enter Class Standing Grade: ")
        majorexamgrade = input("Enter Major Exam Grade: ")

        records.append((studentid, (studentid), classstanding, majorexamgrade))
        print("\nRecord added")

    elif enternumber == "7":  
        studentid = input("\nEnter Student ID: ")
        for x, (sid, (studentname), classstanding, majorexamgrade) in enumerate(records):
            if sid == studentid:
                newstudentname = input(f"Enter New Student Name [{studentname}]: ") or studentname
                newclassstanding = input(f"Enter New Student Class Standing [{classstanding}]: ") or classstanding
                newmajorexamgrade = input(f"Enter New Major Exam Grade [{majorexamgrade}]: ") or majorexamgrade

                records[x] = (sid, (newstudentname), newclassstanding, newmajorexamgrade)
                print("Record updated")
                break
        else:
            print("No record")

    elif enternumber == "8":  
        studentid = input("\nEnter Student ID: ")
        records = [record for record in records if record[0] != studentid]
        print("Record deleted")

    elif enternumber == "9":  
        print("\nExiting")
        break

    else:  
        print("Invalid choice")
