exchangerate = {} 
currency = {}

with open("currency.csv", "r", encoding="ISO-8859-1") as file:
    next(file)  
    for line in file:
        cols = line.strip().split(",") 
        code = cols[0].strip()
        name = cols[1].strip()
        rate = float(cols[2].strip())

        exchangerate[code] = rate
        currency[code] = name  


dollar = float(input("How much dollar do you have?"))
whatcurrency = input("What currency you want to have?").strip().upper()


if whatcurrency in exchangerate:
    amount = dollar * exchangerate[whatcurrency]
    print(f"\nDollar: {dollar} USD")
    print(f"{currency[whatcurrency]}: {amount:}") 
else:
    print("No currency found.")