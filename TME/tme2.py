months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month, day, year  = input("Enter the date mm/dd/yyyy: ").split("/")
monthzz = months[int(month) - 1]
print(f"Date Output: {monthzz} {int(day)}, {year}")