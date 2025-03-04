#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# generate n random numbers
letter = ""
for lett in range(nr_letters):
    rnum_letters = random.randrange(nr_letters)
    # get those 4 random letters
    letter += letters[rnum_letters]
    
# print(letter)
symbol = ""
for symb in range(nr_symbols):
    rnum_symb = random.randrange(nr_symbols)
    symbol += symbols[rnum_symb]
    
# print(symbol)

number = ""
for num in range(nr_numbers):
    rnum_numb = random.randrange(1,nr_numbers)
    number += numbers[rnum_numb]
    
password = letter + symbol+ number
print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
list_password = list(password)
random.shuffle(list_password)
random_password = "".join(list_password)
print(random_password)