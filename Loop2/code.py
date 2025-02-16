# Task 1
length = int(input("Введите длину: "))
symbol = input("Введите символ: ")

for i in range(length):
    print(symbol)


# Task 2
summa = 0
max_num = 0
min_num = 0

number = int(input("Ведите число: "))
if number != 7:
    summa = number
    max_num = number
    min_num = number

while True and number != 7:
    number = int(input("Ведите число: "))

    if number == 7:
        print("Goodbye!")
        break

    summa += number

    if min_num > number:
        min_num = number

    if max_num < number:
        max_num = number


print(f"Сумма: {summa}\nМинимальное число: {min_num}\nМаксимальное число: {max_num}")
# В задании не сказано, что число "7" тоже участвует во всех операциях. Это число лишь завершает цикл.
# Поэтому я написала код таким образом.


# Task 3
num = int(input("Введите число: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i
print(f"Факториал: {factorial}")
