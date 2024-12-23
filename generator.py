import random


lettersList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbersList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbolsList = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

number_letters = int(input("How many letters would you like in your password?\n"))

passLetters = ""
for number in range(0,number_letters):
    passLetters += random.choice(lettersList)



number_symbols = int(input(f"How many symbols would you like?\n"))

passSymbols = ""
for number in range(0,number_symbols):
      passSymbols += random.choice(symbolsList)




nr_numbers = int(input(f"How many numbers would you like?\n"))

passNumber = ""
for number in range(0,nr_numbers):
    passNumber += random.choice(numbersList)




password = passLetters + passSymbols + passNumber

print(f"Your password is: {password}")

