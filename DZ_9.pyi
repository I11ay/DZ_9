# Задание 1:
# Запросить у пользователя 5 чисел и записать их в список
A = []
for i in range(5):
    a = int(input(f'Введите число №{i + 1}: '))
    A.append(a)

print(A)

# Задание 2:
# Дан список A = [1, 2, 3, 4, 5]
# Удалить последнее число из списка

A = [1, 2, 3, 4, 5]
A.pop()
print(A)

# Задание 3:
# Запросить у пользователя 10 чисел и записать их в список A
# Запросить у пользователя число N
# Вывести пользователю сколько в списке A повторяется число N
A = []
count = 0
for i in range(10):
    user_numbers = int(input(f'Введите число №{i + 1}: '))
    A.append(user_numbers)
N = int(input("Введите число: "))
for j in A:
    if j == N:
        count += 1
print(count)

# Задание 4:
# Запросить у пользователя число N
# Запросить у пользователя N чисел и записать их в список A
# Вывести список в обратной последовательности
A = []
N = int(input("Введите число: "))
for i in range(N):
    user_number = int(input(f'Введите число №{i + 1}: '))
    A.append(user_number)
print(A[::-1])

# Задание 5:
# Запросить у пользователя 5 чисел и записать их в список A
# Записать все числа из списка A которые больше 5 в список C

A = []
for i in range(5):
    a = int(input(f'Введите число №{i + 1}: '))
    A.append(a)
C = []
for j in A:
    if j > 5:
        C.append(j)
print(C)

# Задание 6:
# Запросить у пользователя число N
# Запросить у пользователя N целых чисел и записать их в список A
# Найти в нем минимальное и максимальное число с помощью цикла (запрещено использовать функцию min и max). Вывести эти числа.

A = []
N = int(input("Введите число: "))
for i in range(N):
    user_number = int(input(f'Введите число №{i + 1}: '))
    A.append(user_number)
sorted(A)
a, *_, b = A
print(a, b)

# Задание 7:
# Пользователь вводит текст нужно вывести количество цифр в этом тексте
digit_count = 0
text = input("Введите текст: ")
for i in text:
    if i.isdigit():
        digit_count += 1
print(digit_count)
