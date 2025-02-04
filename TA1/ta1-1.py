inputstring = input("Input: ")
vowel = "aAeEiIoOuU"
consonant = "bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ"
space = " "
vowels = 0
consonants = 0
spaces = 0
others = 0

for i in inputstring:
    if i in vowel:
        vowels = vowels + 1
    elif i in consonant:
        consonants = consonants + 1
    elif i in space:
        spaces = spaces + 1
    else:
        others = others + 1
        
print(" ")
print("Vowels: ", vowels)
print("Consonants: ", consonants)
print("Spaces:", spaces)
print("Others: ", others)
