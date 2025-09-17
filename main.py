import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

generated_password = ''

random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)
letter_counter = 0
symbol_counter = 0
numbers_counter = 0

for l in letters:
    if letter_counter < nr_letters:
        generated_password += l + ' '
        letter_counter += 1

for n in numbers:
    if numbers_counter < nr_numbers:
        generated_password += n + ' '
        numbers_counter += 1

for s in symbols:
    if symbol_counter < nr_symbols:
        generated_password += s + ' '
        symbol_counter += 1

splited = generated_password.split()
random.shuffle(splited)

final_password = ''
for s in splited:
    final_password += s

print(f"Here is your generated password: {final_password}")
