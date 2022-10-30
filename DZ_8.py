text = input('Enter text: ')
space = 0
digit = 0
low = 0
up = 0

for symbol in text:
    if symbol.isspace():
        space += 1
    if symbol.isdigit():
        digit += 1
    if symbol.islower():
        low += 1
    if symbol.isupper():
        up += 1

if space > 0 and digit > 0 and low > 0 and up > 0:
    print("YES")
else:
    print("NO")


count = int(input("Enter Fibonacci number: "))
if count == 1:
    print(0)
    exit()
a = 0
b = 1
print(a)
print(b)

for i in range(count - 2):
        b = a + b
        a = b - a
        print(b)


import random

symbol = r"""!"# $%&'()*+,-./:;<=>?@[\]^_`{|}~"""
low = 'abcdefghijklmnopqrstuvwxyz'
up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digit = '0123456789'
all_pass = random.choice(symbol) + random.choice(low) + random.choice(up) + random.choice(digit)
all = symbol + low + up + digit
symbol_len = int(input('Enter an integer greater than 4: '))


for i in range(symbol_len):
    password = "".join(random.choice(all))
    print(password, end="")



password = input('Введите ваш пароль: ')

digit = False
upper = False
lower = False
spec = False


if not password or password == 'admin' or password == 'qwerty':
    print('Level 1')
    exit()

for i in password:
    if i.isdigit():
        digit = True
    elif i.isupper():
        upper = True
    elif i.islower():
        lower = True
    else:
        spec = True

len_true = len(password) > 8
total_result = digit + upper + lower + spec

if total_result == 1:
    print('Level 2')
elif total_result == 2:
    print('Level 3')
elif total_result >= 3 and not len_true:
    print('Level 4')
elif total_result == 4 and len_true:
    print('Level 5')