# Task 1
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

choice = input("Сделайте выбор: Сумма(+) или Произведение(*)")

if choice == '+':
    print(num1 + num2 + num3)
elif choice == '*':
    print(num1 * num2 * num3)
else:
    print("Неверный выбор")


# Task 2
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

choice = int(input("Сделайте выбор: 1-Максимальное число, 2-Минимальное число, 3-Среднеарифметическое трёх чисел"))

if choice == 1:
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    elif num3 > num1 and num3 > num2:
        print(num3)

elif choice == 2:
    if num1 < num2 and num1 < num3:
        print(num1)
    elif num2 < num1 and num2 < num3:
        print(num2)
    elif num3 < num1 and num3 < num2:
        print(num3)

elif choice == 3:
    print((num1 + num2 + num3) / 3)

else:
    print("Неверный выбор")


# Task 3
m = float(input("Введите количество метров: "))

choice = int(input("Сделайте выбор: 1-Мили, 2-Дюймы, 3-Ярды"))

if choice == 1:
    print(m * 0.000621)
elif choice == 2:
    print(m * 39.37)
elif choice == 3:
    print(m / 0.9144)
else:
    print("Неверный выбор")


