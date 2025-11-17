import random

print('Welcome to the pypassword generator')

a = int(input('how many letter would you like in your passwords?'))
b = int(input('how many symbol would you like?'))
c = int(input('how many number would you like?'))

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letter_ = random.randint(0, 27)
# print(letter[letter_])


for char in range(1, a + 1):
    random_ = random.choice(letter)
    print(random_, end="")

for char in range(1, b + 1):
    random_ = random.choice(number)
    print(random_, end="")

for char in range(1, c + 1):
    random_ = random.choice(symbol)
    print(random_, end="")

# number_=random.randint(0,9)
# print(number[number_])

# symbol_=random.randint(0,9)
# print(symbol[symbol_])